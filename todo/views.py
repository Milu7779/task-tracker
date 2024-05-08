from django.shortcuts import render
from rest_framework.response import Response
from . models import todo
from . serializers import TodoSerializer
from rest_framework.views import APIView
# Create your views here.
class ListTodoAPIView(APIView):
    def get(self,request):
        todos = todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class detailesTodoAPIView(APIView):
    def get(self,request,pk):
        todos = todo.objects.get(id=pk)
        serializer = TodoSerializer(todos,many=False)
        return Response(serializer.data)
class createTodoAPIView(APIView):
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class updateTodoAPIView(APIView):
    def put(self,request,pk):
        todos = todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=todos,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
class deleteTodoAPIView(APIView):
    def get(self,request,pk):
        todo_instance = todo.objects.get(id=pk)
        todo_instance.delete()
        return Response('deleted')
def listd(request):
    return render(request,'todo.html')
def add_task(request):
    if request.method == 'POST':
        task=request.POST['task']
        priority= request.POST['priority']
        tasks = todo(title=task, description=priority)
        tasks.save()
    return render(request,'todo.html')
