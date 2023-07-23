sudo rm -r /home/pi/Documents/SciSpin_Max_RELEASE
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
	cd /home/pi/Documents/Restore/SciSpin_Max_RELEASE
	sudo git pull
fi
sudo cp -r /home/pi/Documents/Restore/SciSpin_Max_RELEASE /home/pi/Documents