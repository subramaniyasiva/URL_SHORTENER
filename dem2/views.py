from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method == 'POST':
        if 'siva1' in request.FILES:
            uf = request.FILES['siva1']
            print(f'File Name: {uf.name}')
            print(f'File Size: {uf.size}')
            fs=FileSystemStorage()
            fs.save(uf.name,uf)

            # Optionally save the file if needed
            # with open(f'media/{uf.name}', 'wb+') as destination:
            #     for chunk in uf.chunks():
            #         destination.write(chunk)
        else:
            print('No file with the name "siva1" was uploaded.')
    return render(request, 'a.html')
