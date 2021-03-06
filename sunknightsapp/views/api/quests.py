from rest_framework import viewsets
from ...serializers.daily_quest_serializer import QuestSerializer
from ...models.daily_quest import Quest
import datetime
from datetime import timedelta



class QuestsViewSet(viewsets.ModelViewSet):

    serializer_class = QuestSerializer


    def get_queryset(self):
        from django.db.models import Q
        return Quest.objects.filter(Q(permed=True)|Q(date=(datetime.datetime.utcnow()- timedelta(days=datetime.datetime.utcnow().weekday())).replace(hour=0, minute=0, second=0, microsecond=0)))


