from django.urls import path
from api.views import Checklist, CheckListWithId, ChecklistCreateApi, ChecklistItemApi

urlpatterns = [
    # path('', show_Hello),
    path('api/checklists', Checklist.as_view()),
    path('api/checklist/<int:pk>', CheckListWithId.as_view()),
    path('api/checklistcreate/', ChecklistCreateApi.as_view()),
    path('api/checklistget/<int:pk>', ChecklistItemApi.as_view()),
]
