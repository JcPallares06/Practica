from decimal import Decimal
from django.shortcuts import render
from apprecoleccion.models import Caneca
from apprecoleccion.models import Operario
from apprecoleccion.models import Colegio
from apprecoleccion.models import Caneca
from apprecoleccion.models import Colegio
from apprecoleccion.models import Recoleccion
from django.db.models import Sum
from django.db import connection

def mostrarlogin(request):
    return render (request, 'index.html')

def mostrarprincipal(request):
    return render(request, 'principal.html')

def mostrarconsultas(request):
    canfk=Caneca.objects.all().values()
    opefk=Operario.objects.all().values()
    colfk=Colegio.objects.all().values()
    datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
    return render(request, 'consultas.html',datos)

def mostraractualizarcolegio(request,nit):
    try:
        col=Colegio.objects.get(nit=nit)
        datos={'col':col}
        render(request, 'actualizarcolegio.html',datos)
    except:
        col=Colegio.objects.all().values()
        datos={'col':col,
               'r2':'El documento ('+str(nit)+') no existe'}
    return render(request, 'actualizarcolegio.html',datos)

def mostraragregarcolegio(request):
    return render(request, 'agregar_colegio.html')

def mostrarlistarcolegio(request):
    col=Colegio.objects.all().values()
    datos={'col':col}
    return render(request, 'listarcolegio.html',datos)

def mostraractualizaroperario(request, codigo):
    try:
        ope=Operario.objects.get(documento=codigo)
        datos={'ope':ope}
        return render(request, 'actualizaroperario.html',datos)
    except:
        ope=Operario.objects.all().values()
        datos={'ope':ope,
               'r2': 'El documento ('+str(codigo)+') no existe.'}
        return render(request, 'actualizaroperario.html',datos)

def mostraragregaroperario(request):
    return render(request, 'agregar_operario.html')

def mostrarlistaroperario(request):
    ope=Operario.objects.all().values()
    datos={'ope': ope}
    return render(request, 'listaroperario.html', datos)

def mostraractualizarcaneca(request, codigo):
    try:
        can=Caneca.objects.get(codigo=codigo)
        datos={'can':can}
        return render(request, 'actualizarcaneca.html',datos)
    except:
        can=Caneca.objects.get(codigo=codigo)
        datos={'can':can,
               'r2': 'El codigo ('+str(codigo)+') no existe.'}
        return render(request, 'actualizarcaneca.html',datos)
    
def mostraragregarcaneca(request):
    return render(request, 'agregar_caneca.html')

def mostrarlistarcaneca(request):
    can=Caneca.objects.all().values()
    datos={'can':can}
    return render(request, 'listarcaneca.html', datos)

def mostraractualizarrecoleccion(request, id):
    try:
        rec=Recoleccion.objects.get(id=id)
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'rec':rec,
               'canfk':canfk,
               'opefk': opefk,
               'colfk': colfk}
        return render(request, 'actualizarrecoleccion.html',datos)
    except:
        rec=Recoleccion.objects.get(id=id)
        datos={'rec':rec,
               'r2': 'El codigo ('+str(id)+') no existe.'}
        return render(request, 'actualizarrecoleccion.html',datos)

def mostraragregarrecoleccion(request):
    canfk=Caneca.objects.all().values()
    opefk=Operario.objects.all().values()
    colfk=Colegio.objects.all().values()
    datos={'canfk':canfk,
           'opefk':opefk,
           'colfk':colfk}
    return render(request, 'agregar_recoleccion.html',datos)

def mostrarlistarrecoleccion(request):
    rec=Recoleccion.objects.all().values()
    datos={'rec':rec}
    return render(request, 'listarrecoleccion.html',datos)

def insertarrecoleccion(request):
    if request.method=='POST':
        ope=Operario.objects.get(documento=request.POST['operario'])
        cane=Caneca.objects.get(codigo=request.POST['caneca'])
        cole=Colegio.objects.get(nit=request.POST['colegio'])
        pes=request.POST['peso']
        can=request.POST['cantidad']
        pre=request.POST['precio']
        tot=Decimal(request.POST['peso'])*Decimal(request.POST['precio'])
        fec=request.POST['fecha']
        rec=Recoleccion(operario=ope, caneca=cane,colegio=cole, peso=pes, cantidad=can, preciokilo=pre, total=tot, fecha=fec)
        rec.save()
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'r1':'Registro Exitoso',
               'canfk': canfk,
               'opefk': opefk,
               'colfk': colfk}
        return render(request, 'agregar_recoleccion.html',datos)
    else:
        datos={'r2':'Accion no valida'}
        return render(request, 'agregar_recoleccion.html',datos)
    
def insertarcaneca(request):
    if request.method=='POST':
        cod=request.POST['codigo']
        anc=request.POST['ancho']
        alt=request.POST['alto']
        can=Caneca(codigo=cod, ancho=anc, alto=alt)
        can.save()
        datos={'r1':'Registro Exitoso'}
        return render(request, 'agregar_caneca.html',datos)
    else:
        datos={'r2':'Accion no valida'}
        return render(request, 'agregar_caneca.html',datos)
    
def insertaroperario(request):
    if request.method=='POST':
        doc=request.POST['documento']
        nom=request.POST['nombre']
        tel=request.POST['telefono']
        cor=request.POST['correo']
        sul=request.POST['sueldo']
        ope=Operario(documento=doc, nombre=nom, telefono=tel, correo=cor, sueldo=sul)
        ope.save()
        datos={'r1': "Registro Exitoso"}
        return render(request, 'agregar_operario.html',datos)
    else:
        datos={'r2': 'Accion no valida'}
        return render(request, 'agregar_operario.html',datos)

def insertarcolegio(request):
    if request.method=='POST':
        nit=request.POST['nit']
        nom=request.POST['nombre']
        dir=request.POST['direccion']
        tel=request.POST['telefono']
        con=request.POST['contacto']
        fec=request.POST['fecha']
        col=Colegio(nit=nit, nombre=nom, direccion=dir, telefono=tel, contacto=con, fecha=fec)
        col.save()
        datos={'r1':'Registro Exitoso'}
        return render(request, "agregar_colegio.html",datos)
    else:
        datos={'r2':'Accion no valida'}
        return render(request,'agregar_colegio',datos)
    
def actualizaroperario(request, ndocumento):
    if request.method=='POST':
        doc=request.POST['documento']
        nom=request.POST['nombre']
        tel=request.POST['telefono']
        cor=request.POST['correo']
        sul=request.POST['sueldo']
        ope=Operario.objects.get(documento=ndocumento)
        ope.documento=doc
        ope.nombre=nom
        ope.telefono=tel
        ope.correo=cor
        ope.sueldo=sul
        ope.save()
        ope=Operario.objects.all().values()
        datos={'ope':ope
            ,'r1': "Actualización Exitosa"}
        return render(request, 'listaroperario.html',datos)
    else:
        datos={'r2': 'Accion no valida'}
        return render(request, 'listaoperario.html',datos)

def actualizarcaneca(request,codigo):
    if request.method=='POST':
        cod=request.POST['codigo']
        anc=request.POST['ancho']
        alt=request.POST['alto']
        can=Caneca.objects.get(codigo=codigo)
        can.codigo=cod
        can.ancho=anc
        can.alto=alt
        can.save()
        can=Caneca.objects.all().values()
        datos={'can':can,
               'r1': 'Actualización Exitosa '}
        return render(request, 'listarcaneca.html',datos)
    else:
        datos={'r2': 'Accion no valida'}
        return render(request, 'listarcaneca.html',datos)

def actualizarrecoleccion(request,id):
    if request.method=='POST':
        ope=Operario.objects.get(documento=request.POST['operario'])
        cane=Caneca.objects.get(codigo=request.POST['caneca'])
        cole=Colegio.objects.get(nit=request.POST['colegio'])
        pes=request.POST['peso']
        can=request.POST['cantidad']
        pre=request.POST['precio']
        tot = (Decimal(request.POST['peso']) * Decimal(request.POST['precio'])).quantize(Decimal('0.01'))
        fec=request.POST['fecha']
        rec=Recoleccion.objects.get(id=id)
        rec.operario=ope
        rec.caneca=cane
        rec.colegio=cole
        rec.peso=pes
        rec.cantidad=can
        rec.preciokilo=pre
        rec.total=tot
        rec.fecha=fec
        rec.save()
        rec=Recoleccion.objects.all().values()
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'rec':rec,
               'canfk': canfk,
               'opefk': opefk,
               'colfk': colfk,
               'r1':'Actualización Exitosa '}
        return render(request, 'listarrecoleccion.html',datos)
    else:
        datos={'r2':'Accion no valida'}
        return render(request, 'listarrecoleccion.html',datos)


def actualizarcolegio(request,nit):
    if request.method=='POST':
        niit=request.POST['nit']
        nom=request.POST['nombre']
        dir=request.POST['direccion']
        tel=request.POST['telefono']
        con=request.POST['contacto']
        fec=request.POST['fecha']
        col=Colegio.objects.get(nit=nit)
        col.nit=niit
        col.nombre=nom
        col.direccion=dir
        col.telefono=tel
        col.contacto=con
        col.fecha=fec
        col.save()
        col=Colegio.objects.all().values()
        datos={'col':col,
               'r1':'Actualización Exitosa'}
        return render(request, "listarcolegio.html",datos)
    else:
        datos={'r2':'Accion no valida'}
        return render(request,'listarcolegio.html',datos)

def eliminaroperario(request, codigo):
    try:
        ope=Operario.objects.get(documento=codigo)
        ope.delete();
        ope=Operario.objects.all().values()
        datos={'ope':ope,
               'r1': 'Registro eliminado'}
        return render(request, 'listaroperario.html', datos)
    except:
        ope=Operario.objects.all().values()
        datos={'ope':ope,
               'r2':'El documento('+str(codigo)+') no se puede eliminar, No existe'}
        return render(request, 'listaroperario.html',datos)
    
def eliminarcaneca(request, codigo):
    try:
        can=Caneca.objects.get(codigo=codigo)
        can.delete();
        can=Caneca.objects.all().values()
        datos={'can':can,
               'r1':'Registro eliminado'}
        return render(request, 'listarcaneca.html',datos)
    except:
        can=Caneca.objects.all().values()
        datos={'can':can,
               'r2':'El codigo('+str(codigo)+') no se puede eliminar, No existe'}
        return render(request, 'listarcaneca.html',datos)
    
def eliminarcolegio(request, codigo):
    try:
        col=Colegio.objects.get(nit=codigo)
        col.delete();
        col=Colegio.objects.all().values()
        datos={'col':col,
               'r1': 'Registro eliminado'}
        return render(request, 'listarcolegio.html',datos)
    except:
        col=Colegio.objects.all().values()
        datos={'col':col,
               'r2': 'Registro eliminado'}
        return render(request, 'listarcolegio.html',datos)
    
def eliminarrecoleccion(request, id):
    try:
        rec=Recoleccion.objects.get(id=id)
        rec.delete();
        rec=Recoleccion.objects.all().values()
        datos={'rec':rec,
               'r1': 'Registro eliminado'}
        return render(request, 'listarrecoleccion.html',datos)
    except:
        rec=Recoleccion.objects.all().values()
        datos={'rec':rec,
               'r2': 'Registro eliminado'}
        return render(request, 'listarrecoleccion.html',datos)
        
def filtrarcolegios(request, nombre):
    try:
        col=Colegio.objects.filter(nombre=nombre)
        datos={'col':col}
        return render(request, 'listarcolegio.html',datos)
    except:
        col=Colegio.objects.all().values()
        datos={'col':col}
        return render(request, 'listarcolegio.html',datos)

def consultas(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        colegio_id = request.POST['colegio']
        result=None
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        with connection.cursor() as cursor:
            cursor.execute("select sum(cantidad) from apprecoleccion_recoleccion WHERE fecha BETWEEN %s AND %s and colegio_id=%s", [fecha_inicio, fecha_fin,colegio_id])
            result=cursor.fetchone()
            import re
            respuesta=re.findall('\d+', str(result))[0]
            datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk,
            'respuesta':'La cantidad de plastico recogida fue de: '+respuesta}
        return render(request, 'consultas.html', datos)
    else:
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
        return render(request, 'consultas.html', datos)
    
def consultas4(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        result=None
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        with connection.cursor() as cursor:
            cursor.execute("select sum(total) from apprecoleccion_recoleccion WHERE fecha BETWEEN %s AND %s", [fecha_inicio, fecha_fin])
            result=cursor.fetchone()
            import re
            respuesta=re.findall('\d+', str(result))[0]
            datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk,
            'respuesta4':'La cantidad de dinero pagado es de: '+respuesta}
        return render(request, 'consultas.html', datos)
    else:
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
        return render(request, 'consultas.html', datos)
    
def consultas5(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        operario_id=request.POST['operario']
        result=None
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        with connection.cursor() as cursor:
            cursor.execute("select sum(cantidad) from apprecoleccion_recoleccion WHERE fecha BETWEEN %s AND %s and operario_id=%s", [fecha_inicio, fecha_fin,operario_id])
            result=cursor.fetchone()
            import re
            respuesta=re.findall('\d+', str(result))[0]
            datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk,
            'respuesta5':'La cantidad recogida por dicho usuario entre dichas fechas es de: '+respuesta}
        return render(request, 'consultas.html', datos)
    else:
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
        return render(request, 'consultas.html', datos)
    
def consultas7(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        colegio_id=request.POST['colegio']
        result=None
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        with connection.cursor() as cursor:
            cursor.execute("select sum(total) from apprecoleccion_recoleccion WHERE fecha BETWEEN %s AND %s AND colegio_id=%s", [fecha_inicio, fecha_fin,colegio_id])
            result=cursor.fetchone()
            import re
            respuesta=re.findall('\d+', str(result))[0]
            datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk,
            'respuesta7':'La cantidad de dinero pagado es de: '+respuesta}
        return render(request, 'consultas.html', datos)
    else:
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
        return render(request, 'consultas.html', datos)

def consultas8(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['fechainicio']
        fecha_fin = request.POST['fechafin']
        caneca_id=request.POST['caneca']
        result=None
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        with connection.cursor() as cursor:
            cursor.execute("select sum(cantidad) from apprecoleccion_recoleccion WHERE fecha BETWEEN %s AND %s AND caneca_id=%s", [fecha_inicio, fecha_fin,caneca_id])
            result=cursor.fetchone()
            import re
            respuesta=re.findall('\d+', str(result))[0]
            datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk,
            'respuesta8':'La cantidad de plastico es de: '+respuesta}
        return render(request, 'consultas.html', datos)
    else:
        canfk=Caneca.objects.all().values()
        opefk=Operario.objects.all().values()
        colfk=Colegio.objects.all().values()
        datos={'canfk':canfk,
            'opefk': opefk,
            'colfk': colfk}
        return render(request, 'consultas.html', datos)
