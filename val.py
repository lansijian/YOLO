from ultralytics import YOLO

def main():
    # Load the trained model weights
    model = YOLO('runs/train/exp5/weights/best.pt')  # Load your trained model weights

    # Validate the model on the validation dataset
    model.val(data='vision_work/Mydataset/Myvoc.yaml',  # Path to the dataset YAML configuration file
              split='val',  # Use the validation split of the dataset
              imgsz=640,  # Image size during validation
              batch=16,  # Batch size during validation
              save_json=True,  # Save validation results in JSON format (useful for COCO metric calculation)
              project='runs/val',  # Directory to save validation results
              name='exp',  # Name of the validation experiment
              )

if __name__ == '__main__':
    main()