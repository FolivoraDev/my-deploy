from rest_framework import serializers

from members.serializer import UserSerializer
from .models import Restaurant, Tag, Category, Menu, Food, SubChoice, Review, Payment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class SubChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubChoice
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'image', 'name', 'price')


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = (
            'id', 'comment', 'rating', 'rating_delivery', 'rating_quantity', 'rating_taste', 'review_images', 'time',
            'user')


class MenuSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'food')


class RestaurantDetailSerializer(serializers.ModelSerializer):
    menu_set = MenuSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'menu_set',)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'name')


class RestaurantSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)
    payment_methods = PaymentSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = (
            'id', 'name', 'logo_url', 'review_avg', 'min_order_amount', 'review_count', 'owner_reply_count',
            'except_cash', 'payment_methods', 'discount_percent',
            'estimated_delivery_time', 'additional_discount_per_menu', 'tags', 'categories')
