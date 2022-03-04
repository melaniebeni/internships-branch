from django.shortcuts import render
from .forms import InternshipForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    context = {}
    return render(request, 'postings/home.html', context)


def posts(request):
    context = {}
    return render(request, 'postings/posts.html', context)


@csrf_exempt
def create(request):

  if request.method == 'POST':
    filled_form = InternshipForm(request.POST)
    if filled_form.is_valid():
      note = 'Thanks! Your Post Has Been Saved'
      new_form = InternshipForm()
      context = {
        'internshipform': new_form,
        'note': note,
      }
      return render(request, 'postings/create.html', context)
  else:
    form = InternshipForm()
    context = {
      'internshipform': form
    }
    return render(request, 'postings/create.html', context)