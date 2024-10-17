Name:		texlive-colorist
Version:	70101
Release:	1
Summary:	Write your articles or books in a colorful way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorist
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorist.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers you a LaTeX style file and two classes to
typeset articles or books in a colorful way. These classes
currently have native support for English, French, German,
Italian, Portuguese (European and Brazilian), and Spanish
typesetting. They compile with any major TeX engine. You may
also wish to consider the packages lebhart and beaulivre, which
are enhanced versions of the classes provided here. They have
unicode support, thus can only be used with either XeLaTeX or
LuaLaTeX. Currently they have native support for Chinese (both
simplified and traditional), English, French, German, Italian,
Japanese, Portuguese (European and Brazilian), Russian and
Spanish typesetting, and also use more beautiful fonts.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/colorist
%doc %{_texmfdistdir}/doc/latex/colorist

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
