%global theme   Numix

Name:       numix-gtk-theme
Version:    0.0.1
Release:    0%{?dist}
Summary:    %{theme} GTK theme for Gnome, Xfce and Openbox
Group:      User Interface/Desktops

License:    GPL-3
URL:        http://fav.me/d5ygul6

Source0:    %{theme}-%{version}.tar.gz

Requires:   gtk-murrine-engine >= 0.98.1.1
Requires:   gtk3 >= 3.10.0

BuildArch:  noarch

%description
%{theme} is a modern flat theme with a combination of light and dark elements.
It supports Gnome, Unity, XFCE and Openbox.


%prep
%setup -q -n %{theme}-%{version}

%build
make %{?_smp_mflags}


%install
%make_install


%files
%defattr(-,root,root)
%doc CREDITS LICENSE README.md
%{_datadir}/themes/%{theme}


%changelog
* Sat Sep 21 2013 Satyajit Sahoo <satya164@fedoraproject.org> - 2.0-1
- Initial package for Fedora
