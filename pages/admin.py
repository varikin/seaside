from django import forms
from django.contrib import admin
from seaside.pages.models import Media, NavItem, SeasidePage

class SeasidePageForm(forms.ModelForm):
    url = forms.RegexField(max_length=100, regex=r'^[-\w/]+$',
        help_text = "Example: '/about/contact/'. Make sure to have leading and trailing slashes.",
        error_message = "This value must contain only letters, numbers,underscores, dashes or slashes."
    )

    class Meta:
        model = SeasidePage

class SeasidePageAdmin(admin.ModelAdmin):
    form = SeasidePageForm
    list_display = ('url', 'title', 'is_menu')
    search_fields = ('url', 'title')

admin.site.register(SeasidePage, SeasidePageAdmin)
admin.site.register(Media)
admin.site.register(NavItem)
