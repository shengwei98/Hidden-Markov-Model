# Hidden-Markov-Model
 This repo makes use of a Hidden Markov Model to estimate the postion of a robot in a discrete map.

 ## Simulation

 This simulation is run in the RobotLocWrapper.ipynb notebook

 ## Explanation
 This HMM filter makes use of 2 types of models, namely the transition model and the observation model.

### Transition Model
The transition model, <img src="https://render.githubusercontent.com/render/math?math=T"> describes the probability of getting to one state given a state. <img src="https://render.githubusercontent.com/render/math?math=T"> is a <img src="https://render.githubusercontent.com/render/math?math=m \x n"> matrix where <img src="https://render.githubusercontent.com/render/math?math=m=n= number\ of\ possible\ states">, each item in the matrix represents <img src="https://render.githubusercontent.com/render/math?math=P(n|m)"> or the probability of getting to state <img src="https://render.githubusercontent.com/render/math?math=n"> given that the current state is <img src="https://render.githubusercontent.com/render/math?math=m">.

### Observation Model
For each possible sensor reading, <img src="https://render.githubusercontent.com/render/math?math=O">, there exist one Observation model. Each observation model is and <img src="https://render.githubusercontent.com/render/math?math=m \x n"> matrix, where <img src="https://render.githubusercontent.com/render/math?math=m = number\ of\ possible\ states">. 

The matrix is a diagonal matrix, where each element represents <img src="https://render.githubusercontent.com/render/math?math=P(m|O)"> or the probability of being in state <img src="https://render.githubusercontent.com/render/math?math=m"> given the sensor reading <img src="https://render.githubusercontent.com/render/math?math=O">.

### HMM Filter

The prediction matrix <img src="https://render.githubusercontent.com/render/math?math=f"> is a <img src="https://render.githubusercontent.com/render/math?math=m\x 1"> matrix where <img src="https://render.githubusercontent.com/render/math?math=m=number\ of\ possible\ states">. Each item in the matrix represents the probability of the robot being at state m that is estimated by the HMM filter. It first initialises with all values of being equal, as the robot does not know its initial state. For each time step, it updates itself as follows:

<!-- $$f_{t+1} = \alpha * O_{e_{t+1}} * T^T * f_{t}$$ -->
<img src="https://render.githubusercontent.com/render/math?math=f_{t%2B1} = \alpha * O_{e_{t%2B1}} * T^T * f_{t}">

where <img src="https://render.githubusercontent.com/render/math?math=\alpha"> is a normalising factor.

