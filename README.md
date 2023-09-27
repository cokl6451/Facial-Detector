# Face and Smile Detection

This project utilizes the OpenCV library to detect faces and smiles from either an image or a video feed from a camera.

## Dependencies

- `cv2` (OpenCV library)

## How it Works

1. **Classifiers Initialization**: I used OpenCV's pre-trained Haar cascades to detect faces and smiles:
    \```python
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    smileCascade = cv2.CascadeClassifier("smile.xml")
    \```

2. **Loading an Image or Video Feed**:
    - To use the camera feed:
      \```python
      video = cv2.VideoCapture(0)
      \```

3. **Processing the Video Feed**:
    - The video feed is captured frame-by-frame.
    - Each frame is converted to grayscale for better detection.
    - Both faces and smiles are detected and rectangles are drawn around them.

4. **Displaying the Output**:
    - The processed frame is displayed in a window named "Face Detector".
    - The number of detected faces, along with their mood (Happy/Unhappy), is displayed on the frame.

5. **Exit**:
    - Press `q` to exit the video feed and close the windows.

## Usage

Run the script and if you're using a camera feed, position yourself or the subject in front of the camera. The program will detect faces and smiles and display the results in real-time.

## Notes

- Ensure that the Haar cascade XML files (`haarcascade_frontalface_default.xml` and `smile.xml`) are present in the same directory as the script or provide the correct path to them.
- The detection parameters like `scaleFactor` and `minNeighbors` might need tweaking depending on the input source and desired accuracy.
