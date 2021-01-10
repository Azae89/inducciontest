from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from .managers import EventManager




class Attendant(TimeStampedModel):


	PUBLICO_CHOICES = (
		('1', 'Todos'),
        ('2', 'Personal Interno'),
        ('3', 'Invitado'),
     
    )


	name=models.CharField(
		'Nombre Completo',
		max_length=100,
		blank=False,
        null=False
	)


	email = models.EmailField(unique=True)


	typeCompany = models.CharField(
		'Tipo Empresa',
		choices=PUBLICO_CHOICES, 
		blank=False,       
		max_length=1,
        null=False
	)


	class Meta:
		verbose_name='Asistente'
		verbose_name_plural='Asistentes'

	def __str__(self):
		return self.name


class Expositor(TimeStampedModel):

	name=models.CharField(
		'Nombre Completo',
		max_length=100,
		blank=False,
        null=False
	)


	email = models.EmailField(unique=True)



	class Meta:
		verbose_name='Expositor'
		verbose_name_plural='Expositores'

	def __str__(self):
		return self.name



class Event(TimeStampedModel):


	ESTADO_CHOICES = (
		('1', 'Registrado'),
        ('2', 'En Curso'),
        ('3', 'Terminado'),
     
    )

	PUBLICO_CHOICES = (
		('1', 'Todos'),
        ('2', 'Personal Interno'),
        ('3', 'Invitado'),
     
    )


	title=models.CharField(
		'Tema',
		max_length=60,
		blank=False,
        null=False
	)
	description=models.CharField(
		'Descripción',
		max_length=100,
		blank=False,
        null=False
	)
	aforo=models.PositiveIntegerField(
		'Aforo',
		blank=False,
        null=False
	)
	public=models.CharField(
		'Público',
		choices=PUBLICO_CHOICES, 
		blank=False,       
		max_length=1,
        null=False
	)
	DateIni=models.DateTimeField(
        'Fecha Inicio Programada', 
        blank=False,
        null=False
    )
	dateEndProgram=models.DateTimeField(
        'Fecha Fin Programada', 
        blank=False,
        null=False
    )
	dateEndReal=models.DateTimeField(
        'Fecha fin Real', 
        blank=True,
        null=True
    )

	duration=models.CharField(
		'Duración', 
		max_length=40,
		blank=True,
        null=True
	)
	state=models.CharField(
		'Estado',
		choices=ESTADO_CHOICES,
		blank=False, 
		max_length=1
	)
	token=models.TextField(
		blank=True,
		null=True
	)

	attend=models.ManyToManyField(Attendant, through='DetailEventAttend')


	expositor=models.ForeignKey(
		Expositor,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)

	

	objects=EventManager()

	class Meta:
		verbose_name='Evento'
		verbose_name_plural='Eventos'

	def __str__(self):
		return self.title





class DetailEventAttend(TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendant = models.ForeignKey(Attendant, on_delete=models.CASCADE)
    dateTime_joined = models.DateTimeField(
        'Fecha  y hora de ingreso', 
        blank=True,
        null=True
    )
    dateTime_out = models.DateTimeField(
        'Fecha  y hora de salida', 
        blank=True,
        null=True


    )


