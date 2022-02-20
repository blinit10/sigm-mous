from django.db import models


# Create your models here.
#la clase estacion y todas las clases del models.py heredan de models.Model
class Estacion(models.Model):
    #esta clase tiene un campo estacion que es de tipo texto (CharField), tinee una longitud
    #maxima de 255 chars y sera llamado Nombre
    estacion = models.CharField(max_length=255, verbose_name='Nombre')

    #str es una funcion que define la representacion del objeto como cadena de texto
    def __str__(self):
        return self.estacion

    #clase que define los metadatos referencia singular y plural de cada instancia
    class Meta:
        verbose_name = 'Estación'
        verbose_name_plural = '01 - Estaciones'

class ReporteVariableMeteorologica(models.Model):
    #foreignkey es una relacion de uno a muchos en este caso con la tabla estacion
    #cuando se borre la estacion correspondiente, este campo se que vacio
    #null = True y blank = True indican que este campo puede ser vacio y/o nulo
    estacion = models.ForeignKey(Estacion, on_delete=models.SET_NULL, null=True, blank=True)
    meteorologo = models.CharField(max_length=255, verbose_name='Meteorólogo')
    #campo de fecha y hora
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora')
    #FloatField indica un campo de tipo decimal
    dirr = models.FloatField(verbose_name='DIRR')
    dirs = models.FloatField(verbose_name='DIRS')
    vels = models.FloatField(verbose_name='VELS')
    velp = models.FloatField(verbose_name='VELP')
    temperatura = models.FloatField()
    # IntegerField indica un campo de tipo entero
    humedad = models.IntegerField()
    presion = models.IntegerField()

    def __str__(self):
        return self.meteorologo

    class Meta:
        verbose_name = 'Reporte de variable meteorológica'
        verbose_name_plural = '02 - Reportes de variables meteorólogicas'


class InformeOficialVariableMeteorologicaPronvincial(models.Model):
    #lista con tuplas (valor, provincia)
    #el valor izquierdo indica qué se guardara en la base de datos y el valor derecho lo que se mostrara
    #en la interfaz de usuario
    PROVINCIA_CHOICES = (
        ('1','Pinar del Río'),
        ('2', 'La Habana'),
        ('3', 'Artemisa'),
        ('4', 'Mayabeque'),
        ('5', 'Matanzas'),
        ('6', 'Villa Clara'),
        ('7', 'Cienfuegos'),
        ('8', 'Sancti Spíritus'),
        ('9', 'Ciego de Avila'),
        ('10', 'Camaguey'),
        ('11', 'Las Tunas'),
        ('12', 'Holguín'),
        ('13', 'Granma'),
        ('14', 'Santiago de Cuba'),
        ('15', 'Guantánamo'),
        ('16', 'Isla de la Juventud'),
    )
    estacion = models.ForeignKey(Estacion, on_delete=models.SET_NULL, null=True, blank=True)
    #el atributo choises indica cuales seran los elementos del combobox
    provincia = models.CharField(max_length=255, choices=PROVINCIA_CHOICES)
    tecnico = models.CharField(max_length=255, verbose_name='Técnico')
    temperatura = models.FloatField()
    viento = models.FloatField()
    lluvia = models.FloatField()
    humedad = models.IntegerField()
    barometro = models.IntegerField()
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora')

    def __str__(self):
        return self.tecnico

    class Meta:
        verbose_name = 'Informe oficial de variable meteorológica provincial'
        verbose_name_plural = '03 - Informes oficiales de variables meteorólogicas provinciales'

class InformeVariableMeteorologicaGeneral(models.Model):
    tecnico = models.CharField(max_length=255, verbose_name='Técnico')
    temperatura = models.FloatField()
    viento = models.FloatField()
    lluvia = models.FloatField()
    humedad = models.IntegerField()
    barometro = models.IntegerField()
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora')

    def __str__(self):
        return self.tecnico

    class Meta:
        verbose_name = 'Informe de variable meteorológica general'
        verbose_name_plural = '04 - Informes de variables meteorólogicas generales'

class ParteMeteorologicoProvincial(models.Model):
    PROVINCIA_CHOICES = (
        ('1', 'Pinar del Río'),
        ('2', 'La Habana'),
        ('3', 'Artemisa'),
        ('4', 'Mayabeque'),
        ('5', 'Matanzas'),
        ('6', 'Villa Clara'),
        ('7', 'Cienfuegos'),
        ('8', 'Sancti Spíritus'),
        ('9', 'Ciego de Avila'),
        ('10', 'Camaguey'),
        ('11', 'Las Tunas'),
        ('12', 'Holguín'),
        ('13', 'Granma'),
        ('14', 'Santiago de Cuba'),
        ('15', 'Guantánamo'),
        ('16', 'Isla de la Juventud'),
    )
    meteorologo = models.CharField(max_length=255, verbose_name='Meteorólogo')
    provincia = models.CharField(max_length=255, choices=PROVINCIA_CHOICES)
    temperatura = models.FloatField()
    viento = models.FloatField()
    lluvia = models.FloatField()
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora')

    def __str__(self):
        return self.meteorologo

    class Meta:
        verbose_name = 'Parte meteorológico provincial'
        verbose_name_plural = '05 - Partes meteorológicos provinciales'


class ParteMeteorologicoGeneral(models.Model):
    tecnico = models.CharField(max_length=255, verbose_name='Técnico')
    temperatura = models.FloatField()
    viento = models.FloatField()
    lluvia = models.FloatField()
    fecha_hora = models.DateTimeField(verbose_name='Fecha y hora')

    def __str__(self):
        return self.tecnico

    class Meta:
        verbose_name = 'Parte meteorológico general'
        verbose_name_plural = '06 - Partes meteorológicos generales'

