
import cv2
from ultralytics import YOLO
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import easyocr

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Áp dụng GaussianBlur để giảm nhiễu
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Tăng cường độ tương phản bằng cách sử dụng adaptive thresholding
    preprocessed_image = cv2.adaptiveThreshold(blurred, 255,
                                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                               cv2.THRESH_BINARY, 11, 2)
    return preprocessed_image

root = tk.Tk()

# Open a file dialog for the user to select an image
file_path = filedialog.askopenfilename()

# Load the trained YOLOv8 model
model = YOLO('D:/xla/001/001/runs/detect/train23/weights/best.pt')

# Run inference on the image
results = model(file_path)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Read image with EasyOCR
image = cv2.imread(file_path)

# Duyệt qua từng kết quả phát hiện từ YOLOv8
for result in results[0].boxes:
    # Lấy tọa độ các bounding box
    x1, y1, x2, y2 = result.xyxy[0].cpu()
    
    # Cắt vùng ảnh chứa văn bản
    cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
    
    # Sử dụng EasyOCR để đọc văn bản từ vùng ảnh đã cắt
    ocr_result = reader.readtext(cropped_image)

    license_plate = ' '.join([line[1] for line in ocr_result])
    
    # Hiển thị kết quả OCR
    for (bbox, text, prob) in ocr_result:
        print(f'Detected text: {text} (Confidence: {prob:.2f})')
    print('License plate:', license_plate)

    # Hiển thị ảnh gốc
original_image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
original_image_tk = ImageTk.PhotoImage(original_image_pil)
panel_original = tk.Label(root, image=original_image_tk)
panel_original.pack()

cropped_image_pil = Image.fromarray(cropped_image)

# Convert the PIL Image to a ImageTk.PhotoImage object
cropped_image_tk = ImageTk.PhotoImage(cropped_image_pil)

# Create a label for the license plate
label = tk.Label(root, text=f"License Plate: {license_plate}")
label.pack()

# Load and display the image
cropped_image_pil = Image.fromarray(cropped_image)
cropped_image_pil = Image.fromarray(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
cropped_image_tk = ImageTk.PhotoImage(cropped_image_pil)
panel = tk.Label(root, image=cropped_image_tk)
panel.pack()

# Run the GUI
root.mainloop()


        
    



