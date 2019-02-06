from django.db import models
from django.db.models import Q

class MerchantManager(models.Manager):
    
    def get_merchant_status(self, mcht_no):
        return self.filter(mcht_no=mcht_no).values('mcht_sts', flat=True)[0]