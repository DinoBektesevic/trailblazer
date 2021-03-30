from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#from django.urls import reverse, reverse_lazy
#from django.views.generic.edit import FormView
#from .forms import FileFieldForm
#
#def process_image(img):
#    return img
#
#class FileFieldView(FormView):
#    form_class = FileFieldForm
#    template_name = 'upload.html'  # Replace with your template.
#    success_url = '' #reverse_lazy('upload.html') # Replace with your URL or reverse().
#
#    def post(self, request, *args, **kwargs):
#        form_class = self.get_form_class()
#        form = self.get_form(form_class)
#        files = request.FILES.getlist('file_field')
#        breakpoint()
#        if form.is_valid():
#            for f in files:
#                process_image(f)
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)
#
## Create your views here.
#def render_upload(request):
#    #breakpoint()
#    form = FileFieldView()
#    if request.method == "POST":
#        form.post(request)
#    else:
#        pass
#        #form = FileFieldView()
#
#    return render(request, 'upload.html', {"form": form.form_class})

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo

class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'upload.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
