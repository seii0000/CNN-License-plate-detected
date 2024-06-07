from ultralytics import YOLO

def main():
#load a YOLOv8 model 
    model = YOLO('yolov8n.yaml')

    model.train(data='D:/xla/001/001/dataset.yaml', epochs=100, imgsz=640, batch=16, device='0' )  # train

if __name__ == '__main__':
    main()

