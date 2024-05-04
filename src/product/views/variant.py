from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import UpdateView ,CreateView
from django.urls import reverse_lazy
from product.forms import VariantForm
from product.models import Variant


class BaseVariantView(generic.View):
    form_class = VariantForm
    model = Variant
    template_name = 'variants/create.html'
    success_url = '/product/variants'


class VariantView(BaseVariantView, ListView):
    template_name = 'variants/list.html'
    model = Variant
    paginate_by = 5
    context_object_name = 'variants'


    def get_queryset(self):
        queryset = Variant.objects.all()
        filter_string = {}
        # print(self.request.GET)
        # for key in self.request.GET:
        #     if self.request.GET.get(key):
        #         filter_string[key] = self.request.GET.get(key)
        # return Variant.objects.filter(**filter_string)

        for key, value in self.request.GET.items():
            if value:
                filter_string[key] = value
        
        queryset = queryset.filter(**filter_string)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = True
        context['request'] = self.request.GET.get('title__icontains', '')
        return context


class VariantCreateView(BaseVariantView, CreateView):
    template_name = 'variants/create.html'
    form_class = VariantForm
    success_url = reverse_lazy('variant-list')


class VariantEditView(BaseVariantView, UpdateView):
    template_name = 'variants/edit.html'
    form_class = VariantForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('variant-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = True
        context['request'] = self.request.GET.get('title__icontains', '')
        return context
