from django.shortcuts import render_to_response
from django.template import RequestContext
from mazda.apps.home.forms import contact_form
from django.core.mail import EmailMultiAlternatives #enviamos HTML

def about_view (request):
	return render_to_response('home/about.html', context_instance = RequestContext(request))

def contacto_view (request):
	info_enviado = False #Definir  si se envio la informacion o no se envio
	email = ""
	title = ""
	text = ""
	if request.method == "POST": # evalua si el metodo fue POST
		formulario = contact_form(request.POST) #instancia del formulariocon los datos ingresados
		if formulario.is_valid(): #evalua si el formulario es valido
			info_enviado = True #la informacion se envio correctamente
			email = formulario.cleaned_data['correo'] #copia el correo ingresado en el email
			title = formulario.cleaned_data['titulo'] #copia el titulo ingresado en title
			text = formulario.cleaned_data['texto'] #copia el texto ingresado en el text
			'''  Bloque configuracion de envio por GMAIL  '''
			to_admin = 'ulbercastillo1973@gmail.com'
			html_content = "Informacion recibida de %s <br> ---Mensage---<br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com',[to_admin])
			msg.attach_alternative(html_content, 'text/html') #definimos el contenido como HTML
			msg.send() #enviamos el correo
			''' Fin del bloque '''
	else: #si no fue POST entonces fue el metodo GET mostrara un formulario vacio
		formulario = contact_form() # creacion del formulario vacio
	ctx = {'form':formulario, 'email':email, "title":title, "text":text, "info_enviado":info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))