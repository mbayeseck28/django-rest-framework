from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
 
from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer
from rest_framework.permissions import IsAuthenticated

 
# class CategoryAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)


# get_queryset permet d'appliquer des filtres sur un endpoint
   

# class CategoryViewset(ModelViewSet):
class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

 
    def get_queryset(self):
        return Category.objects.filter(active=True)


class AdminCategoryViewset(ModelViewSet):
 
    serializer_class = CategorySerializer

    # Nous avons simplement à appliquer la permission sur le viewset
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()
    
    

# class ProductAPIView(APIView):
 
#     def get(self, *args, **kwargs):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
 
    def get_queryset(self):
        # Nous récupérons tous les produits dans une variable nommée queryset
        queryset = Product.objects.filter(active=True)
        # Vérifions la présence du paramètre ‘category_id’ dans l’url et si oui alors appliquons notre filtre
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
class ArticleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset