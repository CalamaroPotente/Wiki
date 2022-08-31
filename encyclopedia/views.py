from django.shortcuts import render
from . import util
import markdown2
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import logging

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, name):
    if name not in util.list_entries():
        raise Http404('The entry does not exist')
    else:
        return render(request, "encyclopedia/entry.html", {
           "name": name,
           "html": markdown2.markdown_path(f"entries/{name}.md")
        })

def search(request):
    listOfpossibleEntries = []
    count = 0
    if request.method == 'POST':
        entry_search = request.POST.getlist('q')
        entry_search = f"{entry_search}"[2:][:-2]
    for entry in util.list_entries():
        if entry_search == entry:
            return HttpResponseRedirect(reverse("name", kwargs={"name": entry}))
        elif entry_search in entry:
            listOfpossibleEntries.append(entry)
            count = 1
    if count < 1:
        raise Http404("Entry does not exist")
    return render(request, "encyclopedia/possible_entries.html", {
    "entries": listOfpossibleEntries
    })
    
def create_entry(request):
    if request.method == 'POST':
        title = f"{request.POST.getlist('title')}"[2:][:-2]
        content = f"{request.POST.getlist('markdown')}"[2:][:-2]
        content = content.replace('\\r','\r').replace('\\n', '\n')
        if title in util.list_entries():
            raise Http404('This entry title already exists')
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("name", kwargs={"name": title}))
    return render(request, "encyclopedia/createentry.html")
    
   