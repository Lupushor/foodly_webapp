from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_webapp():
    if request.method == 'GET':
        return '''
        <!DOCTYPE html>
        <html>
        <head><title>Telegram WebApp</title></head>
        <body>
            <h1>Hello from WebApp!</h1>
            <script src="https://telegram.org/js/telegram-web-app.js"></script>
            <script>
                const tg = window.Telegram.WebApp;
                tg.ready();
                tg.expand();
                document.write("User: " + JSON.stringify(tg.initData));
            </script>
        </body>
        </html>
        '''
    elif request.method == 'POST':
        data = request.get_json()
        print(data)  # Для отладки
        return {"status": "ok"}

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')