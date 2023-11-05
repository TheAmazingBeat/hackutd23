from flask import *
from distutils.log import debug 
from werkzeug.utils import secure_filename
from fileinput import filename 
import random
import os
from dotenv import load_dotenv
# from model import analyze_image
import openai
app = Flask(__name__)


UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
is_Residential = True
num_Bathrooms = 3
num_Bedrooms = 4
sq_Feet = 2500
location = "Garland, TX"
age = 24
prompt = ''

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/rand")
def hello():
    return str(random.randint(0, 100))

@app.route("/api/sample-analyze1", methods=['GET'])
def sample_analyze1():
    return jsonify(classify_image("images/Residential-Ext1.jpeg"))

@app.route("/api/sample-analyze2", methods=['GET'])
def sample_analyze2():
    return jsonify(analyze_image("images/Commercial-Ext1.jpeg"))

# Import image from file

# returns true or false whether file is of correct file type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        # check if the post request has the file part
        
        if 'file' not in request.files:
            # flash('No file given')
            print('No file given')
            return redirect(request.url)
        
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            # flash('No selected file')
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(file_path)
            file.save(file_path)
            
            result = analyze_image(file_path)
            print(result)
            return jsonify(result)
            # use models here
            
            return redirect("/")
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
app.add_url_rule(
    "/api/upload", endpoint="download_file", build_only=True
)

if(is_Residential):
    prompt = "Make a professional value proposition given these parameters: number of bathrooms: " + str(num_Bathrooms) + ", num of bedrooms: " + str(num_Bedrooms) + ", total square feet: " + str(sq_Feet) + ", located in: " + location + ", age: " + str(age)
else:
    prompt = prompt = "Make a detailed value proposition given these parameters: commercial building, total square feet: " + str(sq_Feet) + ", location: " + str(location) + ", age: " + str(age)

print(prompt)

@app.route('/api/openai-call', methods=['POST'])
def getAPICall():

    completion = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 1000,
        temperature = 1
    )
    result = []
    for choice in completion.choices:
        text = choice.text.replace('\n', '')
        print(choice.text)
        result.append(text)
    
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)