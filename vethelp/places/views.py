from pydoc import cli
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CommentForm

from .models import Clinic


def show_info(request):
    return render(request, 'places/info.html')

def get_clinics(request):
    clinics = Clinic.objects.all()
    context = {
        'clinics': clinics
    }
    return render(request, 'places/clinic.html', context)

def get_areas(request):
    return render(request, 'places/area.html')

def get_profile(request, id):
    clinic = get_object_or_404(Clinic, id=id)
    form = CommentForm(request.POST or None)
    context = {
        'clinic': clinic,
        'form': form,
        'comments': clinic.comments.all()
    }
    return render(request, 'places/profile.html', context)

@login_required
def add_comment(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    form = CommentForm(request.POST or None)
    context = {
        'clinic': clinic,
        'form': form,
        'comments': clinic.comments.all(),
    }
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.clinic = clinic
        comment.save()
        return redirect('places:clinic', id=clinic_id)
    return render(request, 'places/profile.html', context)