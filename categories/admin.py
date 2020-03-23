from django.contrib import admin

from .forms import FootwareForm, ClothingForm, AutomobileForm, FurnitureForm, SportForm, BookForm
from .models import Footware, Clothing, Automobile, Electronic, Furniture, SportsEquipment, Book


class FootwareAdmin(admin.ModelAdmin):
	form = FootwareForm
	list_display = ('title', 'brand', 'type', 'get_sizes', 'get_colors', 'price', 'active', 'featured')
	list_filter = ('brand', 'type', 'active', 'featured')
	fieldsets = (
		('Footware Details', {'fields': ('title', ('brand', 'image'), 'description', ('type', 'gender'))}),
		('Customization', {'fields': ('colors', 'sizes')}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'brand', 'type', 'title', 'gender')
	ordering = ('title', 'brand', 'price', 'active', 'featured')
	filter_horizontal = ()

	def get_colors(self, obj):
		return "\n".join([c.name for c in obj.colors.all()])

	def get_sizes(self, obj):
		return "\n".join([str(c.uk_in) for c in obj.sizes.all()])


class ClothingAdmin(admin.ModelAdmin):
	form = ClothingForm
	list_display = ('title', 'brand', 'category', 'occasion', 'sleeve', 'get_sizes', 'get_colors', 'price', 'active', 'featured')
	list_filter = ('brand', 'category', 'occasion', 'sleeve', 'active', 'featured')
	fieldsets = (
		('Clothing Details', {'fields': ('title', ('brand', 'image'), 'description', ('category', 'occasion', 'gender'))}),
		('Customization', {'fields': (('sleeve', 'colors'), ('type', 'sizes'))}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'brand', 'category', 'title', 'gender', 'occasion')
	ordering = ('title', 'brand', 'category', 'occasion', 'sleeve', 'price', 'active', 'featured')
	filter_horizontal = ['sizes']

	def get_colors(self, obj):
		return "\n".join([color.name for color in obj.colors.all()])

	def get_sizes(self, obj):
		return "\n".join([c.value for c in obj.sizes.all()])


class AutomobileAdmin(admin.ModelAdmin):
	form = AutomobileForm
	list_display = ('title', 'brand', 'type', 'get_colors', 'price', 'active', 'featured')
	list_filter = ('brand', 'brand', 'type', 'active', 'featured')
	fieldsets = (
		('Automobile Details', {'fields': ('title', ('brand', 'image'), 'description')}),
		('Customization', {'fields': ('type', 'colors')}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'brand', 'type', 'price', 'active', 'featured')
	ordering = ('title', 'price', 'active', 'featured')
	filter_horizontal = ()

	def get_colors(self, obj):
		return "\n".join([c.name for c in obj.colors.all()])


class FurnitureAdmin(admin.ModelAdmin):
	form = FurnitureForm
	list_display = ('title', 'brand', 'material', 'price', 'active', 'featured')
	list_filter = ('brand', 'brand', 'material', 'active', 'featured')
	fieldsets = (
		('Furniture Details', {'fields': ('title', ('brand', 'image', 'material'), 'description')}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'brand', 'material', 'price', 'active', 'featured')
	ordering = ('title', 'price', 'active', 'featured')
	filter_horizontal = ()


class SportAdmin(admin.ModelAdmin):
	form = SportForm
	list_display = ('title', 'brand', 'related_sport', 'material', 'weight', 'price', 'active', 'featured')
	list_filter = ('brand', 'brand', 'related_sport', 'active', 'featured')
	fieldsets = (
		('Sports Equipment Details', {'fields': ('title', ('brand', 'image'), 'description')}),
		('Customization', {'fields': ('related_sport', 'material', 'weight')}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'brand', 'related_sport', 'material', 'weight', 'price', 'active', 'featured')
	ordering = ('title', 'weight', 'price', 'active', 'featured')
	filter_horizontal = ()



class BookAdmin(admin.ModelAdmin):
	form = BookForm
	list_display = ('title', 'author', 'publisher', 'language', 'edition', 'get_genre', 'price',  'active', 'featured')
	list_filter = ('author', 'publisher', 'language', 'genre', 'active', 'featured')
	fieldsets = (
		('Book Details', {'fields': ('title', ('author', 'image'), 'description')}),
		('Customization', {'fields': (('publisher', 'language'), ('edition', 'no_of_pages'), 'genre')}),
		('Activity and Pricing', {'fields': ('price', ('featured', 'active'))}),
	)
	search_fields = ('title', 'author', 'publisher', 'language', 'edition', 'get_genre', 'price',  'active', 'featured')
	ordering = ('title', 'edition', 'price',  'active', 'featured')
	filter_horizontal = ['genre']

	def get_genre(self, obj):
		return "\n".join([genre.name for genre in obj.genre.all()])


admin.site.register(Footware, FootwareAdmin)
admin.site.register(Clothing, ClothingAdmin)
admin.site.register(Automobile, AutomobileAdmin)
admin.site.register(Electronic)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(SportsEquipment, SportAdmin)
admin.site.register(Book, BookAdmin)
