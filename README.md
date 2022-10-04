# Digit recognition AI
A simple and extremely light Tensorflow model used in predicting the digits from 1 to 9. Compatible with Python projects using trained.model and with Javascript using Tensorflowjs and tfjs_model.

Images used in training the model are generated from over 3000 fonts downloaded from [Google fonts](https://fonts.google.com/) and those found by default on the Linux Mint distro.

## Generating training data
### Setting up fonts
Download the fonts used in generating this the model [here](https://mega.nz/file/lqhAmQYJ#MWhRw25wPtk43pWgvAUVT4RagPZazoodrFoSH5LipgE). Once downloaded, extract the file contents into the /fonts folder and run list_fonts.sh

### Generating the images
Run generate_data.py to generate the training data images. If you also want to generate the tensorflowjs model, run the make_all_data.sh script before training the model.

## Training and using the model
### Training
Run the train_model notebook to generate the model. Skip the last 2 blocks in the notebook to skip generating the tensorflowjs model.

### Using the model
The model requires the image to be 20x20 pixels and have 1 color channel (tensor shape of \[x, 20, 20, 1] where x is equal to the batch size)
