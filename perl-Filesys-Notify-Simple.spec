#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Filesys-Notify-Simple
Version  : 0.14
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-0.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-0.14.tar.gz
Summary  : 'Simple and dumb file system watcher'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Filesys-Notify-Simple-license = %{version}-%{release}
Requires: perl-Filesys-Notify-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::SharedFork)

%description
NAME
Filesys::Notify::Simple - Simple and dumb file system watcher
SYNOPSIS
use Filesys::Notify::Simple;

my $watcher = Filesys::Notify::Simple->new([ "." ]);
$watcher->wait(sub {
for my $event (@_) {
$event->{path} # full path of the file updated
}
});

%package dev
Summary: dev components for the perl-Filesys-Notify-Simple package.
Group: Development
Provides: perl-Filesys-Notify-Simple-devel = %{version}-%{release}
Requires: perl-Filesys-Notify-Simple = %{version}-%{release}

%description dev
dev components for the perl-Filesys-Notify-Simple package.


%package license
Summary: license components for the perl-Filesys-Notify-Simple package.
Group: Default

%description license
license components for the perl-Filesys-Notify-Simple package.


%package perl
Summary: perl components for the perl-Filesys-Notify-Simple package.
Group: Default
Requires: perl-Filesys-Notify-Simple = %{version}-%{release}

%description perl
perl components for the perl-Filesys-Notify-Simple package.


%prep
%setup -q -n Filesys-Notify-Simple-0.14
cd %{_builddir}/Filesys-Notify-Simple-0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Filesys-Notify-Simple
cp %{_builddir}/Filesys-Notify-Simple-0.14/LICENSE %{buildroot}/usr/share/package-licenses/perl-Filesys-Notify-Simple/6eee64e6240eb3496293e0e3a8d568e984e4f1fa
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Filesys::Notify::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Filesys-Notify-Simple/6eee64e6240eb3496293e0e3a8d568e984e4f1fa

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
