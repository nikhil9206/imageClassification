# Shape Generator and Classification Application

This project generates images with randomly placed and styled shapes (circles, rectangles, and triangles) and prepares them for classification. The goal is to use the generated dataset for training an AI model capable of accurately identifying shapes in images.

---

## Features

1. **Shape Generation**:
   - Generates random shapes (circles, rectangles, triangles) on a black background.
   - Allows customization of the number of images, minimum/maximum shapes per image, and shape sizes.

2. **Image Processing**:
   - Randomly assigns colors, positions, and fill styles to shapes.
   - Saves generated images in a structured format for further use in AI training.

3. **Dataset Preparation**:
   - Images are labeled by their dominant shape (circle or rectangle) for AI model training.
   - Supports scalable generation of datasets to improve model accuracy.

---

## Goals

1. **AI Model Training**:
   - Train an AI model to classify shapes in images as circles, rectangles, or triangles.
   - Achieve high accuracy in shape identification using a robust dataset of labeled images.

2. **Custom Dataset Creation**:
   - Provide flexibility to users to generate datasets of varying sizes and complexities.
   - Enable researchers and developers to train AI models tailored to specific requirements.

---

## File Structure

- **`main.py`**: The primary script for shape generation and image saving.
- **`images/`**: Directory where generated images are saved.
- **`black.jpg`**: A black base image for drawing shapes.

---

## Prerequisites

1. **Python 3.7+**:
   - Install Python from [Python Official Website](https://www.python.org/downloads/).

2. **Required Libraries**:
   Install the necessary libraries using `pip`:
   ```bash
   pip install opencv-python numpy
   ```

3. **File Setup**:
   - Ensure `black.jpg` is present in the working directory.
   - Create an `images/` folder to save the generated images.

---

## How to Use

1. **Run the Script**:
   Execute the `main.py` script:
   ```bash
   python main.py
   ```

2. **Input Parameters**:
   - Enter the number of images to generate.
   - Specify the minimum and maximum number of shapes per image.
   - Set the size of shapes in pixels.

3. **Generated Output**:
   - Images are saved in the `images/` folder.
   - Each image is labeled as either `circle` or `square` in the filename.

4. **Use in AI Training**:
   - Use the labeled dataset for training an AI model to classify shapes.

---

## Example Workflow

1. **Shape Generation**:
   - Generate 50 images with a mix of circles, rectangles, and triangles.
   - Example output: `images/1_circle.jpg`, `images/2_square.jpg`.

2. **AI Model Training**:
   - Use a deep learning framework (e.g., TensorFlow or PyTorch) to train a classification model.
   - Feed the dataset to the model for supervised learning.

3. **Model Evaluation**:
   - Test the trained model on new images.
   - Evaluate its performance using metrics like accuracy, precision, and recall.

---

## Future Enhancements

- Add more shape types (e.g., polygons, ellipses).
- Implement a graphical interface for dataset customization.
- Automate dataset labeling using metadata.
- Extend the application to include noise or real-world backgrounds for enhanced AI robustness.

---

## Contact

For questions or suggestions, please contact:  
**Email**: [your-email@example.com](mailto:your-email@example.com)  
**Phone**: +1 123-456-7890
