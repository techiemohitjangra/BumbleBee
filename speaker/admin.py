from django.contrib import admin

# Register your models here.
from .models import Visitor, Word, Phrase, Contact


class WordAdmin(admin.ModelAdmin):
    list_display = ["word", "from_phrase", "start_time", "end_time"]
    list_filter = ["from_phrase"]
    search_fields = ["from_phrase", "word"]


class PhraseAdmin(admin.ModelAdmin):
    fieldsets = [("Phrase", {"fields": ["phrase"]}),
                 ("Start Time", {"fields": ["start_time"]}),
                 ("End Time", {"fields": ["end_time"]})
                 ]
    list_display = ["phrase", "word_count", "start_time", "end_time"]
    list_filter = ["word_count"]
    search_fields = ["phrase", "word_count"]


class VisitorAdmin(admin.ModelAdmin):
    list_display = ["ip_address", "visit_date_time"]
    list_filter = ["ip_address"]
    search_fields = ["ip_address"]


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Personal Information", {"fields": ["full_name", "email"]}),
        ("Message", {"fields": ["message"]}),
    ]
    list_display = ["full_name", "email", "contact_time", "message"]
    list_filter = ["full_name", "email"]
    search_fields = ["full_name", "email", "message"]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Word, WordAdmin)
