# Data Hybrid: Pioneer Robot Data Collection and Model Training

This repository contains a collection of scripts and notebooks used for data collection, processing, and training deep learning models on sensor and image data obtained from a simulated Pioneer robot.

## Project Structure

```plaintext
datahybrid/
├── bot.avi              # Video recorded after model inference with all sensors disabled
├── csvdata.py           # Script for initial data collection with sensor data (distance from walls)
├── hello.ttt            # CoppeliaSim model for Pioneer bot simulation
├── imagedata.py         # Script for image data extraction
├── main.avi             # Video recorded during data collection with sensors enabled
├── new.txt              # Unstructured data from simulation when sensors were enabled
├── output.csv           # Structured and cleaned data after processing
├── trail.ipynb          # Jupyter Notebook for model training and evaluation
```

## Requirements

To run the project, ensure you have the following Python packages installed:

```bash
pip install torch torchvision pandas numpy matplotlib pillow scikit-learn
```

## Usage

### 1. Data Collection

Data is collected from the simulated Pioneer robot in CoppeliaSim. `csvdata.py` captures sensor data (e.g., distance measurements) as the robot navigates the environment, and `imagedata.py` records the images captured by the robot's camera.

### 2. Data Processing

Data from `new.txt` is converted into structured form and saved in `output.csv` for further processing and model training.

### 3. Model Training

The primary training notebook is `trail.ipynb`, which includes several model architectures:

- **Regression Model**: Trained on sensor data to predict continuous values.
- **Classification Model**: Binary classification based on the presence of sensor signals.
- **Multi-task Model**: Performs both regression and classification tasks on a single network.

The notebook is organized into different sections to load the data, define models, and train each model. This includes setting up custom datasets using PyTorch and training convolutional neural networks (CNNs) for regression, classification, and multi-task learning.

### 4. Model Summary

Below is a summary of the `CustomCNN` architecture used in this project:

```
----------------------------------------------------------------
Layer (type)               Output Shape         Param #
================================================================
Conv2d-1                   [-1, 64, 32, 32]       3,136
BatchNorm2d-2              [-1, 64, 32, 32]         128
Conv2d-3                   [-1, 64, 16, 16]      65,600
BatchNorm2d-4              [-1, 64, 16, 16]         128
Conv2d-5                   [-1, 64, 8, 8]        65,600
BatchNorm2d-6              [-1, 64, 8, 8]           128
Conv2d-7                   [-1, 64, 4, 4]        65,600
BatchNorm2d-8              [-1, 64, 4, 4]           128
Linear-9                   [-1, 256]            262,400
Linear-10                  [-1, 16]               4,112
================================================================
Total params: 466,960
Trainable params: 466,960
Non-trainable params: 0
----------------------------------------------------------------
```

### 5. Training and Evaluation

Run the following cells in `trail.ipynb` to start training:

```python
num_epochs = 100  # Set the number of epochs
trained_model, train_losses, test_losses = train_model(model, train_loader, test_loader, lossfun, optimizer, num_epochs)
```

#### Visualizing Losses

The notebook includes code to plot training and test losses:

```python
plt.plot(train_losses, 's-')
plt.plot(test_losses, 's-')
plt.legend(['Train Loss', 'Test Loss'])
plt.grid()
plt.show()
```

## Results

- **Regression Model**: Trained to predict sensor readings.
- **Classification Model**: Trained to classify the state based on sensor data.
- **Multi-task Model**: Combines regression and classification for a holistic approach.

Training and test losses are logged during each epoch, with results displayed as a loss graph for performance monitoring.
