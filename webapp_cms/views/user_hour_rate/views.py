from webapp import models
from django.views.generic import View
from django.shortcuts import render, redirect
from webapp_cms.forms import UserRateForm


class UserRate(View):
    def get(self, request, *args, **kwargs):
        user_rate_form = UserRateForm()
        user_rate = models.UserHourlyRate.objects.all()
        return render(request, 'User_Hourly_Rate/UserHourlyRate.html', {'user_rate':user_rate, 'user_rate_form':user_rate_form})

    def post(self, request, *args, **kwargs):
        user_rate_form = UserRateForm(request.POST)
        print(user_rate_form.as_p())
        print(user_rate_form.data)
        user_rate = models.UserHourlyRate.objects.all()
        if user_rate_form.is_valid():
            user_rate_form.save()
            return redirect("user_rate")
        else:
            print('Not valid')
            print(user_rate_form.data)
        return render(request, 'User_Hourly_Rate/UserHourlyRate.html', {'user_rate':user_rate, 'user_rate_form':user_rate_form })

