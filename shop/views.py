from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product, Comment
from cart.forms import CartAddProductForm
from .forms import CommentForm


def product_list(request, category_slug=None):
    """
    Функция отображения списка продуктов

    Отвечает за отображение списка продуктов на странице
    Благодаря пагинации количество продуктов отображает в количестве 3
    штук на одной странице.
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop/product/list.html',
                  {'page': page,
                   'category': category,
                   'categories': categories,
                   'products': products})



def product_detail(request, id, slug):
    """
    Функция отображения информации о продукте

    Отвечает за детальное отображение информации о продукте
    а также за отображение комментариев о данном продукте.
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()


    # Список активных комментариев для этой статьи.
    comments = product.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
    # Пользователь отправил комментарий.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем комментарий, но пока не сохраняем в базе данных.
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье.
            new_comment.post = product
            # Сохраняем комментарий в базе данных.
            new_comment.save()
    else:
        comment_form = CommentForm()


    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form':cart_product_form,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form,
                                                        })
