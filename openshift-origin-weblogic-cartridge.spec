%global cartridgedir %{_libexecdir}/openshift/cartridges/weblogic

Name: 		openshift-origin-weblogic-cartridge
Version:	12.1.3
Release:	1%{?dist}
Summary:	Oracle WebLogic Server is a Java EE application server developed by Oracle Corporation.

Group:		Development/Languages
License:	Proprietary
URL:	 	http://oracle.com	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	x86_64

Requires:	ant
Requires:	java

%define _unpackaged_files_terminate_build 0


%description
Oracle WebLogic Server is a Java EE application server developed by Oracle Corporation.

%prep
%setup -q


%build


%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}/%{cartridgedir}
%__cp -r * %{buildroot}/%{cartridgedir}

%clean
rm -rf %{buildroot}


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/container-scripts/
%{cartridgedir}/env
%{cartridgedir}/template
%{cartridgedir}/metadata
%{cartridgedir}

%changelog


