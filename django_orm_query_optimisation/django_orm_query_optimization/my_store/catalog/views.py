from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    items = Item.objects.all().select_related('category').prefeth_selected('tags')
    context = {
        'items': items,
    }
    return render(request, 'catalog/item_list.html', context)


# Самостоятельная работа
def item_detail(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    context = {
        'item': item,
    }
    return render(request, 'catalog/item_detail.html', context)