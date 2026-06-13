
#here is how it should work
#first, the bash file, whether python is installed or not, it will first check the linux distro type to see what command it should use, 
#so in both case, it will make
#sure python is installed whatever the situation
#the bash script, for now, should detect only 3 main distro types, considering that python3 is installed on your system : 
# ---- Debian/Ubuntu => sudo apt-get install  python3-pip python3-venv
# ---- fedora/fedora-based => sudo dnf install python3-pip
# ---- RedHat/Rocky/Alma/CentOS => sudo dnf install python3-pip python3-devel 
# Arch/Arch-based => sudo pacman -S python python-pip 
## Note : those are the only distros and sub-distros that we support for now, we are still working on others
## Warning : Right now we are only testing this on Ubuntu WSL, but we plan to expand testing to other distributions in the future.
##How can we detect the distro type in a bash file??
#first, we can't use lsb_release -a since this is only available on ubuntu and debian, however, it is possible to use cat /etc/os-release
#the variable we are looking for should be ID.
#!/bin/bash
echo "Detecting the type of the distro"
if [ -f /etc/os-release] then ;
    if grep -q "ID=ubuntu" /etc/os-release; then
        echo "Ubuntu/Debian detected"
        sudo apt-get install python3-pip python3-venv
    elif grep -q "ID=fedora" /etc/os-release ; then
        echo "Fedora-based distro detected"
        sudo dnf install python3-pip
    elif grep -q "ID=centos" /etc/os-release ; then
        echo "CentOS/RHEL-based distro detected"
        sudo dnf install python3-pip python3-devel
    elif grep -q "ID=arch" /etc/os-release ; then
        echo "Arch-based distro detected"
        sudo pacman -S python python-pip
    else
        echo "Distro not detected, please install python3 and pip manually"

    fi
echo "creating and activating  environement"
python -m venv env
source env/bin/activate
echo "Installing Pyside6"
pip3 install pyside6
echo "pyside is installed ! attempting to restart the module..."
python3 main_gui.py

