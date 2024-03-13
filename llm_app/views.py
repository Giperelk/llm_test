import json

from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView
from .forms import DocumentForm
from .models import Document
from .utils import get_cohere_answer


class UploadDocumentView(View):
    def get(self, request):
        form = DocumentForm()
        return render(request, 'upload_document.html', {'form': form})

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            uploaded_file = request.FILES['file']
            if not uploaded_file.name.lower().endswith('.pdf'):
                return HttpResponseBadRequest('Будь ласка, завантажте тільки файли у форматі PDF.')
            document.save()
            return redirect('upload_success')
        return render(request, 'upload_document.html', {'form': form})


class QuestionFormView(TemplateView):
    template_name = 'question_form.html'

    def get(self, request):
        documents = Document.objects.all()  # Отримати всі документи з бази даних
        return render(request, 'question_form.html', {'documents': documents})

    def post(self, request, *args, **kwargs):
        question = request.POST.get('question')
        # Реалізація генерації відповіді буде тут
        answer = "Це ваша відповідь на запитання: " + question
        return JsonResponse({'answer': answer})


def upload_success(request):
    return render(request, 'upload_success.html')


def index(request):
    return render(request, 'index.html')


def get_answer(request):

    data = json.loads(request.body)

    # Отримайте текст з PDF-файлу за його id
    uploaded_document = Document.objects.get(id=data['document_id'])

    # Отримайте питання з POST-запиту користувача
    question = data['question']

    return JsonResponse({"answer": get_cohere_answer(str(uploaded_document.file), question)})
