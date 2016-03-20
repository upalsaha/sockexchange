from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=255)

	def __str__(self):
		return self.username

class Sock(models.Model):
	name = models.CharField(max_length=30)
	material = models.CharField(max_length=30)
	color = models.CharField(max_length=30)
	description = models.TextField(max_length=255)
	style = models.CharField(max_length=30)
	theme = models.CharField(max_length=30)
	seller = models.ForeignKey(User)
	price = models.DecimalField(max_digits=3, decimal_places=2)

	def as_json(self):
		return dict(id=self.id, name=self.name, material=self.material, color=self.color, description = self.description, style = self.style, theme = self.theme, seller = str(self.seller), price = float(self.price))

class Order(models.Model):
	customer_name = models.CharField(max_length=30)
	customer_email = models.EmailField()
	date_purchased = models.DateTimeField(auto_now_add=True)
	socks = models.ManyToManyField(Sock)

class Authenticator(models.Model):
	user_id = models.ForeignKey(User)
	auth = models.CharField(max_length=256)
	auth_time = models.DateTimeField(auto_now_add=True)