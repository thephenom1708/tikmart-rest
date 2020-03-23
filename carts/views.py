from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.contenttypes.models import ContentType

from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

from addresses.forms import AddressForm
from addresses.models import Address

from billing.models import BillingProfile
from orders.models import Order
from products.models import Product, ProductInCart
from .models import Cart
from .models import FootwareInCart, ClothingInCart, AutomobileInCart, FurnitureInCart, SportsEquipmentInCart, \
    BookInCart, ElectronicInCart

from choices.models import FootwareCategory, FootwareSize, Color
from categories.models import Footware, Clothing, Automobile, Furniture, SportsEquipment, Book, Electronic
from .utils import get_footwear_cart_obj, product_in_cart_save, get_in_cart_obj, get_clothing_cart_obj, \
    get_automobile_cart_obj, get_furniture_cart_obj, get_sports_equipment_cart_obj, get_book_cart_obj


def get_cart_data(cart_obj):
    products = [{
        "id": x.product_object.id,
        # "url": x.product_object.get_absolute_url(),
        "title": x.product_object.title,
        "price": x.product_object.price,
        "quantity": x.quantity
    }
        for x in cart_obj.products.all()]
    cart_data = {"cart_id": cart_obj.id, "products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
    return cart_data


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    cart_data = get_cart_data(cart_obj)
    return render(request, "carts/home.html", cart_data)


def update_cart_quantity(request, cart_id, product_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')

        product = ProductInCart.objects.get(product_id=product_id)
        product.quantity = quantity
        product.save()
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
        products = cart_obj.products.all()
        total = 0
        for x in products:
            total += x.product_object.price * x.quantity
        if cart_obj.subtotal != total:
            cart_obj.subtotal = total
            cart_obj.save()

        return redirect('cart:home')


def delete_product_in_cart(request, cart_id, product_id):
    product = ProductInCart.objects.get(product_id=product_id)
    cart_obj = Cart.objects.get(id=cart_id)
    cart_obj.products.remove(product)

    product.delete()

    return redirect('cart:home')


def footwear_cart_update(request, product_id, cart_obj):
    model_type = 'footwareincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_footwear_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        footwear_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if footwear_obj is not None:
            first, second = product_obj.compare(footwear_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = footwear_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def clothing_cart_update(request, product_id, cart_obj):
    model_type = 'clothingincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_clothing_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        clothing_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if clothing_obj is not None:
            first, second = product_obj.compare(clothing_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = clothing_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def automobile_cart_update(request, product_id, cart_obj):
    model_type = 'automobileincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_automobile_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        automobile_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if automobile_obj is not None:
            first, second = product_obj.compare(automobile_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = automobile_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def furniture_cart_update(request, product_id, cart_obj):
    model_type = 'furnitureincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_furniture_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        furniture_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if furniture_obj is not None:
            first, second = product_obj.compare(furniture_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = furniture_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def sports_equipment_cart_update(request, product_id, cart_obj):
    model_type = 'sportsequipmentincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_sports_equipment_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        sports_equipment_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if sports_equipment_obj is not None:
            first, second = product_obj.compare(sports_equipment_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = sports_equipment_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def book_cart_update(request, product_id, cart_obj):
    model_type = 'bookincart'
    product_content_type = ContentType.objects.get(model=model_type)

    if product_id is not None:
        product_obj = get_book_cart_obj(request, product_id)

    already_present_in_cart = False
    for obj in cart_obj.products.all():
        book_obj = get_in_cart_obj(obj.product_id, obj.product_type)
        if book_obj is not None:
            first, second = product_obj.compare(book_obj)
            if len(first) == 0 and len(second) == 0:
                product_obj = book_obj
                already_present_in_cart = True
                break

    if not already_present_in_cart:
        product_obj.save()

    product_cart_obj_id_values = [pro['product_id'] for pro in cart_obj.products.values('product_id').all()]

    if product_obj.id in product_cart_obj_id_values:
        product_cart_obj = ProductInCart.objects.get(product_id=product_obj.id, product_type=product_content_type)
        cart_obj.products.remove(product_cart_obj)
        product_cart_obj.delete()
        added = False
    else:
        product_in_cart = product_in_cart_save(product_obj, model_type)
        cart_obj.products.add(product_in_cart)
        added = True
    return added


def cart_update(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    product_id = request.POST.get('product_id')
    product_type = request.POST.get('product_type')

    added = False
    if product_type == 'Footwear':
        added = footwear_cart_update(request, product_id, cart_obj)
    elif product_type == 'Clothing':
        added = clothing_cart_update(request, product_id, cart_obj)
    elif product_type == 'Automobile':
        added = automobile_cart_update(request, product_id, cart_obj)
    elif product_type == 'Furniture':
        added = furniture_cart_update(request, product_id, cart_obj)
    elif product_type == 'SportsEquipment':
        added = sports_equipment_cart_update(request, product_id, cart_obj)
    elif product_type == 'Book':
        added = book_cart_update(request, product_id, cart_obj)

    request.session['cart_items'] = cart_obj.products.count()
    if request.is_ajax():
        print("Ajax request")
        json_data = {
            "added": added,
            "removed": not added,
            "cartItemCount": cart_obj.products.count()
        }
        return JsonResponse(json_data, status=200)  # HttpResponse
        # return JsonResponse({"message": "Error 400"}, status=400) # Django Rest Framework
    return redirect("cart:home")


def set_payment_method(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method', 'cash')
        request.session['payment_method'] = payment_method
        return redirect("cart:checkout")
    else:
        return redirect("cart:checkout")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    cart_data = get_cart_data(cart_obj)

    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    payment_method = request.session.get("payment_method", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if payment_method:
            order_obj.payment_method = payment_method
            del request.session['payment_method']
        if billing_address_id or shipping_address_id or payment_method:
            order_obj.save()

    if request.method == "POST":
        "check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            # order_obj.mark_paid()
            request.session['cart_items'] = 0
            cart_obj.checkout = True
            cart_obj.save()
            request.session['order_obj_id'] = order_obj.id
            return redirect("cart:success")
    context = {
        "object": order_obj,
        "products": cart_data['products'],
        "subtotal": cart_obj.subtotal,
        "total": cart_obj.total,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
        "address_qs": address_qs,
    }
    return render(request, "carts/checkout.html", context)


def checkout_done_view(request):
    order_obj_id = request.session.get('order_obj_id', None)
    order_obj = Order.objects.get(id=order_obj_id)
    cart_data = get_cart_data(order_obj.cart)
    cart_data['object'] = order_obj
    return render(request, "orders/detail.html", cart_data)
