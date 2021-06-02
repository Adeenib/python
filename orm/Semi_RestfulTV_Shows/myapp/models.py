from django.db import models


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releasedate = models.DateField()


def Addshow(new):
    thenew = Show.objects.create(
        title=new['title'], network=new['network'], releasedate=new['R_data'])
    id = thenew.id
    return(id)
