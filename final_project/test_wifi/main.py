#!/usr/bin/env pybricks-micropython
# -*- coding: utf-8 -*-

from umqtt.robust import MQTTClient
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Direction
import sys
sys.path.append('/home/robot/lib')

print(sys.path)
from umqtt.robust import MQTTClient

# initialize EV3 and motors
ev3 = EV3Brick()
motor_a = Motor(Port.A, Direction.CLOCKWISE)
motor_b = Motor(Port.B, Direction.CLOCKWISE)
motor_c = Motor(Port.C, Direction.CLOCKWISE)
motor_d = Motor(Port.D, Direction.CLOCKWISE)

# MQTT settings
BROKER_IP = "172.20.10.2"  # our pc's ip
TOPIC = "control/motor"      # MQTT topic

def message_callback(topic, msg):
    try:
        count = int(msg.decode('utf-8'))
        if count == 1:
            motor_a.run_target(100, 75)
        elif count == 2:
            motor_b.run_target(100, 75)
        elif count == 3:
            motor_c.run_target(100, 75)
        elif count == 4:
            motor_d.run_target(100, -75)
        else:
            print("Invalid count received:", count)
            return

        wait(2000)

        if count == 1:
            motor_a.run_target(100, 0)
        elif count == 2:
            motor_b.run_target(100, 0)
        elif count == 3:
            motor_c.run_target(100, 0)
        elif count == 4:
            motor_d.run_target(100, 0)

    except ValueError:
        print("Invalid message:", msg)

# initialize MQTT client
client = MQTTClient("EV3_Motor_Client", BROKER_IP)

client.set_callback(message_callback)

print("Connecting to broker...")
client.connect()
print("Connected.")


client.subscribe(TOPIC)
print("Subscribed to topic {}.".format(TOPIC))

try:
    while True:
        client.wait_msg()
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()
