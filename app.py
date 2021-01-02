import os
from flask import Flask, flash, render_template, request, session, redirect,send_from_directory
from flask_session import Session
from werkzeug.utils import secure_filename
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img, img_to_array
# --------------------------------------------------------
# --------------------------------------------------------
if __name__ == '__main__':
    print('Hello World!')