from django.urls import path

from tax.views.income_tax import (
    IncomeTaxPolicyListAPIView, IncomeTaxListAPIView, IncomeTaxPolicyViewset, IncomeTaxViewset
)
from tax.views.corporate_tax import (
    CorporateTaxPolicyListAPIView, CorporateTaxListAPIView, CorporateTaxPolicyViewset
)
from tax.views.vehicle_tax import (
    VehicleTaxPolicyListAPIView, VehicleTaxListAPIView, VehicleTaxPolicyViewset
)

urlpatterns = [
    path('income-tax/policy/list/', IncomeTaxPolicyListAPIView.as_view()),
    path('income-tax/policy/', IncomeTaxPolicyViewset.as_view({'post': 'create'})),
    path('income-tax/record/', IncomeTaxViewset.as_view({'post': 'generate'})),
    path('income-tax/record/list/', IncomeTaxListAPIView.as_view()),
    path('corporate-tax/policy/', CorporateTaxPolicyViewset.as_view({'post': 'create'})),
    path('corporate-tax/policy/list/', CorporateTaxPolicyListAPIView.as_view()),
    path('corporate-tax/record/list/', CorporateTaxListAPIView.as_view()),
    path('vehicle-tax/policy/', VehicleTaxPolicyViewset.as_view({'post': 'create'})),
    path('vehicle-tax/policy/list/', VehicleTaxPolicyListAPIView.as_view()),
    path('vehicle-tax/record/list/', VehicleTaxListAPIView.as_view()),
    path('fiscal-year/policy/', IncomeTaxPolicyViewset.as_view({'post': 'create'})),
]

