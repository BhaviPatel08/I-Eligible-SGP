from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import School, College
from .forms import cl_scl_scholar_name,\
    cl_clg_f_income,\
    cl_choice,\
    cl_scl_std,\
    cl_scl_catagory,\
    cl_scl_f_income,\
    cl_scl_cat_wise_pr_open,\
    cl_scl_cat_wise_pr_ews,\
    cl_scl_cat_wise_pr_sebc,\
    cl_scl_cat_wise_pr_scst,\
    cl_scl_gender,\
    cl_scl_pd,\
    cl_scl_official_link,\
    cl_scl_desc,\
    cl_scl_note,\
    cl_clg_scholar_name,\
    cl_clg_degree_bcom,\
    cl_clg_degree_bba,\
    cl_clg_degree_bca,\
    cl_clg_degree_bsc,\
    cl_clg_degree_diploma,\
    cl_clg_degree_btech,\
    cl_clg_degree_bpharma,\
    cl_clg_year_123,\
    cl_clg_year_4,\
    cl_clg_year_5,\
    cl_clg_catagory,\
    cl_clg_for_fy_pr_open,\
    cl_clg_for_fy_pr_ews,\
    cl_clg_for_fy_pr_sebc,\
    cl_clg_for_fy_pr_scst,\
    cl_clg_pre_year_cpi_open,\
    cl_clg_pre_year_cpi_ews,\
    cl_clg_pre_year_cpi_sebc,\
    cl_clg_pre_year_cpi_scst,\
    cl_clg_gender,\
    cl_clg_pd,\
    cl_clg_official_link,\
    cl_clg_desc,\
    cl_clg_note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')

def home(request):
    return render(request, 'home_page.html')

def addNewAdminPanel(request):
    obj_clg_income = cl_clg_f_income()
    obj_select = cl_choice()

#   --------> School Objects
    obj_scl_scholar_name = cl_scl_scholar_name()
    obj_scl_std = cl_scl_std()
    obj_scl_catagory = cl_scl_catagory()
    obj_scl_f_income = cl_scl_f_income()
    obj_scl_cat_wise_pr_open = cl_scl_cat_wise_pr_open()
    obj_scl_cat_wise_pr_ews = cl_scl_cat_wise_pr_ews()
    obj_scl_cat_wise_pr_sebc = cl_scl_cat_wise_pr_sebc()
    obj_scl_cat_wise_pr_scst = cl_scl_cat_wise_pr_scst()
    obj_scl_gender = cl_scl_gender()
    obj_scl_pd = cl_scl_pd()
    obj_scl_official_link = cl_scl_official_link()
    obj_scl_desc = cl_scl_desc()
    obj_scl_note = cl_scl_note()

#   --------> College Objects
    obj_clg_scholar_name = cl_clg_scholar_name()
    obj_clg_degree_bcom = cl_clg_degree_bcom()
    obj_clg_degree_bba = cl_clg_degree_bba()
    obj_clg_degree_bca = cl_clg_degree_bca()
    obj_clg_degree_bsc = cl_clg_degree_bsc()
    obj_clg_degree_diploma = cl_clg_degree_diploma()
    obj_clg_degree_btech = cl_clg_degree_btech()
    obj_clg_degree_bpharma = cl_clg_degree_bpharma()
    obj_clg_year_123 = cl_clg_year_123()
    obj_clg_year_4 = cl_clg_year_4()
    obj_clg_year_5 = cl_clg_year_5()
    obj_clg_catagory = cl_clg_catagory()
    obj_clg_for_fy_pr_open = cl_clg_for_fy_pr_open()
    obj_clg_for_fy_pr_ews = cl_clg_for_fy_pr_ews()
    obj_clg_for_fy_pr_sebc = cl_clg_for_fy_pr_sebc()
    obj_clg_for_fy_pr_scst = cl_clg_for_fy_pr_scst()
    obj_clg_pre_year_cpi_open = cl_clg_pre_year_cpi_open()
    obj_clg_pre_year_cpi_ews = cl_clg_pre_year_cpi_ews()
    obj_clg_pre_year_cpi_sebc = cl_clg_pre_year_cpi_sebc()
    obj_clg_pre_year_cpi_scst = cl_clg_pre_year_cpi_scst()
    obj_clg_gender = cl_clg_gender()
    obj_clg_ask_for_pd = cl_clg_pd()
    obj_clg_official_link = cl_clg_official_link()
    obj_clg_desc = cl_clg_desc()
    obj_clg_note = cl_clg_note()

    parameters = {
                    'Choices': obj_select,
                    'School_Scholarship_name': obj_scl_scholar_name,
                    'School_Standard': obj_scl_std,
                    'Family_Annual_Income': obj_clg_income,
                    'School_catagory': obj_scl_catagory,
                    'School_Family_Annual_Income': obj_scl_f_income,
                    'School_Catagory_wise_pr_open': obj_scl_cat_wise_pr_open,
                    'School_Catagory_wise_pr_ews': obj_scl_cat_wise_pr_ews,
                    'School_Catagory_wise_pr_sebc': obj_scl_cat_wise_pr_sebc,
                    'School_Catagory_wise_pr_scst': obj_scl_cat_wise_pr_scst,
                    'School_Gender': obj_scl_gender,
                    'School_ask_for_pd_required': obj_scl_pd,
                    'School_official_link': obj_scl_official_link,
                    'School_scholarship_description': obj_scl_desc,
                    'School_note': obj_scl_note,

                    'College_Scholarship_name': obj_clg_scholar_name,
                    'College_degree_bcom': obj_clg_degree_bcom,
                    'College_degree_bba': obj_clg_degree_bba,
                    'College_degree_bca': obj_clg_degree_bca,
                    'College_degree_bsc': obj_clg_degree_bsc,
                    'College_degree_diploma': obj_clg_degree_diploma,
                    'College_degree_btech': obj_clg_degree_btech,
                    'College_degree_bpharma': obj_clg_degree_bpharma,
                    'College_year_123': obj_clg_year_123,
                    'College_year_4': obj_clg_year_4,
                    'College_year_5': obj_clg_year_5,
                    'College_catagory': obj_clg_catagory,
                    'College_for_1st_year_12th_pr_open': obj_clg_for_fy_pr_open,
                    'College_for_1st_year_12th_pr_ews': obj_clg_for_fy_pr_ews,
                    'College_for_1st_year_12th_pr_sebc': obj_clg_for_fy_pr_sebc,
                    'College_for_1st_year_12th_pr_scst': obj_clg_for_fy_pr_scst,
                    'College_previous_year_cpi_open': obj_clg_pre_year_cpi_open,
                    'College_previous_year_cpi_ews': obj_clg_pre_year_cpi_ews,
                    'College_previous_year_cpi_sebc': obj_clg_pre_year_cpi_sebc,
                    'College_previous_year_cpi_scst': obj_clg_pre_year_cpi_scst,
                    'College_Gender': obj_clg_gender,
                    'College_ask_for_pd': obj_clg_ask_for_pd,
                    'College_official_link': obj_clg_official_link,
                    'College_scholarship_description': obj_clg_desc,
                    'College_note': obj_clg_note
                  }
    if request.method == 'POST':

        if request.POST.get('name-for-school'):
            aid = 0
            obj_school = School.objects.all()
            flag = 0

            while flag == 0:
                iflag = 0
                for i in obj_school:
                    if i.scl_pk == aid:
                        iflag = 1
                        break
                if iflag == 1:
                    aid += 1
                else:
                    flag = 1

            var_scl_pk = aid

            var_scholar_name = request.POST.get('scl_scholar_name')
            var_std = [request.POST.get('std_1'),
                       request.POST.get('std_2'),
                       request.POST.get('std_3'),
                       request.POST.get('std_4'),
                       request.POST.get('std_5'),
                       request.POST.get('std_6'),
                       request.POST.get('std_7'),
                       request.POST.get('std_8'),
                       request.POST.get('std_9'),
                       request.POST.get('std_10'),
                       request.POST.get('std_11'),
                       request.POST.get('std_12')
                       ]

            for i in range(0, len(var_std)):
                if (var_std[i] == 'on'):
                    var_std[i] = True
                else:
                    var_std[i] = False

            var_scl_catagory = [request.POST.get('scl_open'),
                                request.POST.get('scl_ews'),
                                request.POST.get('scl_sebc'),
                                request.POST.get('scl_sc_st')
                                ]

            for i in range(0, len(var_scl_catagory)):
                if var_scl_catagory[i] == 'on':
                    var_scl_catagory[i] = True
                else:
                    var_scl_catagory[i] = False

            var_scl_open_pr = request.POST.get('scl_open_pr')
            var_scl_ews_pr = request.POST.get('scl_ews_pr')
            var_scl_sebc_pr = request.POST.get('scl_sebc_pr')
            var_scl_sc_st_pr = request.POST.get('scl_sc_st_pr')

            if var_scl_open_pr == '':
                var_scl_open_pr = 200;

            if var_scl_ews_pr == '':
                var_scl_ews_pr = 200;

            if var_scl_sebc_pr == '':
                var_scl_sebc_pr = 200

            if var_scl_sc_st_pr == '':
                var_scl_sc_st_pr = 200

            var_scl_f_income = request.POST.get('scl_f_income')

            var_scl_gender = [request.POST.get('scl_gender_male'),
                              request.POST.get('scl_gender_female'),
                              request.POST.get('scl_gender_other')
                              ]

            for i in range(0, len(var_scl_gender)):
                if var_scl_gender[i] == 'on':
                    var_scl_gender[i] = True
                else:
                    var_scl_gender[i] = False

            var_scl_ask_for_pd = request.POST.get('scl_ask_for_pd')
            var_scl_official_link = request.POST.get('scl_official_link')
            if var_scl_official_link == '':
                var_scl_official_link = 'null'
            var_scl_description = request.POST.get('scl_description')

            var_scl_note = request.POST.get('scl_note')

            obj_scl_save_data = School(scl_pk=var_scl_pk,
                                       scholar_name=var_scholar_name,
                                       std_1=var_std[0],
                                       std_2=var_std[1],
                                       std_3=var_std[2],
                                       std_4=var_std[3],
                                       std_5=var_std[4],
                                       std_6=var_std[5],
                                       std_7=var_std[6],
                                       std_8=var_std[7],
                                       std_9=var_std[8],
                                       std_10=var_std[9],
                                       std_11=var_std[10],
                                       std_12=var_std[11],
                                       scl_open=var_scl_catagory[0],
                                       scl_ews=var_scl_catagory[1],
                                       scl_sebc=var_scl_catagory[2],
                                       scl_sc_st=var_scl_catagory[3],
                                       scl_open_pr=var_scl_open_pr,
                                       scl_ews_pr=var_scl_ews_pr,
                                       scl_sebc_pr=var_scl_sebc_pr,
                                       scl_sc_st_pr=var_scl_sc_st_pr,
                                       scl_f_income=var_scl_f_income,
                                       scl_gender_male=var_scl_gender[0],
                                       scl_gender_female=var_scl_gender[1],
                                       scl_gender_other=var_scl_gender[2],
                                       scl_ask_for_pd=var_scl_ask_for_pd,
                                       scl_official_link=var_scl_official_link,
                                       scl_description=var_scl_description,
                                       scl_note=var_scl_note
                                       )
            obj_scl_save_data.save()
        else:
            aid = 0
            obj_college = College.objects.all()
            flag = 0

            while flag == 0:
                iflag = 0
                for i in obj_college:
                    if i.clg_pk == aid:
                        iflag = 1
                        break
                if iflag == 1:
                    aid += 1
                else:
                    flag = 1

            var_clg_pk = aid

            var_scholar_name = request.POST.get('clg_scholar_name')

            l1 = [request.POST.get('clg_degree_bcom'),
                  request.POST.get('clg_degree_bba'),
                  request.POST.get('clg_degree_bca'),
                  request.POST.get('clg_degree_bsc'),
                  request.POST.get('clg_degree_diploma'),
                  request.POST.get('clg_degree_btech'),
                  request.POST.get('clg_degree_bpharma')
                  ]

            for i in range(0, len(l1)):
                if l1[i] == 'on':
                    l1[i] = True
                else:
                    l1[i] = False

            l2 = [request.POST.get('clg_year_1'),
                  request.POST.get('clg_year_2'),
                  request.POST.get('clg_year_3'),
                  request.POST.get('clg_year_4'),
                  request.POST.get('clg_year_5')
                  ]

            for i in range(0, len(l2)):
                if l2[i] == 'on':
                    l2[i] = True
                else:
                    l2[i] = False

            l3 = [request.POST.get('clg_cat_open'),
                  request.POST.get('clg_cat_ews'),
                  request.POST.get('clg_cat_sebc'),
                  request.POST.get('clg_cat_sc_st')
                  ]

            for i in range(0, len(l3)):
                if l3[i] == 'on':
                    l3[i] = True
                else:
                    l3[i] = False

            var_clg_for_fy_pr_open = request.POST.get('clg_for_fy_pr_open')
            var_clg_for_fy_pr_ews = request.POST.get('clg_for_fy_pr_ews')
            var_clg_for_fy_pr_sebc = request.POST.get('clg_for_fy_pr_sebc')
            var_clg_for_fy_pr_scst = request.POST.get('clg_for_fy_pr_scst')

            if var_clg_for_fy_pr_open == '':
                var_clg_for_fy_pr_open = 200

            if var_clg_for_fy_pr_ews == '':
                var_clg_for_fy_pr_ews = 200

            if var_clg_for_fy_pr_sebc == '':
                var_clg_for_fy_pr_sebc = 200

            if var_clg_for_fy_pr_scst == '':
                var_clg_for_fy_pr_scst = 200

            var_clg_cgpa_open = request.POST.get('clg_cgpa_open')
            var_clg_cgpa_ews = request.POST.get('clg_cgpa_ews')
            var_clg_cgpa_sebc = request.POST.get('clg_cgpa_sebc')
            var_clg_cgpa_scst = request.POST.get('clg_cgpa_scst')

            if var_clg_cgpa_open == '':
                var_clg_cgpa_open = 20

            if var_clg_cgpa_ews == '':
                var_clg_cgpa_ews = 20

            if var_clg_cgpa_sebc == '':
                var_clg_cgpa_sebc = 20

            if var_clg_cgpa_scst == '':
                var_clg_cgpa_scst = 20

            var_clg_f_income = request.POST.get('clg_f_income')

            l4 = [request.POST.get('clg_gender_male'),
                  request.POST.get('clg_gender_female'),
                  request.POST.get('clg_gender_other')
                  ]
            for i in range(0, len(l4)):
                if l4[i] == 'on':
                    l4[i] = True
                else:
                    l4[i] = False

            var_clg_official_link = request.POST.get('clg_official_link')
            if var_clg_official_link == '':
                var_clg_official_link = 'null'
            print(var_clg_official_link)
            var_clg_ask_for_pd = request.POST.get('clg_ask_for_pd')
            var_clg_description = request.POST.get('clg_description')
            var_clg_note = request.POST.get('clg_note')

            obj_clg_save = College(clg_pk=var_clg_pk,
                                   scholar_name=var_scholar_name,
                                   clg_degree_bcom=l1[0],
                                   clg_degree_bba=l1[1],
                                   clg_degree_bca=l1[2],
                                   clg_degree_bsc=l1[3],
                                   clg_degree_diploma=l1[4],
                                   clg_degree_btech=l1[5],
                                   clg_degree_bpharma=l1[6],
                                   clg_year_1=l2[0],
                                   clg_year_2=l2[1],
                                   clg_year_3=l2[2],
                                   clg_year_4=l2[3],
                                   clg_year_5=l2[4],
                                   clg_cat_open=l3[0],
                                   clg_cat_ews=l3[1],
                                   clg_cat_sebc=l3[2],
                                   clg_cat_sc_st=l3[3],
                                   clg_for_fy_pr_open=var_clg_for_fy_pr_open,
                                   clg_for_fy_pr_ews=var_clg_for_fy_pr_ews,
                                   clg_for_fy_pr_sebc=var_clg_for_fy_pr_sebc,
                                   clg_for_fy_pr_sc_st=var_clg_for_fy_pr_scst,
                                   clg_cgpa_open=var_clg_cgpa_open,
                                   clg_cgpa_ews=var_clg_cgpa_ews,
                                   clg_cgpa_sebc=var_clg_cgpa_sebc,
                                   clg_cgpa_sc_st=var_clg_cgpa_scst,
                                   clg_f_income=var_clg_f_income,
                                   clg_gender_male=l4[0],
                                   clg_gender_female=l4[1],
                                   clg_gender_other=l4[2],
                                   clg_ask_for_pd=var_clg_ask_for_pd,
                                   clg_official_link=var_clg_official_link,
                                   clg_description=var_clg_description,
                                   clg_note=var_clg_note
                                   )
            obj_clg_save.save()

    return render(request, 'adminpage.html', parameters)

def viewAdminPanel(request):
    obj_school = School.objects.all()
    obj_college = College.objects.all()
    params = {'sName': obj_school,
              'cName': obj_college
              }
    return render(request, 'view-admin.html', params)

def delete_record(request, arName):
    if request.method == 'GET':
        arName = arName.split('_')
        if arName[0] == 'scl':
            item = School.objects.get(scl_pk=int(arName[1]))
            item.delete()
        else:
            item = College.objects.get(clg_pk=int(arName[1]))
            item.delete()

    return redirect('/view')

li = []

def user(request):

    return render(request, 'user-page.html')

def display(request):

    t = ''

    if request.method == 'POST':
        scl_clg_select = request.POST['scl-clg']
        li.clear()
        if scl_clg_select == 'school':
            t = 'scl'
            std = request.POST['slct2']
            gender = request.POST['gender']
            cat = request.POST['catagory']
            income = request.POST.get('f-income')
            pr = request.POST.get('scl-pr')
            pd = request.POST.get('phy')
            if pd == 'yes':
                for i in School.objects.raw('''select * from main_School where std_{} is true and scl_gender_{} is true and scl_{} is true and scl_f_income >= {} and scl_{}_pr <= {} and scl_ask_for_pd = 'Yes' '''.format(std, gender, cat, income, cat, pr)):
                    li.append(i)
            for i in School.objects.raw('''select * from main_School where std_{} is true and scl_gender_{} is true and scl_{} is true and scl_f_income >= {} and scl_{}_pr <= {} and scl_ask_for_pd = 'No' '''.format(std, gender, cat, income, cat, pr)):
                li.append(i)
        else:
            t = 'clg'
            degree = request.POST['slct3']
            year = None
            if degree == 'bba' or degree == 'bcom' or degree == 'bca' or degree == 'bsc' or degree == 'diploma':
                year = request.POST['slct5']
                print('hello moto')
            elif degree == 'btech':
                year = request.POST['slct6']
            else:
                year = request.POST['slct4']
            pr = None
            cgpa = None
            if year == '1':
                pr = request.POST.get('clg-12th-pr')
            else:
                cgpa = request.POST.get('cgpa')
            gender = request.POST['gender']
            cat = request.POST['catagory']
            income = request.POST.get('f-income')
            pd = request.POST.get('phy')

            if isinstance(pr, str):
                if pd == 'yes':
                    for i in College.objects.raw('''select * from main_College where clg_degree_{} is true and clg_year_{} is true and clg_gender_{} is true and clg_cat_{} is true and clg_f_income >= {} and clg_for_fy_pr_{} <= {} and clg_ask_for_pd = 'Yes' '''.format(degree, year, gender, cat, income, cat, pr)):
                        li.append(i)
                for i in College.objects.raw('''select * from main_College where clg_degree_{} is true and clg_year_{} is true and clg_gender_{} is true and clg_cat_{} is true and clg_f_income >= {} and clg_for_fy_pr_{} <= {} and clg_ask_for_pd = 'No' '''.format(degree, year, gender, cat, income, cat, pr)):
                    li.append(i)
            else:
                if pd == 'yes':
                    for i in College.objects.raw('''select * from main_College where clg_degree_{} is true and clg_year_{} is true and clg_gender_{} is true and clg_cat_{} is true and clg_f_income >= {} and clg_cgpa_{} <= {} and clg_ask_for_pd = 'Yes' '''.format(degree, year, gender, cat, income, cat, cgpa)):
                        li.append(i)
                for i in College.objects.raw('''select * from main_College where clg_degree_{} is true and clg_year_{} is true and clg_gender_{} is true and clg_cat_{} is true and clg_f_income >= {} and clg_cgpa_{} <= {} and clg_ask_for_pd = 'No' '''.format(degree, year, gender, cat, income, cat, cgpa)):
                    li.append(i)

    d = {}

    if len(li) == 0:
        d['data'] = 'No Data Found'
    else:
        d['data'] = list(li)
        d['type'] = t
    return render(request, 'display.html', d)

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1==pass2:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            print(uname,email,pass1,pass2)
            return redirect('login')
        else:
            return HttpResponse("enterd Password and confermed passwords are diffrent!!!")
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/customAdmin')
        else:
            return HttpResponse("user name or Password is incorrect!!!!")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

