# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


import datetime

class User(models.Model):
    idUser = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=500)
    login = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    image = models.ImageField(upload_to='avatars',blank=True)

    def __str__(self):
        return self.name + " " + self.lastName

#se define funcion para actualizar datos de usuario
    def update(self, idUser, name, lastName,email,country,city,password):
        try:
            _user=User.objects.get(idUser=idUser)
            _user.name=name
            _user.lastName= lastName
            _user.email=email
            _user.country=country
            _user.city=city
            _user.password=password
            _user.save()
            return True
        except:
            return False




#photo = models.ImageField(upload_to='/images/')

class Categoria(models.Model):
    idCategoria = models.FloatField(primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Media(models.Model):
    MEDIA_TYPES_CHOICES = (
        ('Video', 'VIDEO'),
        ('Audio', 'AUDIO'),
    )
    idMedia = models.FloatField(primary_key=True)
    mediaType = models.CharField(max_length=10, choices=MEDIA_TYPES_CHOICES, default='Video')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=500)
    fec_create = models.DateField(default=datetime.date.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)




class Clip(models.Model):
    idClip = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    seg_initial = models.BigIntegerField()
    seg_final = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, default=1)

