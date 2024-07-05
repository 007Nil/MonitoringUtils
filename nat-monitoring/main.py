import os
import modules.monitor_battery as mb 
def main():
    os.system("amixer set Master 100% unmute > /dev/null")
    os.system("amixer set PCM 100% unmute > /dev/null")
    mb.monitor_power_supply()


if __name__ == "__main__":
    main()
