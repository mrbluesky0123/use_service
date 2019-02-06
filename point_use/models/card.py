from django.db import models

class Card(models.Model):
    crd_no = models.CharField(max_length = 16)
    mbr_id = models.CharField(max_length = 10)
    crd_sts = models.CharField(max_length = 20)     # normal, use_limited, ...
    crd_cd = models.CharField(max_length = 4)

    class Meta:
        app_label = 'point_use'
        db_table = 'CRD_MASTER_MST'