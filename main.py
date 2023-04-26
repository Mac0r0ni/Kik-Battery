import random

battery_level = rand.int(0, 100)
if battery_level < 51:
    plugged_in = "NOT PLUGGED IN"
else:
    plugged_in = "PLUGGED IN"
self.client.send_chat_message(group_jid, f"Battery level: {battery_level}% ({plugged_in})")
