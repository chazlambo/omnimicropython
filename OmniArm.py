class ARM:
    def __init__(self, ADC_pose, ADC_temp):
        self.pose = ADC_pose
        self.temp = ADC_pose
        self.HT = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.calibrate = False
        self.mapping = False

    def GetPose(): # TODO
        if not calibrate:
            print("Arm is not calibrated. Set the limits")
            return None
        if not mapping:
            print("Missing mapping limits.")
            return None
        self.baseReading = ADC_pose[0]
        self.vertReading = ADC_pose[1]
        self.horzReading = ADC_pose[2]
        self.armReading = ADC_pose[3]
        
        theta1 = self.mapping(self.baseReading, self.baseMin, self.baseMax, self.slewMin, self.slewMax)
        d1 = self.mapping(self.vertReading, self.vertMin, self.vertMax, self.heightMin, self.heightMax)
        d3 = self.mapping(self.horzReading, self.horzMin, self.horzMax, self.jutMin, self.jutMax)
        theta4 = self.mapping(self.armReading, self.armMin, self.armMax, self.swivelMin, self.swivelMax)
        
        self.HT[0][0] = math.cos(theta1)*math.cos(theta4) - math.sin(theta1)*sin(theta4)
        self.HT[0][1] = -math.cos(theta1)*math.sin(theta4) - math.sin(theta1)*math.cos(theta4)
        self.HT[0][3] = d3*math.cos(theta1)
        self.HT[1][0] = math.sin(theta1)*math.sin(theta4) + math.cos(theta1)*math.sin(theta4)
        self.HT[1][1] = -math.sin(theta4)*math.sin(theta1) + math.cos(theta1)*math.cos(theta4)
        self.HT[1][3] = d3*math.sin(theta1)
        self.HT[2][2] = 1
        self.HT[2][3] = d1;
        self.HT[3][2] = 1
        
        return None
    
    def SetLimits(self, base_Max, base_Min, vert_Max, vert_Min, horz_Max, horz_Min, wrist_Max, wrist_Min):
        self.baseMax = base_Max
        self.baseMin = base_Min
        self.vertMax = vert_Max
        self.vertMin = vert_Min
        self.horzMax = horz_Max
        self.horzMin = horz_Min
        self.wristMax = wrist_Max
        self.wristMin = wrist_Min
        self.calibrate = True
        self.mapping = False
        
    def SetMapping(self, slewMin, slewMax, heightMin, heightMax, jutMin, jutMax, swivelMin, swivelMax):
        self.slewMin = slewMin
        self.slewMax = slewMax
        self.heightMin = heightMin
        self.heightMax = heightMax
        self.jutMin = jutMin
        self.jutMax = jutMax
        self.swivelMin = swivelMin
        self.swivelMax = swivelMax
        self.mapping = True
        
    def mapping(x, inputMin, inputMax, outputMin, outputMax):
        return (x - inputMin) * (outputMax-outputMin) + outputMin
    
    def GetTemp(): #TODO
        return 0
