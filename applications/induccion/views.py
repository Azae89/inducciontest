from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse

from django.views.generic import (
	ListView,
	UpdateView,
	View,
	TemplateView,


)
from opentok import OpenTok
from opentok import Roles

from django.http import HttpResponseRedirect

from .forms import (
	EventForm
)

from .models import Event


global Room

class EventListView(ListView):
	template_name='induccion/list_room.html'
	context_object_name = 'eventos'
	paginate_by=3


	def get_context_data(self, **kwargs):
		context = super(EventListView,self).get_context_data(**kwargs)

		return context

	def get_queryset(self):

		# consulta de busqueda

		resultado= Event.objects.listar_eventos()

		return resultado


	def post(self,request,*args,**kwargs):

		
		room=request.POST['id']
		print(room+"eeee")


class UpdateToken(View):

	def post(self,request,*args,**kwargs):


		api_key = '47058394'
		api_secret = '6a0bd6f70f9be22bde0678e0ae81f8d608e5aea1'

		opentok = OpenTok(api_key, api_secret)
		session = opentok.create_session()
		session_id = session.session_id
		token = opentok.generate_token(session_id)

		Event.objects.create_token(request.POST['id'],session_id)

		#logout(request)
		return HttpResponseRedirect(
			reverse(
				'induccion_app:entry-lista'
			)
		)


class OpenRoom(TemplateView):

	template_name ="induccion/Conference_room.html"

	def get_context_data(self,**kwargs):

		#room = "333"
		api_key = '47058394'
		api_secret = '6a0bd6f70f9be22bde0678e0ae81f8d608e5aea1'

		#print(self.request.GET.get('room',))
		context=super(OpenRoom,self).get_context_data(**kwargs)
		

		opentok = OpenTok(api_key, api_secret)


		
		if context['room']==3:
			session_id = Event.objects.get_sala(2)
			token = opentok.generate_token(session_id[0].token,role=Roles.publisher)
		else:
			session_id = Event.objects.get_sala(context['room'])	
			token = opentok.generate_token(session_id[0].token)
		

		

		
		print (token)
		#context=super(OpenRoom,self).get_context_data(**kwargs)

		context['api_key']='47058394'
		context['session_id'] = session_id[0].token
		context['token'] = token


		return context








