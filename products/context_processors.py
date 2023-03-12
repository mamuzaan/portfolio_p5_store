from .models import Wishlist


def wishlist_context_processor(request):
    wishlist_items = []
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).first()
        if user_wishlist:
            wishlist_items = user_wishlist.products.all()
    return {
        'wishlist_items': wishlist_items,
    }
