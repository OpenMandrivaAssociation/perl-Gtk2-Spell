%define upstream_name    Gtk2-Spell
%define upstream_version 1.05

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:	1

Summary:    Perl module for the gtkspell library

License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        https://gtk2-perl.sf.net/
Source0:    https://cpan.metacpan.org/authors/id/X/XA/XAOC/Gtk2-Spell-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires: glitz-devel
BuildRequires: gtkspell-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: perl-Gtk2 
BuildRequires: perl-Glib > 1.00 
Buildrequires: perl-devel

Requires: gtk+2

%description
This module provides perl access to the gtkspell library.

The GtkSpell graphical user interface library allow to write applications that
highlight mis-spelled words.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%{optflags} -Os -s"

%install
%makeinstall_std

%clean

%files
%doc LICENSE gtkspell_simple.pl
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/Gtk2/*
