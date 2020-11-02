#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : powerline-fonts
Version  : 1.2
Release  : 14
URL      : http://localhost/cgit/projects/powerline-fonts/snapshot/powerline-fonts-1.2.tar.gz
Source0  : http://localhost/cgit/projects/powerline-fonts/snapshot/powerline-fonts-1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 OFL-1.0 OFL-1.1
Requires: powerline-fonts-data = %{version}-%{release}
Requires: powerline-fonts-license = %{version}-%{release}

%description
Powerline fonts
===============
This repository contains pre-patched and adjusted fonts for usage with
the new Powerline plugin.

%package data
Summary: data components for the powerline-fonts package.
Group: Data

%description data
data components for the powerline-fonts package.


%package license
Summary: license components for the powerline-fonts package.
Group: Default

%description license
license components for the powerline-fonts package.


%prep
%setup -q -n powerline-fonts-1.2
cd %{_builddir}/powerline-fonts-1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604354212
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604354212
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/powerline-fonts
cp %{_builddir}/powerline-fonts-1.2/AnonymousPro/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/922523145cadbb0141c142e9f76052e6d7e2544d
cp %{_builddir}/powerline-fonts-1.2/DejaVuSansMono/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/a90262f3f77ab67b5b95f505ad1e09bdf8406b36
cp %{_builddir}/powerline-fonts-1.2/DroidSansMono/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/f2a721f0ba643893cf582a0e4ca6728dd7a72784
cp %{_builddir}/powerline-fonts-1.2/FiraMono/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/65437005a79d72b5b8bdcf92a2ff4c4061000185
cp %{_builddir}/powerline-fonts-1.2/Inconsolata-g/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/cd439b2bf8b2e33e8f26a079d039ead4925a4274
cp %{_builddir}/powerline-fonts-1.2/Inconsolata/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/75c39134018d4afb3c50b3ede472a33ee23401ff
cp %{_builddir}/powerline-fonts-1.2/InconsolataDz/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/88c7ef2bce487114f158f515e22bf999bce72804
cp %{_builddir}/powerline-fonts-1.2/LiberationMono/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/303d53c484cd9d503e7666d94a6c7260208f3940
cp %{_builddir}/powerline-fonts-1.2/Meslo/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/8e65cfa675b76cac80432847d50164d115cf62f1
cp %{_builddir}/powerline-fonts-1.2/SourceCodePro/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/486c64e8e44d6b12f3055679f40ab57810049a1c
cp %{_builddir}/powerline-fonts-1.2/Terminus/LICENSE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/eb9af8a5cb9e2c708f9e79d7b37f927135037994
cp %{_builddir}/powerline-fonts-1.2/UbuntuMono/LICENCE.txt %{buildroot}/usr/share/package-licenses/powerline-fonts/959ea919607762464f391a7aa29f82028ae6c3eb
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/X11/OTF/DroidSansMonoforPowerline.otf
/usr/share/fonts/X11/OTF/FuraMono-BoldPowerline.otf
/usr/share/fonts/X11/OTF/FuraMono-MediumPowerline.otf
/usr/share/fonts/X11/OTF/FuraMono-RegularPowerline.otf
/usr/share/fonts/X11/OTF/Inconsolata-dzforPowerline.otf
/usr/share/fonts/X11/OTF/Inconsolata-gforPowerline.otf
/usr/share/fonts/X11/OTF/InconsolataforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGLDZRegularforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGLRegularforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGMDZRegularforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGMRegularforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGSDZRegularforPowerline.otf
/usr/share/fonts/X11/OTF/MesloLGSRegularforPowerline.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineBlack.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineBold.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineExtraLight.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineLight.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineMedium.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineRegular.otf
/usr/share/fonts/X11/OTF/SauceCodePowerlineSemibold.otf
/usr/share/fonts/X11/TTF/AnonymicePowerline.ttf
/usr/share/fonts/X11/TTF/AnonymicePowerlineBold.ttf
/usr/share/fonts/X11/TTF/AnonymicePowerlineBoldItalic.ttf
/usr/share/fonts/X11/TTF/AnonymicePowerlineItalic.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMonoBoldObliqueforPowerline.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMonoBoldforPowerline.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMonoObliqueforPowerline.ttf
/usr/share/fonts/X11/TTF/DejaVuSansMonoforPowerline.ttf
/usr/share/fonts/X11/TTF/LiterationMonoPowerline.ttf
/usr/share/fonts/X11/TTF/LiterationMonoPowerlineBold.ttf
/usr/share/fonts/X11/TTF/LiterationMonoPowerlineBoldItalic.ttf
/usr/share/fonts/X11/TTF/LiterationMonoPowerlineItalic.ttf
/usr/share/fonts/X11/TTF/MonofurBoldforPowerline.ttf
/usr/share/fonts/X11/TTF/MonofurItalicforPowerline.ttf
/usr/share/fonts/X11/TTF/MonofurforPowerline.ttf
/usr/share/fonts/X11/TTF/UbuntuMonoderivativePowerline.ttf
/usr/share/fonts/X11/TTF/UbuntuMonoderivativePowerlineBold.ttf
/usr/share/fonts/X11/TTF/UbuntuMonoderivativePowerlineBoldItalic.ttf
/usr/share/fonts/X11/TTF/UbuntuMonoderivativePowerlineItalic.ttf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/powerline-fonts/303d53c484cd9d503e7666d94a6c7260208f3940
/usr/share/package-licenses/powerline-fonts/486c64e8e44d6b12f3055679f40ab57810049a1c
/usr/share/package-licenses/powerline-fonts/65437005a79d72b5b8bdcf92a2ff4c4061000185
/usr/share/package-licenses/powerline-fonts/75c39134018d4afb3c50b3ede472a33ee23401ff
/usr/share/package-licenses/powerline-fonts/88c7ef2bce487114f158f515e22bf999bce72804
/usr/share/package-licenses/powerline-fonts/8e65cfa675b76cac80432847d50164d115cf62f1
/usr/share/package-licenses/powerline-fonts/922523145cadbb0141c142e9f76052e6d7e2544d
/usr/share/package-licenses/powerline-fonts/959ea919607762464f391a7aa29f82028ae6c3eb
/usr/share/package-licenses/powerline-fonts/a90262f3f77ab67b5b95f505ad1e09bdf8406b36
/usr/share/package-licenses/powerline-fonts/cd439b2bf8b2e33e8f26a079d039ead4925a4274
/usr/share/package-licenses/powerline-fonts/eb9af8a5cb9e2c708f9e79d7b37f927135037994
/usr/share/package-licenses/powerline-fonts/f2a721f0ba643893cf582a0e4ca6728dd7a72784
