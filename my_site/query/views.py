from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models
from .utils import dbhelper
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.


# 查询本医院的病人并筛选
def user_query(request):
    if request.method == 'POST':
        pgender = request.POST.get('patientgender')
        age_lower = request.POST.get('patientage_lower')
        age_higher = request.POST.get('patientage_higher')
        if pgender != '男' and pgender != '女':
            return render(request, 'query/template/query/user_query.html', {'error': 'Invalid information!'})
        elif age_lower > age_lower:
            return render(request, 'query/template/query/user_query.html', {'error': 'Invalid information!'})
        else:
            username = request.session['username']
            db = dbhelper()
            sql_str = 'select instituteid, institutename from hospital_record'
            sql_str_hospital_id = "select HospitalID from user where UserID='%s'" % (username)
            hospitals = dict(db.query(sql_str))
            hospital_id = db.query(sql_str_hospital_id)
            db.close()
            patients = models.Patientbasicinfos.objects.all().filter(gender=pgender, hospitalid=hospital_id[0][0],
                                                                     age__gte=age_lower,
                                                                     age__lte=age_higher).order_by('age')
            if patients:
                return render(request, 'query/template/query/user_query.html',
                              {'posts': patients, 'hospitalname': hospitals[hospital_id[0][0]]})
            else:
                return render(request, 'query/template/query/user_query.html',
                              {'error': 'No such patients!'})
    else:
        username = request.session['username']
        db = dbhelper()
        sql_str = 'select instituteid, institutename from hospital_record'
        sql_str_hospital_id = "select HospitalID from user where UserID='%s'" % (username)
        hospitals = dict(db.query(sql_str))
        hospital_id = db.query(sql_str_hospital_id)
        db.close()
        patients = models.Patientbasicinfos.objects.all().filter(hospitalid=hospital_id[0][0])
        return render(request, 'query/template/query/user_query.html',
                      {'posts': patients, 'hospitalname': hospitals[hospital_id[0][0]]})


# 查询所有病人并筛选
def winter_query(request):
    if request.method == 'POST':
        pgender = request.POST.get('patientgender')
        age_lower = request.POST.get('patientage_lower')
        age_higher = request.POST.get('patientage_higher')
        if pgender != '男' and pgender != '女':
            return render(request, 'query/template/query/winter_query.html', {'error': 'Invalid information!'})
        elif age_lower > age_lower:
            return render(request, 'query/template/query/winter_query.html', {'error': 'FUCKING test!'})
        else:
            patients = models.Patientbasicinfos.objects.all().filter(gender=pgender, age__gte=age_lower,
                                                                     age__lte=age_higher)
            db = dbhelper()
            sql_str = 'select instituteid, institutename from hospital_record'
            hospitals = dict(db.query(sql_str))
            patient_info = []
            for patient in patients:
                patient_info.append(
                    {'patientid': patient.patientid, 'patientname': patient.patientname, 'gender': patient.gender,
                     'age': patient.age, 'clinicaldiagnosis': patient.clinicaldiagnosis,
                     'pathologicaldiagnosis': patient.pathologicaldiagnosis,
                     'hospitalname': hospitals[patient.hospitalid],
                     'checkdate': patient.checkdate})
            return render(request, 'query/template/query/winter_query.html', {'posts': patient_info})
    else:
        patients = models.Patientbasicinfos.objects.all()
        db = dbhelper()
        sql_str = 'select instituteid, institutename from hospital_record'
        hospitals = dict(db.query(sql_str))
        patient_info = []
        for patient in patients:
            patient_info.append(
                {'patientid': patient.patientid, 'patientname': patient.patientname, 'gender': patient.gender,
                 'age': patient.age, 'clinicaldiagnosis': patient.clinicaldiagnosis,
                 'pathologicaldiagnosis': patient.pathologicaldiagnosis,
                 'hospitalname': hospitals[patient.hospitalid],
                 'checkdate': patient.checkdate})
        return render(request, 'query/template/query/winter_query.html', {'posts': patient_info})


# 修改本院病人信息 如果病人ID非本院 报错
def user_modify(request):
    username = request.session['username']
    if request.method == 'POST':
        patient_id = request.POST.get("id_patient")
        new_name = request.POST.get("new_name_patient")
        new_clinical = request.POST.get("new_clinical_patient")
        new_age = request.POST.get("new_age_patient")
        db = dbhelper()
        sql_str_hospital_id = "select HospitalID from user where UserID='%s'" % (username)
        sql_str = "update PatientBasicInfos set PatientName='%s',ClinicalDiagnosis='%s',Age='%s' WHERE PatientID = '%s'" % (
            new_name, new_clinical, new_age, patient_id)
        sql_str_patient_hospitalid = "select HospitalID from patientbasicinfos where PatientID='%s'" % (patient_id)
        user_hospital_id = db.query(sql_str_hospital_id)
        patient_hospital_id = db.query(sql_str_patient_hospitalid)
        if patient_hospital_id == ():  # ID不存在
            patients = models.Patientbasicinfos.objects.all().filter(hospitalid=user_hospital_id[0][0])
            patient_info = []
            for item in patients:
                patient_info.append(
                    {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender,
                     'age': item.age,
                     'clinical': item.clinicaldiagnosis})
            return render(request, 'query/template/modify/user_modify.html',
                          {'posts': patient_info, 'wrong': 'No such patient!'})
        elif user_hospital_id[0][0] == patient_hospital_id[0][0]:
            db.update(sql_str)
            patients = models.Patientbasicinfos.objects.all().filter(hospitalid=user_hospital_id[0][0])
            patient_info = []
            for item in patients:
                patient_info.append(
                    {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender,
                     'age': item.age,
                     'clinical': item.clinicaldiagnosis})
            db.close()
            return render(request, 'query/template/modify/user_modify.html',
                          {'posts': patient_info, 'success': 'Modified Successfully'})
        else:
            patients = models.Patientbasicinfos.objects.all().filter(hospitalid=user_hospital_id[0][0])
            patient_info = []
            for item in patients:
                patient_info.append(
                    {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender,
                     'age': item.age,
                     'clinical': item.clinicaldiagnosis})
            return render(request, 'query/template/modify/user_modify.html',
                          {'posts': patient_info, 'wrong': 'Access Denied!'})
    else:
        db = dbhelper()
        sql_str_hospital_id = "select HospitalID from user where UserID='%s'" % (username)
        user_hospital_id = db.query(sql_str_hospital_id)
        db.close()
        patients = models.Patientbasicinfos.objects.all().filter(hospitalid=user_hospital_id[0][0])
        patient_info = []
        for item in patients:
            patient_info.append(
                {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender, 'age': item.age,
                 'clinical': item.clinicaldiagnosis})

        return render(request, 'query/template/modify/user_modify.html',
                      {'posts': patient_info})


# 修改所有病人的个人信息 带分页
def winter_modify(request):
    if request.method == 'POST':
        patient_id = request.POST.get("id_patient")
        new_name = request.POST.get("new_name_patient")
        new_clinical = request.POST.get("new_clinical_patient")
        new_age = request.POST.get("new_age_patient")
        print(id, new_name, new_clinical, new_age)
        db = dbhelper()
        sql_str = "update PatientBasicInfos set PatientName='%s',ClinicalDiagnosis='%s',Age='%s' WHERE PatientID = '%s'" % (
            new_name, new_clinical, new_age, patient_id)
        sql_str_patient_hospitalid = "select HospitalID from patientbasicinfos where PatientID='%s'" % (patient_id)
        patient_hospital_id = db.query(sql_str_patient_hospitalid)
        if patient_hospital_id == ():  # ID不存在
            db.close()
            patients = models.Patientbasicinfos.objects.all()
            patient_info = []
            for item in patients:
                patient_info.append(
                    {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender,
                     'age': item.age,
                     'clinical': item.clinicaldiagnosis})
            paginator = Paginator(patient_info, 10)  # 设置每页显示的总条数
            current_page = request.GET.get('page')  # 获得当前页数
            print(current_page)
            try:
                posts = paginator.page(current_page)  # 设置当前页数对应的数据
            except PageNotAnInteger as error:  # 当前页面数非整数
                posts = paginator.page(1)
            except EmptyPage as error:  # 当前页码数为空
                posts = paginator.page(1)
            return render(request, 'query/template/modify/winter_modify.html',
                          {'posts': posts, 'wrong': 'No such patient!'})
        else:
            db.update(sql_str)
            db.close()
            patients = models.Patientbasicinfos.objects.all()
            patient_info = []
            for item in patients:
                patient_info.append(
                    {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender,
                     'age': item.age,
                     'clinical': item.clinicaldiagnosis})
            paginator = Paginator(patient_info, 10)  # 设置每页显示的总条数
            current_page = request.GET.get('page')  # 获得当前页数
            print(current_page)
            try:
                posts = paginator.page(current_page)  # 设置当前页数对应的数据
            except PageNotAnInteger as error:  # 当前页面数非整数
                posts = paginator.page(1)
            except EmptyPage as error:  # 当前页码数为空
                posts = paginator.page(1)
            return render(request, 'query/template/modify/winter_modify.html',
                          {'posts': posts, 'success': 'Modified Successfully!'})
    else:
        patients = models.Patientbasicinfos.objects.all()
        patient_info = []
        for item in patients:
            patient_info.append(
                {'patientid': item.patientid, 'patientname': item.patientname, 'gender': item.gender, 'age': item.age,
                 'clinical': item.clinicaldiagnosis})
        paginator = Paginator(patient_info, 10)  # 设置每页显示的总条数
        current_page = request.GET.get('page')  # 获得当前页数
        print(current_page)
        try:
            posts = paginator.page(current_page)  # 设置当前页数对应的数据
        except PageNotAnInteger as error:  # 当前页面数非整数
            posts = paginator.page(1)
        except EmptyPage as error:  # 当前页码数为空
            posts = paginator.page(1)
        return render(request, 'query/template/modify/winter_modify.html',
                      {'posts': posts})


# 用户登录 按照普通用户和管理员跳转到不同页面
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        request.session['username'] = username
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if username != 'winter':
                return redirect('http://127.0.0.1:8000/person/')
            else:
                return redirect('http://127.0.0.1:8000/winter/person')
        else:
            return render(request, 'query/template/login/login.html', {'message': 'Invalid ID or Password'})
    return render(request, 'query/template/login/login.html')


# 修改用户的自己的密码 有很多报错信息
def modify_password(request):
    username = request.session['username']
    db = dbhelper()
    sql_str = "select UserName,HospitalID,Gender,age from user where UserID='%s' " % (username)
    sql_str_hospital = 'select instituteid, institutename from hospital_record'
    hospitals = dict(db.query(sql_str_hospital))
    user_infos = db.query(sql_str)
    db.close()
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        certification = request.POST.get('certification')
        user = User.objects.get(username=username)
        if not authenticate(username=username, password=old_password):
            return render(request, 'query/template/login/person.html',
                          {'wrong': 'Invalid Password! Check it again！', 'name': user_infos[0][0],
                           'hospital': hospitals[user_infos[0][1]], 'gender': user_infos[0][2],
                           'age': user_infos[0][3]})
        elif authenticate(username=username, password=old_password) and new_password != certification:
            return render(request, 'query/template/login/person.html',
                          {'wrong': 'Different Passwords! Check it again!', 'name': user_infos[0][0],
                           'hospital': hospitals[user_infos[0][1]], 'gender': user_infos[0][2],
                           'age': user_infos[0][3]})
        elif authenticate(username=username, password=old_password) and new_password == certification:
            user.set_password(new_password)
            user.save()
            return render(request, 'query/template/login/person.html',
                          {'success': 'Modified Successfully!', 'name': user_infos[0][0],
                           'hospital': hospitals[user_infos[0][1]], 'gender': user_infos[0][2],
                           'age': user_infos[0][3]})  # correct
    else:
        return render(request, 'query/template/login/person.html',
                      {'success': 'Log in Successfully!', 'name': user_infos[0][0],
                       'hospital': hospitals[user_infos[0][1]],
                       'gender': user_infos[0][2],
                       'age': user_infos[0][3]})


# 修改所有人的密码 有很多报错信息
def modify_all_password(request):  # for winter especially
    users = models.User.objects.all()
    db = dbhelper()
    sql_str_hospital = 'select instituteid, institutename from hospital_record'
    hospitals = dict(db.query(sql_str_hospital))
    db.close()
    user_infos = []
    for user in users:
        user_infos.append(
            {'id': user.userid, 'gender': user.gender, 'age': user.age,
             'hospitalname': hospitals[user.hospitalid]})
    paginator = Paginator(user_infos, 8)  # 设置每页显示的总条数
    current_page = request.GET.get('page')  # 获得当前页数
    print(current_page)
    try:
        posts = paginator.page(current_page)  # 设置当前页数对应的数据
    except PageNotAnInteger as error:  # 当前页面数非整数
        posts = paginator.page(1)
    except EmptyPage as error:  # 当前页码数为空
        posts = paginator.page(1)
    if request.method == 'POST':
        username = request.POST.get('userid')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        certification = request.POST.get('certification')
        user = User.objects.get(username=username)
        if not authenticate(username=username, password=old_password):
            return render(request, 'query/template/login/person_winter.html',
                          {'posts': posts, 'wrong': 'Invalid Password! Check it again！'})
        elif authenticate(username=username, password=old_password) and new_password != certification:
            return render(request, 'query/template/login/person_winter.html',
                          {'posts': posts, 'wrong': 'Different Passwords! Check it again!'})
        elif authenticate(username=username, password=old_password) and new_password == certification:
            user.set_password(new_password)
            user.save()
            return render(request, 'query/template/login/person_winter.html',
                          {'posts': posts, 'success': 'Modified Successfully!'})
    else:
        return render(request, 'query/template/login/person_winter.html', {'posts': posts})


def user_add_patient(request):
    username = request.session['username']
    sql_str_hospital_id = "select HospitalID from user where UserID='%s'" % (username)
    db = dbhelper()
    result = db.query(sql_str_hospital_id)
    hospital_id = result[0][0]
    print(hospital_id)
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        check_date = request.POST.get('check_date')
        check_number = request.POST.get('check_number')
        patient_name = request.POST.get('patient_name')
        patient_gender = request.POST.get('patient_gender')
        patient_age = request.POST.get('patient_age')
        clinical = request.POST.get('clinical')
        endoscopic = request.POST.get('endoscopic')
        pathological = request.POST.get('pathological')
        patient_hospital_id = hospital_id
        models.Patientbasicinfos.objects.create(checkdate=check_date, checknumber=check_number,
                                                patientid=patient_id, patientname=patient_name,
                                                gender=patient_gender, age=patient_age,
                                                clinicaldiagnosis=clinical, endoscopicdiagnosis=endoscopic,
                                                pathologicaldiagnosis=pathological,
                                                hospitalid=patient_hospital_id)
        return render(request, 'query/template/add/user_add.html', {'success': 'Added successfully!'})
    else:
        return render(request, 'query/template/add/user_add.html')


def winter_add_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        check_date = request.POST.get('check_date')
        check_number = request.POST.get('check_number')
        patient_name = request.POST.get('patient_name')
        patient_gender = request.POST.get('patient_gender')
        patient_age = request.POST.get('patient_age')
        clinical = request.POST.get('clinical')
        endoscopic = request.POST.get('endoscopic')
        pathological = request.POST.get('pathological')
        hospital_id = request.POST.get('patient_hospital_id')
        models.Patientbasicinfos.objects.create(checkdate=check_date, checknumber=check_number,
                                                patientid=patient_id, patientname=patient_name,
                                                gender=patient_gender, age=patient_age,
                                                clinicaldiagnosis=clinical, endoscopicdiagnosis=endoscopic,
                                                pathologicaldiagnosis=pathological, hospitalid=hospital_id)
        return render(request, 'query/template/add/winter_add.html', {'success': 'Added successfully!'})
    else:
        return render(request, 'query/template/add/winter_add.html')
