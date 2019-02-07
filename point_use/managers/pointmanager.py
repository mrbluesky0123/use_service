from django.db import models
from django.db.models import Q

class PointManager(models.Manager):
    
    def get_point(self, mbr_id):
        return self.filter(mbr_id=mbr_id).values_list('point_amt', flat=True)[0]

    def update_point(self, mbr_id, point):
        return self.filter(mbr_id=mbr_id).update(point_amt=point)