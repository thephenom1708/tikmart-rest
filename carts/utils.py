from carts.models import FootwearInCart, ClothingInCart, AutomobileInCart, FurnitureInCart, SportsEquipmentInCart, \
    BookInCart
from categories.models import Footware, Clothing, Automobile, Book, SportsEquipment, Furniture
from choices.models import FootwearSize, Color, ClothingSize, BookGenre
from products.models import Product, ProductInCart


def get_in_cart_obj(pk, model_type):
    in_cart_obj = None
    # if model == 'Footwear':
    #     in_cart_obj = FootwareInCart.objects.get(id=pk)
    # elif model == 'Clothing':
    #     in_cart_obj = ClothingInCart.objects.get(id=pk)
    in_cart_obj = model_type.model_class().objects.get(id=pk)
    return in_cart_obj


def product_in_cart_save(product_cart_obj, model_type):
    # content_type = ContentType.objects.get(model=model_type)
    product_in_cart = ProductInCart(
        product_object=product_cart_obj,
        # quantity=product_quantity
    )
    product_in_cart.save()
    return product_in_cart


def get_footwear_cart_obj(request, product_id):
    product = Product.objects.get(id=product_id)
    # p = product.content_type
    # c = p.model_class()
    product_size_id = request.POST.get('sizeSelect')
    product_color_id = request.POST.get('colorSelect')
    # product_quantity = request.POST.get('quantity')

    footwear_size = FootwearSize.objects.get(id=product_size_id)
    footwear_color = Color.objects.get(id=product_color_id)
    product_obj = Footware.objects.get(id=product_id)
    footwear_in_cart = FootwearInCart(
        title=product_obj.title,
        price=product_obj.price,
        brand=product_obj.brand,
        size=footwear_size,
        color=footwear_color,
        gender=product_obj.gender,
        type=product_obj.type
    )
    return footwear_in_cart


def get_clothing_cart_obj(request, product_id):
    product_size_id = request.POST.get('sizeSelect')
    product_color_id = request.POST.get('colorSelect')
    # product_quantity = request.POST.get('quantity')

    clothing_size = ClothingSize.objects.get(id=product_size_id)
    clothing_color = Color.objects.get(id=product_color_id)
    product_obj = Clothing.objects.get(id=product_id)
    clothing_in_cart = ClothingInCart(
        title=product_obj.title,
        price=product_obj.price,
        brand=product_obj.brand,
        size=clothing_size,
        color=clothing_color,
        gender=product_obj.gender,
        category=product_obj.category,
        type=product_obj.type,
        sleeve=product_obj.sleeve,
        occasion=product_obj.occasion
    )
    return clothing_in_cart


def get_automobile_cart_obj(request, product_id):
    product_color_id = request.POST.get('colorSelect')
    # product_quantity = request.POST.get('quantity')

    automobile_color = Color.objects.get(id=product_color_id)
    product_obj = Automobile.objects.get(id=product_id)
    automobile_in_cart = AutomobileInCart(
        title=product_obj.title,
        price=product_obj.price,
        brand=product_obj.brand,
        color=automobile_color,
        type=product_obj.type
    )
    return automobile_in_cart


def get_furniture_cart_obj(request, product_id):
    # product_quantity = request.POST.get('quantity')
    product_obj = Furniture.objects.get(id=product_id)
    furniture_in_cart = FurnitureInCart(
        title=product_obj.title,
        price=product_obj.price,
        brand=product_obj.brand,
        material=product_obj.material,
    )
    return furniture_in_cart


def get_sports_equipment_cart_obj(request, product_id):
    # product_quantity = request.POST.get('quantity')
    product_obj = SportsEquipment.objects.get(id=product_id)
    sports_equipment_in_cart = SportsEquipmentInCart(
        title=product_obj.title,
        price=product_obj.price,
        brand=product_obj.brand,
        related_sport=product_obj.related_sport,
        weight=product_obj.weight,
        material=product_obj.material
    )
    return sports_equipment_in_cart


def get_book_cart_obj(request, product_id):
    # product_quantity = request.POST.get('quantity')
    product_obj = Book.objects.get(id=product_id)
    book_in_cart = BookInCart(
        title=product_obj.title,
        price=product_obj.price,
        author=product_obj.author,
        language=product_obj.language,
        genre=product_obj.genre.set(BookGenre.objects.all()),
        publisher=product_obj.publisher,
        edition=product_obj.edition,
        no_of_pages=product_obj.no_of_pages
    )
    return book_in_cart
