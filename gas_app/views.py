from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Order, ContactMessage

# --- HOME PAGE (English Message) ---
def home(request):
    if request.method == 'POST' and 'contact_submit' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg_text = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, message=msg_text)
        
        # English Message (Updated)
        messages.success(request, "Message sent! Our team will contact you soon.")
        
        return redirect('home')
        
    return render(request, 'gas_app/home.html')

# --- REGISTER VIEW ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Registration par bhi message hata diya agar apko nahi chahiye to
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# --- LOGIN VIEW ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            # Error message rehne diya hai taake user ko pata chale password ghalat hai
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# --- LOGOUT VIEW (Message Removed) ---
def logout_view(request):
    logout(request)
    # Yahan se message hata diya hai
    return redirect('home')

# --- BOOKING VIEW ---
@login_required
def book(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        area = request.POST.get('area', '')
        raw_address = request.POST.get('address', '')
        cylinder_type = request.POST.get('cylinder_type', 'Standard')
        qty = request.POST.get('quantity', '1')

        if raw_address and area: final_address = f"{raw_address}, {area}"
        elif raw_address: final_address = raw_address
        elif area: final_address = f"House No missing, Area: {area}"
        else: final_address = "Address Not Provided"

        new_order = Order(
            user=request.user, receiver_name=name if name else request.user.username,
            phone=phone, address=final_address, cylinder_type=cylinder_type,
            quantity=qty, status='Pending'
        )
        new_order.save()
        messages.success(request, "Order placed successfully!")
        return redirect('dashboard')

    return render(request, 'gas_app/book.html')

# --- DASHBOARD VIEW ---
@login_required
def dashboard(request):
    if request.user.is_superuser:
        all_orders = Order.objects.all().order_by('-created_at')
        contact_msgs = ContactMessage.objects.all().order_by('-created_at')
        context = {'orders': all_orders, 'contact_messages': contact_msgs}
        return render(request, 'gas_app/admin_dashboard.html', context)
    else:
        user_orders = Order.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'gas_app/dashboard.html', {'orders': user_orders})

# --- UPDATE STATUS VIEW ---
@login_required
def update_order_status(request, order_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
            messages.success(request, f"Status updated to {new_status}.")
    return redirect('dashboard')