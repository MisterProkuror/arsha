from django.contrib import admin
from myfiles.models import *


# Register your models here.

class adminservices(admin.ModelAdmin):
    list_display = ["image", "name", "malumotnoma", "date"]


admin.site.register(Services, adminservices)


class Admintype(admin.ModelAdmin):
    list_display = ["turi"]

admin.site.register(Type, Admintype)


class Adminportfolio(admin.ModelAdmin):
    list_display = ["image", "ism", "type", "category", "client", "date", "link"]


admin.site.register(Portfolio, Adminportfolio)


class Adminkasbi(admin.ModelAdmin):
    list_display = ["hodim"]


admin.site.register(Kasbi, Adminkasbi)





class Adminteam(admin.ModelAdmin):
    list_display = ["name", "kasb", "malumotnoma", "img", "twit", "face", "inst", "tele", "date"]


admin.site.register(Team, Adminteam)


class Adminqoshish(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message", "date"]

admin.site.register(Ariza, Adminqoshish)


class AdminSubcrise(admin.ModelAdmin):
    list_display = ["subcrise"]

admin.site.register(Subcrise, AdminSubcrise)


class AdminSubcrisePort(admin.ModelAdmin):
    list_display = ["subcriseportfolio"]

admin.site.register(SubPort, AdminSubcrisePort)