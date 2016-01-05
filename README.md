
# REST-API
Flask REST API

## Requirements
 Python 2.7.x, pip, virtualenv installed. Also Jinja2, MarkupSafe, Werkzeug,itsdangerous,wsgiref

 Install Flask with Pip ```$ pip install Flask```


### Test on development server
'''python app.py '''

##### @app.route('/') renders data present in database in HTML
This renders the data in database html accessed by <http://127.0.0.1:5000/>
##### @app.route('/names', methods = ['GET'])
This renders the data in database in JSON accessed <http://127.0.0.1:5000/names>

####### 1 . get the total number of entries in the dataset
"@app.route('/entrynumber', methods = ['GET'])" 

displays the number of entries in the dataset in JSON accessed using <http://127.0.0.1:5000/entrynumber>

####### 2 . get all entries for a specific baby name (supplied in the request)
'''@app.route('/names/<string:name>', methods = ['GET'])'''
Get all entries for a specific baby name by specifying http://127.0.0.1:5000/names/[baby name]

####### 3 (i). get a list of all unique baby names and count []
@app.route('/unique', methods = ['GET'])...
List of all unique baby baby name can be accessed by <http://127.0.0.1:5000/unique>

####### 4. Adding a new entry to the database (name, year, gender, count). 
 '''@app.route('/add', methods=['POST'])''' [needs debugging] and using POSTMAN chrome extension:
<https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en>


