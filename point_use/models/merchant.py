from django.db import models


class Merchant(models.Model):
    mcht_no = models.CharField(max_length = 9)
    mcht_sts = models.CharField(max_length = 20)    # normal, use_limited, ...

    class Meta:
        app_label = 'point_use'
        db_table = 'MCT_MASTER_MST'