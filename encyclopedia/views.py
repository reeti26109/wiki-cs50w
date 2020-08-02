from django.shortcuts import render

from . import util

import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entry=util.get_entry(title)

    if(entry is not None):
        entry= markdown2.markdown(entry)

        context={
            "entry": entry,
            "title": title
        }

        return render(request, "encyclopedia/page.html", context)

    else:
        return render(request, "encyclopedia/error.html")

# def search(request):
    
