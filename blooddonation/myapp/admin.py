from django.contrib import admin
from .models import Article,City,Thana,Donation,Bloodgroup,Contact,Profile,RequestChange



# Register your models here.
@admin.register(RequestChange)

class RequestChangeAdmin(admin.ModelAdmin):
    list_display = ['username']




@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject']
    list_filter = ['subject']


@admin.register(Bloodgroup)
class BloodAdmin(admin.ModelAdmin):
    list_display =['name',]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['name','published']
    list_editable = ['published']



@admin.register(City)


class CityAdmin(admin.ModelAdmin):
    list_display = ['name' ,]

@admin.register(Thana)

class ThanaAdmin(admin.ModelAdmin):
    list_display = ['name' ,]

@admin.register(Donation)

class DonationAdmin(admin.ModelAdmin):

    list_display = ['name','bloodgroup','phone','city','thana']
    list_editable = ['phone']
    search_fields = ('bloodgroup__name','city__name','thana__name')
    list_filter=['city','thana','bloodgroup']


@admin.register(Profile)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','blood','city','thana','phone']
    list_filter = ['blood','city','thana']
    list_editable = ['phone']
    
    search_fields = ('bloodgroup__name','city__name','thana__name')