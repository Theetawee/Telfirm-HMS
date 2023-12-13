from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def index(request):
    title = "Telfirm Hospital Management System."
    description = "Transform healthcare administration with Telfirm Hospital Management System. Streamline patient care and optimize operations."
    if request.user.is_authenticated:
        return redirect('dashboard')
    context = {"title": title, "description": description}
    return render(request, "externals/index.html", context)


def about(request):
    return render(request, "externals/about.html")


def support(request):
    title = "Request for Telfirm Demo - Get in Touch with Us"
    description = "Experience the power of Telfirm firsthand. Request a demo today."
    context = {
        "title": title,
        "description": description,
        
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
