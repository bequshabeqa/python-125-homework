from django.shortcuts import get_object_or_404, render  # type: ignore[import]
from core.models import Actors

def home_view(request):
    return render(
        request, 
        'base.html',
        {
            'actors': Actors.objects.all()
        }   
    )


def actor_view(request, pk):
    return render(
        request, 
        'actor_detail.html',
        {
            "pk": pk,
            "actor": get_object_or_404(Actors, pk=pk)
        }
    )