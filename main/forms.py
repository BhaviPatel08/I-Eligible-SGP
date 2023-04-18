from django import forms

class cl_choice(forms.Form):
    option = (
        ('scl', 'School'),
        ('clg', 'College')
    )
    select = forms.ChoiceField(choices=option, label='')

# ----------------------------------- School ----------------------------------- #

class cl_scl_scholar_name(forms.Form):
        scl_scholar_name = forms.CharField(label='', required=True)

class cl_scl_std(forms.Form):
    std_1 = forms.BooleanField(label='1', required=False)
    std_2 = forms.BooleanField(label='2', required=False)
    std_3 = forms.BooleanField(label='3', required=False)
    std_4 = forms.BooleanField(label='4', required=False)
    std_5 = forms.BooleanField(label='5', required=False)
    std_6 = forms.BooleanField(label='6', required=False)
    std_7 = forms.BooleanField(label='7', required=False)
    std_8 = forms.BooleanField(label='8', required=False)
    std_9 = forms.BooleanField(label='9', required=False)
    std_10 = forms.BooleanField(label='10', required=False)
    std_11 = forms.BooleanField(label='11', required=False)
    std_12 = forms.BooleanField(label='12', required=False)

class cl_scl_catagory(forms.Form):
    scl_open = forms.BooleanField(label='OPEN', required=False)
    scl_ews = forms.BooleanField(label='EWS', required=False)
    scl_sebc = forms.BooleanField(label='SEBC', required=False)
    scl_sc_st = forms.BooleanField(label='SC/ST', required=False)

class cl_scl_cat_wise_pr_open(forms.Form):
    scl_open_pr = forms.IntegerField(min_value=0, max_value=100, label='', step_size=0.01, required=False)

class cl_scl_cat_wise_pr_ews(forms.Form):
    scl_ews_pr = forms.IntegerField(min_value=0, max_value=100, label='', step_size=0.01, required=False)

class cl_scl_cat_wise_pr_sebc(forms.Form):
    scl_sebc_pr = forms.IntegerField(min_value=0, max_value=100, label='', step_size=0.01, required=False)

class cl_scl_cat_wise_pr_scst(forms.Form):
    scl_sc_st_pr = forms.IntegerField(min_value=0, max_value=100, label='', step_size=0.01, required=False)

class cl_scl_f_income(forms.Form):
    scl_f_income = forms.IntegerField(min_value=0, label="")

class cl_scl_gender(forms.Form):
    scl_gender_male = forms.BooleanField(label='Male', required=False)
    scl_gender_female = forms.BooleanField(label='Female', required=False)
    scl_gender_other = forms.BooleanField(label='Other', required=False)

class cl_scl_pd(forms.Form):

    option = [
        ('Yes', 'Yes'),
        ('No', 'No')
              ]

    scl_ask_for_pd = forms.CharField(label='', widget=forms.RadioSelect(choices=option))

class cl_scl_official_link(forms.Form):
    scl_official_link = forms.CharField(label='', max_length=300, required=False)

class cl_scl_desc(forms.Form):
    scl_description = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 6, 'cols': 51}))

class cl_scl_note(forms.Form):
    scl_note = forms.CharField(label='', required=False, max_length=700)

# ----------------------------------- School Over ----------------------------------- #


# ------------------------------------- College ------------------------------------- #

class cl_clg_scholar_name(forms.Form):
    clg_scholar_name = forms.CharField(label='', required=True)

class cl_clg_degree_bcom(forms.Form):
    clg_degree_bcom = forms.BooleanField(label='B.COM', required=False)

class cl_clg_degree_bba(forms.Form):
    clg_degree_bba = forms.BooleanField(label='BBA', required=False)

class cl_clg_degree_bca(forms.Form):
    clg_degree_bca = forms.BooleanField(label='BCA', required=False)

class cl_clg_degree_bsc(forms.Form):
    clg_degree_bsc = forms.BooleanField(label='BSC', required=False)

class cl_clg_degree_diploma(forms.Form):
    clg_degree_diploma = forms.BooleanField(label='Diploma', required=False)

class cl_clg_degree_btech(forms.Form):
    clg_degree_btech = forms.BooleanField(label='BE/B.TECH', required=False)

class cl_clg_degree_bpharma(forms.Form):
    clg_degree_bpharma = forms.BooleanField(label='B.PHARMA', required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_year_123(forms.Form):
    clg_year_1 = forms.BooleanField(label='1', required=False)
    clg_year_2 = forms.BooleanField(label='2', required=False)
    clg_year_3 = forms.BooleanField(label='3', required=False)

class cl_clg_year_4(forms.Form):
    clg_year_4 = forms.BooleanField(label='4', required=False)

class cl_clg_year_5(forms.Form):
    clg_year_5 = forms.BooleanField(label='5', required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_catagory(forms.Form):
    clg_cat_open = forms.BooleanField(label='OPEN', required=False)
    clg_cat_ews = forms.BooleanField(label='EWS', required=False)
    clg_cat_sebc = forms.BooleanField(label='SEBC', required=False)
    clg_cat_sc_st = forms.BooleanField(label='SC/ST', required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_for_fy_pr_open(forms.Form):
    clg_for_fy_pr_open = forms.IntegerField(label='', max_value=100, min_value=0, step_size=0.01, required=False)

class cl_clg_for_fy_pr_ews(forms.Form):
    clg_for_fy_pr_ews = forms.IntegerField(label='', max_value=100, min_value=0, step_size=0.01, required=False)

class cl_clg_for_fy_pr_sebc(forms.Form):
    clg_for_fy_pr_sebc = forms.IntegerField(label='', max_value=100, min_value=0, step_size=0.01, required=False)

class cl_clg_for_fy_pr_scst(forms.Form):
    clg_for_fy_pr_scst = forms.IntegerField(label='', max_value=100, min_value=0, step_size=0.01, required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_pre_year_cpi_open(forms.Form):
    clg_cgpa_open = forms.IntegerField(label='', min_value=0, max_value=10, step_size=0.01, required=False)

class cl_clg_pre_year_cpi_ews(forms.Form):
    clg_cgpa_ews = forms.IntegerField(label='', min_value=0, max_value=10, step_size=0.01, required=False)

class cl_clg_pre_year_cpi_sebc(forms.Form):
    clg_cgpa_sebc = forms.IntegerField(label='', min_value=0, max_value=10, step_size=0.01, required=False)

class cl_clg_pre_year_cpi_scst(forms.Form):
    clg_cgpa_scst = forms.IntegerField(label='', min_value=0, max_value=10, step_size=0.01, required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_f_income(forms.Form):
    clg_f_income = forms.IntegerField(label='', min_value=0)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_gender(forms.Form):
    clg_gender_male = forms.BooleanField(label='Male', required=False)
    clg_gender_female = forms.BooleanField(label='Female', required=False)
    clg_gender_other = forms.BooleanField(label='Other', required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_pd(forms.Form):

    option = [
        ('Yes', 'Yes'),
        ('No', 'No')
              ]

    clg_ask_for_pd = forms.CharField(label='', widget=forms.RadioSelect(choices=option))

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_official_link(forms.Form):
    clg_official_link = forms.CharField(label='', max_length=300, required=False)

# -------------------------------------------------------------------------------------------------------------------- #

class cl_clg_desc(forms.Form):
    clg_description = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 6, 'cols': 51}))

class cl_clg_note(forms.Form):
    clg_note = forms.CharField(label='', required=False, max_length=700)

# -------------------------------------------------------------------------------------------------------------------- #
