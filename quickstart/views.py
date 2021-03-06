# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from django.conf import settings
import json
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .utils import calculate_point
from tutorial.models import FormChoice, Student, Point
import base64
import cv2
from pyzbar.pyzbar import decode

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['POST', ])
@csrf_exempt
def upload_photo(request):
    # android
    if request.data.get('platform') == 'android':
        png_recovered = base64.decodestring(request.data['base64'])

        uniq_slug = str(request.data['uniq_slug'])
        example_slug = str(request.data['example_slug'])
        filename = '{}_{}.jpg'.format(uniq_slug, example_slug)
        path = 'media/{}'.format(filename)

        with open(path, 'wb+') as destination:
            destination.write(png_recovered)
            # can edit f
            data = decode(cv2.imread(path))
            user_slug = data[0].data

            form = FormChoice.objects.get(slug=example_slug)

            name = '{}_{}'.format(user_slug, example_slug)
            point = calculate_point(filename, name, json.loads(form.answers))

            s = Student.objects.get(slug=user_slug)
            f = FormChoice.objects.get(slug=example_slug)

            exist = Point.objects.filter(slug=name)
            if exist:
                exist = exist[0]
                exist.point=str(point)
                exist.save()
            else:
                Point.objects.create(slug=name, student=s, form=f, point=str(point))
            destination.close()
            return Response(status=200, data={
                'point': point,
                'user_id': s.slug,
                'name': u'{} {}'.format(s.firstname, s.lastname)
            })
    # ios
    uniq_slug = str(request.data['uniq_slug'])
    example_slug = str(request.data['example_slug'])
    filename = '{}_{}.jpg'.format(uniq_slug, example_slug)
    path = 'media/{}'.format(filename)

    with open(path, 'wb+') as destination:
        for chunk in request.FILES['file'].chunks():
            destination.write(chunk)

        data = decode(cv2.imread(path))
        user_slug = data[0].data

        form = FormChoice.objects.get(slug=example_slug)

        name = '{}_{}'.format(user_slug, example_slug)
        point = calculate_point(filename, name, json.loads(form.answers))
        s = Student.objects.get(slug=user_slug)
        f = FormChoice.objects.get(slug=example_slug)

        exist = Point.objects.filter(slug=name)
        if exist:
            exist = exist[0]
            exist.point=str(point)
            exist.save()
        else:
            Point.objects.create(slug=name, student=s, form=f, point=str(point))
        return Response(status=200, data={
            'point': point,
            'user_id': s.slug,
            'name': u'{} {}'.format(s.firstname, s.lastname)
        })
