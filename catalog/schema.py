import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Category, Brand, Product, ProductImages, ProductVariant

# List all categories
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "en_title", "ar_title", "en_description",
        "ar_description", "slug", "cat_image", "parent", )

class BrandType(DjangoObjectType):
    class Meta:
        model = Brand
        fields = ("id", "en_title", "ar_title", "en_description",
        "ar_description", "slug", "cat_image", "parent", )

class ProductImagesType(DjangoObjectType):
    class Meta:
        model = ProductImages
        fields = ("image",)

class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = (
            "size", "stock", "child_sku",
        )

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        #images = Product.objects.filter(product_images__image="image")
        fields = ("id", "en_title", "ar_title", "en_description",
        "ar_description", "slug", "thumb_img", "product_status", "sku", "category", "brand", "cost_price",
        "sale_price", "product_images", "product_variants",
        )


# Query all models 
class Query(graphene.ObjectType):
    # listing using graphene this require resolve_method
    all_Categories = graphene.List(CategoryType)
    category_by_slug = graphene.Field(CategoryType, slug=graphene.String())
    all_Brands = graphene.List(BrandType)
    brand_by_slug = graphene.Field(BrandType, slug=graphene.String())

    # another way using django list to list model ALSO it cloudl be extended by resolve_ (root, info)
    all_Products = DjangoListField(ProductType)

    def resolve_all_Categories(self, info):
        return Category.objects.all()
    def resolve_category_by_slug(self, info, slug):
        return Category.objects.get(slug=slug)
    
    def resolve_brand_by_slug(self, info, slug):
        return Brand.objects.get(slug=slug)
    def resolve_all_Brands(self, info):
        return Brand.objects.all()
















# Create Category 
class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)
    class Arguments:
        en_title = graphene.String()

    def mutate(self, info, en_title, ):
        category = Category(en_title=en_title)
        category.save()
        return CreateCategory(category=category)

# Create Category Mutation 
class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()