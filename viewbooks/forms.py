from django.forms import ModelForm
from viewbooks.models import *


class UzBuyerForm(ModelForm):

    class Meta:
        model = UzBuyModel
        exclude = ["kitob"]

class RusBuyerForm(ModelForm):

    class Meta:
        model = RusBuyModel
        exclude = ["kitob"]
        


class EngBuyerForm(ModelForm):

    class Meta:
        model = EngBuyModel
        exclude = ["kitob"]
        
