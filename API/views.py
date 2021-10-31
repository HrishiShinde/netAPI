from django.shortcuts import render
from .models import Advisor, Booking, User
from .serializers import AdvisorSerializer, BookingSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import jwt, datetime
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def getAdvisor(request, id):
    if request.method == 'GET':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id', None)
    #     if id is not None:
    #         data = Advisor.objects.get(id = id)
    #         serializer = AdvisorSerializer(data)
    #         return JsonResponse(serializer.data, safe=False)
        data = Advisor.objects.all()
        serializer = AdvisorSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(['GET', 'POST'])
def setAdvisor(request):
    if request.method == 'POST':
        # json_data = 
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        # serializer = AdvisorSerializer(data = python_data)
        serializer = AdvisorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg' : 'Data Saved Successfully!'}
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)

@csrf_exempt
@api_view(['GET', 'POST'])
def usrRegis(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            for u in User.objects.raw('select * from User where usrName="%s"' % (request.data["usrName"])):
                uId = u.usrID

            payload = {
                'id' : uId,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
                'iat' : datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm="HS256")
            response_msg = {
                            'msg' : 'Data Saved Successfully!',
                            'jwt' : token,
                            'userId' : uId
                            }
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)

@csrf_exempt
@api_view(['GET', 'POST'])
def usrLog(request):
    if request.method == 'POST':
        for u in User.objects.raw('select * from User where usrEmail="%s"' % (request.data["usrEmail"])):
            if u.usrPassword == request.data["usrPass"]:
                payload = {
                'id' : u.usrID,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 60),
                'iat' : datetime.datetime.utcnow()
                }
                token = jwt.encode(payload, 'secret', algorithm="HS256")
                response_msg = {
                                'msg' : 'Data Saved Successfully!',
                                'jwt' : token,
                                'userId' : u.usrID,
                                }
            return JsonResponse(response_msg, safe=True)
        return JsonResponse({'msg' : 'User not found or password incorrect'}, safe=True)
        

@csrf_exempt
@api_view(['GET', 'POST'])
def bookAdvisor(request, uId, aId):
    if request.method == 'POST':
        for a in Advisor.objects.raw('select * from Advisor where adID="%s"' % (aId)):
            aName = a.adName
            aPhoto = a.adPhoto
        
        data = {
            "bookAdID" : aId,
            "bookUsrID" : uId,
            "bookAdName" : aName,
            "bookAdPhoto" : aPhoto,
            "bookTime" : request.data["time"],
        }

        serializer = BookingSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg' : 'Data Saved Successfully!'}
            return JsonResponse(response_msg, safe=True)
        return JsonResponse(serializer.errors)

@csrf_exempt
@api_view(['GET', 'POST'])
def getBookAdvisor(request, uId):
    if request.method == 'GET':
        data = Booking.objects.raw('select * from Booking where bookUsrID="%s"' % (uId))
        serializer = BookingSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
