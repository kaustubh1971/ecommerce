from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class ProductFeaturedListView(ListView):
    template_name='products/list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset=Product.objects.all().featured()
    template_name='products/featured-detail.html'

    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    # queryset=Product.objects.all()
    template_name='products/list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context= super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(res):
    queryset = Product.objects.all()
    context={
        'object_list':queryset
    }
    return render(res,'products/list.html',context)

class ProductDetailSlugView(DetailView):
    queryset=Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self,*args,**kwargs):
        request= self.request
        slug=self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404('object does not exist')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            qs.first()
        except:
            raise Http404('huh ?????')
        return instance


class ProductDetailView(DetailView):
    # queryset=Product.objects.all()
    template_name='products/detail.html'

    # def get_context_data(self,*args,**kwargs):
    #     context= super(ProductDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_object(self,*args,**kwargs):
        request= self.request
        pk=self.kwargs.get('pk')
        instance= Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('object does not exist')
        return instance

    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk=self.kwargs.get('pk')
    #     return Product.objects.all()

def product_detail_view(res,pk):
    # =None ,*args,**kwargs):'
    # 1
    instance = Product.objects.get(pk=pk, featured=True)
    # 2
    # instance= get_object_or_404(Product, pk=pk)
    # 3
    # try:
    #     instance= Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('There is no product')
    #     raise Http404("Product does not exist")
    # except:
    #     print("Huh ??")
    # 4
    # qs=Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() ==1:
    #     instance=qs.first()
    # else:
    #     raise Http404('Object does not exists')
    # 5
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("object does not exist")
    context={
        'object':instance
    }
    return render(res,'products/detail.html',context)
