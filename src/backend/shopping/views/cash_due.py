from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from shopping.models import CashDue
from shopping.serializers.cash_due import CashDueCreateSerializer, CashDueUpdateSerializer, CashDueSerializer


class CashDueListView(ListAPIView):
    serializer_class = CashDueSerializer

    def get_queryset(self):
        show_paid = self.request.GET.get('paid')
        if show_paid:
            return CashDue.objects.filter(paid_back=True)
        return CashDue.objects.filter(paid_back=False)


class CashDueCreateView(CreateAPIView):
    serializer_class = CashDueCreateSerializer


class CashDueUpdateView(UpdateAPIView):
    serializer_class = CashDueUpdateSerializer
    queryset = CashDue.objects.all()
