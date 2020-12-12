import time
from lib.system.servo import SG90_92R_Class

Servo = SG90_92R_Class(Channel=0, ZeroOffset=0)
try:
    while True:
        Servo.SetPos(0)
        print(0)
        time.sleep(1)
        Servo.SetPos(90)
        print(90)
        time.sleep(1)
        Servo.SetPos(180)
        print(180)
        time.sleep(1)
        Servo.SetPos(90)
        print(90)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCtl+C")
except Exception as e:
    print(str(e))
finally:
    Servo.Cleanup()
    print("\nexit program")
