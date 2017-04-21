from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from Employees.models import Employee
# Create your models here.

class PortfolioManager(models.Manager):
	def as_choices(self):
		for portfolio in self.all():
			yield(portfolio.pk, force_text(portfolio))

class Portfolio(models.Model):
	concern_persons = models.ManyToManyField(Employee)
	name = models.CharField(_('name'), max_length = 40)
	description = models.TextField(_('description'), default = "It is a description field")
	status = models.BooleanField(_('status'), default = True)
	created_at = models.DateTimeField(default = datetime.now)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.IntegerField()
	updated_by = models.IntegerField(null = True)

	objects = PortfolioManager()

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'portfolios'

	def get_encoded_id(self):
		return settings.HASHID.encode(self.id)

class Purpose(models.Model):
	name = models.CharField(_('name'), max_length = 40)
	description = models.TextField(_('description'), default = "It is a description field")
	status = models.BooleanField(_('status'), default = True)
	created_at = models.DateTimeField(default = datetime.now)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.IntegerField()
	updated_by = models.IntegerField(null = True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'purposes'

	def get_encoded_id(self):
		return settings.HASHID.encode(self.id)

class Product(models.Model):
	concern_persons = models.ManyToManyField(Employee)
	portfolio = models.ForeignKey(Portfolio, on_delete = models.CASCADE)
	name = models.CharField(_('name'), max_length = 40)
	product_code = models.CharField(_('code'), max_length = 20, unique = True)
	description = models.TextField(_('description'), default = "It is a description field")
	status = models.BooleanField(_('status'), default = True)
	charge = models.ManyToManyField(Purpose, through = 'ProductCharge')
	created_at = models.DateTimeField(default = datetime.now)
	updated_at = models.DateTimeField(auto_now = True)
	created_by = models.IntegerField()
	updated_by = models.IntegerField(null = True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'products'

	def get_encoded_id(self):
		return settings.HASHID.encode(self.id)

class ProductCharge(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	purpose = models.ForeignKey(Purpose, on_delete = models.CASCADE)
	amount = models.FloatField(_('amount'))

	class Meta:
		db_table = 'product_charges'