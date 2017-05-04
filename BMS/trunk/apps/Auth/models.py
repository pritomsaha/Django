from django.conf import settings
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# Create your models here.
class UserManager(BaseUserManager):
	use_in_migrations = True
	def create_user(self, fullname, username, email, password, **extra_fields):
		if not username:
			raise ValueError('The given username must be set')
		email = self.normalize_email(email)
		username = self.model.normalize_username(username)
		user = self.model(fullname=fullname, username=username, email=email, password=password, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

def upload_location(instance, filename):
	return '/'.join(['images', 'users', instance.username, filename])

class User(AbstractBaseUser):
	fullname = models.CharField(_('fullname'), max_length = 50)
	username = models.CharField(_('username'), max_length = 40, unique = True)
	email = models.EmailField(_('email address'), unique = True)
	password = models.CharField(_('password'), max_length =  100)
	status = models.BooleanField(_('status'), default = True)
	profile_image = models.ImageField(_('profile photo'), upload_to = upload_location, null = True)
	created_at = models.DateTimeField(default = datetime.now)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.IntegerField(null = True)
	updated_by = models.IntegerField(null = True)

	objects = UserManager()
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['fullname','email']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_encoded_id(self):
		return settings.HASHID.encode(self.id)

	def get_status(self):
		if self.status:
			return "Active"
		return "Disable"

	def get_profile_image(self):
		if self.profile_image:
			return self.profile_image.url
		return '/media/images/users/default.gif'



