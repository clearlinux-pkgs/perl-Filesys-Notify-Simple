#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Filesys-Notify-Simple
Version  : 0.13
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-0.13.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfilesys-notify-simple-perl/libfilesys-notify-simple-perl_0.13-1.debian.tar.xz
Summary  : 'Simple and dumb file system watcher'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Filesys-Notify-Simple-license = %{version}-%{release}
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

%description dev
dev components for the perl-Filesys-Notify-Simple package.


%package license
Summary: license components for the perl-Filesys-Notify-Simple package.
Group: Default

%description license
license components for the perl-Filesys-Notify-Simple package.


%prep
%setup -q -n Filesys-Notify-Simple-0.13
cd ..
%setup -q -T -D -n Filesys-Notify-Simple-0.13 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Filesys-Notify-Simple-0.13/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Filesys-Notify-Simple
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Filesys-Notify-Simple/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Filesys-Notify-Simple/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Filesys/Notify/Simple.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Filesys::Notify::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Filesys-Notify-Simple/LICENSE
/usr/share/package-licenses/perl-Filesys-Notify-Simple/deblicense_copyright
