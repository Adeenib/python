from time import time
from django.db import models
from time import strftime, gmtime
from datetime import datetime


class BlogManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        # past = datetime.strptime(string_input_with_date, "%d/%m/%Y")
        # present = datetime.now()
        time = datetime.now()
        usertime = data['Release_Date']
        print(usertime)
        user11 = datetime.strptime(usertime, '%Y-%m-%d')
        print('*'*30, type(user11))
        print(data)
        if len(data['Title']) < 2:
            errors["Title"] = "Blog Title should be at least 2 characters"
        if len(data['Network']) < 3:
            errors["Network"] = "Blog Network should be at least 3 characters"
        if len(data['Description']) < 10 or len(data['Description']) == 0:
            errors["Description"] = "Blog Description should be at least 10 characters"
        if user11 > time:
            errors["Release_Date"] = "Blog Release Date should be past"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=200)
    network = models.CharField(max_length=200)
    release = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


def readshows():
    all = Shows.objects.all()
    return all


def createshow(data):
    new_show_creste = Shows.objects.create(title=data['Title'], network=data['Network'],
                                           release=data['Release_Date'], description=data['Description'])
    return(new_show_creste)


def showthis(id):
    data = Shows.objects.get(id=id)
    return data


def delete(id):
    Shows.objects.get(id=id).delete()


def edit_this(data, id):
    editthis = Shows.objects.edit(id=id)


def updateshow(data):
    print(data)
    update_this = Shows.objects.get(id=data['id'])
    update_this.title = data['Title']
    update_this.network = data['Network']
    update_this.release = data['Release_Date']
    update_this.description = data['Description']
    update_this.save()
