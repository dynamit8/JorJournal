from rest_framework import serializers

from journal.models import Journal, Lesson

class JournalLogSerializer(serializers.Serializer):
    summary     = serializers.CharField(max_length=100)
    items       = serializers.ListField(child=serializers.CharField(max_length=100))


class JournalSerializer(serializers.ModelSerializer):
    """
    #logs
    [
        {
            "summary": "Basic setup",
            "items": [
                "Setup template views for easiest interactions of data.", 
                "Update template mixin.", 
                "Create basic structure of Landing page, journal pages(home, list, create), Achievement pages(home, list).", "Set sqlite as default db for local dev, so not depend on docker for most stupid solution on local dev.", 
                "Lean base template fragments including base.html, topbar.html, too much import on css, js, fonts."
            ]
        }, 
        {
            "summary": "More robust field type",
            "items": [
                "Change type of field to JSONField(), let display for template and view responsibilities.", 
                "Change displaying logic on html displaying list."
            ]
        }
    ]
    """
    logs        = JournalLogSerializer(many=True)
    class Meta:
        model = Journal
        fields = "__all__"

    # override create and update due to nested serailizer field in ModelSerializer
    def create(self, validated_data):
        return Journal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.topic = validated_data.get('topic', instance.topic)
        instance.logs = validated_data.get('logs', instance.logs)
        instance.save()
        return instance

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"