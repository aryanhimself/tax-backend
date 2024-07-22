from datetime import datetime

from rest_framework import viewsets, generics

from tax.models import VehicleTaxPolicy, VehicleTaxRecord
from tax.serializers import (
    VehicleTaxRecordSerializer,
    VehicleTaxStatusSerializer,
    VehicleTaxPolicySerializer,
    VehicleTaxPolicyCreateSerializer
)
from utils import response


class VehicleTaxPolicyListAPIView(generics.ListAPIView):
    queryset = VehicleTaxPolicy.objects.all()
    serializer_class = VehicleTaxPolicySerializer
    page_size_query_param = 'limit'


class VehicleTaxListAPIView(generics.ListAPIView):
    queryset = VehicleTaxRecord.objects.all()
    serializer_class = VehicleTaxRecordSerializer
    page_size_query_param = 'limit'


class VehicleTaxUserListAPIView(generics.ListAPIView):
    serializer_class = VehicleTaxRecordSerializer
    page_size_query_param = 'limit'

    def get_queryset(self):
        return VehicleTaxRecord.objects.filter(
            user=self.kwargs['pk']
        ).order_by('-id')


class VehicleTaxPolicyViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = VehicleTaxPolicyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.success('vehicle tax policy created', serializer.data)
        return response.bad_request(serializer.errors)


class VehicleTaxViewset(viewsets.ViewSet):
    def generate_record(self, request, pk):
        record = VehicleTaxRecord()
        record.save()
        return record

    def retrieve(self, request, pk):
        try:
            record = VehicleTaxRecord.objects.get(pk=pk)
        except VehicleTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        return record

    def change_status(self, request, pk):
        try:
            record = VehicleTaxRecord.objects.get(pk=pk)
        except VehicleTaxRecord.DoesNotExist:
            return response.not_found('record not found')
        serializer = VehicleTaxStatusSerializer(data=request.data, instance=record)
        if serializer.is_valid():
            serializer.save()
            return response.success('status changed')

        return response.bad_request(serializer.errors)



