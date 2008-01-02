Name: metaconf
Version: 1.3.1
Release: %mkrel 6
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

find %{buildroot} -name '*.pyc' -name '*.pyo' -exec rm -f {} \;

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(0644,root,root,0755)
%doc LICENSE doc/metaconf.moin
%defattr(-,root,root)
%{_bindir}/metaconf-chooser.sh
%{_bindir}/metaconf-autochooser.sh
%config(noreplace) %{_sysconfdir}/metaconf.macs
%{_initrddir}/metaconf

%post
%_post_service metaconf

%preun
%_preun_service metaconf


