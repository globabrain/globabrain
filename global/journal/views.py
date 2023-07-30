from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, FileResponse
from django.template.response import TemplateResponse
from journal.models import Journal

def published_journals(request):
    # display only published journal and display from old to latest
    published_journals = Journal.objects.filter(status=1).order_by('-created_on')
    return render(request, 'journal/published_journals.html', {'published_journals': published_journals})



def view_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if not journal.journal_file:
        raise Http404("Journal not found")

    # Check the user agent to determine how to handle the PDF
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        # If the user is on mobile, download the PDF
        response = FileResponse(journal.journal_file.open(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{journal.journal_file.name}"'
    else:
        # If the user is not on mobile, view the PDF in the browser
        response = FileResponse(journal.journal_file.open(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline'

    return response


# def view_journal(request, pk):
#     journal = get_object_or_404(Journal, pk=pk)

#     if not journal.journal_file:
#         raise Http404("Journal not found")

#     # Check if the request's user-agent is a mobile device
#     is_mobile = request.user_agent.is_mobile

#     if is_mobile:
#         # If it's a mobile device, download the PDF directly
#         response = FileResponse(journal.journal_file.open(), content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{journal.title}.pdf"'
#         return response
#     else:
#         # If it's not a mobile device, render the view_journal template
#         return TemplateResponse(request, 'journal/view_journal.html', {'journal': journal})

# def view_journal(request, pk):
#     journal = get_object_or_404(Journal, pk=pk)

#     if not journal.journal_file:
#         raise Http404("Journal not found")
#     response = FileResponse(journal.journal_file.open(), content_type='application/pdf')
#     return response



# def download_journal(request, pk):
#     journal = get_object_or_404(Journal, pk=pk)
#     response = FileResponse(journal.journal_file.open(), content_type='application/pdf')
#     return response

