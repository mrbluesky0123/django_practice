from django.db import models

# Create your models here.
class Member(models.Model):
    mbr_id = models.CharField(max_length = 9)
    name = models.CharField(max_length = 15)
    mdn = models.CharField(max_length = 11)
    birth = models.CharField(max_length = 8)
    crdNo = models.CharField(max_length = 16)
    last_sales_day = models.DateField('last sales')

    def __str__(self):
        return self.mbr_id + ', ' + self.name + ', ' + self.mdn

class Point(models.Model):
    mbr_id = models.CharField(max_length = 9)
    point_kind = models.CharField(max_length = 3)
    point_amt = models.IntegerField(default = 0)
    upd_dt = models.DateField('update date')

    def __str__(self):
        return self.mbr_id + ', ' + self.point_kind + ', ' + str(self.point_amt)

