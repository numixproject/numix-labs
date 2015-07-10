%global theme	Numix

Name:		numix-gtk-theme
%if 0%{?fedora} < 21
Version:	2.2.3
%else
Version:	2.5.1
%endif
Release:	12.1
Summary:	%{theme} GTK theme for Gnome, Xfce and Openbox
Group:		User Interface/Desktops

License:	GPL-3
URL:		http://fav.me/d5ygul6

%if 0%{?fedora} < 21
Source0:	v2.2.3.tar.gz
%else
Source0:	v2.5.1.tar.gz
%endif

%if 0%{?suse_version}
Requires:	gtk2-engine-murrine >= 0.98.1.1
%else
Requires:	gtk-murrine-engine >= 0.98.1.1
%endif
Requires:	gtk3 >= 3.6.0

BuildArch:	noarch

%description
%{theme} is a modern flat theme with a combination of light and dark elements.
It supports Gnome, Unity, XFCE and Openbox.


%prep
%if 0%{?fedora} < 21
%setup -q -n %{theme}-2.2.3
%else
%setup -q -n %{theme}-2.5.1
%endif

%build
# Nothing to build


%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/%{theme}
for file in gtk-2.0 gtk-3.0 metacity-1 openbox-3 unity xfce-notify-4.0 xfwm4 index.theme; do
	%{__cp} -pr ${file} %{buildroot}%{_datadir}/themes/%{theme}
done


%files
%defattr(-,root,root)
%doc CREDITS LICENSE README.md
%{_datadir}/themes/%{theme}


%changelog
* Sat Sep 21 2013 Satyajit Sahoo <satya164@fedoraproject.org> - 2.0-1
- Initial package for Fedora
