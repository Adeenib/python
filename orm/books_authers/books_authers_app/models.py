from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Authers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    note = models.TextField()
    books = models.ManyToManyField(Books, related_name="authers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def allbooks():
    theBooks = Books.objects.all()
    return theBooks


def allauthers():
    theAthurs = Authers.objects.all()
    return theAthurs


def createbook(data):
    Books.objects.create(title=data['title'], desc=data['desc'])


def createauther(data):
    Authers.objects.create(
        first_name=data['first_name'], last_name=data['last_name'])


def showauther(id):
    theauther = Authers.objects.get(id=id)
    return theauther


def showbook(id):
    theBook = Books.objects.get(id=id)
    return theBook


def bookauthers(id):
    theBook = showbook(id)
    authers = theBook.authers.all()
    return authers


def autherbooks(id):
    theAuther = showauther(id)
    Books = theAuther.books.all()
    return Books


def addbooktoauther(A_id, B_id):
    thisauther = showauther(A_id)
    thisbook = showbook(B_id)
    thisauther.books.add(thisbook)
