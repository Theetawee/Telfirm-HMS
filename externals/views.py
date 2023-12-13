from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, "externals/index.html")


def about(request):
    return render(request, "externals/about.html")


def support(request):
    title = "Contact Redo Developers Inc. - Get in Touch with Us"
    description = "Contact Redo Developers Inc. for any inquiries or assistance. We're here to help."
    og_title = "Get in Touch with Redo Developers Inc."
    image_url = "https://theetawee.github.io/company_staticfiles/images/logo.png"
    og_type = "website"
    context = {
        "title": title,
        "description": description,
        "og_title": og_title,
        "image": image_url,
        "og_type": og_type,
    }

    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        subject = request.POST["subject"]
        user_message = request.POST["message"]
        message = f"Email from: {email}\nName:{name}\n Message: {user_message}"
        try:
            send_mail(
                subject,
                message,
                "redodevs@gmail.com",
                ["redodevs@gmail.com"],
                fail_silently=True,
            )
            messages.success(request, "Your message was successfully received.")
            return redirect("support")
        except:
            messages.error(request, "We ran into an issue please try again")
            return redirect("support")

    return render(request, "externals/support.html", context)
