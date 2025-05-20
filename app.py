from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    message = request.form.get('message')

    if not name or not message:
        return "Пожалуйста, заполните все поля формы", 400

    processed_data = {
        'name': name.upper(),
        'message': message[::-1]  # переворачиваем сообщение
    }

    return render_template('result.html', data=processed_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)