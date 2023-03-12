from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Wishlist, Like, Comment
from .forms import ProductForm, CommentForm, RatingForm
from django.http import HttpResponseRedirect


def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    liked = False

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            product.rating = rating
            product.save()
            return redirect('product_detail', product.id)
    else:
        form = RatingForm()

    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(user=request.user)
        comments = Comment.objects.filter(product=product)
        if product in like.products.all():
            liked = True
        comments_form = CommentForm()

        context = {
            'product': product,
            'liked': liked,
            'comments_form': comments_form,
            'comments': comments,
            'form': form,
        }
    else:
        context = {
            'product': product,
        }
    return render(request, 'products/product_detail.html', context)


@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            product.rating = form.cleaned_data['rating']
            product.save()
            return redirect('product_detail', product.id)
    else:
        form = RatingForm()

    return render(request, 'products/product_detail.html', {'product': product, 'form': form})


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_product_to_wishlist(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    if product not in wishlist.products.all():
        wishlist.products.add(product)
    else:
        wishlist.products.remove(product)
    wishlist.save()

    wishlist_items = []
    if request.user.is_authenticated:
        user_wishlist = Wishlist.objects.filter(user=request.user).first()
        if user_wishlist:
            wishlist_items = user_wishlist.products.all()

    context = {
        'product': product,
        'wishlist_items': wishlist.products.all(),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def like_product(request, product_id):
    """ A view to show like or unlike individual products """
    product = get_object_or_404(Product, pk=product_id)
    like, created = Like.objects.get_or_create(user=request.user)
    liked = False
    if product not in like.products.all():
        like.products.add(product)
        liked = True
    else:
        like.products.remove(product)
    like.save()

    context = {
        'like': like,
        'liked': liked,
        'product': product,
        'like_count': product.like_set.count(),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            messages.success(request, 'Your comment has been added successfully!')

            return HttpResponseRedirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_comment(request, product_id):
    comment = get_object_or_404(Comment, pk=product_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You are not authorized to perform this action.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated successfully!')
            return HttpResponseRedirect(reverse('product_detail', args=[comment.product.id]))
    else:
        form = CommentForm(instance=comment)

    return render(request, 'products/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        return HttpResponseRedirect(reverse('home'))

    product_id = comment.product.id
    comment.delete()
    messages.success(request, 'Your comment has been deleted successfully!')

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
