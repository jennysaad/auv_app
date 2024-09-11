#!/usr/bin/env python3
import rospy
from substates.utility.controller import Controller
from substates.utility.functions import countdown

# Initialize node and give a name (ROS)
rospy.init_node("pooltest")

# Create controller and set initial time to 0
controls = Controller(rospy.Time(0))

# Begin mission by flattening the AUV robot
controls.flatten()

# Move down (negative value)
controls.moveDelta([0, 0, -0.25])

# Freeze the robots position
controls.freeze_position()

# Start rotating
controls.rotateEuler([0, 0, 90])

# Freeze the robot’s rotation
controls.freeze_rotation()

# Move in local space 
controls.moveDeltaLocal([1, 0, 0])
controls.moveDeltaLocal([0, 1, 0])
controls.moveDeltaLocal([-1, 0, 0])
controls.moveDeltaLocal([0, -1, 0])

# Continue while not shut down
while not rospy.is_shutdown():
    continue
