# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Cc2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', primary_key=True)  # Field name made lowercase.
    number_2019_03_09 = models.BigIntegerField(db_column='2019-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_04_12 = models.FloatField(db_column='2019-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_05_09 = models.FloatField(db_column='2019-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_04 = models.FloatField(db_column='2019-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_14 = models.FloatField(db_column='2019-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_28 = models.FloatField(db_column='2019-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_11 = models.FloatField(db_column='2019-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_18 = models.FloatField(db_column='2019-07-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CC2019'


class Cc2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2020_02_29 = models.BigIntegerField(db_column='2020-02-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_09 = models.BigIntegerField(db_column='2020-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_20 = models.FloatField(db_column='2020-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_01 = models.FloatField(db_column='2020-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_07 = models.FloatField(db_column='2020-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_16 = models.FloatField(db_column='2020-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_23 = models.FloatField(db_column='2020-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_30 = models.FloatField(db_column='2020-04-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_07 = models.FloatField(db_column='2020-05-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_14 = models.FloatField(db_column='2020-05-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_20 = models.FloatField(db_column='2020-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_28 = models.FloatField(db_column='2020-05-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_04 = models.FloatField(db_column='2020-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_11 = models.FloatField(db_column='2020-06-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_18 = models.FloatField(db_column='2020-06-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_24 = models.FloatField(db_column='2020-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_02 = models.FloatField(db_column='2020-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_07 = models.FloatField(db_column='2020-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CC2020'


class Cc2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2021_02_27 = models.BigIntegerField(db_column='2021-02-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_10 = models.BigIntegerField(db_column='2021-03-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_26 = models.FloatField(db_column='2021-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_07 = models.FloatField(db_column='2021-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_19 = models.FloatField(db_column='2021-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_29 = models.FloatField(db_column='2021-04-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_05 = models.FloatField(db_column='2021-05-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_13 = models.FloatField(db_column='2021-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_20 = models.FloatField(db_column='2021-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_27 = models.FloatField(db_column='2021-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_02 = models.FloatField(db_column='2021-06-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_10 = models.FloatField(db_column='2021-06-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_17 = models.FloatField(db_column='2021-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_24 = models.FloatField(db_column='2021-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_30 = models.FloatField(db_column='2021-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_09 = models.FloatField(db_column='2021-07-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_14 = models.FloatField(db_column='2021-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_19 = models.FloatField(db_column='2021-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CC2021'


class Cc2022(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2022_03_15 = models.BigIntegerField(db_column='2022-03-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_03_31 = models.FloatField(db_column='2022-03-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_08 = models.FloatField(db_column='2022-04-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_27 = models.FloatField(db_column='2022-04-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_06 = models.FloatField(db_column='2022-05-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_11 = models.FloatField(db_column='2022-05-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_21 = models.FloatField(db_column='2022-05-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_26 = models.FloatField(db_column='2022-05-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_03 = models.FloatField(db_column='2022-06-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_08 = models.FloatField(db_column='2022-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_17 = models.FloatField(db_column='2022-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_23 = models.FloatField(db_column='2022-06-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_30 = models.FloatField(db_column='2022-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_08 = models.FloatField(db_column='2022-07-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_13 = models.FloatField(db_column='2022-07-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CC2022'


class Cc2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2023_03_04 = models.BigIntegerField(db_column='2023-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_08 = models.BigIntegerField(db_column='2023-03-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_14 = models.BigIntegerField(db_column='2023-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_20 = models.FloatField(db_column='2023-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_25 = models.FloatField(db_column='2023-03-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_01 = models.FloatField(db_column='2023-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_11 = models.FloatField(db_column='2023-04-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_23 = models.FloatField(db_column='2023-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_26 = models.FloatField(db_column='2023-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_01 = models.FloatField(db_column='2023-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_08 = models.FloatField(db_column='2023-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_17 = models.FloatField(db_column='2023-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_24 = models.FloatField(db_column='2023-05-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_31 = models.FloatField(db_column='2023-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_06 = models.FloatField(db_column='2023-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_12 = models.FloatField(db_column='2023-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_21 = models.FloatField(db_column='2023-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_28 = models.FloatField(db_column='2023-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_05 = models.FloatField(db_column='2023-07-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_11 = models.FloatField(db_column='2023-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CC2023'


class Cv2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2019_03_09 = models.BigIntegerField(db_column='2019-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_04_12 = models.FloatField(db_column='2019-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_05_09 = models.FloatField(db_column='2019-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_04 = models.FloatField(db_column='2019-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_14 = models.FloatField(db_column='2019-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_28 = models.FloatField(db_column='2019-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_11 = models.FloatField(db_column='2019-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_18 = models.FloatField(db_column='2019-07-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CV2019'


class Cv2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2020_02_29 = models.BigIntegerField(db_column='2020-02-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_09 = models.BigIntegerField(db_column='2020-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_20 = models.FloatField(db_column='2020-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_01 = models.FloatField(db_column='2020-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_07 = models.FloatField(db_column='2020-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_16 = models.FloatField(db_column='2020-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_23 = models.FloatField(db_column='2020-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_30 = models.FloatField(db_column='2020-04-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_07 = models.FloatField(db_column='2020-05-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_14 = models.FloatField(db_column='2020-05-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_20 = models.FloatField(db_column='2020-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_28 = models.FloatField(db_column='2020-05-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_04 = models.FloatField(db_column='2020-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_11 = models.FloatField(db_column='2020-06-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_18 = models.FloatField(db_column='2020-06-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_24 = models.FloatField(db_column='2020-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_02 = models.FloatField(db_column='2020-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_07 = models.FloatField(db_column='2020-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CV2020'


class Cv2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2021_02_27 = models.BigIntegerField(db_column='2021-02-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_10 = models.BigIntegerField(db_column='2021-03-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_26 = models.BigIntegerField(db_column='2021-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_07 = models.FloatField(db_column='2021-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_19 = models.FloatField(db_column='2021-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_29 = models.FloatField(db_column='2021-04-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_05 = models.FloatField(db_column='2021-05-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_13 = models.FloatField(db_column='2021-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_20 = models.FloatField(db_column='2021-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_27 = models.FloatField(db_column='2021-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_02 = models.FloatField(db_column='2021-06-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_10 = models.FloatField(db_column='2021-06-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_17 = models.FloatField(db_column='2021-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_24 = models.FloatField(db_column='2021-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_30 = models.FloatField(db_column='2021-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_09 = models.FloatField(db_column='2021-07-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_14 = models.FloatField(db_column='2021-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_19 = models.FloatField(db_column='2021-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CV2021'


class Cv2022(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2022_03_15 = models.BigIntegerField(db_column='2022-03-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_03_31 = models.BigIntegerField(db_column='2022-03-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_08 = models.FloatField(db_column='2022-04-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_27 = models.FloatField(db_column='2022-04-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_06 = models.FloatField(db_column='2022-05-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_11 = models.FloatField(db_column='2022-05-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_21 = models.FloatField(db_column='2022-05-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_26 = models.FloatField(db_column='2022-05-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_03 = models.FloatField(db_column='2022-06-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_08 = models.FloatField(db_column='2022-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_17 = models.FloatField(db_column='2022-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_23 = models.FloatField(db_column='2022-06-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_30 = models.FloatField(db_column='2022-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_08 = models.FloatField(db_column='2022-07-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_13 = models.FloatField(db_column='2022-07-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CV2022'


class Cv2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2023_03_04 = models.BigIntegerField(db_column='2023-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_08 = models.BigIntegerField(db_column='2023-03-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_14 = models.BigIntegerField(db_column='2023-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_20 = models.BigIntegerField(db_column='2023-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_25 = models.BigIntegerField(db_column='2023-03-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_01 = models.BigIntegerField(db_column='2023-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_11 = models.FloatField(db_column='2023-04-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_23 = models.FloatField(db_column='2023-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_26 = models.FloatField(db_column='2023-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_01 = models.FloatField(db_column='2023-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_08 = models.FloatField(db_column='2023-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_17 = models.FloatField(db_column='2023-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_24 = models.FloatField(db_column='2023-05-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_31 = models.FloatField(db_column='2023-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_06 = models.FloatField(db_column='2023-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_12 = models.FloatField(db_column='2023-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_21 = models.FloatField(db_column='2023-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_28 = models.FloatField(db_column='2023-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_05 = models.FloatField(db_column='2023-07-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_11 = models.FloatField(db_column='2023-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'CV2023'


class Ecv2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2019_03_09 = models.BigIntegerField(db_column='2019-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_04_12 = models.FloatField(db_column='2019-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_05_09 = models.FloatField(db_column='2019-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_04 = models.FloatField(db_column='2019-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_14 = models.FloatField(db_column='2019-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_28 = models.FloatField(db_column='2019-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_11 = models.FloatField(db_column='2019-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_18 = models.FloatField(db_column='2019-07-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ECV2019'


class Ecv2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2020_02_29 = models.BigIntegerField(db_column='2020-02-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_09 = models.BigIntegerField(db_column='2020-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_20 = models.BigIntegerField(db_column='2020-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_01 = models.FloatField(db_column='2020-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_07 = models.FloatField(db_column='2020-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_16 = models.FloatField(db_column='2020-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_23 = models.FloatField(db_column='2020-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_30 = models.FloatField(db_column='2020-04-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_07 = models.FloatField(db_column='2020-05-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_14 = models.FloatField(db_column='2020-05-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_20 = models.FloatField(db_column='2020-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_28 = models.FloatField(db_column='2020-05-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_04 = models.FloatField(db_column='2020-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_11 = models.FloatField(db_column='2020-06-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_18 = models.FloatField(db_column='2020-06-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_24 = models.FloatField(db_column='2020-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_02 = models.FloatField(db_column='2020-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_07 = models.FloatField(db_column='2020-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ECV2020'


class Ecv2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2021_02_27 = models.BigIntegerField(db_column='2021-02-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_10 = models.BigIntegerField(db_column='2021-03-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_26 = models.BigIntegerField(db_column='2021-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_07 = models.FloatField(db_column='2021-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_19 = models.FloatField(db_column='2021-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_29 = models.FloatField(db_column='2021-04-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_05 = models.FloatField(db_column='2021-05-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_13 = models.FloatField(db_column='2021-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_20 = models.FloatField(db_column='2021-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_27 = models.FloatField(db_column='2021-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_02 = models.FloatField(db_column='2021-06-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_10 = models.FloatField(db_column='2021-06-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_17 = models.FloatField(db_column='2021-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_24 = models.FloatField(db_column='2021-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_30 = models.FloatField(db_column='2021-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_09 = models.FloatField(db_column='2021-07-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_14 = models.FloatField(db_column='2021-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_19 = models.FloatField(db_column='2021-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ECV2021'


class Ecv2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2023_03_04 = models.BigIntegerField(db_column='2023-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_08 = models.BigIntegerField(db_column='2023-03-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_14 = models.BigIntegerField(db_column='2023-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_20 = models.BigIntegerField(db_column='2023-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_25 = models.BigIntegerField(db_column='2023-03-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_01 = models.BigIntegerField(db_column='2023-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_11 = models.FloatField(db_column='2023-04-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_23 = models.FloatField(db_column='2023-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_26 = models.FloatField(db_column='2023-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_01 = models.FloatField(db_column='2023-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_08 = models.FloatField(db_column='2023-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_17 = models.FloatField(db_column='2023-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_24 = models.FloatField(db_column='2023-05-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_31 = models.FloatField(db_column='2023-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_06 = models.FloatField(db_column='2023-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_12 = models.FloatField(db_column='2023-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_21 = models.FloatField(db_column='2023-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_28 = models.FloatField(db_column='2023-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_05 = models.FloatField(db_column='2023-07-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_11 = models.FloatField(db_column='2023-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ECV2023'


class Exg2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2019_03_09 = models.FloatField(db_column='2019-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_04_12 = models.FloatField(db_column='2019-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_05_09 = models.FloatField(db_column='2019-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_04 = models.FloatField(db_column='2019-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_14 = models.FloatField(db_column='2019-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_28 = models.FloatField(db_column='2019-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_11 = models.FloatField(db_column='2019-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_18 = models.FloatField(db_column='2019-07-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ExG2019'


class Exg2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    exg = models.FloatField(db_column='ExG', blank=True, null=True)  # Field name made lowercase.
    number_2_29_2056 = models.FloatField(db_column='2/29/2056', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_9_2057 = models.FloatField(db_column='3/9/2057', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3_20_2058 = models.FloatField(db_column='3/20/2058', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_1_2059 = models.FloatField(db_column='4/1/2059', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_7_2060 = models.FloatField(db_column='4/7/2060', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_16_2061 = models.FloatField(db_column='4/16/2061', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_23_2062 = models.FloatField(db_column='4/23/2062', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4_30_2063 = models.FloatField(db_column='4/30/2063', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_7_2064 = models.FloatField(db_column='5/7/2064', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_14_2065 = models.FloatField(db_column='5/14/2065', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_20_2066 = models.FloatField(db_column='5/20/2066', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5_28_2067 = models.FloatField(db_column='5/28/2067', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_4_2068 = models.FloatField(db_column='6/4/2068', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_11_2069 = models.FloatField(db_column='6/11/2069', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_18_2070 = models.FloatField(db_column='6/18/2070', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_6_24_2071 = models.FloatField(db_column='6/24/2071', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_2_2072 = models.FloatField(db_column='7/2/2072', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_7_7_2073 = models.FloatField(db_column='7/7/2073', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ExG2020'


class Exg2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2021_02_27 = models.FloatField(db_column='2021-02-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_10 = models.FloatField(db_column='2021-03-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_26 = models.FloatField(db_column='2021-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_07 = models.FloatField(db_column='2021-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_19 = models.FloatField(db_column='2021-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_29 = models.FloatField(db_column='2021-04-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_05 = models.FloatField(db_column='2021-05-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_13 = models.FloatField(db_column='2021-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_20 = models.FloatField(db_column='2021-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_27 = models.FloatField(db_column='2021-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_02 = models.FloatField(db_column='2021-06-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_10 = models.FloatField(db_column='2021-06-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_17 = models.FloatField(db_column='2021-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_24 = models.FloatField(db_column='2021-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_30 = models.FloatField(db_column='2021-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_09 = models.FloatField(db_column='2021-07-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_14 = models.FloatField(db_column='2021-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_19 = models.FloatField(db_column='2021-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ExG2021'


class Exg2022(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2022_03_15 = models.FloatField(db_column='2022-03-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_03_31 = models.FloatField(db_column='2022-03-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_08 = models.FloatField(db_column='2022-04-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_27 = models.FloatField(db_column='2022-04-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_06 = models.FloatField(db_column='2022-05-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_11 = models.FloatField(db_column='2022-05-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_21 = models.FloatField(db_column='2022-05-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_26 = models.FloatField(db_column='2022-05-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_08 = models.FloatField(db_column='2022-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_17 = models.FloatField(db_column='2022-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_23 = models.FloatField(db_column='2022-06-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_30 = models.FloatField(db_column='2022-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_08 = models.FloatField(db_column='2022-07-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_13 = models.FloatField(db_column='2022-07-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ExG2022'


class Exg2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2023_03_04 = models.BigIntegerField(db_column='2023-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_08 = models.FloatField(db_column='2023-03-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_14 = models.FloatField(db_column='2023-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_20 = models.FloatField(db_column='2023-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_25 = models.FloatField(db_column='2023-03-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_01 = models.FloatField(db_column='2023-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_11 = models.FloatField(db_column='2023-04-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_23 = models.FloatField(db_column='2023-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_26 = models.FloatField(db_column='2023-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_01 = models.FloatField(db_column='2023-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_08 = models.FloatField(db_column='2023-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_17 = models.FloatField(db_column='2023-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_24 = models.FloatField(db_column='2023-05-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_31 = models.FloatField(db_column='2023-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_06 = models.FloatField(db_column='2023-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_12 = models.FloatField(db_column='2023-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_21 = models.FloatField(db_column='2023-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_28 = models.FloatField(db_column='2023-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_05 = models.FloatField(db_column='2023-07-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_11 = models.FloatField(db_column='2023-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'ExG2023'


class Ph2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2019_03_09 = models.BigIntegerField(db_column='2019-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_04_12 = models.FloatField(db_column='2019-04-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_05_09 = models.FloatField(db_column='2019-05-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_04 = models.FloatField(db_column='2019-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_14 = models.FloatField(db_column='2019-06-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_06_28 = models.FloatField(db_column='2019-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_11 = models.FloatField(db_column='2019-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2019_07_18 = models.FloatField(db_column='2019-07-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'PH2019'


class Ph2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2020_02_29 = models.BigIntegerField(db_column='2020-02-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_09 = models.BigIntegerField(db_column='2020-03-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_03_20 = models.BigIntegerField(db_column='2020-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_01 = models.FloatField(db_column='2020-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_07 = models.FloatField(db_column='2020-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_16 = models.FloatField(db_column='2020-04-16', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_23 = models.FloatField(db_column='2020-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_04_30 = models.FloatField(db_column='2020-04-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_07 = models.FloatField(db_column='2020-05-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_14 = models.FloatField(db_column='2020-05-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_20 = models.FloatField(db_column='2020-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_05_28 = models.FloatField(db_column='2020-05-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_04 = models.FloatField(db_column='2020-06-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_11 = models.FloatField(db_column='2020-06-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_18 = models.FloatField(db_column='2020-06-18', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_06_24 = models.FloatField(db_column='2020-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_02 = models.FloatField(db_column='2020-07-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2020_07_07 = models.FloatField(db_column='2020-07-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'PH2020'


class Ph2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2021_02_27 = models.BigIntegerField(db_column='2021-02-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_10 = models.BigIntegerField(db_column='2021-03-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_03_26 = models.BigIntegerField(db_column='2021-03-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_07 = models.FloatField(db_column='2021-04-07', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_19 = models.FloatField(db_column='2021-04-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_04_29 = models.FloatField(db_column='2021-04-29', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_05 = models.FloatField(db_column='2021-05-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_13 = models.FloatField(db_column='2021-05-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_20 = models.FloatField(db_column='2021-05-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_05_27 = models.FloatField(db_column='2021-05-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_02 = models.FloatField(db_column='2021-06-02', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_10 = models.FloatField(db_column='2021-06-10', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_17 = models.FloatField(db_column='2021-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_24 = models.FloatField(db_column='2021-06-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_06_30 = models.FloatField(db_column='2021-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_09 = models.FloatField(db_column='2021-07-09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_14 = models.FloatField(db_column='2021-07-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2021_07_19 = models.FloatField(db_column='2021-07-19', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'PH2021'


class Ph2022(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2022_03_15 = models.BigIntegerField(db_column='2022-03-15', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_03_31 = models.BigIntegerField(db_column='2022-03-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_08 = models.FloatField(db_column='2022-04-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_04_27 = models.FloatField(db_column='2022-04-27', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_06 = models.FloatField(db_column='2022-05-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_11 = models.FloatField(db_column='2022-05-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_21 = models.FloatField(db_column='2022-05-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_05_26 = models.FloatField(db_column='2022-05-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_03 = models.FloatField(db_column='2022-06-03', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_08 = models.FloatField(db_column='2022-06-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_17 = models.FloatField(db_column='2022-06-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_23 = models.FloatField(db_column='2022-06-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_06_30 = models.FloatField(db_column='2022-06-30', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_08 = models.FloatField(db_column='2022-07-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2022_07_13 = models.FloatField(db_column='2022-07-13', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'PH2022'


class Ph2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    number_2023_03_04 = models.BigIntegerField(db_column='2023-03-04', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_08 = models.BigIntegerField(db_column='2023-03-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_14 = models.BigIntegerField(db_column='2023-03-14', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_20 = models.BigIntegerField(db_column='2023-03-20', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_03_25 = models.BigIntegerField(db_column='2023-03-25', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_01 = models.BigIntegerField(db_column='2023-04-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_11 = models.FloatField(db_column='2023-04-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_23 = models.FloatField(db_column='2023-04-23', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_04_26 = models.FloatField(db_column='2023-04-26', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_01 = models.FloatField(db_column='2023-05-01', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_08 = models.FloatField(db_column='2023-05-08', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_17 = models.FloatField(db_column='2023-05-17', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_24 = models.FloatField(db_column='2023-05-24', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_05_31 = models.FloatField(db_column='2023-05-31', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_06 = models.FloatField(db_column='2023-06-06', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_12 = models.FloatField(db_column='2023-06-12', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_21 = models.FloatField(db_column='2023-06-21', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_06_28 = models.FloatField(db_column='2023-06-28', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_05 = models.FloatField(db_column='2023-07-05', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2023_07_11 = models.FloatField(db_column='2023-07-11', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'PH2023'


class Yield2019(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    number_0_89 = models.FloatField(db_column='0.89', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    lbs_acre = models.FloatField(db_column='lbs/Acre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Yield2019'


class Yield2020(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    lbs_acre = models.FloatField(db_column='lbs/Acre', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Yield2020'


class Yield2021(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'Yield2021'


class Yield2022(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'Yield2022'


class Yield2023(models.Model):
    fid = models.BigIntegerField(db_column='FID', blank=True, null=True)  # Field name made lowercase.
    yield_field = models.FloatField(db_column='yield', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'Yield2023'


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


class CottonShp2019(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField()

    class Meta:
        managed = False
        db_table = 'cotton_shp2019'


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


class UsersUserinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    fristname = models.CharField(db_column='FristName', max_length=100)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_userinfo'


class UsersUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_users'
