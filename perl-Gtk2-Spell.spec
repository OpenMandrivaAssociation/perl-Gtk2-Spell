%define module Gtk2-Spell
%define fmodule Gtk2/Spell

Summary: Perl module for the gtkspell library
Name:    perl-%module
Version: 1.03
Release: %mkrel 7
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  http://ovh.dl.sourceforge.net/sourceforge/gtk2-perl/%module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/

BuildRequires: gtkspell-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-Gtk2 
BuildRequires: perl-Glib > 1.00 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: glitz-devel
Buildrequires: perl-devel

Requires: gtk+2

%description
This module provides perl access to the gtkspell library.

The GtkSpell graphical user interface library allow to write applications that
highlight mis-spelled words.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc LICENSE gtkspell_simple.pl
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/Spell*
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule

