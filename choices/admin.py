from django.contrib import admin

from .forms import ColorForm
from .models import Author, Publisher, Language, BookGenre
from .models import AutomobileType
from .models import ClothingSize, ClothingCategory, ClothingOccasion
from .models import Color
from .models import FootwearSize, FootwearCategory
from .models import Sport


class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
    list_display = ('name', 'hexcode')
    search_fields = ('name', 'hexcode')
    ordering = ('name', 'hexcode')


admin.site.register(Color, ColorAdmin)

admin.site.register(FootwearSize)
admin.site.register(FootwearCategory)

admin.site.register(ClothingSize)
admin.site.register(ClothingCategory)
admin.site.register(ClothingOccasion)

admin.site.register(Sport)

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(BookGenre)

admin.site.register(AutomobileType)