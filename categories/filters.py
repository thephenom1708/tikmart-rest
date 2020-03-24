from django.db.models import Q
from django.shortcuts import render
from django_filters import FilterSet, rest_framework as filters

from categories.models import Footware, Clothing, SportsEquipment, Furniture, Automobile, Book
from categories.utils import footwear_context, automobile_context, clothing_context, book_context, \
    sports_equipment_context
from choices.models import Color
from categories.utils import footwear_context, automobile_context, clothing_context, book_context, \
    sports_equipment_context
from django.db.models import Q
from django.shortcuts import render
from django_filters import FilterSet, rest_framework as filters

from categories.models import Footware, Clothing, SportsEquipment, Furniture, Automobile, Book
from choices.models import Color


class FootwearFilter(FilterSet):
    # brand = filters1.CharFilter('brand')
    categories = filters.CharFilter('type__name')
    colors = filters.CharFilter(method='filter_by_color')
    brands = filters.CharFilter(method='filter_by_brand')

    class Meta:
        model = Footware
        fields = ['title', 'brands', 'gender', 'categories', 'colors']

    def filter_by_color(self, queryset, name, value):
        color_names = value.strip().split(",")
        colors = Color.objects.filter(name__in=color_names)
        return queryset.filter(colors__in=colors).distinct()

    def filter_by_brand(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()


# def filter_by_min_price(self, name, value):
# 	queryset = self.queryset.filter(price__gt=value)
# 	return queryset
#
# def filter_by_max_price(self, name, value):
# 	queryset = self.queryset.filter(price__lt=value)
# 	return queryset


class ClothingFilter(FilterSet):
    categories = filters.CharFilter('category__name')
    occasions = filters.CharFilter('occasion__name')
    colors = filters.CharFilter(method='filter_by_color')
    brands = filters.CharFilter(method='filter_by_brand')
    sleeves = filters.CharFilter(method='filter_by_sleeve')

    class Meta:
        model = Clothing
        fields = ['title', 'brands', 'sleeves', 'occasions', 'gender', 'categories', 'colors']

    def filter_by_color(self, queryset, name, value):
        print(name)
        color_names = value.strip().split(",")
        colors = Color.objects.filter(name__in=color_names)
        return queryset.filter(colors__in=colors).distinct()

    def filter_by_brand(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()

    def filter_by_sleeve(self, queryset, name, value):
        sleeve_names = value.strip().split(",")
        return queryset.filter(sleeve__in=sleeve_names).distinct()


class AutomobileFilter(FilterSet):
    categories = filters.CharFilter('type__name')
    brands = filters.CharFilter(method='filter_by_brand')
    colors = filters.CharFilter(method='filter_by_color')

    class Meta:
        model = Automobile
        fields = ['title', 'brands', 'categories', 'colors']

    def filter_by_color(self, queryset, name, value):
        color_names = value.strip().split(",")
        colors = Color.objects.filter(name__in=color_names)
        return queryset.filter(colors__in=colors).distinct()

    def filter_by_brand(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()


class FurnitureFilter(FilterSet):
    brands = filters.CharFilter(method='filter_by_brand')

    class Meta:
        model = Furniture
        fields = ['title', 'brands', 'material']

    def filter_by_brand(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()


class SportsEquipmentFilter(FilterSet):
    brands = filters.CharFilter(method='filter_by_brand')
    related_sports = filters.CharFilter(method='filter_by_related_sport')

    class Meta:
        model = SportsEquipment
        fields = ['title', 'brands', 'related_sports', 'material']

    def filter_by_brand(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()

    def filter_by_related_sport(self, queryset, name, value):
        related_sport_names = value.strip().split(",")
        return queryset.filter(related_sport__name__in=related_sport_names).distinct()


class BookFilter(FilterSet):
    languages = filters.CharFilter('language__name')
    genres = filters.CharFilter(method='filter_by_genre')

    class Meta:
        model = Book
        fields = ['title', 'languages', 'genres']

    def filter_by_genre(self, queryset, name, value):
        genre_names = value.strip().split(",")
        return queryset.filter(genre__name__in=genre_names).distinct()



def multiple_select_filter(request, product_type):
    if product_type == "footware":
        return footwear_filter(request)
    elif product_type == "clothing":
        return clothing_filter(request)
    elif product_type == "automobile":
        return automobile_filter(request)
    else:
        return


def footwear_filter(request):
    colors = request.GET.getlist('colors')
    brands = request.GET.getlist('brands')

    if len(colors) == 0 and len(brands) == 0:
        products = Footware.objects.filter(active=True)
    else:
        products = Footware.objects.filter(
                    Q(active=True, colors__name__in=colors) | Q(active=True, brand__in=brands)
                ).distinct()

    context = footwear_context(request)
    context['object_list'] = products
    context['selected_brands'] = brands
    context['selected_colors'] = colors
    template_name = "categories/footwear/list.html"

    return render(request, template_name, context)


def clothing_filter(request):
    colors = request.GET.getlist('colors')
    brands = request.GET.getlist('brands')
    sleeves = request.GET.getlist('sleeves')

    if len(colors) == 0 and len(brands) == 0 and len(sleeves) == 0:
        products = Clothing.objects.filter(active=True)
    else:
        products = Clothing.objects.filter(
            Q(active=True, colors__name__in=colors) | Q(active=True, brand__in=brands) | Q(active=True, sleeve__in=sleeves)
        ).distinct()

    context = clothing_context(request)
    context['object_list'] = products
    context['selected_brands'] = brands
    context['selected_colors'] = colors
    context['selected_sleeves'] = sleeves
    template_name = "categories/clothing/list.html"

    return render(request, template_name, context)


def automobile_filter(request):
    colors = request.GET.getlist('colors')
    brands = request.GET.getlist('brands')

    if len(colors) == 0 and len(brands) == 0:
        products = Automobile.objects.filter(active=True)
    else:
        products = Automobile.objects.filter(
                    Q(active=True, colors__name__in=colors) | Q(active=True, brand__in=brands)
                ).distinct()

    context = automobile_context(request)
    context['object_list'] = products
    context['selected_brands'] = brands
    context['selected_colors'] = colors
    template_name = "categories/automobile/list.html"

    return render(request, template_name, context)


def sports_equipment_filter(request):
    brands = request.GET.getlist('brands')
    sports = request.GET.getlist('sports')

    if len(brands) == 0 and len(sports) == 0:
        products = SportsEquipment.objects.filter(active=True)
    else:
        products = SportsEquipment.objects.filter(
            Q(active=True, brand__in=brands) | Q(active=True, related_sport__name__in=sports)
        ).distinct()

    context = sports_equipment_context(request)
    context['object_list'] = products
    context['selected_brands'] = brands
    context['selected_sports'] = sports
    template_name = "categories/sports-equipment/list.html"

    return render(request, template_name, context)


def genre_filter(request):
    genres = request.GET.getlist('genres')
    if len(genres) == 0:
        products = Book.objects.filter(active=True)
    else:
        products = Book.objects.filter(active=True, genre__name__in=genres).distinct()

    context = book_context(request)
    context['object_list'] = products
    context['selected_genres'] = genres
    template_name = "categories/book/list.html"

    return render(request, template_name, context)

