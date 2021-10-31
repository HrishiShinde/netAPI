from django.contrib import admin
from .models import Advisor, Booking, User

# Register your models here.
@admin.register(Advisor)
# admin.site.register(Advisor)
class AdvisorAdmin(admin.ModelAdmin):
    list_display = ['adID', 'adName', 'adPhoto']
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['usrID', 'usrName', 'usrEmail', 'usrPassword']
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['bookID', 'bookAdID', 'bookUsrID', 'bookAdName', 'bookAdPhoto', 'bookTime']
