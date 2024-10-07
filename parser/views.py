from django.shortcuts import render, redirect
from .models import Candidate, FileUpload # Import your models
from .forms import FileUploadForm
import os
from .parser import extract_info_from_pdf
from .models import RequestId 
from django.http import JsonResponse
def upload_file(request):
    extracted_data_list = []  # List to hold extracted data for each file

    if request.method == 'POST':
        if 'save_data' in request.POST:
            # Saving the modified data from the form
            for i in range(len(request.POST.getlist('name'))):
                extracted_info = Candidate(
                    Name=request.POST.getlist('name')[i],
                    PhoneNumber=request.POST.getlist('mobile_number')[i],
                    Email=request.POST.getlist('email')[i],
                    Experience=request.POST.getlist('experience')[i]
                )
                extracted_info.save()

            return redirect('success')  # Redirect after saving the data

        else:
            # Handling file uploads
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                files = request.FILES.getlist('file')  # Get the list of uploaded files

                for uploaded_file in files:
                    # Save the uploaded file temporarily
                    instance = FileUpload(file=uploaded_file)
                    instance.save()

                    file_path = instance.file.path  # Assuming 'file' is the name of the FileField

                    # Check if it's a PDF and extract data
                    if file_path.endswith('.pdf'):
                        extracted_data = extract_info_from_pdf(file_path=file_path)

                        # Append the extracted data to the list
                        extracted_data_list.append({
                            'name': extracted_data.get('name', 'Unknown'),
                            'mobile_number': extracted_data.get('mobile_number', 'Unknown'),
                            'email': extracted_data.get('email', 'Unknown'),
                            'experience': extracted_data.get('experience', 'Not provided'),
                            'file_name': uploaded_file.name  # Add the file name to the extracted data
                        })

            # Render the form with all extracted data so that the user can edit it
            return render(request, 'upload.html', {
                'form': form,
                'extracted_data_list': extracted_data_list,
            })

    else:
        form = FileUploadForm()

    return render(request, 'upload.html', {'form': form})




def success(request):
    return render(request,'success.html')

def searching_req_names(request):
    try:
        search = request.GET.get('search')
        # print(f"search field{search}")
        payload = []
        # print(f"&&&&&&&&&&&&&&&&&&&{type(search)}")
        if search:
            objs = RequestId.objects.filter(req_name__icontains = search)
            # print(f"-------------{objs.query}")
            for obj in objs:
                payload.append(
                    {
                        "req_names":obj.req_name
                    }
                )

        return JsonResponse(
            {
                "status":True,
                "payload":payload
            }
        )
    except Exception as e:
        print(f"Exception---------------------------------{e}")
        # Return an error response if an exception occurs
        return JsonResponse({
            "status": False,
            "message": "An error occurred."
            # "Error": e
        })
def index(request):
    return render(request,"index.html")