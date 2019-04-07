# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Rtstation(models.Model):
    station_no_10 = models.BigIntegerField(blank=True, null=True)
    station_no_100 = models.BigIntegerField(blank=True, null=True)
    station_no_101 = models.BigIntegerField(blank=True, null=True)
    station_no_102 = models.BigIntegerField(blank=True, null=True)
    station_no_103 = models.BigIntegerField(blank=True, null=True)
    station_no_104 = models.BigIntegerField(blank=True, null=True)
    station_no_105 = models.BigIntegerField(blank=True, null=True)
    station_no_106 = models.BigIntegerField(blank=True, null=True)
    station_no_107 = models.BigIntegerField(blank=True, null=True)
    station_no_108 = models.BigIntegerField(blank=True, null=True)
    station_no_109 = models.BigIntegerField(blank=True, null=True)
    station_no_11 = models.BigIntegerField(blank=True, null=True)
    station_no_110 = models.BigIntegerField(blank=True, null=True)
    station_no_111 = models.BigIntegerField(blank=True, null=True)
    station_no_112 = models.BigIntegerField(blank=True, null=True)
    station_no_113 = models.BigIntegerField(blank=True, null=True)
    station_no_114 = models.BigIntegerField(blank=True, null=True)
    station_no_115 = models.BigIntegerField(blank=True, null=True)
    station_no_12 = models.BigIntegerField(blank=True, null=True)
    station_no_13 = models.BigIntegerField(blank=True, null=True)
    station_no_14 = models.BigIntegerField(blank=True, null=True)
    station_no_15 = models.BigIntegerField(blank=True, null=True)
    station_no_16 = models.BigIntegerField(blank=True, null=True)
    station_no_17 = models.BigIntegerField(blank=True, null=True)
    station_no_18 = models.BigIntegerField(blank=True, null=True)
    station_no_19 = models.BigIntegerField(blank=True, null=True)
    station_no_2 = models.BigIntegerField(blank=True, null=True)
    station_no_21 = models.BigIntegerField(blank=True, null=True)
    station_no_22 = models.BigIntegerField(blank=True, null=True)
    station_no_23 = models.BigIntegerField(blank=True, null=True)
    station_no_24 = models.BigIntegerField(blank=True, null=True)
    station_no_25 = models.BigIntegerField(blank=True, null=True)
    station_no_26 = models.BigIntegerField(blank=True, null=True)
    station_no_27 = models.BigIntegerField(blank=True, null=True)
    station_no_28 = models.BigIntegerField(blank=True, null=True)
    station_no_29 = models.BigIntegerField(blank=True, null=True)
    station_no_3 = models.BigIntegerField(blank=True, null=True)
    station_no_30 = models.BigIntegerField(blank=True, null=True)
    station_no_31 = models.BigIntegerField(blank=True, null=True)
    station_no_32 = models.BigIntegerField(blank=True, null=True)
    station_no_33 = models.BigIntegerField(blank=True, null=True)
    station_no_34 = models.BigIntegerField(blank=True, null=True)
    station_no_35 = models.BigIntegerField(blank=True, null=True)
    station_no_36 = models.BigIntegerField(blank=True, null=True)
    station_no_37 = models.BigIntegerField(blank=True, null=True)
    station_no_38 = models.BigIntegerField(blank=True, null=True)
    station_no_39 = models.BigIntegerField(blank=True, null=True)
    station_no_4 = models.BigIntegerField(blank=True, null=True)
    station_no_40 = models.BigIntegerField(blank=True, null=True)
    station_no_41 = models.BigIntegerField(blank=True, null=True)
    station_no_42 = models.BigIntegerField(blank=True, null=True)
    station_no_43 = models.BigIntegerField(blank=True, null=True)
    station_no_44 = models.BigIntegerField(blank=True, null=True)
    station_no_45 = models.BigIntegerField(blank=True, null=True)
    station_no_46 = models.BigIntegerField(blank=True, null=True)
    station_no_47 = models.BigIntegerField(blank=True, null=True)
    station_no_48 = models.BigIntegerField(blank=True, null=True)
    station_no_49 = models.BigIntegerField(blank=True, null=True)
    station_no_5 = models.BigIntegerField(blank=True, null=True)
    station_no_50 = models.BigIntegerField(blank=True, null=True)
    station_no_51 = models.BigIntegerField(blank=True, null=True)
    station_no_52 = models.BigIntegerField(blank=True, null=True)
    station_no_53 = models.BigIntegerField(blank=True, null=True)
    station_no_54 = models.BigIntegerField(blank=True, null=True)
    station_no_55 = models.BigIntegerField(blank=True, null=True)
    station_no_56 = models.BigIntegerField(blank=True, null=True)
    station_no_57 = models.BigIntegerField(blank=True, null=True)
    station_no_58 = models.BigIntegerField(blank=True, null=True)
    station_no_59 = models.BigIntegerField(blank=True, null=True)
    station_no_6 = models.BigIntegerField(blank=True, null=True)
    station_no_60 = models.BigIntegerField(blank=True, null=True)
    station_no_61 = models.BigIntegerField(blank=True, null=True)
    station_no_62 = models.BigIntegerField(blank=True, null=True)
    station_no_63 = models.BigIntegerField(blank=True, null=True)
    station_no_64 = models.BigIntegerField(blank=True, null=True)
    station_no_65 = models.BigIntegerField(blank=True, null=True)
    station_no_66 = models.BigIntegerField(blank=True, null=True)
    station_no_67 = models.BigIntegerField(blank=True, null=True)
    station_no_68 = models.BigIntegerField(blank=True, null=True)
    station_no_69 = models.BigIntegerField(blank=True, null=True)
    station_no_7 = models.BigIntegerField(blank=True, null=True)
    station_no_70 = models.BigIntegerField(blank=True, null=True)
    station_no_71 = models.BigIntegerField(blank=True, null=True)
    station_no_72 = models.BigIntegerField(blank=True, null=True)
    station_no_73 = models.BigIntegerField(blank=True, null=True)
    station_no_74 = models.BigIntegerField(blank=True, null=True)
    station_no_75 = models.BigIntegerField(blank=True, null=True)
    station_no_76 = models.BigIntegerField(blank=True, null=True)
    station_no_77 = models.BigIntegerField(blank=True, null=True)
    station_no_78 = models.BigIntegerField(blank=True, null=True)
    station_no_79 = models.BigIntegerField(blank=True, null=True)
    station_no_8 = models.BigIntegerField(blank=True, null=True)
    station_no_80 = models.BigIntegerField(blank=True, null=True)
    station_no_81 = models.BigIntegerField(blank=True, null=True)
    station_no_82 = models.BigIntegerField(blank=True, null=True)
    station_no_83 = models.BigIntegerField(blank=True, null=True)
    station_no_84 = models.BigIntegerField(blank=True, null=True)
    station_no_85 = models.BigIntegerField(blank=True, null=True)
    station_no_86 = models.BigIntegerField(blank=True, null=True)
    station_no_87 = models.BigIntegerField(blank=True, null=True)
    station_no_88 = models.BigIntegerField(blank=True, null=True)
    station_no_89 = models.BigIntegerField(blank=True, null=True)
    station_no_9 = models.BigIntegerField(blank=True, null=True)
    station_no_90 = models.BigIntegerField(blank=True, null=True)
    station_no_91 = models.BigIntegerField(blank=True, null=True)
    station_no_92 = models.BigIntegerField(blank=True, null=True)
    station_no_93 = models.BigIntegerField(blank=True, null=True)
    station_no_94 = models.BigIntegerField(blank=True, null=True)
    station_no_95 = models.BigIntegerField(blank=True, null=True)
    station_no_96 = models.BigIntegerField(blank=True, null=True)
    station_no_97 = models.BigIntegerField(blank=True, null=True)
    station_no_98 = models.BigIntegerField(blank=True, null=True)
    station_no_99 = models.BigIntegerField(blank=True, null=True)
    index = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rtstation'


class Rtstation1(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    station_no_10 = models.BigIntegerField(blank=True, null=True)
    station_no_100 = models.BigIntegerField(blank=True, null=True)
    station_no_101 = models.BigIntegerField(blank=True, null=True)
    station_no_102 = models.BigIntegerField(blank=True, null=True)
    station_no_103 = models.BigIntegerField(blank=True, null=True)
    station_no_104 = models.BigIntegerField(blank=True, null=True)
    station_no_105 = models.BigIntegerField(blank=True, null=True)
    station_no_106 = models.BigIntegerField(blank=True, null=True)
    station_no_107 = models.BigIntegerField(blank=True, null=True)
    station_no_108 = models.BigIntegerField(blank=True, null=True)
    station_no_109 = models.BigIntegerField(blank=True, null=True)
    station_no_11 = models.BigIntegerField(blank=True, null=True)
    station_no_110 = models.BigIntegerField(blank=True, null=True)
    station_no_111 = models.BigIntegerField(blank=True, null=True)
    station_no_112 = models.BigIntegerField(blank=True, null=True)
    station_no_113 = models.BigIntegerField(blank=True, null=True)
    station_no_114 = models.BigIntegerField(blank=True, null=True)
    station_no_115 = models.BigIntegerField(blank=True, null=True)
    station_no_12 = models.BigIntegerField(blank=True, null=True)
    station_no_13 = models.BigIntegerField(blank=True, null=True)
    station_no_14 = models.BigIntegerField(blank=True, null=True)
    station_no_15 = models.BigIntegerField(blank=True, null=True)
    station_no_16 = models.BigIntegerField(blank=True, null=True)
    station_no_17 = models.BigIntegerField(blank=True, null=True)
    station_no_18 = models.BigIntegerField(blank=True, null=True)
    station_no_19 = models.BigIntegerField(blank=True, null=True)
    station_no_2 = models.BigIntegerField(blank=True, null=True)
    station_no_21 = models.BigIntegerField(blank=True, null=True)
    station_no_22 = models.BigIntegerField(blank=True, null=True)
    station_no_23 = models.BigIntegerField(blank=True, null=True)
    station_no_24 = models.BigIntegerField(blank=True, null=True)
    station_no_25 = models.BigIntegerField(blank=True, null=True)
    station_no_26 = models.BigIntegerField(blank=True, null=True)
    station_no_27 = models.BigIntegerField(blank=True, null=True)
    station_no_28 = models.BigIntegerField(blank=True, null=True)
    station_no_29 = models.BigIntegerField(blank=True, null=True)
    station_no_3 = models.BigIntegerField(blank=True, null=True)
    station_no_30 = models.BigIntegerField(blank=True, null=True)
    station_no_31 = models.BigIntegerField(blank=True, null=True)
    station_no_32 = models.BigIntegerField(blank=True, null=True)
    station_no_33 = models.BigIntegerField(blank=True, null=True)
    station_no_34 = models.BigIntegerField(blank=True, null=True)
    station_no_35 = models.BigIntegerField(blank=True, null=True)
    station_no_36 = models.BigIntegerField(blank=True, null=True)
    station_no_37 = models.BigIntegerField(blank=True, null=True)
    station_no_38 = models.BigIntegerField(blank=True, null=True)
    station_no_39 = models.BigIntegerField(blank=True, null=True)
    station_no_4 = models.BigIntegerField(blank=True, null=True)
    station_no_40 = models.BigIntegerField(blank=True, null=True)
    station_no_41 = models.BigIntegerField(blank=True, null=True)
    station_no_42 = models.BigIntegerField(blank=True, null=True)
    station_no_43 = models.BigIntegerField(blank=True, null=True)
    station_no_44 = models.BigIntegerField(blank=True, null=True)
    station_no_45 = models.BigIntegerField(blank=True, null=True)
    station_no_46 = models.BigIntegerField(blank=True, null=True)
    station_no_47 = models.BigIntegerField(blank=True, null=True)
    station_no_48 = models.BigIntegerField(blank=True, null=True)
    station_no_49 = models.BigIntegerField(blank=True, null=True)
    station_no_5 = models.BigIntegerField(blank=True, null=True)
    station_no_50 = models.BigIntegerField(blank=True, null=True)
    station_no_51 = models.BigIntegerField(blank=True, null=True)
    station_no_52 = models.BigIntegerField(blank=True, null=True)
    station_no_53 = models.BigIntegerField(blank=True, null=True)
    station_no_54 = models.BigIntegerField(blank=True, null=True)
    station_no_55 = models.BigIntegerField(blank=True, null=True)
    station_no_56 = models.BigIntegerField(blank=True, null=True)
    station_no_57 = models.BigIntegerField(blank=True, null=True)
    station_no_58 = models.BigIntegerField(blank=True, null=True)
    station_no_59 = models.BigIntegerField(blank=True, null=True)
    station_no_6 = models.BigIntegerField(blank=True, null=True)
    station_no_60 = models.BigIntegerField(blank=True, null=True)
    station_no_61 = models.BigIntegerField(blank=True, null=True)
    station_no_62 = models.BigIntegerField(blank=True, null=True)
    station_no_63 = models.BigIntegerField(blank=True, null=True)
    station_no_64 = models.BigIntegerField(blank=True, null=True)
    station_no_65 = models.BigIntegerField(blank=True, null=True)
    station_no_66 = models.BigIntegerField(blank=True, null=True)
    station_no_67 = models.BigIntegerField(blank=True, null=True)
    station_no_68 = models.BigIntegerField(blank=True, null=True)
    station_no_69 = models.BigIntegerField(blank=True, null=True)
    station_no_7 = models.BigIntegerField(blank=True, null=True)
    station_no_70 = models.BigIntegerField(blank=True, null=True)
    station_no_71 = models.BigIntegerField(blank=True, null=True)
    station_no_72 = models.BigIntegerField(blank=True, null=True)
    station_no_73 = models.BigIntegerField(blank=True, null=True)
    station_no_74 = models.BigIntegerField(blank=True, null=True)
    station_no_75 = models.BigIntegerField(blank=True, null=True)
    station_no_76 = models.BigIntegerField(blank=True, null=True)
    station_no_77 = models.BigIntegerField(blank=True, null=True)
    station_no_78 = models.BigIntegerField(blank=True, null=True)
    station_no_79 = models.BigIntegerField(blank=True, null=True)
    station_no_8 = models.BigIntegerField(blank=True, null=True)
    station_no_80 = models.BigIntegerField(blank=True, null=True)
    station_no_81 = models.BigIntegerField(blank=True, null=True)
    station_no_82 = models.BigIntegerField(blank=True, null=True)
    station_no_83 = models.BigIntegerField(blank=True, null=True)
    station_no_84 = models.BigIntegerField(blank=True, null=True)
    station_no_85 = models.BigIntegerField(blank=True, null=True)
    station_no_86 = models.BigIntegerField(blank=True, null=True)
    station_no_87 = models.BigIntegerField(blank=True, null=True)
    station_no_88 = models.BigIntegerField(blank=True, null=True)
    station_no_89 = models.BigIntegerField(blank=True, null=True)
    station_no_9 = models.BigIntegerField(blank=True, null=True)
    station_no_90 = models.BigIntegerField(blank=True, null=True)
    station_no_91 = models.BigIntegerField(blank=True, null=True)
    station_no_92 = models.BigIntegerField(blank=True, null=True)
    station_no_93 = models.BigIntegerField(blank=True, null=True)
    station_no_94 = models.BigIntegerField(blank=True, null=True)
    station_no_95 = models.BigIntegerField(blank=True, null=True)
    station_no_96 = models.BigIntegerField(blank=True, null=True)
    station_no_97 = models.BigIntegerField(blank=True, null=True)
    station_no_98 = models.BigIntegerField(blank=True, null=True)
    station_no_99 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rtstation1'


class Station(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    banking = models.BooleanField(blank=True, null=True)
    bike_stands = models.BigIntegerField(blank=True, null=True)
    bonus = models.BooleanField(blank=True, null=True)
    contract_name = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    number = models.BigIntegerField(primary_key=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'station'
