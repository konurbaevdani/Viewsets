from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


from review.models import Review
from review.serializers import ReviewListSerializer, CreateReviewSerializer


class CreateReviewView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer


class UpdateReviewView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer


class DeleteReviewView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateReviewSerializer
