from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request 
from survey.models import VaccinationOptions, VaccinationSurvey, DependantPerson
from survey.serializers import VaccinationOptionsSerializer, VaccinationSurveySerializer, DependantPersonSerializer
from datetime import datetime
#  Create your views here.
class GetOption(APIView):
    def get(self, request : Request) -> JsonResponse:
        try:
            options_list_objects = VaccinationOptions.objects.filter(locationtype='India')
            options_list_data = VaccinationOptionsSerializer(options_list_objects,many=True).data
        except Exception as e:
            print(e)
            return JsonResponse(create_failure(500,'Server Error'+str(e)))
        return JsonResponse(create_success("Data Found!",options_list_data))


class GetVaccinationStatus(APIView):
    def get(self,request:Request)-> JsonResponse:
        try:
            try:
                self.username=request.GET['username']
            except Exception as e:
                self.username = 000000
            survey_details_object = VaccinationSurvey.objects.filter(username=self.username)
            survey_details_data = VaccinationSurveySerializer(survey_details_object,many=True).data
            print(survey_details_data,"here printed")
            employee_dependant_details_object = DependantPerson.objects.filter(username=self.username)
            employee_dependant_details_data = DependantPersonSerializer(employee_dependant_details_object,many=True).data
            try:
                survey_details_data[0]['dependant'] = employee_dependant_details_data
            except Exception as e:
                print(e)
        except Exception as e:
            return JsonResponse(create_failure(500,'Server Error'+str(e)))
        return JsonResponse(create_success('Data Found!',survey_details_data))


class UpdateVaccinationStatus(APIView):
    def post(self,request:Request)-> JsonResponse:
        try:
            self.username = request.data['Username']
            self.optionid = request.data['OptionID']
            self.location_type = request.data['LocationType']
            self.vaccination_date = request.data['VaccinationDate']
            self.vaccine_name = request.data['VaccineName']
            self.dependant_details_list = request.data['DependantDetails']
            self.getdate = datetime.utcnow()
        except Exception as e:
            return JsonResponse(create_failure(500,'Error in Payload'+str(e)))
        try:
            getdate = datetime.utcnow()
            if_survey_exists = VaccinationSurvey.objects.filter(username=self.username).count()
            if if_survey_exists != 0:
                survey_add_or_update = self.updateSurveyDetails()
            elif if_survey_exists == 0:
                survey_add_or_update = self.insertSurveyDetails()
        except Exception as e:
            return JsonResponse(create_failure(500, 'Server Error'+str(e)))
        return JsonResponse(survey_add_or_update)

    def updateSurveyDetails(self):
        try:
            update_vaccination_survey = VaccinationSurvey.objects.filter(username=self.username).update(
                optionid=self.optionid, locationtype=self.location_type,vaccinationdate=self.vaccination_date,vaccinename=self.vaccine_name,modifiedby=self.username,modifieddate=self.getdate)
            for dependant in self.dependant_details_list:
                update_dependant = DependantPerson.objects.filter(username=self.username,dependantfullname=dependant['DependentFullName'],dob=dependant['DOB']).update(currentcity=dependant['CurrentCity'],optionid=dependant['OptionID'], locationtype=dependant['LocationType'],vaccinationdate=dependant['VaccinationDate'],vaccinename=dependant['VaccineName'],modifiedby=self.username,modifieddate=self.getdate)
                if update_dependant == 0:
                    update_dependant = DependantPerson.objects.create(username=self.username,dependantfullname=dependant['DependentFullName'],dob=dependant['DOB'],currentcity=dependant['CurrentCity'],optionid=dependant['OptionID'], locationtype=dependant['LocationType'],vaccinationdate=dependant['VaccinationDate'],vaccinename=dependant['VaccineName'],createdby=self.username,createddate=self.getdate)
        except Exception as e:
            return create_failure(500,'Server Error'+str(e))
        return create_success(200,'Data Updated SuccessFully')

    def insertSurveyDetails(self):
        try:
            insert_vaccination_survey = VaccinationSurvey.objects.create(username=self.username,
                optionid=self.optionid, locationtype=self.location_type,vaccinationdate=self.vaccination_date,vaccinename=self.vaccine_name,modifiedby=self.username,modifieddate=self.getdate)
            for dependant in self.dependant_details_list:
                    update_dependant = DependantPerson.objects.filter(username=self.username,dependantfullname=dependant['DependentFullName'],dob=dependant['DOB']).update(currentcity=dependant['CurrentCity'],optionid=dependant['OptionID'], locationtype=dependant['LocationType'],vaccinationdate=dependant['VaccinationDate'],vaccinename=dependant['VaccineName'],modifiedby=self.username,modifieddate=self.getdate)
                    if update_dependant == 0:
                        update_dependant = DependantPerson.objects.create(username=self.username,dependantfullname=dependant['DependentFullName'],dob=dependant['DOB'],currentcity=dependant['CurrentCity'],optionid=dependant['OptionID'], locationtype=dependant['LocationType'],vaccinationdate=dependant['VaccinationDate'],vaccinename=dependant['VaccineName'],createdby=self.username,createddate=self.getdate)
        except Exception as e:
            return create_failure(500,'Server Error'+str(e))
        return create_success(200,'Data Updated SuccessFully')


def create_success(msg,data=[]):
    outputJson = {
        "StatusCode":200,
        "MSG":msg,
        "ReplyCode":"Success",
        "Data":data,
    }
    return outputJson
    
def create_failure(statusCode,msg):
    outputJson = {
        "StatusCode":statusCode,
        "MSG":msg,
        "ReplyCode":"Failed",
        "Data":[],
    }
    return outputJson