from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Team 

# Create your views here.
@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)

    context={'team: team'}
    return render(request, 'team/edit_team.html', context)
