from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from segregator.models import Entity

def index(request):
    all_entities = Entity.objects.all()
    objects = {obj.title:(obj.parent.title if obj.parent else None) for obj in all_entities}
    
    return render(request, 'tree/index.html', context={"objects":objects, "nodes":all_entities})


def info(request, pk):
    node = Entity.objects.filter(pk=pk).first()
    files_list = node.entities.all()
    return render(request, "tree/info.html", context={
        "title":node.title,
        "description": node.body,
        "files_list": files_list
    })