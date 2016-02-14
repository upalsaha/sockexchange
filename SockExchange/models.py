from django.db import models

class Sock(models.Model):
	name = models.CharField(max_length=30)
	material = models.CharField(max_length=30)
	color = models.CharField(max_length=30)
	description = models.TextField(max_length=255)
	style = models.CharField(max_length=30)
	theme = models.CharField(max_length=30)
	seller = models.EmailField()
	price = models.DecimalField(max_digits=3, decimal_places=2)

	def as_json(self):
		return dict(name=self.name, material=self.material, color=self.color, description = self.description, style = self.style, theme = self.theme, seller = self.seller, price = float(self.price))

class Review(models.Model):
	username = models.CharField(max_length=30)
	rating = models.IntegerField()
	review_text = models.TextField(max_length=255)
	review_title = models.CharField(max_length=30)
	date_published = models.DateField(auto_now_add=True)
	sock_reviewed = models.ForeignKey(Sock)

	def as_json(self):
		return dict(username = self.username, rating = self.rating, review_text = self.review_text, review_title = self.review_title, date_published = self.date_published)


class Order(models.Model):
	customer_name = models.CharField(max_length=30)
	customer_email = models.EmailField()
	date_purchased = models.DateTimeField(auto_now_add=True)
	socks = models.ManyToManyField(Sock)