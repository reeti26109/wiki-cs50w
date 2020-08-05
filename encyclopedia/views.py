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

def search(request):
    title= request.POST["q"]
    entries= util.list_entries()
    flag=0
    new=[]
    for entry in entries:

        if (title == entry):
            flag=1
            Entry=util.get_entry(title)
            Entry= markdown2.markdown(Entry)

            context={
                "entry": Entry,
                "title": title
            }
            return render(request, "encyclopedia/page.html",context)
    if(flag==0):
        for entry in entries:
            s1=title.lower()
            s2=entry.lower()
            if(s2.find(s1)!=-1):
                new.append(entry)
        if len(new)==0:
            return render(request,"encyclopedia/error.html")
        else:
            return render(request, "encyclopedia/search.html", {
            "entries": new
            })    
        

