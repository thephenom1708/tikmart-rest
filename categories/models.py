from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from choices.models import Color, FootwareSize, FootwareCategory, ClothingSize, ClothingCategory, ClothingOccasion, \
	AutomobileType, Sport, Author, Publisher, Language, BookGenere
from products.models import Product
from tikmart.utils import unique_slug_generator

FOOTWEAR_CATEGORY_CHOICES = (
	('chappal', 'Chappal'), ('sandal', 'Sandal'), ('slippers', 'Slippers'), ('loafers', 'Loafers'),
	('sneakers', 'Sneakers'),
	('boots', 'Boots'), ('flip-flops', 'Flip-Flops'), ('heels', 'Heels'),
	('casual', 'Casual Shoes'), ('sport', 'Sport Shoes'),
)

CLOTHING_CATEGORY_CHOICES = (
	('t-shirt', 'T-Shirt'), ('shirt', 'Shirt'), ('ethnic', 'Ethnic'), ('suits & blazers', 'Suits & Blazers'),
	('hoodie', 'Hoodie'),
	('jeans', 'Jeans'), ('trouser', 'Trouser'), ('shorts', 'Shorts'), ('cargo', 'Cargo'),

	('top', 'Top'), ('skirt', 'Skirt'), ('legging', 'Legging'), ('saree', 'Saree'), ('lehenga', 'Lehenga'),
	('anarkali', 'Anarkali'), ('petticoat', 'Petticoat'), ('dupatta', 'Dupatta'),

	('sports t-shirt', 'Sports T-Shirt'), ('tracksuit', 'Tracksuit'), ('trackpant', 'Trackpant'),
	('sweater', 'Sweater'), ('sweatshirt', 'Sweatshirt'), ('jacket', 'Jacket'), ('raincoat', 'Raincoat'),
	('innerwares', 'Innerwares'), ('sleepware', 'Sleepware'),
)

CLOTHING_OCCASION_CHOICES = (
	('casual', 'Casual'), ('formal', 'Formal'), ('party', 'Party'), ('lounge wear', 'Lounge Wear'),
	('beach wear', 'beach wear'), ('sports', 'Sports'), ('festive', 'Festive'), ('sleep wear', 'Sleep Wear'),
	('innerwear', 'Innerwear'),
)

CLOTHING_SLEEVE_CHOICES = (
	('short', 'Short Sleeve'), ('half', 'Half Sleeve'), ('3/4', '3/4 Sleeve'),
	('full', 'Full Sleeve'), ('sleeveless', 'Sleeveless'),
)

GENDER_CHOICES = (
	('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex'), ('kid', 'Kid')
)


def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		model_type = instance.__class__.__name__
		# print(model_type)
		instance.content_type = ContentType.objects.get(model=model_type.lower())


class Footware(Product):
	brand = models.CharField(max_length=100, blank=True, null=True)
	sizes = models.ManyToManyField(FootwareSize, blank=True)
	colors = models.ManyToManyField(Color, blank=True)
	gender = models.CharField(max_length=50, default='male', choices=GENDER_CHOICES)
	type = models.ForeignKey(FootwareCategory, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title + "--" + self.brand

	def get_absolute_url(self):
		return reverse("categories:footware_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=Footware)


class Clothing(Product):
	brand = models.CharField(max_length=100, blank=True, null=True)
	category = models.ForeignKey(ClothingCategory, blank=True, null=True, on_delete=models.SET_NULL)
	type = models.CharField(max_length=100, blank=True, null=True)
	sleeve = models.CharField(max_length=50, blank=True, null=True, choices=CLOTHING_SLEEVE_CHOICES)
	colors = models.ManyToManyField(Color, blank=True)
	sizes = models.ManyToManyField(ClothingSize, blank=True)
	gender = models.CharField(max_length=50, blank=True, null=True, choices=GENDER_CHOICES)
	occasion = models.ForeignKey(ClothingOccasion, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title + "--" + self.brand

	def get_absolute_url(self):
		return reverse("categories:clothing_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=Clothing)


class Automobile(Product):
	brand = models.CharField(max_length=100, blank=True, null=True)
	type = models.ForeignKey(AutomobileType, blank=True, null=True, on_delete=models.SET_NULL)
	colors = models.ManyToManyField(Color, blank=True)

	def __str__(self):
		return self.title + "--" + self.brand

	def get_absolute_url(self):
		return reverse("categories:automobile_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=Automobile)


class Electronic(Product):
	pass


pre_save.connect(pre_save_receiver, sender=Electronic)


class Furniture(Product):
	brand = models.CharField(max_length=100, blank=True, null=True)
	material = models.CharField(max_length=100, blank=True, null=True)

	def get_absolute_url(self):
		return reverse("categories:furniture_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=Furniture)


class SportsEquipment(Product):
	brand = models.CharField(max_length=100, blank=True, null=True)
	related_sport = models.ForeignKey(Sport, blank=True, null=True, on_delete=models.SET_NULL)
	weight = models.CharField(max_length=100, blank=True, null=True)
	material = models.CharField(max_length=100, blank=True, null=True)

	def get_absolute_url(self):
		return reverse("categories:sportsequipment_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=SportsEquipment)


class Book(Product):
	author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
	language = models.ForeignKey(Language, blank=True, null=True, on_delete=models.SET_NULL)
	genre = models.ManyToManyField(BookGenere, blank=True)
	publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
	edition = models.CharField(max_length=100, blank=True, null=True)
	no_of_pages = models.IntegerField(blank=True, null=True)

	def get_absolute_url(self):
		return reverse("categories:book_detail", kwargs={"slug": self.slug})


pre_save.connect(pre_save_receiver, sender=Book)
