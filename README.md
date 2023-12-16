# Pedestrian Tracking and Vehicle Speed Estimation Using Deep Learning
A Capstone final year project for my bachelor.

## Description
We proposed a system to detect pedestrian with counting and to detect vehicles with speed estimation using deep learning and OpenCV. We used MobileNet V2 SSD (Single Shot Multibox Detector) Caffe model, which was pre-trained on Coco dataset. Our system detects pedestrian and vehicles using deep learning Caffe model from video sources, and tracks them. Using OpenCV, the system counts the number of people who are heading “Up” and
“Down” in the roads, and calculates speed estimation to detect the KPH (Kilometers Per Hour) of the moving vehicle. VASCAR method is the base of our speed estimation. This system has also an implementation of Dropbox API for storing the summarized results.

## Features
* Pedestrian tracker and counter
* Vehicle speed estimation

## Required Tools
* Python
* OpenCV
* TensorFlow
* Dropbox
* Dlib
* Imutils
* Numpy
* Tkinter

## Usage
### For Person :
python pedestrian.py --conf config/config.json --input videos/example_01.mp4 --output output/output_01.avi

### For Vehicle :
python vehicle.py --conf config/config.json --input sample_data/cars.mp4 --output output/car.avi

## Snapshot
Fig: Pedestrian tracker in action.
![ped](https://github.com/shuuuvo/pedestrian-vehicle-tracking/assets/129393771/344fff98-b2e6-4eae-93d5-2fc9836ae660)

Fig: Vehicle tracker in action.
![veh](https://github.com/shuuuvo/pedestrian-vehicle-tracking/assets/129393771/1f22d09b-1969-4f97-b6c9-5661ea7a7ddf)
