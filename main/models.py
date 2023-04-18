from django.db import models


# Create your models here.

option = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

class School(models.Model):
    scl_pk = models.IntegerField(default=1)
    scholar_name = models.CharField(max_length=500)
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
    scl_open_pr = models.FloatField(default=200)
    scl_ews_pr = models.FloatField(default=200)
    scl_sebc_pr = models.FloatField(default=200)
    scl_sc_st_pr = models.FloatField(default=200)
    scl_f_income = models.IntegerField  ()
    scl_gender_male = models.BooleanField()
    scl_gender_female = models.BooleanField()
    scl_gender_other = models.BooleanField()
    scl_ask_for_pd = models.CharField(max_length=10, choices=option)
    scl_official_link = models.CharField(max_length=300, default='null')
    scl_description = models.TextField()
    scl_note = models.CharField(max_length=700, default='')

    def __str__(self):
        return self.scholar_name

class College(models.Model):
    clg_pk = models.IntegerField(default=1)
    scholar_name = models.CharField(max_length=200)
    clg_degree_bcom = models.BooleanField()
    clg_degree_bba = models.BooleanField()
    clg_degree_bca = models.BooleanField()
    clg_degree_bsc = models.BooleanField()
    clg_degree_diploma = models.BooleanField()
    clg_degree_btech = models.BooleanField()
    clg_degree_bpharma = models.BooleanField()
    clg_year_1 = models.BooleanField()
    clg_year_2 = models.BooleanField()
    clg_year_3 = models.BooleanField()
    clg_year_4 = models.BooleanField()
    clg_year_5 = models.BooleanField()
    clg_cat_open = models.BooleanField()
    clg_cat_ews = models.BooleanField()
    clg_cat_sebc = models.BooleanField()
    clg_cat_sc_st = models.BooleanField()
    clg_for_fy_pr_open = models.FloatField()
    clg_for_fy_pr_ews = models.FloatField()
    clg_for_fy_pr_sebc = models.FloatField()
    clg_for_fy_pr_sc_st = models.FloatField()
    clg_cgpa_open = models.FloatField()
    clg_cgpa_ews = models.FloatField()
    clg_cgpa_sebc = models.FloatField()
    clg_cgpa_sc_st = models.FloatField()
    clg_f_income = models.IntegerField()
    clg_gender_male = models.BooleanField()
    clg_gender_female = models.BooleanField()
    clg_gender_other = models.BooleanField()
    clg_ask_for_pd = models.CharField(max_length=10, choices=option)
    clg_official_link = models.CharField(max_length=300, default='null')
    clg_description = models.TextField()
    clg_note = models.CharField(max_length=700, default='')

    def __str__(self):
        return self.scholar_name
