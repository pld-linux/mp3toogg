Summary:	Utility for MP3 information and tag modification
Name:		mp3toogg
Version:	2.0
Release:	0.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3toogg/%{name}-%{version}.tar.gz
# Source0-md5:	9385153067fbccda4cd7d182160f5dfe
URL:		http://mp3toogg.sourceforge.net/  
Requires:	zenity
Requires:	mp3info-rmc
Requires:	vorbis-tools
Requires:	mpg321
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mp3info is a command line utility to extract and manipulate TAG (ID3)
info from MP3 files. It also has a VERY configurable output.


%prep
%setup -q

%build
%configure \
	SH=/bin/bash \
	ZENITY=/usr/bin/zenity \
	MP3INFO=/usr/bin/mp3info-rmc \
	MPG321=/usr/bin/mpg321 \
	OGGENC=/usr/bin/oggenc \
	VORBISCOMMENT=/usr/bin/vorbiscomment 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
