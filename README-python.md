# wrap4u - Python

WebSite hosted with Python & Flask in a Docker Container.

This project is part of a solution to show different possibilities to host a WebSite inside a Docker container 
with the help of different servers and frameworks.  
See [WebSite wrap4u](README.md).

Flask is a web framework, it’s a Python module that lets you develop web applications easily.
See [What is Flask Python](https://pythonbasics.org/what-is-flask-python/).

## Prerequisites

To host a WebSite with Python and the use of the Flask-library & -server
- python3
- pip

```bash
$ sudo apt-get update
$ sudo apt-get install python3-pip
$ pip3 install flask
```

## Directory-Structure
```
.
├── README-python.md            Python & Flask documentation
├── README.md                   Documentation of the main-project
├── app_python                  Contains the templates for the dynamic webpages.
│   └── index.html              Landing-Page with dynamic content (included with Jinja2 Markup)
├── app_python.py               The Main script to start the WebSite
├── build-python.sh             Build script, creates the Docker container
├── run-python.sh               Run script, executes the pre-built Docker container
├── static                      Static pages of the wrap4u sample website
│   ├── ... 
└── tempdir                     Temporary directory used by the build-scripts to generate the docker container
    ├── Dockerfile              The generated Dockerfile
```

## Build
```bash
./build-python.sh
```
The generated docker container is based on the official dockerhub-image python

## Run the WebSite directly (without docker)
```bash
python app_python.py
```

## Run the WebSite (as docker container)
Attention: The docker image has to be built already.
```bash
./run-python.sh
```

Details:
- Run ```docker run -t -d -p 8080:8080 --name wrap4u wrap4u-app``` to start the container
- Open http://127.0.0.1:8080/ in your browser.
- Run ```docker stop wrap4u``` to shutdown container.

## Flask template rendering
Flask is using templates to fill the statical HTML-pages with dynamic content. 
The templates are stored in an extra directory (here app_python) and are using the Jinja2 Markup, f.e.
```html
<html>
    <body>
        <h1>Hello {{ username }}</h1>
    </body>
</html>
```

In the Python-file (here app_python.py) the call to template-rendering looks like this
```Python
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name = 'Timotheus'
    return render_template('index.html', username=name)
```

Further Material:
- A starter tutorial can be found here https://pythonbasics.org/flask-tutorial-templates/
- For a reference see https://flask.palletsprojects.com/en/2.0.x/api/
- Templating with Jinja2 in Flask https://code.tutsplus.com/tutorials/templating-with-jinja2-in-flask-essentials--cms-25571 