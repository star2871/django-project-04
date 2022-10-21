from django.shortcuts import render, redirect
from .forms import ReviewForm
from reviews.models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.order_by("-pk")
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # Article.objects.create(title=title, content=content)
    # return redirect("articles:index")
    if request.method == "POST":
        # DB에 저장하는 로직
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:create")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/new.html", context=context)
