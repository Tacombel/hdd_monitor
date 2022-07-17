Simple script to add your hdd temperatures to Home Assistant.

Copy the two files to a directory.

Install hddtemp

Get a "Long lived access token" from your Home Assistant Dashboard.

Edit the config.py to your needs.

Add a cron job to your root crontab. Needs root access to read the temperatures

* * * * * sudo python3 /path_to_script/hdd_monitor.py

The entities will be named server_temp_disk

-----------------------------------------------

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
