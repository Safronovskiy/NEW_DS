from django.contrib import admin
from .models import *


admin.site.register(SubjectModel)
admin.site.register(StructureComponentModel)
admin.site.register(AnswerModel)
admin.site.register(ConspectModel)
admin.site.register(CustomAnswerModel)