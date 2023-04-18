from django.db import models

option = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]

class School(models.Model):
    scholar_name = models.CharField()
    std_1 = models.BooleanField()
    std_2 = models.BooleanField()
    std_3 = models.BooleanField()
    std_4 = models.BooleanField()
    std_5 = models.BooleanField()
    std_6 = models.BooleanField()
    std_7 = models.BooleanField()
    std_8 = models.BooleanField()
    std_9 = models.BooleanField()
    std_10 = models.BooleanField()
    std_11 = models.BooleanField()
    std_12 = models.BooleanField()
    scl_open = models.BooleanField()
    scl_ews = models.BooleanField()
    scl_sebc = models.BooleanField()
    scl_sc_st = models.BooleanField()
    scl_open_pr = models.IntegerField(default=200)
    scl_ews_pr = models.IntegerField(default=200)
    scl_sebc_pr = models.IntegerField(default=200)
    scl_sc_st_pr = models.IntegerField(default=200)
    scl_f_income = models.IntegerField()
    scl_gender_male = models.BooleanField()
    scl_gender_female = models.BooleanField()
    scl_gender_other = models.BooleanField()
    scl_ask_for_pd = models.CharField(choices=option)
    scl_description = models.TextField()
