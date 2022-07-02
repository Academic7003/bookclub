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
    free = models.BooleanField(blank=True, null=True)
    barcode = models.PositiveBigIntegerField(blank=True, null=True)
    whose = models.TextField(max_length=255, blank=True, null=True)
    user = models.TextField(max_length=255, blank=True, null=True)




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
    free = models.BooleanField(blank=True, null=True)
    barcode = models.PositiveBigIntegerField(blank=True, null=True)
    whose = models.TextField(max_length=255, blank=True, null=True)
    user = models.TextField(max_length=255, blank=True, null=True)


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
    free = models.BooleanField(blank=True, null=True)
    barcode = models.PositiveBigIntegerField(blank=True, null=True)
    whose = models.TextField(max_length=255, blank=True, null=True)
    user = models.TextField(max_length=255, blank=True, null=True)
    

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
    tel=models.CharField(max_length=20, null=True, blank=True )
    adres=models.TextField(max_length=255, name="Manzil:")
    kitob = models.ForeignKey(UzbBooksModel, on_delete=models.CASCADE ,  null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True )



    def __str__(self):
        return str(f"{self.kitob}-{self.tel}-{self.created_time}")

class RusBuyModel(models.Model):
    tel=models.CharField(name="ваш номер телефон номер:", max_length=20, null=True, blank=True)
    adres=models.TextField(max_length=255, name="Адрес:")
    kitob = models.ForeignKey(RusBooksModel, on_delete=models.CASCADE ,  null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    


    def __str__(self):
       return str(f"{self.kitob}-{self.tel}-{self.created_time}")


class EngBuyModel(models.Model):
    tel=models.CharField(name="telephone number:", max_length=20, null=True, blank=True)
    adres=models.TextField(max_length=255, name="Address:")
    kitob = models.ForeignKey(EngBooksModel, on_delete=models.CASCADE , null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return str(f"{self.kitob}-{self.tel}-{self.created_time}")
