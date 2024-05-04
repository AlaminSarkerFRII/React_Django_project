from django.views import generic
from django.views.generic import ListView
from product.models import Variant, Product
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView ,CreateView,FormView
from product.forms import ProductForm 
from django.core.paginator import Paginator
from django.http import JsonResponse


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.all().order_by('title')
        filter_string = {}
       
        
        for key, value in self.request.GET.items():
            if value:
                filter_string[key] = value
        
        queryset = queryset.filter(**filter_string)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['request'] = self.request.GET.get('title__icontains', '')
        context['variant_options'] = Variant.objects.filter(active=True).values('id', 'title')
        return context



class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variants'] = list(Variant.objects.filter(active=True).values('id', 'title'))
        products_queryset = Product.objects.all().values()
        for product in products_queryset:
            product['created_at'] = product['created_at'].isoformat()
            product['updated_at'] = product['updated_at'].isoformat()

        context['products'] = list(products_queryset)
        
        return context




class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit.html' 
    success_url = reverse_lazy('list')
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['variants'] = Variant.objects.filter(active=True).values('id', 'title')
        return context