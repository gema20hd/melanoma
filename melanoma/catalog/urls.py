
from django.urls import path
from . import views
# importamos los forms.py para utlizar en los urls
from catalog.views import GeneroView, GeneroNew, GeneroEdit, GeneroDel,\
    EspecialidadEdit, EspecialidadNew, EspecialidadDel, EspecialidadView, EvaluacionCompletada,\
    PacienteDel, PacienteNew, PacienteEdit, PacienteView, MedicoNew, MedicoView, MedicoEdit, MedicoDel, MedicoDetailView, \
    EvaluacionEdit, EvaluacionDel, EvaluacionView, EvaluacionNew, PacienteDetailView,  EvaluacionViewDetalle, ReportePacientePDF, ReportePacienteTablaPDF

# creamos los urls de cada tabla para editar, eliminar, crear actulizar
urlpatterns = [

    # Creamos los urls para el crud de la tabla genero
    # Genero
    path('gender', GeneroView.as_view(), name='genero_list'),
    path('gender/new',  GeneroNew.as_view(), name='genero_new'),
    path('gender/edit/<int:pk>', GeneroEdit.as_view(), name='genero_edit'),
    path('gender/delete/<int:pk>', GeneroDel.as_view(), name='genero_delete'),

    # Creamos los urls para el crud de la tabla Paciente
    # ===========================Paciente==========================
    path('patient', PacienteView.as_view(), name='paciente_list'),
    path('patient/new', PacienteNew.as_view(), name='paciente_new'),
    path('patient/edit/<int:pk>', PacienteEdit.as_view(), name='paciente_edit'),
    path('patient/delete/<int:pk>', PacienteDel.as_view(), name='paciente_delete'),
    path('patient/patient_detail/<int:pk>',PacienteDetailView.as_view(), name='paciente_detail'),

    # ===========================medico==========================
    path('doctor', MedicoView.as_view(), name='medico_list'),
    path('doctor/new', MedicoNew.as_view(), name='medico_new'),
    path('doctor/edit/<int:pk>', MedicoEdit.as_view(), name='medico_edit'),
    path('doctor/delete/<int:pk>', MedicoDel.as_view(), name='medico_delete'),
    path('doctor/detail/<int:pk>',
         MedicoDetailView.as_view(), name='medico_detail'),


    # Creamos los urls para el crud de la tabla tipo_especialidad
    # ===========================especialidad==========================
    path('medical_speciality', EspecialidadView.as_view(), name='especialidad_list'),
    path('medical_speciality/new', EspecialidadNew.as_view(), name='especialidad_new'),
    path('medical_speciality/edit/<int:pk>',
         EspecialidadEdit.as_view(), name='especialidad_edit'),
    path('medical_speciality/delete/<int:pk>',EspecialidadDel.as_view(), name='especialidad_delete'),

    # Creamos los urls para el crud de la tabla evaluation
    # =============evaluation- fotos============================
    path('evaluation', EvaluacionView.as_view(), name='evaluacion_list'),
    path('evaluation/new',  EvaluacionNew.as_view(), name='evaluacion_new'),
    path('evaluation/edit/<int:pk>',
         EvaluacionEdit.as_view(), name='evaluacion_edit'),
    path('evaluation/delete/<int:pk>',
         EvaluacionDel.as_view(), name='evaluacion_delete'),
    path('evaluation/detail/<int:pk>',
         EvaluacionViewDetalle.as_view(), name='evaluacion_detalle'),

    # ==========================Impresion==============================000
    path('file/print/<int:pk>', ReportePacientePDF.as_view(),name='reportepaciente'),
    path('file_table/print/<int:pk>', ReportePacienteTablaPDF.as_view(),name='reportepaciente_tabla'),
    # inform
    path('full_report/', EvaluacionCompletada.as_view(), name="informacion_completada"),

]
