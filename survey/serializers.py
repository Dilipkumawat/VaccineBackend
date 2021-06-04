from rest_framework import serializers
from survey.models import VaccinationOptions,VaccinationSurvey,DependantPerson,VaccinationSurveyLog

class VaccinationOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = VaccinationOptions
        fields = '__all__'

class VaccinationSurveySerializer(serializers.ModelSerializer):

    class Meta:
        model = VaccinationSurvey
        fields = '__all__'

class DependantPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = DependantPerson
        fields = '__all__'

class VaccinationSurveyLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = VaccinationSurveyLog
        fields = '__all__'