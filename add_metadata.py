import json
import onnx

model = onnx.load('best2.onnx')

class_names = {
    0: 'free_standing_pool',
    1: 'pernament_pool',
    2: 'pond'
}

m1 = model.metadata_props.add()
m1.key = 'model_type'
m1.value = json.dumps('Detector')

m2 = model.metadata_props.add()
m2.key = 'class_names'
m2.value = json.dumps(class_names)

m3 = model.metadata_props.add()
m3.key = 'resolution'
m3.value = json.dumps(10)

m4 = model.metadata_props.add()
m4.key = 'det_conf'
m4.value = json.dumps(0.2)

m5 = model.metadata_props.add()
m5.key = 'det_type'
m5.value = json.dumps('YOLO_Ultralytics')

onnx.save(model, 'models/model_w_metadata.onnx')