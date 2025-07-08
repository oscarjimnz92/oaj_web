import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()  # Cargar variables desde .env

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configuración de correo usando variables del entorno
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')


@app.route('/mensaje', methods=['POST'])
def mensaje():
    nombre = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    mensajes = request.form.get('message')

    msg = Message('Nuevo mensaje desde OAJ Web',
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['ozcar.21@hotmail.com'])
    msg.body = f"Nombre: {nombre}\nEmail: {email}\nServicio: {service}\n\nMensaje:\n{mensajes}"
    mail.send(msg)

    flash('¡Gracias por tu mensaje! Nos pondremos en contacto contigo pronto.')
    return redirect(request.referrer or url_for('index'))

@app.route('/acerca')
def acerca():
    return render_template('acerca.html', active_page='acerca')


@app.route('/servicios')
def servicios():
    return render_template('servicios.html', active_page='servicios')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', active_page='contacto')

@app.route('/privacidad')
def privacidad():
    return render_template('privacidad.html', active_page='privacidad')

if __name__ == '__main__':
    app.run(debug=True)


