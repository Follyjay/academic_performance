# Student Academic Performance Prediction

This web application predicts student academic performance using a machine learning model. The raw data, processed and cleaned in Python, is used to train the model, which is then integrated into a Flask-based web application for predictions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to predict student academic performance based on various factors. The raw data from Kaggle was processed and cleaned using Python, and a machine learning model was trained. The trained model is then integrated into a web application developed using Flask.

## Features

- Data processing and cleaning using Python
- Machine learning model training and evaluation
- Web application for making predictions
- Integration of the trained model into the web application

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- Numpy
- HTML/CSS/JavaScript

## Installation

### Prerequisites

- Python 3.x
- Flask
- Pip

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/student-performance-prediction.git
    cd student-performance-prediction
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

1. Open the web application in your browser.
2. Enter the required student data into the form.
3. Submit the form to get the prediction of the student's academic performance.

## Project Structure

```plaintext
student-performance-prediction/
│
├── data/
│   └── data.csv
│
|── Data_Analysis/
|   └── model.pkl
|
├── web_application/
|   |── model/
|   |   ├── dt_model.pkl
|   |   ├── encoder.pkl
|   |   ├── scaler.pkl
│   |   └── model.pkl
|   |
|   ├── static/
│   |   ├── script.js
│   |   └── styles.css
│   |
│   ├── templates/
│   |   └── index.html
│   |
|   └── app.py
|
└── README.md

  - data/: Directory containing the cleaned data.
  - model/: Directory containing the trained model.
  - static/: Directory for static files like CSS and JavaScript.
  - templates/: Directory for HTML templates.
  - app.py: Main Flask application file.
  - modelling.py: Script for data processing, cleaning, and model training.

## Acknowledgements
- Kaggle for providing the dataset.
- Flask documentation and tutorials for guidance on web development.
- Scikit-learn documentation for machine learning model training and evaluation.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.
