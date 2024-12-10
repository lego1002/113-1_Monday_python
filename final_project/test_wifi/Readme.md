# LEGO EV3 Connect to PC by Using MQTT

## Motivation and Introduction
I undertook this project as part of my Python lecture. Our main goal was to build a smart trash can. We used YOLOv8 to train a trash image recognition model, and I was responsible for the hardware. I built a large trash can using LEGO parts, which includes four doors to classify different types of trash. The system is controlled by an EV3 running MicroPython.

## Experience Sharing
Initially, I wanted to use Arduino to construct all the hardware. However, I realized that regardless of whether we used 3D printing, acrylic, or even chopsticks to build a large trash can, these methods had significant drawbacks, such as consuming too much time, being inconvenient to carry, or having weak structural integrity.

As a big fan of LEGO, I thought it would be ideal for connecting everything seamlessly. That's how this idea came about.

Unfortunately, I had never used MicroPython on EV3 before, so I spent a lot of time on trial and error. My initial idea was to use USB serial communication to connect EV3 and PC, but no suitable library supports this.

Luckily, I found this [video tutorial](https://www.youtube.com/watch?v=UIqabk5VxZ0) and its corresponding [GitHub repository](https://github.com/JorgePe/ev3-mqtt-micropython/).

Words cannot fully describe my struggle—I even nearly failed my Engineering Mathematics test because of this project!

Here, I record the problems I faced and my learning process:

---

### 1. Mosquitto

1. **Install Mosquitto Clients:**
   ```bash
   sudo apt install mosquitto-clients
   ```

2. **Find the IP Address of Your PC:**
   ```bash
   ip a
   ```

3. **Check if Mosquitto Is Running:**
   ```bash
   systemctl status mosquitto.service
   ```

4. **Verify Mosquitto Settings:**
   ```bash
   sudo ss -tuln | grep 1883
   ```
   This command should return something like `1883`.

5. **If Port 1883 Is Not Open:**
   Open the Mosquitto configuration file:
   ```bash
   sudo vim /etc/mosquitto/mosquitto.conf
   ```
   Add these lines:
   ```text
   listener 1883
   allow_anonymous true
   ```

6. **Restart Mosquitto:**
   ```bash
   sudo systemctl restart mosquitto
   ```

7. **Check EV3 Connection to PC:**
   ```python
   import os
   response = os.system("ping -c 1 192.168.1.170")
   if response == 0:
       print("PC is reachable")
   else:
       print("PC is not reachable")
   ```

8. **Publish Messages:**
   Use the following command in the terminal to publish messages:
   ```bash
   mosquitto_pub -h [PC_IP_ADDRESS] -t TOPIC/MESSAGE -m [PARAMETERS]
   ```

---

### 2. EV3 Doesn't Have the `umqtt` Library?!

#### (a) **Wrong Environment**
I mistakenly used this shebang:
```bash
#!/usr/bin/env python3
```
However, for EV3 MicroPython, the correct shebang is:
```bash
#!/usr/bin/env pybricks-micropython
```
This line is critical because EV3 treats the program as a script, and this line ensures it recognizes and executes it correctly.

#### (b) **Missing `umqtt` Libraries**
The process to resolve this was complex and took significant trial and error. Here's what worked:

1. Create the necessary directories:
   ```bash
   mkdir -p /home/robot/lib/umqtt
   ```
   Then, create an empty `__init__.py` file in the folder to signal it's a package.

2. Transfer `simple.py` and `robust.py` to EV3:
   Use the `scp` command to send the files:
   ```bash
   scp -r simple.py robust.py robot@<EV3_IP>:/home/robot/lib/umqtt
   ```
   These files can be found on the [MicroPython GitHub repository](https://github.com/micropython/micropython-lib/tree/master).

3. Modify the second line in `robust.py`:
   ```python
   from umqtt.simple import MQTTClient
   ```
   This small change worked for me, though I'm unsure of the underlying differences.

4. Understanding the `from umqtt.robust` Syntax:
   I'm still uncertain whether it refers to a file, library, or something else. This requires further research.

#### (c) **Coding Issues**
Add this line to avoid encoding errors:
```python
# -*- coding: utf-8 -*-
```

---

It's now 2024/12/11, 3:01 AM. I am exhausted.

---