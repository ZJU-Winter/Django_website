# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AArearoi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    anatomyid = models.CharField(db_column='AnatomyID', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_arearoi'


class ALabeledimage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    imageid = models.CharField(db_column='ImageID', max_length=45)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pathtype = models.CharField(db_column='PathType', max_length=20)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=45)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10)  # Field name made lowercase.
    userid_check_1 = models.CharField(db_column='UserID_Check_1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userid_check_2 = models.CharField(db_column='UserID_Check_2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a_labeledimage'


class Anatomydict(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    anatomyname = models.CharField(db_column='AnatomyName', max_length=45)  # Field name made lowercase.
    anatomyid = models.CharField(db_column='AnatomyID', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anatomydict'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DArearoi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    diseaseid = models.CharField(db_column='DiseaseID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_arearoi'


class DLabeledimage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    imageid = models.CharField(db_column='ImageID', max_length=45)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pathtype = models.CharField(db_column='PathType', max_length=20)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=45)  # Field name made lowercase.
    usertype = models.CharField(db_column='UserType', max_length=10)  # Field name made lowercase.
    userid_check_1 = models.CharField(db_column='UserID_Check_1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    userid_check_2 = models.CharField(db_column='UserID_Check_2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'd_labeledimage'


class Diseasedict(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    diseasename = models.CharField(db_column='DiseaseName', max_length=45)  # Field name made lowercase.
    diseaseid = models.CharField(db_column='DiseaseID', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diseasedict'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HospitalRecord(models.Model):
    instituteid = models.CharField(db_column='InstituteID', primary_key=True, max_length=11)  # Field name made lowercase.
    institutename = models.CharField(db_column='InstituteName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hospital_record'


class Imagepath(models.Model):
    checknumber = models.CharField(db_column='CheckNumber', max_length=20)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=45)  # Field name made lowercase.
    imageid = models.CharField(db_column='ImageID', primary_key=True, max_length=45)  # Field name made lowercase.
    imgpath = models.CharField(db_column='ImgPath', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'imagepath'


class Patientbasicinfos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    checkdate = models.DateTimeField(db_column='CheckDate', blank=True, null=True)  # Field name made lowercase.
    checknumber = models.CharField(db_column='CheckNumber', max_length=15)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=15)  # Field name made lowercase.
    patientname = models.CharField(db_column='PatientName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=25, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    clinicaldiagnosis = models.CharField(db_column='ClinicalDiagnosis', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    examinationfindings = models.CharField(db_column='ExaminationFindings', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    endoscopicdiagnosis = models.CharField(db_column='EndoscopicDiagnosis', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    pathologicaldiagnosis = models.CharField(db_column='PathologicalDiagnosis', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    patientreport = models.CharField(db_column='PatientReport', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.CharField(db_column='HospitalID', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientbasicinfos'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=45)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.CharField(db_column='HospitalID', max_length=3)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('id', 'userid'),)
