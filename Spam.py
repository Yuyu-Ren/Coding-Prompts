import os
import time


# enter relevant info here.
key = ""
channel_id = ""
message = ""


def send_message(channel_id = "", message = "", key = ""):
    command = '''curl 'https://discordapp.com/api/v6/channels/''' + str(  # Just sends curl command to command line
        channel_id) + '''/messages' -H 'authorization: ''' \
              + key + ''' ' -H 'content-type: application/json' --data-binary '{"content":"''' + str(message) \
              + '''"}' --compressed'''
    os.system(command)  # sends the properly formatted curl command


send_message(channel_id, message, key)
time.sleep(10)  # Prevent flood delay from Discord from taking effect
