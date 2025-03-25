import psutil
import time
import os

def is_charging():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def switch_to_pc_screen_only():
    print("Switching to PC Screen Only...")
    os.system("DisplaySwitch.exe /internal")  # Sets display to PC screen only

def switch_to_extend_screen():
    print("Charging detected! Waiting 5 seconds before extending screen...")
    time.sleep(5)
    print("Switching to Extend Screen...")
    os.system("DisplaySwitch.exe /extend")  # Sets display to Extend mode

def main():
    last_state = is_charging()
    
    while True:
        current_state = is_charging()
        
        if last_state and not current_state:  # Charging was ON, now OFF
            switch_to_pc_screen_only()
        
        elif not last_state and current_state:  # Charging was OFF, now ON
            switch_to_extend_screen()
        
        last_state = current_state
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
