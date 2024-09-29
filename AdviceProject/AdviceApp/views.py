from django.shortcuts import render
from .models import Advice
from django.utils import timezone
import requests

# Create your views here.
def advice(request):
    response = requests.get("https://api.adviceslip.com/advice")
    advice = response.json()["slip"]
    newAdvice = Advice(advice=advice["advice"])
    newAdvice.save()

    advices = Advice.objects.order_by("-id").all()[:12:1]
    return render(request, "advice.html", {"advice": advice["advice"], "history":advices})