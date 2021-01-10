from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager




class razonSocial(TimeStampedModel):

    name=models.CharField(
        'Nombre',
        max_length=30,
    )

    class Meta:
        verbose_name='Razon Social'
        verbose_name_plural='Razones Sociales'

    def __str__(self):
        return self.name

class unidadOperativa(TimeStampedModel):


    razonSocial=models.ForeignKey(
        razonSocial,
        on_delete=models.CASCADE,

    )

    name=models.CharField(
        'Nombre',
        max_length=30,
    )

    unique_together = [['razonSocial', 'id']]

    class Meta:
        verbose_name='Unidad Operativa'
        verbose_name_plural='Unidades Operativas'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):


    TYPEDOC_CHOICES = (
        ('1', 'DNI'),
        ('2', 'Carnet Extranjeria'),
   
    )

    TYPECOMPANY_CHOICES = (
        ('1', 'Colaborador'),
        ('2', 'Contrata'),
   
    )


    email = models.EmailField(unique=True)
  

    full_name=models.CharField(
        'Nombre',
        max_length=30,
    )
    lastnamep=models.CharField(
        'Apellido Paterno',
        max_length=30,
    )

    lastnamem=models.CharField(
        'Apellido Materno',
        max_length=30,
    )

    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True,
    )

    ocupation = models.CharField(
        'Cargo',
        max_length=30, 
        blank=True,
    )
    TypeDoc = models.CharField(
        'Tipo Documento',
        max_length=1, 
        choices=TYPEDOC_CHOICES, 
        blank=True,
    )


    NroDoc = models.CharField(
        'Nro. Documento',
        max_length=8, 
        blank=True,
    )


    TypeCompany = models.CharField(
        'Tipo Empresa',
        max_length=1, 
        choices=TYPECOMPANY_CHOICES, 
        blank=True,
    )

    razonSocial=models.ForeignKey(
        razonSocial,
        on_delete=models.CASCADE,
        blank=True, 
        null=True,

    )

    unidadOperativa=models.ForeignKey(
        unidadOperativa,
        on_delete=models.CASCADE,
        blank=True, 
        null=True,

    )

    Contrata = models.CharField(
        'Contrata',
        max_length=70,
        null=True,
    )


    Ruc = models.CharField(
        'RUC',
        max_length=11,
        null=True,
    )


    #
    is_staff = models.BooleanField("Es solicitante",default=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name






