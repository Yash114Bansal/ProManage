from rest_framework.serializers import ModelSerializer
from .models import Tasks, subTasks

class subTasksSerializer(ModelSerializer):
    class Meta:
        model = subTasks
        fields = '__all__'

class TasksSerializer(ModelSerializer):
    subtasks = subTasksSerializer(many=True,required=False)
    class Meta:
        model = Tasks
        fields = '__all__'

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Tasks.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            subTasks.objects.create(task=task, **subtask_data)

        return task