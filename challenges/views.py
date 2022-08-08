from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        redirect_path = reverse("challenge_of_the_month", args=[month_text])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month")


def challenge_by_month(request, month):
    try:
        challenge = monthly_challenges[month]
        challenge_text = f"<h1>{month}</h1><br><h3>{challenge}</h3>"
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This page is located in a different castle.</h1>")


def get_all_months(request):
    all_months = ""

    # for each month from 0 to 12
    # month_link = "<p href=""> name of month</p>"
    # all_months = all_months + month_link

    months = monthly_challenges.keys()

    for x in months:
        month_link = reverse("challenge_of_the_month", args=[x])
        month_li = f"<li><a href={month_link}>{x}</a><br></li>"
        all_months = all_months + month_li

    month_list = f"<h1>All Challenges</h1><br><ul>{all_months}</ul>"

    return HttpResponse(month_list)
