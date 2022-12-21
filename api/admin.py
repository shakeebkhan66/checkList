from django.contrib import admin
from api.models import MyCheckList, MyCheckListItem

admin.site.register(MyCheckList)
admin.site.register(MyCheckListItem)