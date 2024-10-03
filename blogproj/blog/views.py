from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseServerError, HttpResponse
from django.contrib import messages

from .forms import PostForm, CommentForm
from django.shortcuts import render

from .models import Post, Comment  # Import the Comment model
from .forms import PostForm

def home(request):
    print("hello")
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

# Post list
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)  # Show only approved comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = False  # Comment is not approved by default
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def test_view(request):
    print("This is a test view")  # Debug message
    return HttpResponse("This is a test view")  # Returns the response

def post_list(request):
    posts = Post.objects.all()  # Retrieves all posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True)  # Show only approved comments

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = False  # Comment is not approved by default
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# Creating a new post
from django.shortcuts import render, redirect
from .forms import PostForm

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Associate the logged-in user as the post author
            post.save()
            return redirect('post_list')  # Redirect to the post list after saving
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        # Logged in user
        print(f"The user {request.user.username} is logged in.")
    else:
        # Not logged in user
        print("The user is not logged in.")

    return render(request, 'blog/home.html')

# For editing a post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm

@login_required
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)  # Find the post to edit
    if request.user != post.author:  # Check if the user is the post author
        return redirect('post_list')  # If not the author, redirect to the post list
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Pre-fill the form with existing data
        if form.is_valid():
            form.save()  # Save the post changes
            return redirect('post_detail', slug=post.slug)  # Redirect to the updated post
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

# For deleting a post
@login_required
def post_delete(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug)
        if request.user != post.author:
            return redirect('post_list')
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        return render(request, 'blog/post_confirm_delete.html', {'post': post})
    except Exception as e:
        # Log the error or show an error message
        print(f"Error occurred while deleting post: {e}")
        return HttpResponseServerError("An error occurred while trying to delete the post.")

# Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('blog-home')  # Redirect to the homepage or another page after logout
