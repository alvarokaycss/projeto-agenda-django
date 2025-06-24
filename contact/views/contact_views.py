# flake8: noqa
# type: ignore

from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q # Esse Q é para usar o OR em filtros BD


def index(request):
    contacts = Contact.objects \
    .all() \
    .filter(show=True)\
    .order_by("-id")
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - ',
    }               

    return render(
        request,
        'contact/index.html', context
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    # Caso esteja vendo isso para relemebrar o que acontece por trás:
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # if single_contact is None:
    #     raise Http404()

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    
    return render(
        request,
        'contact/contact.html', context
    )

def search(request):
    search_value = request.GET.get("q", "").strip()
    
    if search_value == '':
        redirect("contact:index")
    
    # Realiza buscas
    contacts = Contact.objects \
    .all() \
    .filter(show=True)\
    .filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value)
        )\
    .order_by("-id") \
    # Buscar sem o Q vai utilizar o operador AND invés de OR.
    # OR é representado por "|" entre os "Q".
    # __icontains é insensitive contains, ou seja, 
    # contêm algo independente de maiúsculo/Minúsculo.
    # Tá na doc. do Django.    
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Buscar - ',
        'search_value': search_value,
    }               

    return render(
        request,
        'contact/index.html', context
    )
