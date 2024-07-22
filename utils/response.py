from django.db import models
from django.forms.models import model_to_dict

from rest_framework import response


def success(message, data=None, meta=None):
    if isinstance(data, models.Model):
        data = model_to_dict(data, exclude=['file'])
    return response.Response({
        'message': message,
        'data': data,
        'meta': meta
    }, status=200)


def not_found(message, meta=None):
    return response.Response({
        'message': message,
        'meta': meta
    }, status=404)


def auth_required(message, meta=None):
    return response.Response({
        'message': message,
        'meta': meta
    }, status=401)


def bad_request(message, meta=None):
    return response.Response({
        'message': message
    }, status=400)


def error(message, status):
    return response.Response({
        'message': message,
    }, status=status)

