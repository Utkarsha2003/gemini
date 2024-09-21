# Import the pywhatkit library
import pywhatkit as kit
import time

# Phone numbers to send messages to
phone_numbers = [
    "+916207466694",
    "+919263541538",
]  # Add the numbers you want to message

# Message to be sent
message_text = "Hello, this is a test message."

# Loop through the list of phone numbers and send the message
for phone_number in phone_numbers:
    kit.sendwhatmsg_instantly(phone_number, message_text, 15, True, 3)
    time.sleep(5)
    print(f"Message sent to {phone_number}")
