#!/usr/bin/env python
import rospy, cv2
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import subprocess

class Face():
    def __init__(self):
        sub = rospy.Subscriber("/cv_camera/image_raw", Image, self.get_image)
        self.pub = rospy.Publisher("face", Image, queue_size=1)
        self.bridge = CvBridge()
        self.image = None
        self.p_number = 0
        self.flag = True
        self.flag_counter = 0
        self.cmd = "gpio -g write 20 0"


    def get_image(self,img):
        try:
            self.image = self.bridge.imgmsg_to_cv2(img, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)

    def count_face(self):
        if self.flag == True:
            self.p_number += 1
            self.flag = False

    def control(self):
        if self.image is None:
            return None

        image_org = self.image

        image_gray = cv2.cvtColor(image_org,cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")
        face = cascade.detectMultiScale(image_gray,scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        if len(face) > 0:
            self.count_face()
            self.cmd = "gpio -g write 20 1"
            self.flag_counter = 0

        else:
            self.flag_counter += 1
            if self.flag_counter == 3:
                self.flag = True
                self.cmd = "gpio -g write 20 0"
                self.flag_counter = 0
                
        proc = subprocess.call( self.cmd , shell=True)

    def get_p_num(self):
        return self.p_number

if __name__ == '__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    pub_face = rospy.Publisher('count_face', Int32, queue_size=1)
    face = Face()
    rate = rospy.Rate(10)
    n = 0
    face_num = 0
    while not rospy.is_shutdown():
        if (n % 5)==0:
            face.control()
            face_num = face.get_p_num()
            pub_face.publish(face_num)

        n += 1
        pub.publish(n)
        rate.sleep()
