from flask import Flask, render_template, request, redirect, url_for ,send_file
import os
from src.process import *
from src.CryptoSteganography import *

# app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#setting UP default secrate key
default_secret_key = 'sadbsdfgdfmnbdvcsdvsndbvjdsfg'
crypto_steganography = CryptoSteganography(default_secret_key)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hide', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    #getting Input
    file = request.files['file']
    data = request.form['input_for_encoding']        
    user_secret_key = request.form.get('key')
    print(user_secret_key)

    #checking the Input file Extension 
    extension = file.filename.rsplit('.', 1)[1].lower()
    file_name = generate_random_text()

    tamp = "output."
    output_filename = file_name + tamp + extension

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        #storing input file
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print("filenamea is : ", filename)
        file.save(filename)
        #converting the Input file 
        new_filename = convert_to_png(filename, app.config['UPLOAD_FOLDER'])
        
        if new_filename is None:
            return ("error")
        
        print(new_filename)

        #if password id provided then Use it Otherwise use Default passs
        if user_secret_key:
            crypto_steganography = CryptoSteganography(user_secret_key)
        else:
            crypto_steganography = CryptoSteganography(default_secret_key)

        #hide the data inside the Image 
        crypto_steganography.hide(new_filename, output_filename,  data)
        
        #Remove the file 
        os.remove(filename)
        os.remove(new_filename)
        #return the file t the user for downloading 
        return_data = send_file(output_filename, mimetype='image/png', as_attachment=True, download_name=output_filename)
        os.remove(output_filename)
        return return_data

    return redirect(request.url)


#API for Decoding route 
@app.route('/decode', methods=['GET', 'POST'])
def decode_file():
    result = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            user_secret_key = request.form.get('key')

            if user_secret_key:
                crypto_steganography = CryptoSteganography(user_secret_key)
            else:
                crypto_steganography = CryptoSteganography(default_secret_key)
           
            # result = crypto_steganography.retrieve(filename)
            try:
                result = crypto_steganography.retrieve(filename)
            except IndexError as e:
                result = "Wrong password or image has no hidden message"
                # os.remove(filename)

            os.remove(filename)

            if result is None:
                result = "Wrong password or image has no hidden message"

    return render_template('decode.html', result=result)

#temp Api For test new code 
@app.route('/en')
def encod():
    return render_template('en.html')

@app.route('/de')
def decod():
    return render_template('de.html')


if __name__ == '__main__'zcv:
    app.run(debug=True)

