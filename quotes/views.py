from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse
from .models import Quote
from .serializer import QuoteSerializer
from .ml import predict_mood
import random

class QuoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Manage Quote database"""
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(name='text', type=str, location=OpenApiParameter.QUERY, description='Text input for mood prediction'),
            OpenApiParameter(name='mood', type=str, location=OpenApiParameter.QUERY, description='Mood for filtering quotes'),
            OpenApiParameter(name='category', type=str, location=OpenApiParameter.QUERY, description='Category for filtering quotes')
        ],
        responses={200: QuoteSerializer, 400: OpenApiResponse(description='Error response')}
    )
    @action(detail=False, methods=['get'], url_path='filter-quote')
    def filter_quote(self, request, *args, **kwargs):
        """Filter and retrieve a single quote based on mood and category"""
        text_input = request.GET.get('text')
        category = request.GET.get('category')
        if text_input:
            mood = predict_mood(text_input)
        else:
            mood = request.GET.get('mood')
        quotes = self.queryset

        if mood == 'neutral':
            quotes = Quote.objects.all()

        elif mood:
            q1 = quotes.filter(mood=mood)
            if q1.exists():
                quotes = q1
            if category:
                q2 = quotes.filter(category=category)
                if q2.exists():
                    quotes = q2

    
        if quotes.exists():
            quote = random.choice(list(quotes))
            response_data = {
                'text': quote.text,
                'author': quote.author,
                'mood': quote.mood,
                'category': quote.category,
            }
            return Response(response_data)
        else:
            rand = Quote.objects.all()
            quote = random.choice(list(rand))
            response_data = {
                'text': quote.text,
                'author': quote.author,
                'mood': quote.mood,
                'category': quote.category,
            }
            return Response(response_data)
