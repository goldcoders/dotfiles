# installed larbs dwm version

# add downgrade command
- lock kernel on 5.3.13-arch1-1
- remove lts kernel
- installed pamac-aur-git

# fix wifi issue
- installed lts kernel and lts-headers

# added huawei specifics
- make sure you are running kernel 5.3.1
- installed huawei-wmi
- patch huawei-wmi https://github.com/qu1x/huawei-wmi
- install debtap
- install ioport https://ubuntu.pkgs.org/19.10/ubuntu-universe-amd64/ioport_1.2-1_amd64.deb.html
- added batpro script

# fix brightness control
- installed brightnessctl-git
- bind keys it using sxhkd

# fix mouse tap
- https://wiki.archlinux.org/index.php/Libinput
- add tap to mouse 1,m,r

# added fusuma touchpad gestures
- added fusuma-git in .profile
- https://github.com/iberianpig/fusuma
- added swipe 3 fingers for zoom, navigate
- swipe 4 fingers to add tab and close tab in windows up and down
- swipe 4 fingers left and right to switch workspace prev and next

# fix ncmcpp no sound
- added pulseaudio , pulseaudio-alsa , pulseaudio-bluetooth

# update compositor
- install picom-git, unintall xcompmgr
- cp default picom config

# dust configured
- added ctrl space to clear all notifications
- added mod shift v to show all notications one by one

# add bluetooth
- install blueberry
- pulseaudio-bluetooth
- pulseaudio-alsa
- bluez-utils
- bluez-libs
- bluez
- pulseaudio-alsa
- alsa-utils
- alsa-tools
- alsa-plugins
- pavucontrol
- playerctl
- bluez-alsa-git
- SS enable bluetooth

# added newsboat settings
- themed config

# enable high quality audi
- https://medium.com/@gamunu/enable-high-quality-audio-on-linux-6f16f3fe7e1f
- https://www.youtube.com/watch?v=DLP-peyMLq0

# fix mpd and ncmcpp visulizer
- https://wiki.archlinux.org/index.php/ncmpcpp#Enabling_visualization
- fix config of ncmcpp and mpd
# fix ranger extract
- we ln -s ext extract on scripts bin
# fix mouse issue
- remember to upload your cursor on .icons
- any icons installed to /usr/share is not fixed and will not persist by lxappearance

# add i3-swallow command
- now we can press "o" then type command on any terminal then it will swallow that space
# fix crontog
- installed cronie
# added to nemo open in terminal
- gsettings set org.cinnamon.desktop.default-applications.terminal exec st
# Pomodoro
- installed i3-gnome-pomodoro
- installed gnome-pomodoro
- add command on i3config to show status


## fix shxkd & i3config
- remove unncessary keys in i3config
- added keys in i3config not working in sxhkd
- remodify keys


## TODO
- Patch dwm to use shallow

## Force BAT on tlp /etc/default/tlp
- TLP_DEFAULT_MODE=BAT
- TLP_PERSISTENT_DEFAULT=1

## Bumblebee with Nvidia Driver /etc/default/tlp
- RUNTIME_PM_BLACKLIST="01:00.0"
- RUNTIME_PM_DRIVER_BLACKLIST="nouveau nvidia"

## hybernate on low bat /etc/udev/rules/d/99-lowbat.rules
- SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", ATTR{capacity}=="[0-5]", RUN+="/usr/bin/systemctl hibernate"
## add i915 on /etc/mkinitcpio.conf
= Module = (i915)

## readit https://aymanbagabas.com/2018/07/23/archlinux-on-matebook-x-pro.html
## added for powersaving /etc/modprobe.d/audio_powersave.conf
- options snd_hda_intel power_save=1

## added power saving /etc/modprobe.d/i915.conf
- options i915 enable_guc=3 enable_fbc=1

## Revert all changes in tlp modprobe

## follow 2 steps here that enable nvidia https://aymanbagabas.com/2018/07/23/archlinux-on-matebook-x-pro.html
-  sudo vim /etc/bumblebee/bumblebee.conf set [driver-nvidia] PMMethod=bbswitch
- sudo vim /etc/bumblebee/xorg.conf.nvidia , uncomment BusID

## enabled multilip in pacman.conf so we can install other packages needed
- uncomment #[multilib]
- #Include = /etc/pacman.d/mirrorlist

 ## installed new
 - acpi_call
 - lib32-virtualgl
 - lib32-nvidia-utils

## fix zsh history set to 1m
- added HISTFILE
- added HISTSIZE
- added SAVEHIST

## remove /etc/rc.local
- https://support.system76.com/articles/battery/

## added xprofile check for nvidia
- https://tonymugen.github.io/ArchLinuxSys76OP.html#nvidia-set-up
- https://ebobby.org/2018/08/06/archlinux-nvidia-on-oryp4#usingadesktopmanager

## added fonts
- ttf-twemoji-color
- ttf-joypixels
- ttf-ms-fonts
- noto-fonts-emoji

## use all cores when compiling code
- https://github.com/arcolinuxd/arco-plasma/blob/master/000-use-all-cores-makepkg-conf-v4.sh

## Android set up
- flutter-git
- select java 8
- npm global EACCESS - https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
- android-sdk
- android-emulator
- android-sdk-platform-tools
- add .zshrc paths

## create flutterusers
groupadd flutterusers
Add your user into this group:
gpasswd -a <user> flutterusers
Change folder's group.
chown -R :flutterusers /opt/flutter
Change permissions of the folder so the user that was just add
chmod -R g+w /opt/flutter
Re-login your terminal in to the newly created group:
newgrp flutterusers

## adbusers
sudo gpasswd -a uriah adbusers
## fix /opt/androids-sdk
- ownthis
## fix tmp too small
- sudo mount -o remount,size=8G,noatime /tmp;
- https://bytefreaks.net/applications/android-studio-no-space-left-on-device

## set nativescript
- https://docs.nativescript.org/angular/start/ns-setup-linux

## create virtual device
- https://docs.nativescript.org/angular/tooling/android-virtual-devices
- emul_add
- but first run install_system_images.sh
- then fix ##tmp
## fix java home
- https://wiki.archlinux.org/index.php/Android#Java_Development_Kit

## fix android group writable
- https://wiki.archlinux.org/index.php/Android#Making_.2Fopt.2Fandroid-sdk_group-writeable

## Installed all android packages
- https://wiki.archlinux.org/index.php/Android#SDK_packages
## fix flutter doctor licenses not working
- sdkmanager --licenses
## TODO
- https://wiki.archlinux.org/index.php/Android_Debug_Bridge

## Installed KDE connect
- kdeconnect
- indicator-kdeconnect

## enable on i3config kdeconnecd
- exec --no-startup-id /usr/lib/kdeconnectd
- exec --no-startup-id /usr/bin/indicator-kdeconnect

## install srccpy
- run srccpy
- connect usb and phone
- enjoy

## fix pamac authentication error
- add to i3 polkit policy daemon
- https://forum.manjaro.org/t/pamac-manager-issues/9813/29
## fix wifi
- installed crda

# fix wifi
- delete bumbleed
- delete primus
- delete tlp

# fix gnome slow apps after flatpak installed
- change .xinitrc
- added : dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY

# fix fusuma
- added to input group
- sudo gpasswd -a $USER input
- use fusuma on xprofile , remove the sudo
- added gem bin on path so we can load fusuma
- $(ruby -e 'puts Gem.user_dir')/bin

