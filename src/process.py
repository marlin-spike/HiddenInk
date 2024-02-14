import os
import random
import string

from PIL import Image
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
def generate_random_text(length=4):
    characters = string.ascii_letters + string.digits  # You can customize the character set as needed
    random_text = ''.join(random.choice(characters) for _ in range(length))
    return random_text

def get_file_extension(file_path):
    # Split the file path into base name and extension
    base_name, extension = os.path.splitext(file_path)


def convert_to_png(image_path, output_folder, compression_level=6):
    try:
        image = Image.open(image_path)
        # Construct the output filename with the PNG extension
        output_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".png")
        # Save the image as PNG format with compression
        image.save(output_filename, "PNG", optimize=True, quality=compression_level)
        
        print(f"Image {image_path} has been successfully converted to PNG with compression level {compression_level}.")
        return output_filename  # Return the path to the converted PNG image
    except Exception as e:
        print(f"An error occurred while converting the image: {e}")
        return None

# Example usage:
convert_to_png("Untitled.png", "/path/to/output_folder", compression_level=6)

    