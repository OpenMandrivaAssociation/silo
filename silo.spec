%define	name	silo
%define	version	1.4.13
%define	release	%mkrel 1

Summary:	The SILO boot loader for SPARCs
Summary(fr):	Chargeur de boot Linux pour SPARCs
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
ExclusiveArch:	%{sunsparc}
Group:		System/Kernel and hardware
Url:		http://sparc-boot.org/
Source0:	http://www.sparc-boot.org/pub/%{name}/%{name}-%{version}.tar.bz2
Patch0:		silo-1.2.4-ext3.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	e2fsprogs-devel elftoaout
Provides:       bootloader

%description
The silo package installs the SILO (Sparc Improved LOader) boot
loader, which you'll need to boot Mandriva Linux on a SPARC.  SILO
installs onto your system's boot block and can be configured to boot
Linux, Solaris and SunOS.

%description -l fr
Le paquetage silo installe le chargeur de boot SILO (Sparc Improved
LOader) dont vous avez besoin pour démarrer Mandriva Linux sur une
SPARC.  SILO s'installe sur le "boot block" de votre système et peut
être configuré pour démarrer Linux, Solaris et SunOS.

%prep 
%setup -q
%patch0 -p0 -b .ext3

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
/boot/*.b
%config(noreplace) %{_sysconfdir}/%{name}.conf
%defattr(755,root,root,755)
/sbin/%{name}
%{_sbindir}/silocheck
%{_bindir}/*
%{_mandir}/*/*
 
