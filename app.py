import sys
import os
from flask import Flask, flash, render_template, request, session, redirect,send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# --------------------------------------------------------
# Load the model
with open('static/classifier/model.json', 'r') as f:
    model = model_from_json(f.read())
model.load_weights("static/classifier/model_weights.h5")
# --------------------------------------------------------
if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
sess = Session()
# --------------------------------------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# --------------------------------------------------------
def predict(file_path):
    img = load_img(file_path, target_size=(150, 150)) 
    x = img_to_array(img)         
    x = x.reshape((1,) + x.shape) 
    x /= 255.0 
    classes = model.predict(x)[0][0]
    pred = "Dog" if classes>0.5 else "Cat"
    prob = classes if classes > 0.5 else 1 - classes
    prob = round((prob * 100), 2)
    return pred, prob
# --------------------------------------------------------
@app.route('/static/uploads/<filename>')
def send_image(filename):
    return send_from_directory('static/uploads', filename)
# --------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            pred, prob = predict(file_path)
            return render_template('index.html', prediction= pred, confidence = prob, image_name = filename)
      
    return render_template('index.html', image_name = 'catdog.jpg')
# --------------------------------------------------------
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    app.secret_key = 'my super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run(host = '0.0.0.0', port=port)