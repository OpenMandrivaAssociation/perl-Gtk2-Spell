%define upstream_name    Gtk2-Spell
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl module for the gtkspell library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    http://ovh.dl.sourceforge.net/sourceforge/gtk2-perl/%upstream_name-%upstream_version.tar.bz2
Patch0:     Gtk2-Spell-1.03.diff
BuildRequires: glitz-devel
BuildRequires: gtkspell-devel 
BuildRequires: perl-ExtUtils-Depends 
BuildRequires: perl-ExtUtils-PkgConfig 
BuildRequires: perl-Gtk2 
BuildRequires: perl-Glib > 1.00 
Buildrequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: gtk+2

%description
This module provides perl access to the gtkspell library.

The GtkSpell graphical user interface library allow to write applications that
highlight mis-spelled words.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
find -type d -name CVS | rm -rf 

%build
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="%optflags -Os -s"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc LICENSE gtkspell_simple.pl
%{_mandir}/*/*
%{perl_vendorarch}/Gtk2/*
%{perl_vendorarch}/auto/Gtk2/*
