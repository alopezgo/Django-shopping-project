from django.db import models

# Creación clases asociadas al Producto

class EmpresaPyme (models.Model):
    CHILE = 'CHI'
    SANTANDER = 'SAN'
    SCOTIABANK = 'SCO'
    ESTADO = 'EST'
    FALABELLA = 'FAL'
    DESARROLLO = 'DES'
    BICE = 'BIC'
    CONSORCIO = 'CON'
    BCI = 'BCI'
    ITAU = 'ITA'
    SECURITY = 'SEC'
    CITIBANK = 'CIT'
    INTERNACIONAL = 'INT'
    
    CORRIENTE = 'COR'
    AHORRO = 'AHOR'
        
    BANCO_OPCIONES = [
        (CHILE, 'Banco de Chile'),
        (SANTANDER, 'Banco Santander-Santiago'),
        (SCOTIABANK, 'Banco Scotiabank'),
        (ESTADO, 'Banco del Estado de Chile'),
        (FALABELLA, 'Banco Falabella'),
        (DESARROLLO, 'Banco del Desarrollo'),
        (BICE, 'Banco Bice'),
        (CONSORCIO, 'Banco Consorcio'),
        (BCI, 'Banco de Credito e Inversiones'),
        (ITAU, 'Banco Itau'),
        (SECURITY, 'Banco Security'),
        (CITIBANK, 'Citibank N.A'),
        (INTERNACIONAL, 'Banco Internacional'),
    ]
    
    CUENTA_OPCIONES = [
        (CORRIENTE, 'Cuenta Corriente/Cuenta Vista'),
        (AHORRO, 'Cuenta Ahorro'),
    ]
        
    idPyme = models.AutoField(primary_key= True, verbose_name= 'ID Pyme')
    nombrePyme = models.CharField(max_length=50, verbose_name='Nombre Pyme')
    rutPyme = models.CharField(max_length= 12, verbose_name= 'Rut Pyme')
    bancoPyme = models.CharField(max_length= 4, choices = BANCO_OPCIONES, verbose_name= 'Banco Pyme')
    tipoCuentaPyme = models.CharField(max_length= 4, choices = CUENTA_OPCIONES, verbose_name= 'Tipo cuenta Banco Pyme')
    cuentaBancoPyme = models.CharField(max_length= 15, verbose_name= 'Cuenta Bancaria Pyme')
    correoPyme = models.EmailField(max_length=100, verbose_name='Email Pyme')
    
    def __str__(self) -> str:
        return self.nombrePyme


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoria')

    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='ID Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre Producto')
    descripcionProducto = models.TextField(max_length=500, verbose_name='Descripcion Producto')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    activoProducto = models.BooleanField(default=True, verbose_name='active')
    precioProducto = models.PositiveIntegerField(verbose_name= 'Precio Producto')
    imagenProducto = models.ImageField(upload_to='static/images/upload/')
    stockProducto = models.PositiveIntegerField(verbose_name= 'Stock Producto')
    pymeProducto = models.ForeignKey(EmpresaPyme, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombreProducto
