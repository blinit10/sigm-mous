from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
#funcion para mostrar el index
def cerrar_sesion(request):
	logout(request)
	return redirect('login')

@login_required
def estacion_add_view(request):
	if 'principal.add_estacion' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = EstacionForm()
	if request.method == 'POST':
		form = EstacionForm(request.POST)
		if form.is_valid():
			estacion = Estacion(estacion=form.cleaned_data['estacion'])
			estacion.save()
			return redirect('admin_index')
		else:
			form = EstacionForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'estación',  'usuario':request.user})

@login_required
def estacion_modify_view(request, estacion_id):
	if 'principal.change_estacion' not in request.user.get_all_permissions():
		return redirect('admin_index')
	estacion = get_object_or_404(Estacion, pk=estacion_id)
	form = EstacionForm(instance=estacion)
	if request.method == 'POST':
		form = EstacionForm(request.POST)
		if form.is_valid():
			estacion.estacion = form.cleaned_data['estacion']
			estacion.save()
			return redirect('admin_index')
		else:
			form = EstacionForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'estación',  'usuario':request.user, 'puede_eliminar':request.user.has_perm('principal.delete_estacion')})

@login_required
def estacion_delete_view(request, estacion_id):
	puede_eliminar = request.user.has_perm('principal.delete_estacion')
	if puede_eliminar == False:
		return redirect('/estaciones/modificar/'+estacion_id+'/eliminar/')
	estacion = get_object_or_404(Estacion, pk=estacion_id)
	estacion.delete()
	return redirect('admin_index')

@login_required
def rvm_add_view(request):
	if 'principal.add_reportevariablemeteorologica' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = RVMForm()
	if request.method == 'POST':
		form = RVMForm(request.POST)
		if form.is_valid():
			rvm = ReporteVariableMeteorologica(estacion=form.cleaned_data['estacion'],
											   meteorologo=form.cleaned_data['meteorologo'],
											   fecha_hora=form.cleaned_data['fecha_hora'],
											   temperatura=form.cleaned_data['temperatura'],
											   humedad=form.cleaned_data['humedad'],
											   presion=form.cleaned_data['presion'],
											   dirr=form.cleaned_data['dirr'], dirs=form.cleaned_data['dirs'],
											   velp=form.cleaned_data['velp'], vels=form.cleaned_data['vels'])
			rvm.save()
			return redirect('admin_index')
		else:
			form = RVMForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'reporte de variable meteorologica',  'usuario':request.user})

@login_required
def rvm_modify_view(request, rvm_id):
	if 'principal.change_reportevariablemeteorologica' not in request.user.get_all_permissions():
		return redirect('admin_index')
	rvm = get_object_or_404(ReporteVariableMeteorologica, pk=rvm_id)
	form = RVMForm(instance=rvm)
	if request.method == 'POST':
		form = RVMForm(request.POST)
		if form.is_valid():
			rvm.estacion = form.cleaned_data['estacion']
			rvm.meteorologo = form.cleaned_data['meteorologo']
			rvm.fecha_hora = form.cleaned_data['fecha_hora']
			rvm.temperatura = form.cleaned_data['temperatura']
			rvm.humedad = form.cleaned_data['humedad']
			rvm.presion = form.cleaned_data['presion']
			rvm.dirr = form.cleaned_data['dirr']
			rvm.dirs = form.cleaned_data['dirs']
			rvm.velp = form.cleaned_data['velp']
			rvm.vels = form.cleaned_data['vels']
			rvm.save()
			return redirect('admin_index')
		else:
			form = RVMForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'reporte de variable meteorologica',  'usuario':request.user})

@login_required
def rvm_delete_view(request, rvm_id):
	puede_eliminar = request.user.has_perm('principal.delete_ereportevariablemeteorologica')
	if puede_eliminar == False:
		return redirect('/rvm/modificar/' + rvm_id + '/eliminar/')
	rvm = get_object_or_404(ReporteVariableMeteorologica, pk=rvm_id)
	rvm.delete()
	return redirect('admin_index')

#{'auth.delete_permission', 'auth.add_user', 'auth.add_group', 'principal.delete_informeoficialvariablemeteorologicapronvincial', 'principal.delete_partemeteorologicoprovincial', 'principal.add_partemeteorologicogeneral', 'admin.delete_logentry', 'principal.add_informeoficialvariablemeteorologicapronvincial', 'auth.delete_group', 'admin.view_logentry', 'principal.view_estacion', 'principal.change_informevariablemeteorologicageneral', 'principal.change_partemeteorologicogeneral', 'principal.change_partemeteorologicoprovincial', 'contenttypes.change_contenttype', 'admin.add_logentry', 'auth.view_group', 'principal.add_reportevariablemeteorologica', 'principal.delete_partemeteorologicogeneral', 'principal.delete_estacion', 'principal.view_informevariablemeteorologicageneral', 'principal.add_informevariablemeteorologicageneral', 'principal.view_informeoficialvariablemeteorologicapronvincial', 'principal.change_informeoficialvariablemeteorologicapronvincial', 'contenttypes.add_contenttype', 'principal.view_partemeteorologicogeneral', 'auth.add_permission', 'auth.delete_user', 'auth.view_user', 'auth.change_group', 'auth.view_permission', 'principal.view_reportevariablemeteorologica', 'sessions.delete_session', 'auth.change_user', 'principal.add_estacion', 'principal.delete_informevariablemeteorologicageneral', 'admin.change_logentry', 'principal.delete_reportevariablemeteorologica', 'contenttypes.delete_contenttype', 'principal.change_estacion', 'contenttypes.view_contenttype', 'sessions.view_session', 'principal.view_partemeteorologicoprovincial', 'principal.add_partemeteorologicoprovincial', 'sessions.change_session', 'principal.change_reportevariablemeteorologica', 'auth.change_permission', 'sessions.add_session'}

@login_required
def iovmg_add_view(request):
	if 'principal.add_informevariablemeteorologicageneral' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = IOVMGForm()
	if request.method == 'POST':
		form = IOVMGForm(request.POST)
		if form.is_valid():
			iovmg = InformeVariableMeteorologicaGeneral(
				tecnico=form.cleaned_data['tecnico'], fecha_hora=form.cleaned_data['fecha_hora'],
				temperatura=form.cleaned_data['temperatura'], viento=form.cleaned_data['viento'],
				lluvia=form.cleaned_data['lluvia'], humedad=form.cleaned_data['humedad'],
				barometro=form.cleaned_data['barometro']
			)
			iovmg.save()
			return redirect('admin_index')
		else:
			form = IOVMGForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'informe oficial de variable meteorologica general',  'usuario':request.user})

@login_required
def iovmg_modify_view(request, iovmg_id):
	if 'principal.change_informevariablemeteorologicageneral' not in request.user.get_all_permissions():
		return redirect('admin_index')
	iovmg = get_object_or_404(InformeVariableMeteorologicaGeneral, pk=iovmg_id)
	form = IOVMGForm(instance=iovmg)
	if request.method == 'POST':
		form = IOVMGForm(request.POST)
		if form.is_valid():
			iovmg.tecnico = form.cleaned_data['tecnico']
			iovmg.fecha_hora = form.cleaned_data['fecha_hora']
			iovmg.temperatura = form.cleaned_data['temperatura']
			iovmg.viento = form.cleaned_data['viento']
			iovmg.lluvia = form.cleaned_data['lluvia']
			iovmg.humedad = form.cleaned_data['humedad']
			iovmg.barometro = form.cleaned_data['barometro']
			iovmg.save()
			return redirect('admin_index')
		else:
			form = IOVMGForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'informe de variable meteorologica general',  'usuario':request.user})

@login_required
def iovmg_delete_view(request, iovmg_id):
	puede_eliminar = request.user.has_perm('principal.delete_informevariablemeteorologicageneral')
	if puede_eliminar == False:
		return redirect('/iovmg/modificar/' + iovmg_id + '/eliminar/')
	iovmg = get_object_or_404(InformeVariableMeteorologicaGeneral, pk=iovmg_id)
	iovmg.delete()
	return redirect('admin_index')

@login_required
def iovmp_add_view(request):
	if 'principal.add_informeoficialvariablemeteorologicapronvincial' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = IOVMPForm()
	if request.method == 'POST':
		form = IOVMPForm(request.POST)
		if form.is_valid():
			iovmp = InformeOficialVariableMeteorologicaPronvincial(
				provincia=form.cleaned_data['provincia'], estacion=form.cleaned_data['estacion'],
				fecha_hora=form.cleaned_data['fecha_hora'], viento=form.cleaned_data['viento'],
				lluvia=form.cleaned_data['lluvia'], temperatura=form.cleaned_data['temperatura'],
				humedad=form.cleaned_data['humedad'], barometro=form.cleaned_data['barometro']
			)
			iovmp.save()
			return redirect('admin_index')
		else:
			form = IOVMPForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'informe oficial de variable meteorologica provincial',  'usuario':request.user})

@login_required
def iovmp_modify_view(request, iovmp_id):
	if 'principal.change_informeoficialvariablemeteorologicapronvincial' not in request.user.get_all_permissions():
		return redirect('admin_index')
	iovmp = get_object_or_404(InformeOficialVariableMeteorologicaPronvincial, pk=iovmp_id)
	form = IOVMPForm(instance=iovmp)
	if request.method == 'POST':
		form = IOVMPForm(request.POST)
		if form.is_valid():
			iovmp.provincia = form.cleaned_data['provincia']
			iovmp.estacion = form.cleaned_data['estacion']
			iovmp.fecha_hora = form.cleaned_data['fecha_hora']
			iovmp.viento = form.cleaned_data['viento']
			iovmp.lluvia = form.cleaned_data['lluvia']
			iovmp.temperatura = form.cleaned_data['temperatura']
			iovmp.humedad = form.cleaned_data['humedad']
			iovmp.barometro = form.cleaned_data['barometro']
			iovmp.save()
			return redirect('admin_index')
		else:
			form = IOVMGForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'informe de variable meteorologica provincial',  'usuario':request.user})

@login_required
def iovmp_delete_view(request, iovmp_id):
	puede_eliminar = request.user.has_perm('principal.delete_informeoficialvariablemeteorologicapronvincial')
	if puede_eliminar == False:
		return redirect('/iovmp/modificar/' + iovmp_id + '/eliminar/')
	iovmp = get_object_or_404(InformeOficialVariableMeteorologicaPronvincial, pk=iovmp_id)
	iovmp.delete()
	return redirect('admin_index')

@login_required
def pmp_add_view(request):
	if 'principal.add_partemeteorologicoprovincial' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = PMPForm()
	if request.method == 'POST':
		form = PMPForm(request.POST)
		if form.is_valid():
			pmp = ParteMeteorologicoProvincial(
				provincia=form.cleaned_data['provincia'], meteorologo=form.cleaned_data['meteorologo'],
				fecha_hora=form.cleaned_data['fecha_hora'], temperatura=form.cleaned_data['temperatura'],
				viento=form.cleaned_data['viento'], lluvia=form.cleaned_data['lluvia']
			)
			pmp.save()
			return redirect('admin_index')
		else:
			form = PMPForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'parte meteorologico provincial',  'usuario':request.user})

@login_required
def pmp_modify_view(request, pmp_id):
	if 'principal.change_partemeteorologicoprovincial' not in request.user.get_all_permissions():
		return redirect('admin_index')
	pmp = get_object_or_404(ParteMeteorologicoProvincial, pk=pmp_id)
	form = PMPForm(instance=pmp)
	if request.method == 'POST':
		form = PMPForm(request.POST)
		if form.is_valid():
			pmp.provincia = form.cleaned_data['provincia']
			pmp.meteorologo = form.cleaned_data['meteorologo']
			pmp.fecha_hora = form.cleaned_data['fecha_hora']
			pmp.temperatura = form.cleaned_data['temperatura']
			pmp.viento = form.cleaned_data['viento']
			pmp.lluvia = form.cleaned_data['lluvia']
			pmp.save()
			return redirect('admin_index')
		else:
			form = PMPForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'parte meteorologico provincial',  'usuario':request.user})

@login_required
def pmp_delete_view(request, pmp_id):
	puede_eliminar = request.user.has_perm('principal.delete_partemeteorologicoprovincial')
	if puede_eliminar == False:
		return redirect('/pmp/modificar/' + pmp_id + '/eliminar/')
	pmp = get_object_or_404(ParteMeteorologicoProvincial, pk=pmp_id)
	pmp.delete()
	return redirect('admin_index')

@login_required
def pmg_add_view(request):
	if 'principal.add_partemeteorologicogeneral' not in request.user.get_all_permissions():
		return redirect('admin_index')
	form = PMGForm()
	if request.method == 'POST':
		form = PMGForm(request.POST)
		if form.is_valid():
			pmg = ParteMeteorologicoGeneral(
				tecnico=form.cleaned_data['tecnico'], fecha_hora=form.cleaned_data['fecha_hora'],
				temperatura=form.cleaned_data['temperatura'],
				viento=form.cleaned_data['viento'], lluvia=form.cleaned_data['lluvia']
			)
			pmg.save()
			return redirect('admin_index')
		else:
			form = PMGForm(request.POST)
	return render(request, 'add_template.html', {'form':form, 'objeto':'parte meteorologico general',  'usuario':request.user})

@login_required
def pmg_modify_view(request, pmg_id):
	if 'principal.change_partemeteorologicogeneral' not in request.user.get_all_permissions():
		return redirect('admin_index')
	pmg = get_object_or_404(ParteMeteorologicoGeneral, pk=pmg_id)
	form = PMGForm(instance=pmg)
	if request.method == 'POST':
		form = PMGForm(request.POST)
		if form.is_valid():
			pmg.tecnico = form.cleaned_data['tecnico']
			pmg.fecha_hora = form.cleaned_data['fecha_hora']
			pmg.temperatura = form.cleaned_data['temperatura']
			pmg.viento = form.cleaned_data['viento']
			pmg.lluvia = form.cleaned_data['lluvia']
			pmg.save()
			return redirect('admin_index')
		else:
			form = PMGForm(request.POST)
	return render(request, 'modify_template.html', {'form':form, 'objeto':'parte meteorologico general',  'usuario':request.user})

@login_required
def pmg_delete_view(request, pmg_id):
	puede_eliminar = request.user.has_perm('principal.delete_partemeteorologicogeneral')
	if puede_eliminar == False:
		return redirect('/pmg/modificar/' + pmg_id + '/eliminar/')
	pmg = get_object_or_404(ParteMeteorologicoGeneral, pk=pmg_id)
	pmg.delete()
	return redirect('admin_index')

@login_required
def admin_index(request):
	estaciones = Estacion.objects.all()
	rvm = ReporteVariableMeteorologica.objects.all()
	iovmp = InformeOficialVariableMeteorologicaPronvincial.objects.all()
	iovmg = InformeVariableMeteorologicaGeneral.objects.all()
	pmp = ParteMeteorologicoProvincial.objects.all()
	pmg = ParteMeteorologicoGeneral.objects.all()
	return render(request, 'admin_index.html', {'estaciones':estaciones, 'rvm':rvm,
												'iovmp':iovmp, 'iovmg':iovmg, 'pmp':pmp,
												'pmg':pmg,  'usuario':request.user})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("admin_index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def index(request):
    #creas una variable pmg que contiene todos los partes meteorologicos generales
    # ordenados por fecha, los mas recientes primero
    pmg = ParteMeteorologicoGeneral.objects.order_by('-fecha_hora')
    #retornas una pagina html basado en la plantilla index.html con 'pmg' como contexto para pmg
    return render(request, 'index.html', {'pmg':pmg})