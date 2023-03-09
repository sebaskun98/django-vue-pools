from django.contrib import admin

from .models import Choice, Question
import adminactions.actions as actions
from import_export.admin import ImportExportModelAdmin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(ImportExportModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
actions.add_to_site(admin.site)