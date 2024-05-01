from django.views import generic
from django.views.generic import ListView
from product.models import Variant, Product
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView ,CreateView
from product.forms import ProductForm 




class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.all()
        filter_string = {}
        
        for key, value in self.request.GET.items():
            if value:
                filter_string[key] = value
        
        queryset = queryset.filter(**filter_string)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['dashboard'] = True
        context['product'] = True
        context['request'] = self.request.GET.get('title__icontains', '')
        return context



# class CreateProductView(generic.TemplateView):
#     template_name = 'products/create.html'

#     def get_context_data(self, **kwargs):
#         context = super(CreateProductView, self).get_context_data(**kwargs)
#         variants = Variant.objects.filter(active=True).values('id', 'title')
#         context['product'] = True
#         context['variants'] = list(variants.all())
#         return context


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = True
        context['variants'] = Variant.objects.filter(active=True).values('id', 'title')
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
        # Provide variant options for the form
        context['variants'] = Variant.objects.filter(active=True).values('id', 'title')
        return context