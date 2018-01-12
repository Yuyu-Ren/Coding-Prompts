import os
import time


# enter relevant info here.
key = ""
channel_id = ""
message =  ""


def send_message(channel_id = "", message = "", key = ""):
    command = '''curl 'https://discordapp.com/api/v6/channels/''' + str(
        channel_id) + '''/messages' -H 'authorization: ''' \
              + key + ''' ' -H 'content-type: application/json' --data-binary '{"content":"''' + str(message) \
              + '''"}' --compressed'''
    os.system(command)


send_message(channel_id, message, key)
time.sleep(10)
