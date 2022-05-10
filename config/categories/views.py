from rest_framework import serializers, permissions
from rest_framework import viewsets
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # verbose_name_plural = 'Categories'
        model = Category
        fields = ('id', 'name',)


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
