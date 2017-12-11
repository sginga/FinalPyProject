from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import QuoteForm


# Create your views here.
class LandingView(TemplateView):

    template_name = "home/landing.html"

class SuccessView(TemplateView):

    template_name = "home/success.html"

class QuoteView(FormView):

    template_name = "home/quote.html"
    form_class = QuoteForm
    success_url = "/success"

    def form_valid(self, form):
        #called when form data has been posted
        #returns an HttpResponse
        form.send_email()
        return super(QuoteView, self).form_valid(form)
