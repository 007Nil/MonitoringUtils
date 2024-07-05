import subprocess
import os
import modules.speech_info as sp

BAT_LOW_THRESHOLD = 40
RUNNING_BAT_FILE = "/tmp/running_on_bat"

def is_running_on_bat():
    bat_status = subprocess.getoutput("cat /sys/class/power_supply/BAT0/status")
    if bat_status.replace("\n", "") == "Discharging":
        return True
    return False

def check_bat_capacity():
    bat_capacity = subprocess.getoutput("cat /sys/class/power_supply/BAT0/capacity")
    return bat_capacity

def monitor_power_supply():
    if is_running_on_bat():
        sp.info_running_on_bat()
        # write a file to infom laptop is on battery
        os.system(f"touch {RUNNING_BAT_FILE}")
        bat_capacity = int(check_bat_capacity())
        if bat_capacity <= BAT_LOW_THRESHOLD:
            sp.alert_bat_critical(bat_capacity)
    else:
        if os.path.isfile(RUNNING_BAT_FILE):
            sp.info_charger_connected()
            os.system("rm -rf /tmp/running_on_bat")

