from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

from .models import Question

# Create your views here.


def rates(request):
    return render(request, 'booking/rates.html')

class CreateView(generic.edit.CreateView):
    model = Question
    fields = ['question_text', 'pub_date']
    def get_form(self):
        form = super().get_form()
        form.fields['pub_date'].widget = DatePickerInput()
        return form

# FIle: add these to polls/views.py
class UpdateView(generic.edit.UpdateView):
    model = Question
    fields = ['question_text', 'pub_date']
    def get_form(self):
        form = super().get_form()
        form.fields['pub_date'].widget = DateTimePickerInput()
        return form