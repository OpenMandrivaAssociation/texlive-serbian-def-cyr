Name:		texlive-serbian-def-cyr
Version:	23734
Release:	2
Summary:	TeXLive serbian-def-cyr package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive serbian-def-cyr package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-def-cyr/serbian-def-cyr.sty
%doc %{_texmfdistdir}/doc/latex/serbian-def-cyr/README
%doc %{_texmfdistdir}/doc/latex/serbian-def-cyr/proba.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-def-cyr/proba.tex
%doc %{_texmfdistdir}/doc/latex/serbian-def-cyr/usage.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-def-cyr/usage.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
