# views.py
from django.shortcuts import render, redirect
from .forms import UploadForm
from .question_creater import get_questions
from .to_text_converter import return_text
from .models import UploadedFile
from urllib.parse import quote
from django.utils.safestring import mark_safe
import html
import os

def example_func():
    return "\ndhahlan is a good\n boy***bfhv?hebfh2- hjwb\nekjwbf - kdn : hbew"

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save()
            file_path = uploaded_file_instance.pdf_file.path
            file_name = str(os.path.basename(file_path))
            file_path1 = str("./media/pdf_uploads/" + file_name)
            result1 = get_questions(file_path1)
            #result1 = result1.split('\n \n')
            return redirect('success_page', result=result1)  # Redirect to a success page with result as a parameter
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})

def success_page(request, result):
    #result = mark_safe(result)
    #result = html.escape(result)
    return render(request, 'success_page.html', {'result': result})
