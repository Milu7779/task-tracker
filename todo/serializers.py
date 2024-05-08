from rest_framework import serializers
from todo.models import todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = "__all__"