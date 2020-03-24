from django.db import models

CLOTHING_SIZE_TYPES = (
	('IN', 'IN'),
	('UK', 'UK'),
	('US', 'US')
)

GENDER_CHOICES = (
	('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex'), ('kid', 'Kid')
)


class Color(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	hexcode = models.CharField(max_length=8, blank=True, null=True)

	def __str__(self):
		return self.name + " -- " + self.hexcode


class FootwearSize(models.Model):
	uk_in = models.IntegerField(blank=True, null=True)
	eu = models.IntegerField(blank=True, null=True)
	length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return str(self.uk_in) + " -- " + str(self.eu)


class FootwearCategory(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(max_length=50, default='male', choices=GENDER_CHOICES)

	def __str__(self):
		return self.name


class ClothingCategory(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	gender = models.CharField(max_length=50, default='male', choices=GENDER_CHOICES)

	def __str__(self):
		return self.name


class ClothingOccasion(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class ClothingSize(models.Model):
	value = models.CharField(max_length=10, blank=True, null=True)
	chest = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	shoulder = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	length = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
	type = models.CharField(max_length=10, blank=True, null=True, choices=CLOTHING_SIZE_TYPES)

	def __str__(self):
		return self.type + " -- " + self.value


class AutomobileType(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class Sport(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name


class Publisher(models.Model):
	name = models.CharField(max_length=50)
	city = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	website = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name


class Language(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class BookGenre(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name
