import cv2
import easyocr

# Load the trained YOLOv8 model
model = YOLO('D:/xla/001/001/runs/detect/train23/weights/best.pt')

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Run inference on the frame
    results = model(frame)

    # Iterate over each detection from YOLOv8
    for result in results[0].boxes:
        # Get the coordinates of the bounding box
        x1, y1, x2, y2 = result.xyxy[0].cpu()

        # Convert the coordinates to integers
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])

        # Crop the license plate from the frame
        cropped_image = frame[y1:y2, x1:x2]

        # Recognize the license plate with EasyOCR
        license_plate = reader.readtext(cropped_image)

        # Display the license plate
        print(f"License Plate: {license_plate}")


    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()