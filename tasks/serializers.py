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
    
    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.isComplete = validated_data.get('isComplete', instance.isComplete)
        instance.deadLine = validated_data.get('deadLine', instance.deadLine)
        instance.save()

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id', None)

            if subtask_id:

                subtask = subTasks.objects.get(pk=subtask_id)
                subtask.title = subtask_data.get('title', subtask.title)
                subtask.description = subtask_data.get('description', subtask.description)
                subtask.isComplete = subtask_data.get('isComplete', subtask.isComplete)
                subtask.deadLine = subtask_data.get('deadLine', subtask.deadLine)
                subtask.save()
            else:
    
                subTasks.objects.create(task=instance, **subtask_data)

        return instance