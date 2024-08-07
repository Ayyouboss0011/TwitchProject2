#!/usr/bin/env bash

# If VNC_PASSWORD is not set, use a default password
: ${VNC_PASSWORD:=}
echo "Current vnc password is: ${VNC_PASSWORD}"

# Store the password
if [ "$VNC_PASSWORD" ]; then
    sed -i "s/^\(command.*x11vnc.*\)$/\1 -passwd '$VNC_PASSWORD'/" /etc/supervisord.conf
fi

# If VNC_RESOLUTION is not set, use a default resolution
: ${VNC_RESOLUTION:=400x400}
echo "Current VNC resolution is: ${VNC_RESOLUTION}"

# If STARTING_WEBSITE_URL is not set, use a default website
: ${STARTING_WEBSITE_URL:=https://twitch.tv/einsamerigel}
echo "Current starting website is: ${STARTING_WEBSITE_URL}"

# Start Supervisor
exec supervisord -c /etc/supervisord.conf
