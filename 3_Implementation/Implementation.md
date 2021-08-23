# Implementation

  ## Software Requirements
    1. Programming Language: Python 3.8 and below.
    2. Model used to create the predictor object: shape_predictor_68_face_landmarks.dat.
    3. Library used : OpenCV(Open Source Computer Vision Library).
    
  ## Hardware Requirements
    1. Hardware            :  Pentium Based System with a minimum of P4
    2. RAM                 :  1GB(minimum)

# Steps of Implementation
    1.We have to check whether the face is detecting through the webcam or not.
    2.The picture in the video is transformed from RGB to Grayscale because it is easy to detect faces in grayscale.
    3.Image Segmentation which is used for counter detection or segment the multiple objects in a single image so that the model used can easily or quickly detect the faces in the video.
    4.We use dlib.get_frontal_face_detector () to detect whether the face is in the webcam video or not . dlib.shape_predictor() is a tool that takes in an image region containing some object and outputs a set of point locations that define the pose of the object. 
      Here we use the shape_predictor_68_face_landmarks.dat model to create the predictor object. We then pass the frame and detect the rectangular dimensions.
    5.We then can detect the facial keypoints using the landmark points which range from 0 to 68 : 
         1. 0 – 26  -  Face Outline from Eyebrows
         2. 27 – 35 – Nose
         3. 36 – 41 – Right Eye
         4. 42 – 47 – Left Eye
         5. 48 – 68 – Mouth
    6.The next Step is to give the coordinates of x1, x2, y1, y2 which makes a circle in the video to show the keypoints of the face.
    7.Finally, If there is a face in the video opened via webcam then the rectangular box which detects whether the face is present or not and the circular keypoints around the face.

     
