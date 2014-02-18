from lettuce import step
from lettuce import world

import client

@step ('the message "(\w+)"')
def the_message(step, msg):
    world.string = msg

@step ('i send the message')
def send_message(step):
    client.msgsend(world.string)

@step('the server echoes "(\w+)"')
def server_echo(step, expected):
    assert world.string == expected, "Got %s" % world.string