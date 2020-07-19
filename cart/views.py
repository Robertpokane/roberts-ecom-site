from django.shortcuts import render, redirect, reverse
# Create your views here.

def view_cart(request):
    """A view that renders the cart contets page"""
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """add a quanty of the specified product to vthe cart """
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    
    """The if statment bellow changes the behaviour of the cart from replacing the total in the basket with the new total selected, to adding to the total"""
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
        
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
def adjust_cart(request,id):
    """adjust a quanty of the specified product ny the specified amount """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
     
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
            
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    