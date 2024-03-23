from django.db import models
from django.contrib import admin
from apps.employee.models import Employee, Company, Doctor, Patient


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("curp", "name", "last_name", "second_last_name", "company")
    list_display_links = ("curp",)
    search_fields = ("curp", "name", "last_name", "second_last_name", "company__name")
    list_filter = ("company",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.remote_field and db_field.remote_field.model:
            model = db_field.remote_field.model
            if issubclass(model, models.Model) and hasattr(model, "is_active"):
                kwargs["queryset"] = model.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "rfc", "name", "description")
    list_display_links = ("id",)
    search_fields = ("rfc", "name")
    list_filter = ("name",)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("curp", "professional_id", "user")
    list_display_links = ("curp",)
    search_fields = ("curp__name", "curp__last_name", "curp__second_last_name", "professional_id", "user__email")
    list_filter = ("curp__name", "curp__last_name", "curp__second_last_name", "professional_id", "user__email")


class PatientAdmin(admin.ModelAdmin):
    list_display = ("curp", "user")
    list_display_links = ("curp",)
    search_fields = ("curp__name", "curp__last_name", "curp__second_last_name", "user__email")
    list_filter = ("curp__name", "curp__last_name", "curp__second_last_name", "user__email")


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)

