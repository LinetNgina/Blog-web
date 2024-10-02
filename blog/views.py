from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Post
from django.core.mail import send_mail



def index(request):
    posts = Post.objects.filter()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        location = request.POST.get('location')
        message = request.POST.get('message')

        # Send email
        send_mail(
            'New Message from Contact Form',
            f'Name: {name}\nTelephone: {telephone}\nLocation: {location}\nMessage: {message}',
            'noreply@example.com',
            ['linetngina097@gmail.com'],
            fail_silently=False,
        )

        # Set a flag to display the feedback message
        request.session['message_sent'] = True
        return redirect('success_page')  # Redirect to success_page URL

    # Clear the message_sent flag if the page is accessed directly
    message_sent = request.session.pop('message_sent', False)

    return render(request, 'blog/contact.html', {'message_sent': message_sent})

def success_page(request):
    return render(request, 'blog/success.html')  # Render the success page template
