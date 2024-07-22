from datetime import datetime

from rest_framework import viewsets, generics

from users.models import User

from tax.models import IncomeTaxPolicy, IncomeTaxRecord
from tax.serializers import (
    IncomeTaxRecordSerializer,
    IncomeTaxStatusSerializer,
    IncomeTaxPolicySerializer,
    IncomeTaxPolicyCreateSerializer
    
)
from rest_framework.decorators import action
from tax.utils import calculate_income_tax
from utils import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
class IncomeTaxPolicyListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IncomeTaxPolicy.objects.all().order_by('-id')
    serializer_class = IncomeTaxPolicySerializer
    page_size_query_param = 'limit'


class IncomeTaxListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = IncomeTaxRecord.objects.all().order_by('-id')
    serializer_class = IncomeTaxRecordSerializer
    page_size_query_param = 'limit'


class IncomeTaxUserListAPIView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = IncomeTaxRecordSerializer
    page_size_query_param = 'limit'

    def get_queryset(self):
        return IncomeTaxRecord.objects.filter(
            user=self.kwargs['pk']
        ).order_by('-id')

class IncomeTaxPolicyViewset(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def create(self, request):
        serializer = IncomeTaxPolicyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('income tax policy created', serializer.data)
        return response.bad_request(serializer.errors)


class IncomeTaxViewset(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication]

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def generate(self, request):
        try:
            user = User.objects.get(pan=request.data['pan'])
        except User.DoesNotExist:
            return response.not_found('record not found') 
        year = datetime.now().year
        policy = IncomeTaxPolicy.objects.all()[1]
        amount = calculate_income_tax(policy.meta[user.maritial_status], user.annual_income)
        return response.success('', {'amount': amount})

    def retrieve(self, request, pk):
        try:
            record = IncomeTaxRecord.objects.get(pk=pk)
        except IncomeTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        return record

    def change_status(self, request, pk):
        try:
            record = IncomeTaxRecord.objects.get(pk=pk)
        except IncomeTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        serializer = IncomeTaxStatusSerializer(data=request.data, instance=record)
        if serializer.is_valid():
            serializer.save()
            return response.success('status changed')
        return response.bad_request(serializer.errors)

