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

def detail(request, pk):
    # 특정 글을 가져온다.
    review = Review.objects.get(pk=pk)
    # template에 객체 전달
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)

def update(request, pk):
    # GET : Form을 제공
    review = Review.objects.get(pk=pk)
    # review_form = ReviewForm(instance=review)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            review_form.save()
            return redirect("reviews:detail", review.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/update.html", context)