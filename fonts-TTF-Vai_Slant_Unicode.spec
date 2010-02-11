Summary:	Free TrueType font for the Vai script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma vai
Name:		fonts-Vai_Slant_Unicode
Version:	1.0
Release:	1
License:	SIL OFL, distributable
Group:		Fonts
Source0:	http://openfontlibrary.org/people/iwsfutcmd/iwsfutcmd_-_Vai_Slant_Unicode.ttf
# Source0-md5:	e1d035ab042dba9d36f98b5130ca1ad4
URL:		http://openfontlibrary.org/media/files/iwsfutcmd/383
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This is the Unicode version of SIL's Vai font, including the glyphs
from the Vai Extra Characters Set.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

# remove uploader name from the font file name
install %{SOURCE0} $RPM_BUILD_ROOT%{ttffontsdir}/Vai_Slant_Unicode.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/Vai_Slant_Unicode.ttf
