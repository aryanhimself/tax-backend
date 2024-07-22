from rest_framework import serializers

from tax.models import IncomeTaxPolicy, IncomeTaxRecord, CorporateTaxPolicy, CorporateTaxRecord, VehicleTaxPolicy, VehicleTaxRecord

class IncomeTaxPolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxPolicy
        fields = '__all__'

class IncomeTaxPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxPolicy
        fields = '__all__'
        depth = 1

class IncomeTaxRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxRecord
        fields = '__all__'

class IncomeTaxStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeTaxRecord
        fields = ['status']

class CorporateTaxPolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTaxPolicy
        fields = '__all__'

class CorporateTaxPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTaxPolicy
        fields = '__all__'
        depth = 1

class CorporateTaxRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTaxRecord
        fields = '__all__'

class CorporateTaxStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateTaxRecord
        fields = ['status']

class VehicleTaxPolicyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTaxPolicy
        fields = '__all__'

class VehicleTaxPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTaxPolicy
        fields = '__all__'
        depth = 1

class VehicleTaxRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTaxRecord
        fields = '__all__'

class VehicleTaxStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTaxRecord
        fields = ['status']

