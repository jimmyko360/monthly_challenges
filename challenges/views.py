from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}


def challenge_by_month_by_number(request, month_number):
    try:
        month_text = list(monthly_challenges.keys())[month_number - 1]
        redirect_path = reverse("challenge_of_the_month", args=[month_text])
        return HttpResponseRedirect(redirect_path)
    except:
        # HttpResponseNotFound should return an HTML template, either an inline one like this, or by referencing a template file like is done in challenge_by_month below
        return HttpResponseNotFound("<h1>Invalid month</h1>")


def challenge_by_month(request, month):
    try:
        challenge = monthly_challenges[month]

        # returning this inline HTML is not the best pattern
        # challenge_text = f"<h1>{month}</h1><br><h3>{challenge}</h3>"
        # return HttpResponse(challenge_text)

        # a good alternative but still not the most popular pattern
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        # the Django best practice
        return render(request, "challenges/challenge.html", {"month_name": month, "challenge_name": challenge})
    except:
        # response = render_to_string("404.html")
        # return HttpResponseNotFound(response)
        raise Http404()
        # remember, Http404 does nothing because DEBUG=True and cannot be False in a local environment


def index(request):
    all_months = ""

    # for each month from 0 to 12
    # month_link = "<p href=""> name of month</p>"
    # all_months = all_months + month_link

    months = monthly_challenges.keys()

    # we move this for loop into the template and delegate the iterating work to it using a tag
    # for x in months:
    #     month_link = reverse("challenge_of_the_month", args=[x])
    #     month_li = f"<li><a href={month_link}>{x}</a><br></li>"

    #     # Max defines this href with escaped quotations for some reason
    #     # e.g. f"href=\'{month_link}\'"
    #     # it works without them though
    #     # shouldn't it be fine since month_link is a string anyways?

    #     all_months = all_months + month_li

    # month_list = f"<h1>All Challenges</h1><br><ul>{all_months}</ul>"

    # return HttpResponse(month_list)

    # month_link = reverse("challenge_of_the_month", args=[x])
    return render(request, "challenges/index.html", {"months": months})
