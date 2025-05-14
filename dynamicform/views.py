from django.shortcuts import render, redirect
from .models import Submission

def form_view(request):
    if request.method == 'POST':
        data = {k: v for k, v in request.POST.items() if k.startswith('name')}
        Submission.objects.create(data=data)
        return redirect('results')
    return render(request, 'dynamicform/form.html')

def results_view(request):
    subs = Submission.objects.order_by('-created_at')
    return render(request, 'dynamicform/results.html', {'subs': subs})
