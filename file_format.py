import os
import cv2

def parse_filename(filename):
    parts = filename.split('_')
    x_min = int(parts[4])
    y_min = int(parts[5])
    x_max = int(parts[6])
    y_max = int(parts[7].split('.')[0])
    return x_min, y_min, x_max, y_max

def convert_to_yolo_format(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

# Paths
image_dir = 'D:/test/001/two_rows'
label_dir = 'D:/test/001/val'
os.makedirs(label_dir, exist_ok=True)

# Iterate over images and create labels
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg'):
        x_min, y_min, x_max, y_max = parse_filename(filename)
        image_path = os.path.join(image_dir, filename)
        
        # Load image to get dimensions
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        
        # Convert bounding box to YOLO format
        bbox_yolo = convert_to_yolo_format((width, height), (x_min, y_min, x_max, y_max))
        
        # Save label file
        label_path = os.path.join(label_dir, filename.replace('.jpg', '.txt'))
        with open(label_path, 'w') as f:
            f.write(f"0 {bbox_yolo[0]} {bbox_yolo[1]} {bbox_yolo[2]} {bbox_yolo[3]}\n")
