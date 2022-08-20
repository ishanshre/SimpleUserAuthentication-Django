from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    template_name = 'base/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
