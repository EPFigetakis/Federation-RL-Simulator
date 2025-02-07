from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
####Setting GlobalVars
TCAP = .4 #Capcity of Task




### Action Dict ### 
action_dict = {
    0 : 'V1',
    1 : 'V2',
    2 : 'V3',
    3 : 'V4',
    4 : 'V5',
    5 : 'V6',
    6 : 'V7',
    7 : 'V8'
}


### VNO CAP Dict ###

VCap_dict = {
    'V1': .3,
    'V2': .3,
    'V3': .1,
    'V4': .3,
    'V5': .3,
    'V6': .2,
    'V7': .2,
    'V8': .3
}

### VNO SLA IP Dict ###

VSLA_dict = {
    'V1': 5,
    'V2': 5,
    'V3': 4,
    'V4': 5,
    'V5': 5,
    'V6': 4,
    'V7': 4,
    'V8': 3
}

### VNO FED Cost Dict ###

VFed_dict = {
    'V1': 19,
    'V2': 13,
    'V3': 7,
    'V4': 10,
    'V5': 5,
    'V6': 7,
    'V7': 4,
    'V8': 14
}



class MECStandard(Env):
    def __init__(self):
        self.action_space = Discrete(8)
        self.observation_space = Box(low=np.array([-100]), high=np.array([100]))
        self.state = 1
        self.reward = 0
        self.done = False

    def step(self, action):

        VNO_Selection = action_dict[action] 
        #### Legacy Game ####

        X = (VCap_dict[VNO_Selection]) - TCAP
        if X >= 0 :
            cost = (VSLA_dict[VNO_Selection]) + (VFed_dict[VNO_Selection])
            FED = False
        else:
            FEDCAP = TCAP - (VCap_dict[VNO_Selection])
            FED = True
            cost = VSLA_dict[VNO_Selection] + VFed_dict[VNO_Selection] + (FEDCAP * 2)


        if FED == True : 
            FEDcost = -1
        else:
            FEDcost = 0

        self.reward = FEDcost - cost

        self.state = 0
        
        if self.state <= 0:
            self.done = True
        else:
            self.done = False
        
        info = {}

        return self.state, self.reward, self.done, info

    def render(self):
        pass
    def reset(self):
        FEDcost = 0 
        cost = 0
        self.state = 1
        self.reward = 0
        self.done = False
        return self.state

