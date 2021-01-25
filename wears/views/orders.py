from django.shortcuts import render, redirect
from django.views import View
from wears.models.orders import Order
from wears.middlewares.auth import auth_middleware


class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders': orders})
