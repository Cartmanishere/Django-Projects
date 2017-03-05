# from django.contrib import admin

# from .models import Link

# admin.site.register(Link)
from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Link.objects.all()
        return Link.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Link, LinkAdmin)