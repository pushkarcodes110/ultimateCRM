from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Team 
from .forms import TeamForm

# Create your views here.
@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)

    if request.method=='POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()

            messages.success(request, 'The changes were saved!' )
            return redirect('account')
    else:
        form = TeamForm(instance=team)

    context={'team':team, 'form': form}
    return render(request, 'teams/edit_team.html', context)
