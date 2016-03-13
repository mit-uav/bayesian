# bayes_update

import copy

def update(curr_state, roombas_info, uav_info, threshold):
    """ 
    Performs the update to full state based on the information received

    input:
        curr_state: 
            {uav:<UAVEst>, roombas:<RoombaEstList>} dict
            a read of the persistent state saved to ROS node passed as a dictionary
            keys:
                uav: contains the current info about uav
                roombas: contains the current info about roomba locations
        roombas_info: 
            <RoombaEstList> object
            a list containing RoomabEst objects that CV currently sees
        uav_info:
            <UAVEst> object
            a list containing UAVEst properties that Comm currently detects
        threshold:
            float
            threshold where we determine if a Roomba that we have seen is the same as one we see

    output:
        full_state:
            {uav:<UAVEst>, roombas:<RoombaEstList>} dict
            updated dictionary of the UAV estimate and the list of roomba location estimates
    """ 

    # Initialize full_state as curr_state
    full_state = copy.deepcopy(curr_state)

    # Update UAV state first; make sure timestamps are monotonically increasing
    if curr_state[uav].timestamp > uav_info.timestamp and \
            curr_state[roombas].timestamp > roombas_info.timestamp:
        return full_state

    # Possible cases:
    # UAV sees a brand new roomba, adds it to the list of RoombaEst objects
    # UAV sees a roomba it thinks it has already seen; updates that particular RoombaEst object
    # UAV doesn't see any roomba; the RoombaEst object in question is 
    for i, roomba_est in enumerate(roombas_info):
        closest = threshold
        for j in range(len(curr_state[roombas])):
            dist = l2(curr_state[roombas][i], roomba_est)
            if dist < closest:
                closest = j
        # Finish this; add it to full_state
        pass 

    return full_state

def l2(r1, r2, threshold):
    """
    Given two roombas, computes the L2 norm between them (difference in the coordinate and velocities)

    input:
        r1, r2:
            RoombaEst objects describing two roomba instances 

    output:
        dist:
            "L2" norm between the two roombas
    """

    dist = (r1.x - r2.x)**2 + (r1.y - r2.y)**2 + (r1.vel_x - r2.vel_x)**2 = (r1.vel_y - r2.vel_y)**2
    if r1.
    return dist
