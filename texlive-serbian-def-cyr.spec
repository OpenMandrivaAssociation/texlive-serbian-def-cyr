# revision 23734
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-serbian-def-cyr
Version:	20190228
Release:	1
Summary:	TeXLive serbian-def-cyr package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-def-cyr.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755913
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719511
- texlive-serbian-def-cyr
- texlive-serbian-def-cyr
- texlive-serbian-def-cyr
- texlive-serbian-def-cyr

