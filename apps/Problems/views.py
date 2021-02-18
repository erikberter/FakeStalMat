from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Problem



class DetailProblem(DetailView):
    model = Problem
    template_name = "problems/detail.html"

class CreateProblem(CreateView):
    model = Problem
    fields = ['title', 'statement'] 
    template_name = "problems/create.html"

class ProblemListView(ListView):
    context_object_name = "problems"
    model = Problem
    paginate_by = 100  
    template_name = "problems/list.html"


from django_tex.shortcuts import render_to_pdf

def createPDF(request):
    template_name = 'template.tex'
    problems = Problem.objects.all()
    code = ""
    for i in problems:
        code += i.get_latex()

    context = {'foo': 'Bar', 'problems':code}
    return render_to_pdf(request, template_name, context, filename='test.pdf')
