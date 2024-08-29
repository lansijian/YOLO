from ultralytics import YOLO

def main():
    # Load a model
    model = YOLO("ultralytics/cfg/models/v8/yolov8n.yaml")  # build a new model from scratch
    # model = YOLO("yolov8n.pt")  # load a pretrained model, uncomment this line if you want to use pretrained weights

    # Train the model
    model.train(data='vision_work/Mydataset/Myvoc.yaml',
                cache=False,
                imgsz=640,
                epochs=100,
                batch=16,
                close_mosaic=0,
                workers=4,
                device='0',
                optimizer='SGD',  # using SGD
                amp=False,  # close amp
                project='runs/train',
                name='exp',
                )

if __name__ == '__main__':
    main()