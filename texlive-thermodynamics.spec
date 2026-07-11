%global tl_name thermodynamics
%global tl_revision 78482

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.04
Release:	%{tl_revision}.1
Summary:	Macros for multicomponent thermodynamics documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thermodynamics
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thermodynamics.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package makes typesetting quantities found in thermodynamics texts
relatively simple. The commands are flexible and intended to be
relatively intuitive. It handles several sets of notation for total,
specific, and molar quantities; allows changes between symbols (e.g., A
vs. F for Helmholtz free energy); and greatly simplifies the typesetting
of symbols and partial derivatives commonly encountered in mixture
thermodynamics. Changes of one's notes from one textbook to another can
be achieved relatively easily by changing package options. The package
offers a collection of macros and environments which are intended to
make typesetting thermodynamics documents faster, more convenient, and
more reliable. Macros include symbols for extensive, molar, specific,
and partial molar properties; excess and residual (departure)
properties; partial derivatives; heat capacities, compressibilities, and
expansivities; saturation, mixture, and pure-component properties;
Henry's Law parameters and activity coefficients; changes on mixing,
fusion, reaction, sublimation, and vaporization; and sets of all
moles/mole fractions/masses/etc. being held constant in derivatives.
Conversion of notes between textbooks is trivial for textbooks supported
by the package, and more general changes in notation are also possible
through package options.

