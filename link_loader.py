from flask import Flask, request, render_template
from webbrowser import open

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def indext():
    if request.method == 'POST':
        open(request.form.get('url'))
    return render_template('index.html')


app.run(host='0.0.0.0', debug=True, ssl_context=('cert.pem', 'key.pem'))
