from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from lead.models import Lead
from client.models import Client
from teams.models import Team

# Create your views here.
@login_required
def dashboard(request):
    team=Team.objects.filter(created_by=request.user)[0]
    lead= Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients= Client.objects.filter(team=team).order_by('-created_at')[0:5]

    return render(request, 'dashboard/dashboard.html', {
        'lead': lead, 'clients': clients,
    })
 