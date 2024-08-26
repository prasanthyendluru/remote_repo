from django.contrib import admin
from jobs.models import hydjobs,punejobs,banglorejobs
# Register your models here.
class hydAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(hydjobs,hydAdmin)

class banAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(banglorejobs,banAdmin)

class puneAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(punejobs,puneAdmin)