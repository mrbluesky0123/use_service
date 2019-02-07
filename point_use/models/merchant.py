from django.db import models
from point_use.managers.merchantmanager import MerchantManager

class Merchant(models.Model):
    mcht_no = models.CharField(max_length = 9)
    mcht_sts = models.CharField(max_length = 20)    # normal, use_limited, ...

    objects = MerchantManager()

    def __str__(self):
        return '%s, %s' % (self.mcht_no, self.mcht_sts)

    class Meta:
        app_label = 'point_use'
        db_table = 'MCT_MASTER_MST'