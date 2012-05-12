%define modname		panels
%define drupal_version	7
%define module_version	3.2
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Panels module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
Requires:	drupal-ctools

%description
The Panels module allows a site administrator to create customized layouts
for multiple uses. At its core it is a drag and drop content manager that lets
you visually design a layout and place content within that layout. Integration
with other systems allows you to create nodes that use this, landing pages
that use this, and even override system pages such as taxonomy and the node
page so that you can customize the layout of your site with very fine grained
permissions.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%defattr(644,root,root,755)
%{_var}/www/drupal/modules/%{modname}
%doc CHANGELOG.txt KNOWN_ISSUES.txt README.txt UPGRADE.txt
