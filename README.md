# Bayesian Estimation Team

## TODO:
In the ROS script that handles bayes stuff, we consume information from CV and Comm (see marshall/Messages) for specifics. This ROS script subscribes to both of these nodes, and publishes to a FullState node (see marshall/Messages); given the current state of information and the new info, just call `bayes_update.update()` to update the current state and return this FullState. 
