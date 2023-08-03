from django.contrib import admin
from .models import Order, Payment, OrderProduct


# Register your models here.
class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = (
        "payment",
        "user",
        "product",
        "quantity",
        "product_price",
        "is_ordered",
    )
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "payment",
        "order_number",
        "first_name",
        "last_name",
        "order_total",
        "status",
    )
    list_filter = ["status", "is_ordered"]
    search_fields = [
        "order_number",
        "first_name",
        "last_name",
        "phone",
        "email",
    ]
    inlines = [OrderProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
