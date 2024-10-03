from django.shortcuts import render, redirect
from .models import ExtractedInfo
from .forms import FileUploadForm
import os

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file')  # Get the list of uploaded files
            extracted_data_list = []  # List to hold extracted data for each file

            for uploaded_file in files:
                # Save the uploaded file temporarily
                instance = form.save(commit=False)  # Don't save yet
                instance.file = uploaded_file  # Set the file to the instance
                instance.save()  # Save the instance

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
