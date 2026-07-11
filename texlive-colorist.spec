%global tl_name colorist
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Write your articles or books in a colorful way
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorist
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorist.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(projlib)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package offers you a LaTeX style file and two classes to typeset
articles or books in a colorful way. These classes currently have native
support for English, French, German, Italian, Portuguese (European and
Brazilian), and Spanish typesetting. They compile with any major TeX
engine. You may also wish to consider the packages lebhart and
beaulivre, which are enhanced versions of the classes provided here.
They have unicode support, thus can only be used with either XeLaTeX or
LuaLaTeX. Currently they have native support for Chinese (both
simplified and traditional), English, French, German, Italian, Japanese,
Portuguese (European and Brazilian), Russian and Spanish typesetting,
and also use more beautiful fonts.

