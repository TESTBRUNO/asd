from django.contrib import admin
from myapp.models import tech



class techProps(admin.ModelAdmin):
  list_display = ["name", "cost","count"]


admin.site.register(tech,techProps)

# Register your models here.
