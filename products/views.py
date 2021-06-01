from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from products.forms import BuynowForm
from django.shortcuts import redirect, render, resolve_url
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from .models import Product
from .forms import CommentCreateForm, ProductUpdateForm
import uuid
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from profiles.models import User
from purchases.models import Purchase, Cart
from comments.models import Comment

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
        if 'comment_form' not in context:
            context['comment_form'] = CommentCreateForm()
        context['owner'] = False   
        if obj.seller == self.request.user:
            context['owner'] = True
        context['comments'] = self.get_object().comments.all()
        return context

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if 'buynow' in request.POST:
            if self.request.user not in self.user.objects.all():
                raise Http404('To buy a product user need to be logged in!')
            buynow_form = BuynowForm(request.POST, amount=obj.amount)
            if buynow_form.is_valid():
                purchase = Purchase.objects.create(product=obj,
                                        buyer=self.request.user,
                                        amount=int(buynow_form.clean_amount()),
                                        price=obj.price)
                return HttpResponseRedirect(reverse('new-purchase-shipping', kwargs={'uuid': purchase.pk, 'product_uuid': self.kwargs['uuid']})) 

        if 'addtocart' in request.POST:
            if self.request.user not in self.user.objects.all():
                raise Http404('To add product to cart you need to be logged in!')
            buynow_form = BuynowForm(request.POST, amount=obj.amount)
            if buynow_form.is_valid():
                Cart.objects.create(product=obj,
                                    user=self.request.user,
                                    amount=int(buynow_form.clean_amount()),
                                    price=obj.price)
                return redirect('product-details', uuid=self.kwargs['uuid'])

        if 'addcomment' in request.POST:
            if self.request.user not in self.user.objects.all():
                raise Http404('To add comment you need to be logged in!')
            comment_form = CommentCreateForm(request.POST)
            if comment_form.is_valid():
                self.get_object().comments.create(creator=self.request.user,
                                                  content=comment_form.cleaned_data.get("content"))
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


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = ProductUpdateForm
    template_name = 'products/product_edit_page.html'

    def get_object(self):
        obj = get_object_or_404(Product, pk=self.kwargs['uuid'])
        if self.request.user == obj.seller:
            return obj
        else:
            raise Http404('You are not seller of the product!')
    
    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        obj = self.get_object()
        context['product'] = obj
        return context

    def get_success_url(self):
        return self.get_object().get_absolute_url()