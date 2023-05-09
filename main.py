#Импорт
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

#Результаты формы
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # получаем выбранное изображение
        selected_image = request.form.get('image-selector')

        # Задание №2.Получаем текст
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')

        # Задание №3. Получаем расположение текста
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        # Задание №3. Получаем цвет текста
        selected_color = request.form.get('color-selector')

        return render_template('index.html', 
                               # отображаем выбранное изображение
                               selected_image=selected_image, 

                               # Задание №2. Отображаем текст
                               text_bottom=text_bottom, 
                               text_top=text_top,

                               # Задание №3. Отображаем цвет 
                               selected_color=selected_color,
                               
                               #Задание №3. Отоброжаем расположение текста
                               text_top_y=text_top_y,
                               text_bottom_y=text_bottom_y)
    else:
        # отображаем первое изображение по умолчанию
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)