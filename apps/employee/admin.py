from django.db import models
from django.contrib import admin
from apps.employee.models import Employee, Doctor, Patient


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("curp", "name", "last_name", "second_last_name")
    list_display_links = ("curp",)
    search_fields = ("curp", "name", "last_name", "second_last_name")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.remote_field and db_field.remote_field.model:
            model = db_field.remote_field.model
            if issubclass(model, models.Model) and hasattr(model, "is_active"):
                kwargs["queryset"] = model.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("employee", "professional_id", "user")
    list_display_links = ("employee",)
    search_fields = ("employee__name", "employee__last_name", "professional_id", "user__email")


class PatientAdmin(admin.ModelAdmin):
    list_display = ("employee", "user")
    list_display_links = ("employee",)
    search_fields = ("employee__name", "employee__last_name", "user__email")


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)

