Summary:	Peter's Disk Performance Benchmarking Tool
Name:		piozone
Version:	1.0
Release:	1
License:	no restrictions
Group:		Applications/System
Source0:	ftp://ftp.lysator.liu.se/pub/unix/piozone/%{name}-%{version}.tar.gz
# Source0-md5:	e48370a9aa80aed212b18e16c08b9056
URL:		http://www.lysator.liu.se/~pen/piozone/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Peter's Disk Performance Benchmarking Tool.

Piozone is freely available and may be used by anyone without any
restrictions except that you may not pretend that you wrote this...

%prep
%setup  -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE=1" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
