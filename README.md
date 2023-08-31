# Optical Character Recognition (OCR) Service

This repository contains a Flask-based REST API for performing Optical Character Recognition (OCR) on uploaded images. It utilizes the Flask-RESTx library to define the API endpoints and manage request and response formats.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Install required packages using `pip install -r requirements.txt`

### Running the API

1. Clone this repository: `git clone https://github.com/idan1356/flask_OCR_Service.git`
2. Navigate to the project directory: `cd ocr-service`
3. Run the application: `python app.py`

The API will be accessible at `http://localhost:5000/api/decipher-text`.

## API Endpoints

### Upload Image for OCR

Endpoint: `POST /api/decipher-text`

This endpoint allows you to upload an image for Optical Character Recognition.

**Parameters:**

- `user_image`: The image file to be processed.
- `langs`: Comma-separated list of languages in the image (see language list in config file).
- `get_processed_image`: Whether the processed image (rectangles around sentences found by the model) should be returned.

**Responses:**

- `200 OK`: OCR successful. Returns OCR results and optional processed image.
- `400 Bad Request`: OCR unsuccessful. Returns an error message.

## Project Structure

The project is organized as follows:

- `app.py`: The main Flask application file.
- `api/`: Contains the API definition and resources.
- `api/components/`: Contains parser and data model definitions.
- `api/utils/`: Contains utility functions for processing images and handling API logic.

## OCR Model Caching

The OCR model used by the service is LRU (Least Recently Used) cached to improve performance. The caching is implemented using the `functools.lru_cache` decorator.

The OCR model initialization is managed through the `OCRModelSingleton` class, ensuring that only one instance of the model is created. Additionally, the `LRUCachedOCRModel` class uses the `lru_cache` decorator to cache OCR models based on the languages used for processing.

## Configuration

You can configure languages and other settings in the config file.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, features, or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
