# Hidden-Markov-Model
 This repo makes use of a Hidden Markov Model to estimate the postion of a robot in a discrete map.

 ## Simulation

 This simulation is run in the RobotLocWrapper.ipynb notebook

 ## Explanation
 This HMM filter makes use of 2 types of models, namely the transition model and the observation model.

### Transition Model
The transition model, $T$ describes the probability of getting to one state given a state. $T$ is a $m \times  n$ matrix where $m =  n = number\  of\  possible\  states$, each item in the matrix represents $P(n|m)$ or the probability of getting to state $n$ given that the current state is $m$.

### Observation Model
For each possible sensor reading, $O$, there exist one Observation model. Each observation model is and $m \times m$ matrix, where $ m = number\ of\ possible\ states$. 

The matrix is a diagonal matrix, where each element represents $ P(m|O)$ or the probability of being in state $m$ given the sensor reading $O$.

### HMM Filter

The prediction matrix $f$ is a $m \times 1$ matrix where $m = number\ of\ possible\ states$. Each item in the matrix represents the probability of the robot being at state $m$ that is estimated by the HMM filter. It first initialises with all values of being equal, as the robot does not know its initial state. For each time step, it updates itself as follows:

$$f_{t+1} = \alpha * O_{e_{t+1}} * T^T * f_{t}$$

where $\alpha$ is a normalising factor.

