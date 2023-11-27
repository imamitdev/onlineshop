from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = (
        Product.objects.all()
        .filter(is_available=True)
        .order_by("created_date")
    )
    
    product_reviews = []  # Create an empty list to store reviews for each product

    for product in products:
        reviews = ReviewRating.objects.filter(
            product_id=product.id,
            status=True,
        )
        product_reviews.append(reviews)  # Append reviews to the list

    context = {
        "products": products,
        "product_reviews": product_reviews,  # Pass the list of reviews to the context
    }
    return render(request, "home.html", context)
