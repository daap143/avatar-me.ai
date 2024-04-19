from os import system as cmd

def down_dep():
    try:
        cmd('pip install requirements.txt')
    except:
        return 'error downloading requirements.txt'

# from flask import Flask, render_template, request
# from brows import search_img
# from os import system as cmd


# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


# import os
# from flask import Flask, render_template, request, send_from_directory ,send_file
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# @app.route('/', methods=['GET', 'POST'])
# def upload_page():
#     if request.method == 'POST':
#         file = request.files['image']
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
#         return send_file(os.path.join(app.config['UPLOAD_FOLDER'], 'image_to_show.jpg'), as_attachment=True)
#     return render_template('index.html')

# @app.route('/static/uploads/image_to_show.jpg')
# def default_image():
#     return send_from_directory(app.config['UPLOAD_FOLDER'], 'image_to_show.jpg')

# if __name__ == '__main__':
#     app.run(debug=True)

import run
import brows

print("upload the file as image.jpg")
query = input("enter a the prompt:")
brows.search_img(query)

run(source_path='image.jpg',target_path='temp.jpg',output_path='generated.jpg')