Name:		texlive-thermodynamics
Version:	71522
Release:	1
Summary:	Macros for multicomponent thermodynamics documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thermodynamics
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes typesetting quantities found in
thermodynamics texts relatively simple. The commands are
flexible and intended to be relatively intuitive. It handles
several sets of notation for total, specific, and molar
quantities; allows changes between symbols (e.g., A vs. F for
Helmholtz free energy); and greatly simplifies the typesetting
of symbols and partial derivatives commonly encountered in
mixture thermodynamics. Changes of one's notes from one
textbook to another can be achieved relatively easily by
changing package options. The package offers a collection of
macros and environments which are intended to make typesetting
thermodynamics documents faster, more convenient, and more
reliable. Macros include symbols for extensive, molar,
specific, and partial molar properties; exces and residual
(departure) properties; partial derivatives; heat capacities,
compressibilities, and expansivities; saturation, mixture, and
pure-component properties; Henry's Law parameters and activity
coefficients; and changes on mixing, fusion, reaction,
sublimation, and vaporization; and sets of all moles/mole
fractions/masses/etc. being held constant in derivatives.
Conversion of notes between textbooks is trivial for textbooks
supported by the package, and more general changes in notation
are also possible through package options.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/thermodynamics
%{_texmfdistdir}/tex/latex/thermodynamics
%doc %{_texmfdistdir}/doc/latex/thermodynamics

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
