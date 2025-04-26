from django.urls import path
from .views import StockListCreateView, OrderCreateView, PortfolioValueView, StockInvestmentView

urlpatterns = [
    path('stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    path('portfolio/value/', PortfolioValueView.as_view(), name='portfolio-value'),
    path('portfolio/stock/<int:pk>/', StockInvestmentView.as_view(), name='stock-investment'),
]
