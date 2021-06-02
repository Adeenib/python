
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

    def book_validator(self, postdata):
        errors = {}
        if len(postdata['title']) < 2:
            errors['title'] = "Title should be at least 2 Chars."

        if len(postdata['desc']) < 2:
            errors['desc'] = "Descrption should be at least 2 Chars."
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    birthday = models.DateField()
    # favbook= favorit books for user
    # updated_books= book how updated by this uaer
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()


class Books(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    userfav = models.ManyToManyField(Users, related_name="favbook")
    updated_by = models.ForeignKey(
        Users, related_name="updated_books", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UsersManager()


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


def get_user(email):
    user = Users.objects.filter(email=email)
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


def all_books():
    allbook = Books.objects.all()
    return allbook


def create_book(data):
    errors = Users.objects.book_validator(data)
    return errors


def add_book(bookifo, userid):
    thisuser = Users.objects.get(id=userid)
    thisbook = Books.objects.create(
        title=bookifo['title'], desc=bookifo['desc'], updated_by=thisuser)

    return thisbook.id


def add_book_to_fav(bookid, userid):
    thisuser = Users.objects.get(id=userid)
    thisbook = Books.objects.get(id=bookid)
    thisbook.userfav.add(thisuser)


def thebook(id):
    thisbook = Books.objects.get(id=id)
    return thisbook


def update_book(id, userid, data):
    errors = Users.objects.book_validator(data)
    thisuser = Users.objects.get(id=userid)
    thisbook = Books.objects.create(
        title=data['title'], desc=data['desc'], updated_by=thisuser)

    thisbook = Books.objects.get(id=id)
    thisbook.title = data['title']
    thisbook.desc = data['desc']
    thisbook.save()


def delete_book(id):
    thisbook = Books.objects.delete(id=id)
    thisbook.delete()


def user_fav_this_book(id):
    thisbook = Books.objects.get(id=id)
    data = thisbook.userfav.all()
    print(data)
    return data


def un_fav(userid, id):
    thisbook = Books.objects.get(id=id)
    thisuser = Users.objects.get(id=userid)
    thisbook.userfav.remove(thisuser)


def favit(userid, id):
    thisbook = Books.objects.get(id=id)
    thisuser = Users.objects.get(id=userid)
    thisbook.userfav.add(thisuser)
