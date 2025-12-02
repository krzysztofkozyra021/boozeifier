# Boozeifier

A university machine learning project that trains image classification models to detect and distinguish whether an image contains alcohol.

## Project Description

Boozeifier is an ML-powered image classifier designed to identify alcoholic beverages in images. The model is trained to classify images into two categories: those containing alcohol and those without.

## Dataset Structure

The training data is organized in the following folder structure:

```
dataset/
├── alcohol/        # Images containing alcoholic beverages
└── not_alcohol/    # Images without alcoholic beverages
```

Place your training images in the appropriate folders before training the model.

## Usage

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Training the Model

To train the model, run the following command:

```bash
python train_model.py
```

This will train the model using the images in the `dataset/` directory and save the trained model as `boozeifier_model.keras`.

### Running the Web App

To start the Streamlit web application, run:

```bash
streamlit run main.py
```

This will launch the web interface where you can upload images to be classified.

## License

See [LICENSE](LICENSE) for details.
