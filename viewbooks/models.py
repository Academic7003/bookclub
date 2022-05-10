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

class UzBuyModel(models.Model):
    tel=models.PositiveBigIntegerField(name="telefon raqam:")
    adres=models.TextField(max_length=255, name="Manzil:")
    Kitob = models.ForeignKey(UzbBooksModel, on_delete=models.CASCADE , name="Kitob nomi:")

    def __str__(self):
        return str(self.id)

class RusBuyModel(models.Model):
    tel=models.PositiveBigIntegerField(name="ваш номер телефон номер:")
    adres=models.TextField(max_length=255, name="Адрес:")
    Kitob = models.ForeignKey(RusBooksModel, on_delete=models.CASCADE , name="Называния книги:")

    def __str__(self):
        return str(self.id)

class EngBuyModel(models.Model):
    tel=models.PositiveBigIntegerField(name="telephone number:")
    adres=models.TextField(max_length=255, name="Address:")
    Kitob = models.ForeignKey(EngBooksModel, on_delete=models.CASCADE , name="The book name:")

    def __str__(self):
        return str(self.id)