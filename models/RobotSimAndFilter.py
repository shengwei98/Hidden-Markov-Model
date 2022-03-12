
import random
from matplotlib import collections
import numpy as np

from models import TransitionModel,ObservationModel,StateModel

#
# Add your Robot Simulator here
#
class RobotSim:
    def __init__(self, stateModel,trueState, sense):
        self.__stateModel = stateModel
        self.__rows, self.__cols, self.__head = stateModel.get_grid_dimensions()
        self.__dim = self.__rows * self.__cols * self.__head

        self.__state = trueState
        self.__states = np.array([i for i in range(self.__dim)])

        self.__observations = np.array([i for i in range(self.__rows * self.__cols + 1)])
        self.__reading = sense

    def update(self, transModel, obsModel):
        proba = transModel.get_T()[self.__state]
        self.__state = random.choices(self.__states, weights = proba, k = 1)[0]
        self.update_reading(obsModel)

    def update_reading(self, obsModel):
        obs = np.array([obsModel.get_o_reading_state( i,self.__state) for i in range(self.__rows * self.__cols + 1)])
        self.__reading = random.choices(self.__observations, weights= obs, k = 1)[0]
        
        # print("Hello World")

    def get_state(self):
        return self.__state

    def get_reading(self):
        return self.__reading
        
#
# Add your Filtering approach here (or within the Localiser, that is your choice!)
#
class HMMFilter:
    def __init__(self, stateModel, proba):
        self.__stateModel = stateModel
        self.__rows, self.__cols, self.__head = stateModel.get_grid_dimensions()
        self.__dim = self.__rows * self.__cols * self.__head
        self.__state = np.zeros(shape = (self.__dim, 1))
        self.__state = proba

        self.__states = np.array([i for i in range(self.__dim)])

    def update(self, transModel, obsModel, reading):
        TT =  transModel.get_T_transp()
        O = obsModel.get_o_reading(reading)

        self.__state = np.transpose(O @ TT @ np.transpose(self.__state))
        self.__state = self.__state / np.sum(self.__state)
        # print("Hello again, World")
    
    def get_prob(self):
        return self.__state

        
        
        
