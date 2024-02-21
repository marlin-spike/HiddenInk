# Flask Steganography App

This Flask application provides a web interface for steganography operations, including hiding and extracting information using image-based steganography techniques.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/marlin-spike/HiddenInk
    cd HiddenInk
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate      # On Linux/Mac
    # OR
    .\venv\Scripts\activate       # On Windows
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Make sure your virtual environment is activated.

2. Run the Flask application:

    ```bash
    flask run
    ```

3. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Steganography Overview

Steganography is the practice of concealing data within other non-secret data. In the context of this application, it involves hiding information within images. The application uses the `stegano` and `pycryptodome` libraries for steganography operations.

### Encryption and Decryption

The application supports encrypting and decrypting information before hiding or after extracting from an image. AES encryption is used for secure data handling.

### Image Steganography

The application utilizes the `stegano` library to perform image-based steganography. It can hide and extract text or files within/from images using the least significant bit (LSB) technique.

For more information about steganography and the libraries used, refer to the respective documentation:

- [stegano Documentation](https://pypi.org/project/stegano/)
- [pycryptodome Documentation](https://www.pycryptodome.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

Feel free to explore and customize the application based on your needs!
