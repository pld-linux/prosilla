
Summary:	ProSilla - a program which accelerates file transfers over SSH
Summary(pl.UTF-8):	ProSilla - program przyspieszający pobieranie dużych plików przez SSH
Name:		prosilla
Version:	1.2
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.v-lo.krakow.pl/~anszom/%{name}/%{name}-%{version}.tgz
# Source0-md5:	a22c90786122ea1ab6cfd3807001d23e
Patch0: 	%{name}-no-gtk.patch
URL:		http://www.v-lo.krakow.pl/~anszom/prosilla/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
Obsoletes:	prosilla-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProSilla is a program which accelerates file transfers over SSH by
opening multiple connections just like other download accelerators.
The only difference is that proSilla uses SSH instead of HTTP/FTP for
download. Of course you must have a shell account on the remote server
to use this program.

%description -l pl.UTF-8
ProSilla to program przyspieszający pobieranie dużych plików poprzez
otwieranie wielu połączeń na raz (tak jak inne "przyspieszacze").
Jedyną różnicą jest to, że proSilla używa SSH zamiast HTTP/FTP do
ściągania. Oczywiście w związku z tym trzeba mieć konto shellowe na
docelowym serwerze żeby skorzystać z tego programu.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION='\$(VERSION)' -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lutil -lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DSTDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
