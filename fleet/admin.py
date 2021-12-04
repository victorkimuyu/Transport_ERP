from django.contrib import admin

from fleet.forms import TruckForm, TrailerForm, DriverForm
from fleet.models import Truck, Trailer, Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    form = DriverForm
    list_display = ("first_name", "last_name", "assigned_truck", "phone_no", "id_no")
    fieldsets = (
        ("Personal Details", {
            "fields": ('first_name',
                       'last_name',
                       'id_no',
                       'phone_no',
                       'email',
                       'dob',
                       'assigned_truck',
                       'date_hired',),
        }),
        ("Next of Kin", {
            "fields": ('nok_first_name',
                       'nok_last_name',
                       'nok_phone_no',
                       'nok_relationship',
                       'nok_id_no',
                       'nok_email'),
        }),
    )


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("static/admin/css/custom.css",)}

    form = TrailerForm
    list_display = ("reg_no", "type", "mounted_truck", "status")


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("static/admin/css/custom.css",)}

    form = TruckForm
    list_display = ("reg_no", "make", "model", "model_no", "trailer", 'effective_LC', "driver", "status")
    list_filter = ('status',)
