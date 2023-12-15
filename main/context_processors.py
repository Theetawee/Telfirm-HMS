# myapp/context_processors.py
from .models import Notice


def global_data(request):
    nots_num = 0  # Default value

    if request.user.is_authenticated:
        unread_notices = Notice.objects.exclude(read_by=request.user).count()
        nots_num = unread_notices

    return {"nots_num": nots_num}
