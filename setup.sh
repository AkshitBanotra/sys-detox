#!/usr/bin/env bash

#############################################################

service_path="${HOME}/.config/systemd/user/sys-detox.service"
sound_path="${HOME}/sys-detox/sounds/Positive.ogg"

##############################################################

# If the sys-detox.service file doesn't exist, then it will create it...

if [[ ! -f ${service_path} ]];then
	cat > ${service_path} << EOF
[Unit]
Description=sys-detox scanner

[Service]
ExecStart=${HOME}/sys-detox/scanner.sh
Restart=always

[Install]
WantedBy=default.target
EOF
	systemctl --user daemon-reload
	systemctl --user enable sys-detox
	systemctl --user start sys-detox
	notify-send "sys-detox configured!"
	paplay "${sound_path}"
else
	echo "sys-detox is already configured!"
fi
