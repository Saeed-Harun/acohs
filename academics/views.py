from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Result

@login_required
def my_results(request):
    if request.user.role != 'student':
        return render(request, 'academics/no_access.html')

    results = Result.objects.filter(student=request.user)

    total_credits = 0
    total_points = 0

    for r in results:
        total_credits += r.course.credit
        total_points += r.course.credit * r.gpa_point()

    if total_credits > 0:
        gpa = round(total_points / total_credits, 2)
    else:
        gpa = 0.00

    return render(request, 'academics/my_results.html', {
        'results': results,
        'gpa': gpa
    })

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def result_pdf(request):
    if request.user.role != 'student':
        return render(request, 'academics/no_access.html')

    results = Result.objects.filter(student=request.user)
    total_credits = 0
    total_points = 0

    for r in results:
        total_credits += r.course.credit
        total_points += r.course.credit * r.gpa_point()

    gpa = round(total_points / total_credits, 2) if total_credits > 0 else 0.00

    template = get_template('academics/pdf_result.html')
    html = template.render({'user': request.user, 'results': results, 'gpa': gpa})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result-slip.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    return response
