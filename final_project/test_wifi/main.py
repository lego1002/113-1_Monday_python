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

# 初始化 EV3 和马达
ev3 = EV3Brick()
motor_a = Motor(Port.A, Direction.CLOCKWISE)
motor_b = Motor(Port.B, Direction.CLOCKWISE)
motor_c = Motor(Port.C, Direction.CLOCKWISE)
motor_d = Motor(Port.D, Direction.CLOCKWISE)

# MQTT 配置
BROKER_IP = "192.168.1.170"  # 替换为你的电脑 IP 地址
TOPIC = "control/motor"      # MQTT 主题

# 定义消息回调函数
def message_callback(topic, msg):
    try:
        # 解码消息并转换为整数
        count = int(msg.decode('utf-8'))
        if count == 1:
            motor_a.run_target(100, 75)  # A 马达顺时针转 75 度
        elif count == 2:
            motor_b.run_target(100, 75)  # B 马达顺时针转 75 度
        elif count == 3:
            motor_c.run_target(100, 75)  # C 马达顺时针转 75 度
        elif count == 4:
            motor_d.run_target(100, -75)  # D 马达顺时针转 75 度
        else:
            print("Invalid count received:", count)
            return

        wait(5000)  # 等待 5 秒

        # 转回初始位置
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

# 初始化 MQTT 客户端
client = MQTTClient("EV3_Motor_Client", BROKER_IP)

# 设置回调函数
client.set_callback(message_callback)

# 连接到 MQTT Broker
print("Connecting to broker...")
client.connect()
print("Connected.")

# 订阅主题
client.subscribe(TOPIC)
print("Subscribed to topic {}.".format(TOPIC))

# 循环接收消息
try:
    while True:
        # 等待消息
        client.wait_msg()
except KeyboardInterrupt:
    print("Disconnecting...")
    client.disconnect()
