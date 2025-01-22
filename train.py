import os
import yaml
import torch
from ultralytics import YOLO

# Zakładamy strukturę folderów:
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

# Zakładamy, że plik dataset/data.yaml już istnieje

# Załaduj pretrenowany model YOLOv11
model = YOLO('yolo11n.pt')  # Wybór wersji modelu (n=mały, s=średni, itd.)

# Dodanie augmentacji danych
augmentation_params = {
    'degrees': 10.0,
    'translate': 0.1,
    'scale': 0.5,
    'shear': 2.0,
    'flipud': 0.5,  # Flip up-down
    'fliplr': 0.5   # Flip left-right
}

# Trening modelu
model.train(
    data='datasets/data.yaml',
    epochs=50,  # Liczba epok
    imgsz=512,  # Rozdzielczość obrazu
    batch=16,  # Rozmiar batcha
    project='pool_detection',
    name='exp',
    augment=True,  # Włączenie augmentacji
    **augmentation_params
)

model.export(format='onnx')
