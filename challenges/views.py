from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "gym",
    "february": "tan",
    "march": "laundry",
    "april": "gym",
    "may": "tan",
    "june": "laundry",
    "july": "gym",
    "august": "tan",
    "september": "laundry",
    "october": "gym",
    "november": "tan",
    "december": "laundry"
}


def challenge_by_month(request, month):
    try:
        monthly_challenges[month]
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This page is located in a different castle.")
