# KeyChronicle

## Description

This Python program is designed to log keystrokes as well as the date and time at regular intervals. It employs the keyboard library to capture key presses and the datetime and time libraries to log the date and time.

Here's a breakdown of what it does:

1. It imports the necessary libraries: keyboard, datetime, and time.
2. Defines an output file named 'KeyChronicleData.txt' where the logged information will be stored.
3. Defines a function save_key(e) to capture and save the keystrokes to the output file in real time.
4. Sets up a listener using keyboard.on_press(save_key) to trigger the save_key function whenever a key is pressed.
5. Defines a function log_date_time() to log the current date and time every minute and writes this information to the output file.
6. Utilizes a loop and the time.sleep(60) function to call the log_date_time function at regular intervals of 60 seconds (1 minute).
7. Starts logging the date and time every one minute and waits for the keyboard input using keyboard.wait().

Overall, the program continuously logs keystrokes and appends the current date and time every minute to the specified output file 'KeyChronicleData.txt'. 📝⌨️🕒

## How to use it

This program is a simple keylogging script written in Python. It uses the keyboard library to capture keystrokes and log them to a file with a timestamp.

To use this program, you need to have Python installed on your computer. Once Python is installed, you can follow these steps:

1. Install the required keyboard library using pip:
   pip install keyboard
   pip install datetime
   pip install time

2. run it using Python:
   python KeyChronicle.py

Once you run the script, it will start recording keystrokes and saving them, along with the current date and time, to a file called KeyChronicleData.txt in the same directory as the script.

However, please be aware that monitoring and logging keystrokes without proper authorization may violate privacy and security laws, and it can be unethical. It's important to use this kind of software responsibly and only where it is legal and ethical to do so. 👍
