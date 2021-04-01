import machine
import time
from pcf8591 import PCF8591
sda=machine.Pin(0)
scl=machine.Pin(1)
i2c_pose = machine.I2C(0,sda=sda, scl=scl, freq=400000)
print(i2c_pose)
print(i2c_pose.scan())
sda=machine.Pin(2)
scl=machine.Pin(3)
i2c_temp =machine.I2C(1,sda=sda, scl=scl, freq=400000)
print(i2c_temp.scan())
pc1 = PCF8591(i2c_pose,0x48)
#ADC_POSE_arm1 = PCF8591(i2c_pose,0x48)
#ADC_TEMP_arm1 = PCF8591(i2c_temp,0x48)
#ARM arm1 (PCF8591(i2c_pose,0x48), PCF8591(i2c_temp,0x48))

PC1.write(100)
print(PC1.read(0))
time.sleep(0.3)
PC1.write(0)
print(PC1.read(0))
