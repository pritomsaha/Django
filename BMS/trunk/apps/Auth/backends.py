from django.contrib.auth.hashers import check_password
from .models import User

class ModelBackend:

	def authenticate(self, username=None, password=None):
		if '@' in username:
			kwargs = {'email': username}
		else:
			kwargs = {'username': username}
		try:
			user = User.objects.get(**kwargs)
			if user.check_password(password) and self.user_can_authenticate(user):
				return user
		except User.DoesNotExist:
			return None

	def user_can_authenticate(self, user):
		is_active = getattr(user, 'is_active', None)
		return is_active or is_active is None
	
	def get_user(self, user_id):
		try:
			user = User.objects.get(pk = user_id)
		except User.DoesNotExist:
			return None
		return user if self.user_can_authenticate(user) else None

				
		