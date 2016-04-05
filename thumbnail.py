from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.db.models.fields.files import ImageField



class ImagePreviewEnabledAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.__class__ == ImageField:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImagePreviewEnabledAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        
