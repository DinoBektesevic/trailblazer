from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from .forms import FileFieldForm

from .image_processing.process_fits import process_fits

#def process_image(img):
#    with open(f"static/upload/fits/{img.name}", "wb") as f:
#        f.write(img.read())
#    return (img.name, True)

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = reverse_lazy('upload') # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                process_fits(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
