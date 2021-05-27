from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse_lazy
from products.forms import BuynowForm
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Product
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from purchases.models import Purchase

class ProductDetailsView(generic.DetailView):
    model = Product
    user = get_user_model()
    template_name = 'products/product_page.html'
    
    def get_object(self):
        try:
            obj = Product.objects.get(pk=self.kwargs['uuid'])
        except:
            raise Http404('Product not found!')
        return obj

    def get_context_data(self, **kwargs):
        context = super(ProductDetailsView, self).get_context_data(**kwargs)
        obj = self.get_object()
        if 'buynow_form' not in context:
            context['buynow_form'] = BuynowForm(amount=obj.amount)
        return context

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if 'buynow' in request.POST:
            if self.request.user not in self.user.objects.all():
                raise Http404('To buy a product user need to be logged in!')
            buynow_form = BuynowForm(request.POST, amount=obj.amount)
            if buynow_form.is_valid():
                obj.amount -= int(buynow_form.clean_amount())
                if obj.amount == 0:
                    obj.publicly_listed = False
                obj.save()
                Purchase.objects.create(product=obj,
                                        buyer=self.request.user,
                                        amount=int(buynow_form.clean_amount()),
                                        price=obj.buy_now)
                return redirect('product-details', uuid=self.kwargs['uuid'])
        

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/products_list_page.html'

    def get_ordering(self):
        if self.request.GET.get('ordering'):
            ordering = str(self.request.GET['ordering'])
        else:
            ordering = '-creation_date'
        return ordering
    
    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.order_by(self.get_ordering())
        return queryset
