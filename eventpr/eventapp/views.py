from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking
from .forms import BookingForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def events(request):
    return render(request, 'events.html', {'eve': Event.objects.all()})


@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_obj = form.save()
            return redirect('booking_success', pk=booking_obj.pk)
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def booking_success(request, pk):
    booking_obj = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_success.html', {'booking': booking_obj})


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        return render(request, 'contact.html', {'contact_success': True})
    return render(request, 'contact.html')
