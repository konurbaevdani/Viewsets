from rest_framework import serializers
from review.models import Review


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = '__all__'
