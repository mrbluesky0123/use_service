from django.db import models

class Transaction(models.Model):
    aprv_dy = models.CharField(max_length = 8)
    aprv_tm = models.CharField(max_length = 6)
    rep_aprv_no = models.CharField(max_length=9)
    slp_cd = models.CharField(max_length = 2)
    deal_amt = models.IntegerField()

    class Meta:
        app_label = 'point_use'
        db_table = 'APR_DEALTR_TRN'