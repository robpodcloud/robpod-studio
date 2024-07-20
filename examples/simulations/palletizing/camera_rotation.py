import time

import robodk.robolink
from robodk.robomath import *

RDK = robodk.robolink.Robolink()
camera = RDK.Item("Camera Base", robodk.robolink.ITEM_TYPE_FRAME)


while True:
    pose = camera.Pose()
    p = Pose_2_UR(pose)
    p[5] = p[5] + 0.002
    camera.setPose(UR_2_Pose(p))
    time.sleep(0.01)