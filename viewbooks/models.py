from django.db import models
from uuid import uuid4



    


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'books_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path

class UzbBooksModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    b_date = models.DateField(blank=True, null=True)
    free = models.NullBooleanField(null=True)



    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)



class RusBooksModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    b_date = models.DateField(blank=True, null=True)
    free = models.NullBooleanField(null=True)



    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class EngBooksModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    b_date = models.DateField(blank=True, null=True)
    free = models.NullBooleanField(null=True)

    
    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)

class BuyModel(models.Model):
    tel=models.PositiveBigIntegerField(name="telefon raqam:")
    adres=models.TextField(max_length=255, name="Manzil:")
    Kitob = models.ForeignKey(UzbBooksModel, on_delete=models.CASCADE , name="Kitob nomi:")

    def __str__(self):
        return str(self.id)