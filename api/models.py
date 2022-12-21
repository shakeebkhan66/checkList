from django.db import models


# Create your models here.
class MyCheckList(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class MyCheckListItem(models.Model):
    text = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checkList = models.ForeignKey(MyCheckList, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
