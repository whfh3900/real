# models.py
from django.db import models

class Transaction(models.Model):
    bas_ym = models.IntegerField()
    age_dc = models.CharField(max_length=10)
    gender = models.IntegerField()
    bas_dt = models.IntegerField()
    tran_md = models.CharField(max_length=45)
    ats_kdcd_dtl = models.CharField(max_length=45)
    dps_trn_am = models.IntegerField(blank=True, null=True)
    text_1 = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    user_info_uid = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='user_info_uid', related_name='transaction')
    result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transaction'
        unique_together = (('id', 'user_info_uid'),)


class UserInfo(models.Model):
    uid = models.CharField(primary_key=True, max_length=45)
    c0 = models.IntegerField()
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    c4 = models.IntegerField()
    c5 = models.IntegerField()
    c6 = models.IntegerField()
    c7 = models.IntegerField()
    c8 = models.IntegerField()
    c9 = models.IntegerField()
    c10 = models.IntegerField()
    c11 = models.IntegerField()
    c12 = models.IntegerField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_info'
