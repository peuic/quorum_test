from django.contrib import admin
from .models import Legislator, Bill, VoteResult, Vote

admin.site.register(Legislator)
admin.site.register(Bill)
admin.site.register(VoteResult)
admin.site.register(Vote)
