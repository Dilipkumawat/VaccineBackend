from django.db import models

# Create your models here.
class VaccinationSurvey(models.Model):
    rowid = models.AutoField(db_column='RowID',primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    optionid = models.CharField(db_column='OptionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='LocationType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    vaccinationdate = models.DateTimeField(db_column='VaccinationDate', blank=True, null=True)  # Field name made lowercase.
    vaccinename = models.CharField(db_column='VaccineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'VACCINATION_SURVEY'


class VaccinationOptions(models.Model):
    id = models.IntegerField(db_column='ID',primary_key = True)  # Field name made lowercase.
    optiontext = models.CharField(db_column='OptionText', max_length=250, blank=True, null=True)  # Field name made lowercase.
    questionid = models.CharField(db_column='QuestionID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='LocationType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'VACCINATION_OPTIONS'


class VaccinationSurveyLog(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    rowid = models.IntegerField(db_column='RowID', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    optionid = models.CharField(db_column='OptionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='LocationType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    vaccinationdate = models.DateTimeField(db_column='VaccinationDate', blank=True, null=True)  # Field name made lowercase.
    vaccinename = models.CharField(db_column='VaccineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'VACCINATION_SURVEY_LOG'


class DependantPerson(models.Model):
    rowid = models.AutoField(db_column='RowID',primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dependantfullname = models.CharField(db_column='DependantFullName', max_length=50, blank=True, null=True)  # Field name made lowercase.    relationtype = models.CharField(db_column='RelationType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    currentcity = models.CharField(db_column='CurrentCity', max_length=250, blank=True, null=True)  # Field name made lowercase.
    optionid = models.CharField(db_column='OptionID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locationtype = models.CharField(db_column='LocationType', max_length=250, blank=True, null=True)  # Field name made lowercase.
    vaccinationdate = models.DateTimeField(db_column='VaccinationDate', blank=True, null=True)  # Field name made lowercase.
    vaccinename = models.CharField(db_column='VaccineName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'DEPENDANT_PERSON'