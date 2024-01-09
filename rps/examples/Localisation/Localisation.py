#Import Robotarium Utilities
import rps.robotarium as robotarium
from rps.utilities.transformations import *
from rps.utilities.graph import *
from rps.utilities.barrier_certificates import *
from rps.utilities.misc import *
from rps.utilities.controllers import *

#Other Imports
import numpy as np
import time

# Instantiate Robotarium object
N = 5
initial_conditions = np.array(np.mat('1 0.5 -0.5 0 0.28; 0.8 -0.3 -0.75 0.1 0.34; 0 0 0 0 0'))
r = robotarium.Robotarium(number_of_robots=N, show_figure=True, initial_conditions=initial_conditions,sim_in_real_time=True)

# Experiment Constants
iterations = 5000 #Run the simulation/experiment for 5000 steps (5000*0.033 ~= 2min 45sec)

