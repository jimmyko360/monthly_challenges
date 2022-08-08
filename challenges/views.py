from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def challenge_by_month_by_number(request, month_number):
    try:
        month_text = list(monthly_challenges.keys())[month_number - 1]
        return HttpResponseRedirect(month_text)
    except:
        return HttpResponseNotFound("Invalid month")


def challenge_by_month(request, month):
    try:
        monthly_challenges[month]
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This page is located in a different castle.")
