# NB!
# - anacron provides crondaemon but no crontab binary!
%define	_beta	b2
Summary:	A wrapper around cron jobs
Summary(pl):	Wrapper dla zadañ cronowych
Name:		shush
Version:	1.1
Release:	0.%{_beta}.1
License:	custom, distributable
Group:		Applications/Console
Source0:	http://web.taranis.org/shush/dist/%{name}-%{version}%{_beta}.tgz
# Source0-md5:	0b8fd87f6e12a3e9bf55cc8bd349a3d8
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-progs.patch
URL:		http://web.taranis.org/shush/
BuildRequires:	autoconf
BuildRequires:	pcre-devel
Requires:	/usr/bin/crontab
Requires:	/usr/lib/sendmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shush runs a command and optionally reports its output by email. It is
a powerful wrapper around cron jobs.

%description -l pl
Shush wykonuje komendê i opcjonalnie wysy³a wynik jej dzia³ania
poprzez email. Jest to potê¿ny wrapper dla zadañ cronowych.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1
%patch1 -p1

%build
export SENDMAIL=/usr/lib/sendmail
export CRONTAB=/usr/bin/crontab
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# LICENSE file is required (read it)
%doc CHANGES LICENSE
%attr(755,root,root) %{_bindir}/shush
%{_mandir}/man1/*.1*
