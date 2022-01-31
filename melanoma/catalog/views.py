# importamos las librerias necesarias
import sys
import io
from io import BytesIO, StringIO
from django.db import connection
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from django.contrib.auth.models import User
from catalog.forms import GeneroForm, EspecialidadForm, MedicoForm,  EvaluacionForm, PacienteForm
from catalog.models import Genero, Especialidad, Paciente, Evaluacion, Medico

# visualizar los registros


class EvaluacionCompletada(generic.ListView, LoginRequiredMixin):
    model = Evaluacion
    template_name = "catalog/evaluacion_inf.html"
    context_object_name = "obj"


def evaluacionCompletada(request):
    return render(request, "catalog/evaluacion_inf.html")


class GeneroView(generic.ListView, LoginRequiredMixin):
    model = Genero
    template_name = "catalog/genero_list.html"
    context_object_name = "obj"


# crear un nuevo registro
class GeneroNew(SuccessMessageMixin, LoginRequiredMixin,  generic.CreateView):
    permission_required = "catalog.add_genero"
    model = Genero
    template_name = "catalog/genero_form.html"
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy("catalog:genero_list")
    success_message = "Genero Creada Satisfactoriamente"
    # login_url='generales:login'

# editar un registro


class GeneroEdit(SuccessMessageMixin, LoginRequiredMixin,  generic.UpdateView):
    permission_required = "catalog.change_genero"
    model = Genero
    template_name = "catalog/genero_form.html"
    context_object_name = 'obj'
    form_class = GeneroForm
    success_url = reverse_lazy("catalog:genero_list")
    success_message = "Genero Editado Satisfactoriamente"

# eliminamos un registro


class GeneroDel(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    permission_required = "catalog.delete_genero"
    model = Genero
    template_name = "catalog/genero_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalog:genero_list")
    # login_url='generales:login'

# =========================Paciente=========================================000

# visaulizamos un registro


class PacienteView(LoginRequiredMixin, generic.ListView):
    model = Paciente
    template_name = "catalog/paciente_list.html"
    context_object_name = "obj"
    paginate_by = 6


class PacienteNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    permission_required = "catalog.add_paciente"
    model = Paciente
    template_name = "catalog/paciente_form.html"
    context_object_name = 'obj'
    form_class = PacienteForm
    success_url = reverse_lazy("catalog:paciente_list")
    success_message = "Paciente Creado Satisfactoriamente"
    # login_url='generales:login'


class PacienteEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    permission_required = "catalog.change_paciente"
    model = Paciente
    template_name = "catalog/paciente_form.html"
    context_object_name = 'obj'
    form_class = PacienteForm
    success_url = reverse_lazy("catalog:paciente_list")
    success_message = "Paciente Actualizada Satisfactoriamente"
    # login_url='generales:login'


class PacienteDel(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    permission_required = "catalog.del_paciente"
    model = Paciente
    template_name = "catalog/paciente_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalog:paciente_list")
    success_message = "Paciente Eliminado Satisfactoriamente"


# detallamos un registro
class PacienteDetailView(DetailView, LoginRequiredMixin):
    model = Paciente
    template_name = 'catalog/paciente_detail.html'
    success_url = reverse_lazy("catalogs:paciente_list")


# =========================Medico=========================================000

# visaulizamos un registro
class MedicoView(LoginRequiredMixin, generic.ListView):
    model = Medico
    template_name = "catalog/medico_list.html"
    context_object_name = "obj"
    paginate_by = 6


class MedicoNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    permission_required = "catalog.add_medico"
    model = Medico
    template_name = "catalog/medico_form.html"
    context_object_name = 'obj'
    form_class = MedicoForm
    success_url = reverse_lazy("catalog:medico_list")
    success_message = "Médico Creado Satisfactoriamente"
    # login_url='generales:login'


class MedicoEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    permission_required = "catalog.change_medico"
    model = Medico
    template_name = "catalog/medico_form.html"
    context_object_name = 'obj'
    form_class = MedicoForm
    success_url = reverse_lazy("catalog:medico_list")
    success_message = "Médico Actualizado Satisfactoriamente"
    # login_url='generales:login'


class MedicoDel(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    permission_required = "catalog.del_medico"
    model = Medico
    template_name = "catalog/medico_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalog:medico_list")
    success_message = "Médico Eliminado Satisfactoriamente"


# detallamos un registro
class MedicoDetailView(DetailView, LoginRequiredMixin):
    model = Medico
    template_name = 'catalog/medico_detail.html'
    success_url = reverse_lazy("catalog:medico_list")


# ============================================================== Especialidad ================

# visaulizamos un registro
class EspecialidadView(LoginRequiredMixin, generic.ListView):
    model = Especialidad
    template_name = "catalog/especialidad_list.html"
    context_object_name = "obj"
    #login_url = 'registration:login'

# creamos un registro


class EspecialidadNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    permission_required = "catalog.add_especialidad"
    model = Especialidad
    template_name = "catalog/especialidad_form.html"
    context_object_name = 'obj'
    form_class = EspecialidadForm
    success_url = reverse_lazy("catalog:especialidad_list")
    success_message = "Especialidad Creada Satisfactoriamente"
    # login_url='generales:login'

# detallamos un registro


class EspecialidadEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    permission_required = "catalog.change_especialidad"
    model = Especialidad
    template_name = "catalog/especialidad_form.html"
    context_object_name = 'obj'
    form_class = EspecialidadForm
    success_url = reverse_lazy("catalog:especialidad_list")
    success_message = "Especialidad Actualizada Satisfactoriamente"
    # login_url='generales:login'


class EspecialidadDel(SuccessMessageMixin, LoginRequiredMixin,  generic.DeleteView):
    permission_required = "catalog.del_especialidad"
    model = Especialidad
    template_name = "catalog/especialidad_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalog:especialidad_list")
    success_message = "Especialidad Eliminada Satisfactoriamente"


# =======================FOTO==============================
# visaulizamos un registro
class EvaluacionView(generic.ListView, LoginRequiredMixin):
    model = Evaluacion
    template_name = "catalog/evaluacion_list.html"
    context_object_name = "obj"


# creamos un registro


class EvaluacionNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    permission_required = "catalog.add_evaluacion"
    model = Evaluacion
    template_name = "catalog/evaluacion_form.html"
    context_object_name = 'obj'
    form_class = EvaluacionForm
    success_url = reverse_lazy("catalog:informacion_completada")
    success_message = "Evaluacion Creada Satisfactoriamente"
    # login_url='generales:login'

# detallamos un registro


class EvaluacionEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    permission_required = "catalog.change_evaluacion"
    model = Evaluacion
    template_name = "catalog/evaluacion_form.html"
    context_object_name = 'obj'
    form_class = EvaluacionForm
    success_url = reverse_lazy("catalog:evaluacion_list")
    success_message = "Foto Editado Satisfactoriamente"


class EvaluacionDel(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    permission_required = "catalog.delete_evaluacion"
    model = Evaluacion
    template_name = "catalog/evaluacion_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalog:evaluacion_list")
    # login_url='generales:login'
# detalle de cada registro


class EvaluacionViewDetalle(DetailView, LoginRequiredMixin):
    model = Evaluacion
    template_name = "catalog/evaluacion_detalle.html"


# =========================Consultas========================================
# Ficha Medica
contexto = 0


class ReportePacientePDF(View):

    def cabecera(self, pdf, pk):
        # Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        instance = [(p.imagen)for p in Evaluacion.objects.filter(id=pk)]
        nombre = self.request.user.first_name
        apellido = self.request.user.last_name
        medico = nombre + " "+apellido
        instance1 = [(p.codigo, p.paciente.cedula, p.paciente.edad, p.paciente.nombre, p.paciente.apellido, p.paciente.genero.genero, p.fecha, p.evaluacion_foto)
                     for p in Evaluacion.objects.filter(id=pk)]
        img1 = instance[0]
        nombre = str(img1)
        nombre1 = nombre[49:]
        img2 = img1.name
        lista = [x for t in instance1 for x in t]

        print('probando', img2)
        print('lista: ', lista)
        print('imagen: ', nombre1)
        archivo_imagen = img2
        width = 94
        height = 94
        x = 263
        y = 618
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.setStrokeColorRGB(0, 0, 255)  # choose your line color
        pdf.rect(x, y, width, height)
        pdf.drawImage(archivo_imagen, 250, 620, 120,
                      90, preserveAspectRatio=True)
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFillColorRGB(0, 0, 255)  # choose your font colour
        pdf.drawString(273, 780, u"REPORTE")
        pdf.drawString(
            100, 740, u"SISTEMA DE DETECCIÓN DEL CÁNCER DE PIEL")
        pdf.setFillColorRGB(0, 0, 0)  # choose your font colour
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 590, nombre1)

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 560, u"Código: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 560, lista[0])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 540, u"Cédula: ")  # Helvetica-Bold
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 540, lista[1])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 520, u"Edad: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 520, lista[2])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 500, u"Nombres: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 500, lista[3])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 480, u"Apellidos: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 480, lista[4])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 460, u"Género: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 460, lista[5])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 440, u"Fecha: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 440, lista[6])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 420, u"Evaluación: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 420, lista[7])

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(200, 400, u"Médico: ")
        pdf.setFont("Helvetica", 12)
        pdf.drawString(270, 400, medico)

        pdf.setFillColorRGB(0, 0, 255)   # choose your line color
        pdf.setFont("Helvetica", 12)
        pdf.drawString(
            80, 100, u"Copyright © 2020 Universidad Central del Ecuador. Todos los derechos reservados.")
        pdf.setFillColorRGB(0, 0, 255)   # choose your line color
        pdf.setFont("Helvetica", 12)
        pdf.drawString(280, 80, u"Quito-Ecuador")

    def get(self, request, pk=None, *args, **kwargs):
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        y = 600
        # Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf, pk)
        # Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


class ReportePacienteTablaPDF(View):

    def cabecera(self, pdf, pk):
        # Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        instance = [(p.imagen)for p in Evaluacion.objects.filter(id=pk)]
        img1 = instance[0]
        img2 = img1.name
        archivo_imagen = img2
        # Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 250, 650, 120,
                      90, preserveAspectRatio=True)
        # Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        # Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(290, 790, u"UCE")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(270, 770, u"  REPORTE")

    def tabla(self, pdf, y, pk=None):
        cm = 15
        # Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Cedula', 'Edad', 'Nombre', 'Apellido',
                       'Genero', 'Evaluacion')
        # Creamos una lista de tuplas que van a contener a las personas

        if not pk:
            detalles = [(p.paciente.cedula, p.paciento.edad, p.paciente.nombre, p.paciente.apellido, p.paciente.genero.genero, p.evaluacion_foto)
                        for p in Evaluacion.objects.all().order_by('pk')]
        else:
            detalles = [(p.paciente.cedula, p.paciente.edad, p.paciente.nombre, p.paciente.apellido, p.paciente.genero.genero, p.evaluacion_foto)
                        for p in Evaluacion.objects.filter(id=pk)]

        # Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles,
                              colWidths=[5 * cm, 2 * cm, 6 * cm, 7 * cm, 4 * cm, 9 * cm])
        # Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                # La primera fila(encabezados) va a estar centrada
                ('ALIGN', (0, 0), (3, 0), 'CENTER'),
                # Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                # El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        # Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        # Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60, y)

    def get(self, request, pk=None, *args, **kwargs):
        # Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        # La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        # Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)

        y = 600
        self.tabla(pdf, y, pk)
        # Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf, pk)
        # Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
