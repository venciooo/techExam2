from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, F
from .models import Stock, Order
from .serializers import StockSerializer, OrderSerializer

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PortfolioValueView(APIView):
    def get(self, request):
        total_value = Order.objects.aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0
        return Response({'total_portfolio_value': total_value})

class StockInvestmentView(APIView):
    def get(self, request, pk):
        investment = Order.objects.filter(stock_id=pk).aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0
        return Response({'stock_id': pk, 'total_invested': investment})
