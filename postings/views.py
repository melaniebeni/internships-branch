from django.shortcuts import render
from .models import Internship
from .forms import InternshipForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    context = {}
    return render(request, 'postings/home.html', context)


def posts(request):
    internships = Internship.objects
    # context = {
    #   'internshps': internships
    # }
    return render(request, 'postings/posts.html', {'internships': internships})


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

      
      internshipname = request.POST['internship_name']
      employername = request.POST['company_name']
      link = request.POST['link']
      description = request.POST['description']
      new_post = Internship(internship_name=internshipname, employer_name=employername, link=link, description=description)
      
      new_post.save()

      
      return render(request, 'postings/create.html', context)
  else:
    form = InternshipForm()
    context = {
      'internshipform': form
    }
    return render(request, 'postings/create.html', context)