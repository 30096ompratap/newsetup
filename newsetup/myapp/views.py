# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyFileForm
from .models import MyFileModel
from django.conf import settings

def upload_file(request):
    if request.method == 'POST':
        form = MyFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        File = MyFileModel.objects.create(file_name=str(file),uploaded_file=file)
        File.save()
        return HttpResponse(str(file) + str(File.uploaded_file))
    else:
        form = MyFileForm()
    return render(request, 'upload.html', {'form': form})

def file_print(request):
    def print_file_content(file_path):
        try:
            print(">>>>>>>>>>>>>>>",file_path)
            with open(file_path, 'r') as file:
                print(">>>>>>>>>>>>>>>",file_path)
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("File not found.")

    # Example usage:
    file_url = settings.MEDIA_ROOT + '/uploads/dump.txt'
    print_file_content(file_url)
    print(file_url)
    return HttpResponse("success")