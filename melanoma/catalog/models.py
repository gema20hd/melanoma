
from django.db import models
from core.models import ClaseModelo
from django.contrib.auth.models import User
import time
import glob
import os
import random
# Create your models here.

# cargar las imagenes para perfiles de las Pacientes
def custom_upload_to(instance, filename):
    old_instance = Paciente.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'catalog/' + filename

# crea la tabla genero en la base de datos


class Genero(ClaseModelo):
    codigo = models.CharField(max_length=10)
    genero = models.CharField(max_length=10, blank=False)
    unique = True

    def __str__(self):
        return '{}'.format(self.genero)

    # crea un codigo de forma automatica para la clase genero
    def save(self):
        self.genero = self.genero.upper()
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'G-'
        self.codigo = cod+codi
        super(Genero, self).save()

    class Meta:
        verbose_name_plural = "Generos"
        ordering = ['-creado']

# crea la tabla tipo Paciente con los campos que se indican, tipo Paciente se refiere, si es empleado o supervisor


class Especialidad(ClaseModelo):
    codigo = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=300, blank=False)

    def __str__(self):
        return '{}'.format(self.especialidad)

# crea un codigo aleatorio para la tabla tipo Paciente y lo guarda al momento  de realizar un registro
    def save(self):
        self.especialidad = self.especialidad.upper()
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'ESP-'
        self.codigo = cod+codi
        super(Especialidad, self).save()

    class Meta:
        verbose_name_plural = "Especialidades"
        ordering = ['-creado']


# crea la tabla Paciente en la base de datos con los campos que se indican
# ================= Paciente==================

class Medico(ClaseModelo):
    codigo = models.CharField(max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, blank=False)
    nombre = models.CharField(max_length=300, blank=False)
    apellido = models.CharField(max_length=300, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
# crea un codigo aleatorio para la tabla medico y lo guarda al momento  de realizar un registro

    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'MED-'
        self.codigo = cod+codi
        super(Medico, self).save()

    class Meta:
        verbose_name_plural = "Medicos"
        ordering = ['-creado']
    # @property

# crea la tabla paciente en la base de datos con los campos que se indican
# ================= Paciente==================


class Paciente(ClaseModelo):
    codigo = models.CharField(max_length=10)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, blank=False)
    nombre = models.CharField(max_length=300, blank=False)
    apellido = models.CharField(max_length=300, blank=False)
    fecha_nacimiento = models.CharField(max_length=50, blank=False)
    edad = models.CharField(max_length=8)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    telefono = models.CharField(max_length=9, blank=True, unique=True)
    celular = models.CharField(max_length=10, blank=True, unique=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
# crea un codigo aleatorio para la tabla Paciente y lo guarda al momento  de realizar un registro

    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        self.edad = str(self.edadFuncion())
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'PER-'
        self.codigo = cod+codi
        super(Paciente, self).save()

    # @property

    # esta funcio permite calcular la edad de una Paciente recibiendo como parametro la fecha de nacimiento
    def edadFuncion(self):
        tiempoactual = time.strftime("%d/%m/%Y")
        print(tiempoactual)
        tiempo = tiempoactual.split('/')
        diasactual = int(tiempo[2])*365+int(tiempo[1])*30+int(tiempo[0])
        print(diasactual)
        nacimiento = self.fecha_nacimiento
        print(nacimiento)
        tiempoNacimiento = nacimiento.split('/')
        diasactualNacimiento = int(
            tiempoNacimiento[2])*365+int(tiempoNacimiento[1])*30+int(tiempoNacimiento[0])
        print(diasactualNacimiento)
        diasTotales = diasactual-diasactualNacimiento
        print(diasTotales)
        anios = round(diasTotales/365)
        print(anios)
        return anios

# pone tabla Paciente en plural


class Meta:
    verbose_name_plural = "Pacientes"
    ordering = ['-creado']
   # unique_together = ('genero', 'nombre')

# crea la tabla cita en la base de datos con los campos que se indican
# ================= Paciente==================


class Cita(ClaseModelo):
    codigo = models.CharField(max_length=10)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)


# crea un codigo aleatorio para la cita y lo guarda al momento  de realizar un registro


    def save(self):
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'CITA-'
        self.codigo = cod+codi
        super(Paciente, self).save()

    # @property


# crea la tabla Foto en la base de datos con los campos que se indican


class Evaluacion(ClaseModelo):
    codigo = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagen_original', blank=False)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    evaluacion_foto = models.CharField(
        max_length=200, default="No realizado la evaluación")
    fecha = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = 'evaluacion'
        verbose_name_plural = 'evaluaciones'
        ordering = ['-creado']
# crea un codigo aleatorio para la tabla  foto y lo guarda al momento  de realizar un registro
    def save(self):
        self.presave1()
        codi = ''.join(random.choice("1234567890ABCDEFGHIJKMNPQRSTUVWXYZ")
                       for _ in range(5))
        cod = 'EV-'
        self.codigo = cod+codi
        self.imagen = self.imgprefuncion()
        time.sleep(1)
        self.evaluacion_foto = self.predice()
        #self.fecha = time.strftime("%d/%m/%Y")
        self.evaluacion_foto = self.evaluacion_foto.upper()
        # self.comment=self.predice()
        time.sleep(1)
        self.correoEnvio()

        super(Evaluacion, self).save()

    def presave1(self):
        self.fecha = time.strftime("%d/%m/%Y")
        self.evaluacion_foto = self.evaluacion_foto.upper()
        # self.comment=self.predice()
        super(Evaluacion, self).save()

    def imgprefuncion(self):
        import time
        import cv2
        import glob
        import numpy
        import os
        import sys
        from datetime import datetime
        try:
            # nombre = 'La fecha de {} es el {} de {}.'.format(c, 20+1, 'Enero')
            pathimgor = "D:/PROYECTO_TESIS/melanoma/media/imagen_original/"
            f = pathimgor+os.path.basename(self.imagen.name)
            img = cv2.imread(f)
            print('imagen', img)
            # newImg = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
            newImg = cv2.resize(img, (64, 64))
            time.sleep(1)
            apellido = self.paciente.apellido
            fecha1 = datetime.today().strftime('%Y%m%d%H%M')
            #fecha2 = datetime.today().strftime('%H:%M')
            apellido1 = apellido+fecha1
            print("nombre nuevo: ", apellido1)
            time.sleep(1)
            cv2.imwrite(
                'D:/PROYECTO_TESIS/melanoma/media/imagen_original/{}.jpg'.format(apellido1.replace(' ', '_')), newImg)
            time.sleep(1)
            return 'D:/PROYECTO_TESIS/melanoma/media/imagen_original/{}.jpg'.format(apellido1.replace(' ', '_'))
        except:
            print("Error inesperado:", sys.exc_info()[0])
            return "Ingrese una imagen mas grande"
            raise

    def predice(self):
        import numpy as np
        from keras.preprocessing import image
        from keras import models
        from keras.models import load_model
        import tensorflow as tf
        resultado = ""
        image_width = 64
        image_height = 64
        modelo = 'D:/PROYECTO_TESIS/modeloML/modeloMelanoma.h5'
        model = tf.keras.models.load_model(modelo)
        pesos = 'D:/PROYECTO_TESIS/modeloML/better_weight_model.weights.best.hdf5'
        model.load_weights(pesos)
        img = image.load_img(self.imagen.name,
                             target_size=(image_height, image_width))
        img = image.img_to_array(img)/255
        img_expand = np.expand_dims(img, axis=0)
        y_pred = model.predict(img_expand, steps=1)
        print(y_pred)
        y_pred = (y_pred > 0.5).astype(int)
        if y_pred == 0:
            y_pred = 'Tiene Melanoma'
            print(y_pred)
        elif y_pred == 1:
            y_pred = 'No Tiene Melanoma'
            print(y_pred)
        return y_pred

# funcion permite enviar un correo al supervisor

    def correoEnvio(self):
        from django.db.models.fields.files import ImageFieldFile
        from email.mime.multipart import MIMEMultipart
        from email.mime.image import MIMEImage
        from email.mime.text import MIMEText
        import smtplib
        #especialista = "Juan"
        centroMedico="SISTEMA DE DETECCIÓN DE CÁNCER DE PIEL 'MELANOMA' "
        print(centroMedico)
        imagen1 = self.imagen
        # create message object instance
        msg = MIMEMultipart()
        sms = "Estimad@ sr/a: "
        sms1 = " resultado obtenido con una precisión del 95 %"
        sms2 = "Sr/a"
        sms3 = "Código de evaluación: "
        sms4 = "No responda a este mensaje, es un envío automático."
        sms5 = "Saludos cordiales,"
        sms6 = "Derechos reservados UCE"
        # setup the parameters of the message
        password = "aso12345Aop"
        msg['From'] = "melanomasdcp@gmail.com"
        msg['To'] = self.paciente.email
        msg['Subject'] = "Resultado"
        part1 = MIMEText(str(sms)+str(self.paciente.nombre) + " "+str(self.paciente.apellido)
                         + "\n" + str(sms3)+str(self.codigo)+"\n"
                         + str(self.evaluacion_foto) + ":" +
                         str(sms1)+"\n"
                         + "\n\n" + str(sms4)
                         + "\n\n" + str(sms5)
                         + "\nAtentamente,\n"
                         + str(centroMedico)
                         + "\n\n" + str(sms6)+ "\n\n", 'plain')

        mediapath = '{}'.format(imagen1)
        print('part: ', mediapath)
        file = open(mediapath, "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition',
                                'attachment; filename = "IMAGENOGRAFIA"')
        msg.attach(attach_image)
        # msg.attach(part2)
        msg.attach(part1)

        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Envio exitoso  :"+msg['To'])


