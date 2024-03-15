from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import AddClientForm

# Create your views here.
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    context={
        'clients': clients
    }

    return render (request, 'client/client_list.html', context)

@login_required
def client_delete(request,pk):
    client = get_object_or_404(Client,created_by=request.user,pk=pk)
    client.delete()
    messages.success(request, "The client was Deleted")
    return redirect('clients_list')

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes are Saved")
            return redirect('clients_list')
    else:
        form = AddClientForm(instance=client)
        
    context = {'form': form}
    return render(request, 'client/edit_client.html', context)


@login_required
def clients_detail(request,pk):
    client= get_object_or_404(Client, created_by=request.user, pk=pk)

    context={
        'client': client
    }

    return render (request, 'client/client_detail.html', context)

@login_required
def clients_add(request):
    if request.method=='POST':
        form = AddClientForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            messages.success(request, "The Client was Created")

            return redirect('clients_list')
    else:
        form = AddClientForm()

    context ={'form': form}
    return render (request,'client/clients_add.html', context)
