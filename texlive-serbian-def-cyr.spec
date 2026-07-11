%global tl_name serbian-def-cyr
%global tl_revision 23734

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Serbian cyrillic localization
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/serbian-def-cyr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides abstract, chapter, title, date etc, for serbian
language in cyrillic scripts in T2A encoding and cp1251 code pages.

