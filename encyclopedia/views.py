from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from django.urls import reverse

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
        title=title.lower()
        entry=entry.lower()
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


def create(request):
    return render(request, "encyclopedia/new.html") 


def save(request):
    title=request.POST["q1"]
    text=request.POST["q2"]
    if util.get_entry(title):
        messages.error(request, 'Page with this title already exists!')
        return render(request, "encyclopedia/new.html")
    else:
        util.save_entry(title,text)
        return redirect('page',title=title)
        # HttpResponseRedirect(reverse('page'), title=title)


def edit(request,title):
    return render(request, "encyclopedia/edit.html",{
        "title":title.capitalize(),
        "content":util.get_entry(title)
        })


def edited(request,title):
    title=title.capitalize()
    content=request.POST["q4"]
    util.save_entry(title,content)
    return redirect('page',title=title)
    # HttpResponseRedirect(reverse('page'), title=title)




    

        

