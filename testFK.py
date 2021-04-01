import machine
import time
import math
from OmniArm import *

armInp = 500
baseInp = 200
horzInp = 300
vertInp =  400

arm1_ADC_pose = [armInp, baseInp, horzInp, vertInp]          #=PCF8591(i2c_pose,0x48)
arm1_ADC_temp = [0,0,0]                                      #=PCF8591(i2c_temp,0x48)
arm1 = ARM(arm1_ADC_pose, arm1_ADC_temp)
print("Checkpoint")

baseMax = 1000
baseMin = 1
heightMax = 2000
heightMin = 2
horzMax = 3000
horzMin = 3
armMax = 4000
armMin = 4
print("Checkpoint")
#arm1.SetLimits(1, 2, 3, 4, 5, 6, 7,8)
print("Checkpoint")
slewMin= 0
slewMax= 2*math.pi
heightMin= 0.2
heightMax= 0.4
jutMin= 0.1
jutMax= 0.5
swivelMin= 0
swivelMax= 2*math.pi
arm1.SetMapping(baseMax, baseMin, vertMax, heightMin, horzMax, horzMin, armMax, armMin)





