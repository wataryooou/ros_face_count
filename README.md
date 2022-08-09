# ros_face_count
## OverView
Raspberry Pi 3とROSを使い，顔を発見したらCount upし，LEDを点灯するプログラムを作成した．以下，ファイル構成を示す．  
[launch/](https://github.com/wataryooou/ros_face_count/tree/master/launch) - ROSのLaunch File．  
[scripts/count.py](https://github.com/wataryooou/ros_face_count/blob/master/scripts/count.py) - 顔認識をしてCount upする．また顔を発見したらLEDを点灯し，失ったら消す．  
[scripts/twice.py](https://github.com/wataryooou/ros_face_count/blob/master/scripts/twice.py) - Countを2倍にする．  

## Demo
[Youtube](https://youtu.be/OmNGXfXs4kM)  
![gif](https://github.com/wataryooou/ros_face_count/blob/images/ros_face.gif)

## Requirement
* Raspberry Pi 3
* Ubuntu 16.04
* LED
* Resistor

## Installation
### Hardware
回路に関しては以下を参照。GPIO20 PinとGroundを接続。

![回路図](https://github.com/wataryooou/ros_face_count/blob/images/ros_face_count1.png)

### Software
`$ git clone https://github.com/Ryou-Watanabe/ros_face_count.git`  
cv_camera，mjpeg_server等は各自インストールしてください．

## Usage
launchする．  
`$ roslaunch ros_face_count run_face_count.launch &`

顔を発見した回数を見る場合は，  
`$ rostopic echo /count_face`

単純なcount upを見る場合は，  
`rostopic echo /count_up`

2倍のcount upを見る場合は，  
`rostopic echo /twice`

カメラ映像を見る場合はブラウザで以下のリンクを参照．  
`http://[IP Address]:10002/stream?topic=/cv_camera/image_raw`

## Reference
[twice.pyに関して](https://lab.ueda.asia/?presenpress=ロボットシステム学2016第13回#/)  
[ROS 画像処理に関して](https://github.com/ryuichiueda/pimouse_vision_control)  
[cv_camera インストール方法等](https://lab.ueda.asia/?presenpress=ロボットシステム学2016第12回#/11)

## Licence
[Licence](https://github.com/wataryooou/ros_face_count/blob/master/LICENSE)

## Author
[wataryooou](https://github.com/wataryooou)
