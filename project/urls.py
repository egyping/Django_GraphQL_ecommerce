from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    # Graphene GUI tool
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    # Catalog urls 
    # All Products 
    # All Products per category, paginated 
    # All Products per category, paginated, sorted by high price
    # All Products per category, paginated, sorted by low price
    # All Products per category, paginated, filtered to specific brand
    # All Products per brand, paginated 
    # All Products per brand, paginated, sorted by high price
    # All Products per brand, paginated, sorted by low price
    # All Products per brand, paginated, filtered to specific brand
    # All Both languages 
    # All categories > Done
    # Category per slug > Done
    # All Brands > Done
    # Brand per slug > Done

]
