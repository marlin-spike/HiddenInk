import os
import random
import string

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
    