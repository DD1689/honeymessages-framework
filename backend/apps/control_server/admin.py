from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

# Register all models
for model in apps.get_app_config("control_server").get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
