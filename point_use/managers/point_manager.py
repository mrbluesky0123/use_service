from django.db import models
from django.db.models import Q

class PointManager(models.Manager):
    
    def get_point(self, mbr_id):
        return self.filter(mbr_id=mbr_id).values('point_amt', flat=True)[0]