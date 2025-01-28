import os
import yaml
import torch
from ultralytics import YOLO

# Folder structure should look like this:
# - dataset/
#   - train/
#     - images/
#     - labels/
#   - valid/
#     - images/
#     - labels/
#   - test/
#     - images/
#     - labels/
#   - data.yaml

# Load YOLO model
model = YOLO('yolo11m.pt')

# Augmentations
augmentation_params = {
    'degrees': 10.0,
    'translate': 0.1,
    'scale': 0.5,
    'shear': 2.0,
    'flipud': 0.5,
    'fliplr': 0.5
}

# Model training
model.train(
    data='datasets/data.yaml',
    epochs=50,  # Epoch count
    imgsz=512,  # Img resolution
    batch=16,
    project='pool_detection',
    name='exp',
    augment=True,
    **augmentation_params
)

# Export to onnx
model.export(format='onnx')
