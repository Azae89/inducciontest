from django.db import models

class EventManager(models.Manager):
	"""procedimiento para entrada"""


	def listar_eventos(self):

		return self.order_by('-created')[:4]


	def create_token(self,id,token):

		obj = self.filter(id=id).update(state=2,token=token)

		#obj.state = "2"
		#obj.token = "dasdasdsa"
		#obj.save()

		return "ok"

	def get_sala(self,id):
		return self.filter(id=id).values_list('token' ,named=True)