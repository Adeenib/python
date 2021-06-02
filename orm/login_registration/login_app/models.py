
from django.contrib.messages.api import error
from django.core.checks import messages
from django.db import models
from django.http import request
from django.shortcuts import redirect
import re
from time import strftime, gmtime
from datetime import datetime
import bcrypt


class UsersManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        time = datetime.now()
        user70 = post_data['birthday']
        user71 = datetime.strptime(user70, '%Y-%m-%d')
        x = abs((time-user71).days)
        if x < 4745:
            errors["birthday"] = "you are  younger than allowed age "
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 Chars."

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 Chars."

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"

        if len(post_data['password']) < 8:
            errors['password'] = "password should be at least 8 Chars."

        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = "confirm pw should be at least 8 Chars and mach your Password"

        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UsersManager()


class Posts(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        Users, related_name='massege', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        Users, related_name='usercomment', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Posts, related_name='postcomment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_user(data):
    dbemeil = Users.objects.filter(email=data['email'])
    errors = Users.objects.basic_validator(data)
    if len(dbemeil) > 0:
        errors['dbemail'] = "this email was used!"

    if len(errors) == 0:

        pw = bcrypt.hashpw(data["password"].encode(),
                           bcrypt.gensalt()).decode()
        Users.objects.create(first_name=data['first_name'], last_name=data['last_name'],
                             email=data['email'], birthday=data['birthday'], password=pw,)

    return errors


def get_user(data):
    user = Users.objects.get(email=data)
    return user


def login_user(data):
    errors = {}
    userdata = get_user(data['email']).first().password
    print(userdata)
    if len(userdata) > 0:
        #pw = userdata[0]['password']

        print('#'*30)
        print(data['password'])
        if bcrypt.checkpw(
                data['password'].encode(), userdata.encode()):
            return errors
    errors['login'] = "user name or password not valide"
    return errors


def all_post():
    postdata = Posts.objects.all()
    return postdata


def this_post(id):
    postdata = Posts.objects.filter(id=id)
    return postdata


def all_postcomment(id):
    thispost = this_post(id)
    all_comment = thispost.postcomment.all()
    return all_comment


def add_post(data, email):
    print(data)

    print(email)
    thisuser = get_user(email)
    thispost = Posts.objects.create(message=data, user=thisuser)


def add_com(postdata, userdata):
    thisuser = get_user(userdata)
    thispost = Posts.objects.get(id=postdata['posid'])
    Comments.objects.create(
        comment=postdata['com'], user=thisuser, post=thispost)


def all_com_of_post():
    allcom = Comments.objects.all()
    return allcom


def delete_com(id):
    com = Comments.objects.get(id=id)
    com.delete()
