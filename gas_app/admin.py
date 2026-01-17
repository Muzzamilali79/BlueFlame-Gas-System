from django.contrib import admin
from .models import Order

# Order model ko Admin Panel par register kar rahe hain
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Admin list mein ye columns nazar ayenge
    list_display = ('id', 'receiver_name', 'cylinder_type', 'quantity', 'status', 'created_at')
    
    # In cheezon se filter kar sakenge
    list_filter = ('status', 'cylinder_type')
    
    # In cheezon se search kar sakenge
    search_fields = ('receiver_name', 'phone', 'address')