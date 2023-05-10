from django.contrib import admin

from .models import Competition, Lecture, Workshop, Point, Certificate

admin.site.register(Competition)
admin.site.register(Lecture)
admin.site.register(Workshop)
admin.site.register(Point)
admin.site.register(Certificate)