
#Conditional build:
%bcond_without gtk    # don't build gtk version
#

Summary:	ProSilla - a program which accelerates file transfers over ssh
Summary(pl):	ProSilla - program przyspieszaj±cy pobieranie du¿ych plików przez ssh
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
%if %{with gtk}
BuildRequires:  gtk+-devel
%endif
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProSilla is a program which accelerates file transfers over ssh by
opening multiple connections just like other download accelerators.
The only difference is that proSilla uses ssh instead of http/ftp for
download. Of course you must have a shell account on the remote server
to use this program.

%description -l pl
ProSilla to program przyspieszaj±cy pobieranie du¿ych plików poprzez
otwieranie wielu po³±czeñ na raz (tak jak inne "przyspieszacze").
Jedyn± ró¿nic± jest to, ¿e proSilla u¿ywa ssh zamiast http/ftp do
¶ci±gania. Oczywi¶cie w zwi±zku z tym trzeba mieæ konto shellowe na
docelowym serwerze ¿eby skorzystaæ z tego programu.

%prep
%setup -q -n %{name}
%if !%{with gtk}
%patch0 -p1
%endif

%build
%if %{with gtk}
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION='\$(VERSION)' `gtk-config --cflags` -DWITH_GTK -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lutil -lncurses `gtk-config --libs` -lpthread"
%else
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION='\$(VERSION)' -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lutil -lncurses"
%endif

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
