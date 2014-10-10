%define upstream_name    Gtk2-Spell
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

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


%changelog
* Wed Jan 25 2012 Per √òyvind Karlsen <peroyvind@mandriva.org> 1.30.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 1.30.0-2mdv2011.0
+ Revision: 556797
- add fedora patch to get it build

* Mon Aug 03 2009 J√©r√¥me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 408463
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.03-10mdv2009.0
+ Revision: 257183
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.03-8mdv2008.1
+ Revision: 152114
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 1.03-7mdv2008.0
+ Revision: 43104
- rebuild


* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.03-6mdk
- arg bad work again :(

* Fri Sep 30 2005 Nicolas LÈcureuil <neoclust@mandriva.org> 1.03-5mdk
- Add buildrequires
- mkrel
- add better source url

* Sun Feb 06 2005 Sylvie Terjan <erinmargault@mandrake.org> 1.03-4mdk
- rebuild for new perl
- buildrequires on perl-ExtUtils-PkgConfig

* Fri Aug 13 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-3mdk
- rebuild for perl-5.8.5
- relink against libapspell rather than libpspell

* Fri Apr 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-2mdk
- fix summary
- fix build

* Sat Jan 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.03-1mdk
- new release
- nename spec file

* Wed Aug 20 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.0-1mdk
- new release

* Mon Jul 14 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.cvs.2003.07.04.1-1mdk
- xs snapshot

