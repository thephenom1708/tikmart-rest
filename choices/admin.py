from django.contrib import admin

from .models import Color
from .models import FootwareSize, FootwareCategory
from .models import ClothingSize, ClothingCategory, ClothingOccasion 
from .models import AutomobileType
from .models import Sport
from .models import Author, Publisher, Language, BookGenere

from .forms import ColorForm


class ColorAdmin(admin.ModelAdmin):
    form = ColorForm
    list_display = ('name', 'hexcode')
    search_fields = ('name', 'hexcode')
    ordering = ('name', 'hexcode')


admin.site.register(Color, ColorAdmin)

admin.site.register(FootwareSize)
admin.site.register(FootwareCategory)

admin.site.register(ClothingSize)
admin.site.register(ClothingCategory)
admin.site.register(ClothingOccasion)

admin.site.register(Sport)

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(BookGenere)

admin.site.register(AutomobileType)