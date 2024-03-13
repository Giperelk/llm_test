from django.urls import path
from .views import UploadDocumentView, upload_success, QuestionFormView, get_answer, index

urlpatterns = [
    path('upload/', UploadDocumentView.as_view(), name='upload_document'),
    path('upload-success/', upload_success, name='upload_success'),
    path('question-form/', QuestionFormView.as_view(), name='question_form'),
    path('get-answer/', get_answer, name='get_answer'),
    path('', index, name='index')
]
