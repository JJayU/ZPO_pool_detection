# ZPO Project - Your Deepness Model
This is a template for a Project.
Please follow the structure below and address all required points.
Please put it in a public repository.

AT THE TOP OF THIS README ADD AN IMAGE/GIF WITH EXAMPLE MODEL PREICTION, AS A BANNER

We reecommend making this README pleaseant to read, you can later use it as portfolio `:)`

## Dataset
- on what data trained
- how many annotations
- how the data was prepared (e.g. preprocessed)
- store the dataset with annotations in XXX and provide a link here
- what format for data and how to load it

## Training
- what network, how trained, what parameters
- what augmentation methods used
- what script to run the training
- remember to have a fully specified Python environemnt (Python version, requirements list with versions)
- other instructions to reproduce the training process

## Results
- Example images from dataset:
<table>
  <tr>
    <td><img src="img/dataset1.png" alt="Image 1" width="300"></td>
    <td><img src="img/dataset2.png" alt="Image 2" width="300"></td>
  </tr>
  <tr>
    <td><img src="img/dataset3.png" alt="Image 3" width="300"></td>
    <td><img src="img/dataset4.png" alt="Image 4" width="300"></td>
  </tr>
</table>
- Examples of good and bad predictions:
<table>
  <tr>
    <td><img src="img/good_prediction1.png" alt="Image 1" width="300"></td>
    <td><img src="img/good_prediction2.png" alt="Image 2" width="300"></td>
  </tr>
  <tr>
    <td><img src="img/good_prediction3.png" alt="Image 3" width="300"></td>
    <td><img src="img/bad_prediction1.png" alt="Image 4" width="300"></td>
  </tr>
</table>


- Metrics on the test and train dataset
# TODO

## Trained model in ONNX ready for `Deepness` plugin
- Model is available in the `model` directory
- After training, the model is converted automatically to ONNX format but needs to have appropriate metadata added to it. In order to do it, run script `add_metadata.py`, modyifing parameters if needed.

## Demo instructions and video
- a short video of running the model in Deepness (no need for audio), preferably converted to GIF
- what ortophoto to load in QGIS and what physical place to zoom-in. E.g. Poznan 2022 zoomed-in at PUT campus
- showing the results of running the model

## People
- Jakub Junkiert - Annotations & Training Scripts - [GitHub](https://github.com/JJayU)
- Maksymilian Klemenczak - Annotations & Training Scripts - [GitHub](https://github.com/MaksymilianKlemen)
- Hubert Górecki - Annotations - [GitHub](https://github.com/theHaUBe)
- Jarosław Kuźma - Annotations - [GitHub](https://github.com/Yerbiff)
