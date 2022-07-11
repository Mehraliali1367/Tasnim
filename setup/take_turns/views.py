from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . import forms
from . import models
from account.models import User
from .serializers import DoctorSerializer, PresenceSerializer
from django.contrib import messages
from rest_framework.generics import ListCreateAPIView
from django.http import JsonResponse


class DoctorDifinit(View):
    template_name = 'take_turns/doctordifinit.html'
    form_class = forms.DoctorForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            doctor = models.Doctor(name=cd['name'])
            doctor.save()
            name = cd['name']
            messages.success(request, f' دکتر{name} ذخیره شد', 'success')
            return redirect('take_turns:doctordifinit')
        else:
            messages.success(request, 'can not save doctor', 'warning')
            return redirect('take_turns:doctordifinit')


class GetDoctorApi(ListCreateAPIView):
    queryset = models.Doctor.objects.all()
    serializer_class = DoctorSerializer


class PresenceDoctor(View):
    template_name = 'take_turns/presencedoctor.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        doctor = request.POST.get('doctor')
        datetime_persian = request.POST.get('date')
        from_hour = request.POST.get('from_hour')
        to_hour = request.POST.get('to_hour')
        interval_sick = request.POST.get('interval_sick')
        instance_doctor = get_object_or_404(models.Doctor, id=doctor)
        models.Presence.objects.create(
            doctor=instance_doctor,
            datetime_persian=datetime_persian,
            from_hour=from_hour,
            to_hour=to_hour,
            interval_sick=interval_sick
        )
        return JsonResponse({"status": 'Success'})


class GetDoctorDateApi(ListCreateAPIView):
    serializer_class = PresenceSerializer

    def get_queryset(self):
        return models.Presence.objects.filter(datetime_persian=self.request.GET["date"])


class Visit(View):
    template_name = 'take_turns/visit.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        doctor = request.POST.get('doctor')
        datetime_persian = request.POST.get('date')
        hour = request.POST.get('hour')
        user = request.POST.get('serial')
        instance_doctor = get_object_or_404(models.Doctor, id=doctor)
        instance_user = get_object_or_404(User, serial=user)
        models.Visit.objects.create(
            doctor=instance_doctor,
            datetime_persian=datetime_persian,
            hour=hour,
            user=instance_user
        )
        return JsonResponse({"status": 'Success'})
