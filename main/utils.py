from django.shortcuts import render
from django.http import HttpResponse
import os
from django.template import loader
from pathlib import Path
from django.views.generic import View
import hashlib


def offline(request):
    return render(request, "base/offline.html")


class RobotsTxtView(View):
    def get(self, request):
        template = loader.get_template("base/robots.txt")
        content = template.render()
        return HttpResponse(content, content_type="text/plain; charset=utf-8")


def sitemap(request):
    return render(request, "base/sitemap.xml")


def custom_404_view(request, exception):
    return render(request, "base/error.html", status=404)


def custom_500_view(request):
    return render(request, "base/505.html", status=500)


def service_worker(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR, "templates", "base", "sw.js")
    response = HttpResponse(open(path).read(), content_type="application/javascript")
    return response


def manifest(request):
    return render(request, "base/manifest.json", content_type="application/json")




def generate_sku_from_name(name):
    # Hash the name using MD5 (you can choose a different hashing algorithm)
    hashed_name = hashlib.md5(name.encode()).hexdigest()

    # Take the first 8 characters of the hash as the SKU
    sku = hashed_name[:8].upper()

    return sku

# original_sku = 'telfirm-v1.1' 
