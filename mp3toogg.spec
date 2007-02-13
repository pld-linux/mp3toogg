Summary:	Tool for MP3 to Ogg/Vorbis reencoding
Summary(pl.UTF-8):	Narzędzie do przekodowania MP3 do Ogg/Vorbis
Name:		mp3toogg
Version:	2.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3toogg/%{name}-%{version}.tar.gz
# Source0-md5:	9385153067fbccda4cd7d182160f5dfe
URL:		http://mp3toogg.sourceforge.net/  
Requires:	mp3info-rmc
Requires:	mpg321
Requires:	vorbis-tools
Requires:	zenity
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool allow you to convert MP3 files into the free Ogg format.

%description -l pl.UTF-8
To narzędzie pozwala na konwersje plików MP3 na wolnodostępny format Ogg.

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
