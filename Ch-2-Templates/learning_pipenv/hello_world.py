from flask import Flask
import os

app = Flask(__name__)

name = os.environ.get('name')
print(name)



