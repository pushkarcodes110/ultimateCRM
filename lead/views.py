from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lead
from client.models import Client
from teams.models import Team

from .forms import AddLeadForm

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
    context ={'leads': leads}

    return render(request, 'lead/leads_list.html', context)

@login_required
def lead_delete(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)
    lead.delete()
    messages.success(request, "The Lead was Deleted")
    return redirect('leads_list')

# Create your views here.
@login_required
def leads_details(request, pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)

    context ={'lead': lead}
    return render (request,'lead/leads_detail.html', context)

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes are Saved")
            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
        
    context = {'form': form}
    return render(request, 'lead/edit_lead.html', context)


@login_required
def add_lead(request):
    if request.method=='POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            team=Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team=team
            lead.save()

            messages.success(request, "The Lead was Created")

            return redirect('leads_list')
    else:
        form = AddLeadForm()

    context ={'form': form}
    return render (request,'lead/add_lead.html', context)

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team=Team.objects.filter(created_by=request.user)[0]
    

    client=Client.objects.create(
        name=lead.name,
        email =lead.email,
        description=lead.description, 
        created_by = request.user,
        team=team,
    )
    lead.converted_to_client = True 
    lead.save()
    messages.success(request, "The Lead was Converted to Client! ")
    return redirect('leads_list')