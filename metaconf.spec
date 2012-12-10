Name: metaconf
Version: 1.3.1
Release: %mkrel 11
License: GPL
Group: System/Configuration/Other
Summary: Maintains multiple configurations in the same machine
Source: metaconf-%{version}.tar.bz2
Patch0:  metaconf-use_our_arping.patch
URL: http://niemeyer.net/metaconf
Requires(post,preun): rpm-helper
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildArch: noarch 

%description
metaconf is a generic software for maintenance of multiple
configurations in a single machine. One of its main uses is for
notebook users which need mobility between several places, but
unlike other similar softwares, metaconf is not designed to work
specifically with network configurations. Indeed, it may be used
to alternate between almost any kind of configuration, as far as
the user knows how to configure the softwares properly.

%prep
%setup -q 
%patch0 -p0

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

mkdir -p %{buildroot}%{_bindir} %{buildroot}/%{_initrddir}
install -m 755 contrib/metaconf-chooser.sh %{buildroot}%{_bindir}/
install -m 755 contrib/metaconf.init %{buildroot}%{_initrddir}/%{name}
install -m 755 contrib/metaconf-autochooser.sh %{buildroot}%{_bindir}/
install -m 600 contrib/metaconf.macs %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE doc/metaconf.moin
%defattr(-,root,root)
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/metaconf.macs
%{py_puresitedir}/*
%{_initrddir}/metaconf

%post
%_post_service metaconf

%preun
%_preun_service metaconf




%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.3.1-11mdv2011.0
+ Revision: 598843
- fix file list

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - rebuild for python 2.7

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-10mdv2010.0
+ Revision: 439798
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.3.1-9mdv2009.1
+ Revision: 325695
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.3.1-8mdv2009.0
+ Revision: 252335
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Olivier Blin <oblin@mandriva.com> 1.3.1-6mdv2008.1
+ Revision: 117690
- update URL


* Fri Mar 16 2007 Michael Scherer <misc@mandriva.org> 1.3.1-5mdv2007.1
+ Revision: 144936
- Rebuild for new python
- Import metaconf

* Thu Dec 08 2005 Michael Scherer <misc@mandriva.org> 1.3.1-4mdk
- use macro for etc/init.d and rpm-helper script
- use blino patch ( close #18255 )

* Mon Nov 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.3.1-3mdk
- Fix BuildRequires
- %%mkrel

* Fri Jun 17 2005 Gustavo Niemeyer <gustavo@niemeyer.net> 1.3.1-2mdk
- Adding prereq on rpm-helper.

* Fri Jun 17 2005 Gustavo Niemeyer <gustavo@niemeyer.net> 1.3.1-1mdk
- New upstream Version: 1.3.1
- Including add/del-service calls.

* Fri Jun 17 2005 Gustavo Niemeyer <gustavo@niemeyer.net> 1.3-1mdk 
- New upstream version: 1.3

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 1.2-2mdk
- Rebuild for new python

* Sat Apr 24 2004 Michael Scherer <misc@mandrake.org> 1.2-1mdk
- first package

