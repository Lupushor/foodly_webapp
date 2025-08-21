from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def handle_webapp():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')