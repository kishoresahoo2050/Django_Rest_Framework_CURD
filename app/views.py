from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import CreateSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def CreateStudent(request):
    if request.method == 'POST':
        b_data = request.body
        stream = io.BytesIO(b_data)
        p_data = JSONParser().parse(stream)
        c_serializer = CreateSerializer(data=p_data)
        if c_serializer.is_valid():
            c_serializer.save()
            return JsonResponse({"msg":"Data Inserted Successfully."})
        else:
            return JsonResponse(c_serializer.errors)
    else:
        return HttpResponse("It GET method")


# Get Data
@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        j_data = request.body
        strem  = io.BytesIO(j_data)
        py_data = JSONParser().parse(strem)
        id = py_data.get('id',None)
        
        if id:
            stu = Student.objects.get(id = id)
            serializer = CreateSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = CreateSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe= False )
    else:
        stu = Student.objects.all()
        # print(stu)
        serializer = CreateSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe = False)


@csrf_exempt
def UpdateStudent(request):
    
    if request.method == 'PUT':
        r_body = request.body
        stream = io.BytesIO(r_body)
        py_data = JSONParser().parse(stream)
        id   =  py_data.get('id')
        stu  = Student.objects.get(id=id)
        serialize_up = CreateSerializer(stu,data=py_data,partial=True)
        if serialize_up.is_valid():
            serialize_up.save()
            return JsonResponse({"msg":"Data Updated Sucessfully."})
        else:
            return JsonResponse(serialize_up.errors)
    else:
        return HttpResponse("Its PUT Respone")


@csrf_exempt
def DeleteStudent(request):

    if request.method == "DELETE":
        j_body = request.body
        stream = io.BytesIO(j_body)
        py_data = JSONParser().parse(stream)
        id = py_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        return JsonResponse({"msg":"Data Delted Successfully."})
        





        
        
