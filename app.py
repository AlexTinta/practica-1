from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        # Aquí podrías procesar la información, como guardarla en una base de datos
        return f"Gracias por tu mensaje, {nombre}!"
    return render_template('contacto.html')

# Rutas para servicios individuales (opcional)

@app.route('/servicios/servicio1')
def servicio1():
    return render_template('services/servicio1.html')  # Incluye la subcarpeta 'services'
@app.route('/servicios/servicio2')
def servicio2():
    return render_template('services/servicio2.html')  # Incluye la subcarpeta 'services'


if __name__ == '__main__':
    app.run(debug=True)
