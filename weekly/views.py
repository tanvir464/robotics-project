from django.shortcuts import render

def weekly(request):
    return render(request, 'weekly/weekly.html')