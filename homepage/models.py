from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=128)                #프로젝트 이름
    center_name = models.CharField(max_length=128)         #기관 이름
    center_location = models.CharField(max_length=128)     #기관 위치
    center_type = models.CharField(max_length=128)         #기관 종류 = 아동, 노인....
    product_type = models.CharField(max_length=128)        #후원 물품
    project_explain = models.CharField(max_length=128)     #프로젝트 설명
    date = models.DateField()                #작성일자
    
    def __str__(self):
        return self.name
