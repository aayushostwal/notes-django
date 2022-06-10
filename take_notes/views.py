import re
from venv import create
from django.shortcuts import render
from rest_framework.views import APIView
import pandas as pd
from difflib import SequenceMatcher

import nltk
from nltk.translate import bleu
from nltk.translate.bleu_score import SmoothingFunction
smoothie = SmoothingFunction().method4

from take_notes.models import TakeNotes

# Create your views here.

class list_notes(APIView):
    def post(self, request):
        search_string = request.data.get("search_string", "")
        # df = pd.DataFrame(list(TakeNotes.objects.all().values()))
        # # df['MatchScore'] = df['title'].apply(lambda x: bleu([x], search_string, smoothing_function=smoothie))
        # df['MatchScore'] = df['title'].apply(lambda x: SequenceMatcher(None, search_string, x).ratio())
        # df.sort_values(by=['MatchScore'], ascending=True)
        # results = df.head(10)['id'].values
        
        # database = TakeNotes.objects.filter(id__in=results)
        # objects = dict([(obj.id , obj) for obj in database])
        # sorted_odjects = [objects[id] for id in results]
        sorted_odjects = TakeNotes.objects.all().filter(title__icontains=search_string).order_by('id')
        print(search_string, sorted_odjects)
        context = {
            'database': sorted_odjects
        }
        return render(request, 'search_results.html', context)
    def get(self, request):
        database = TakeNotes.objects.all()
        context = {
            'database': database
        }
        return render(request, 'list_notes.html', context)

class initiate_new_note(APIView):
    def post(self, request):
        title = request.POST.get("title", "")
        body = request.POST.get("body", "")
        context = {
            'title': title,
            'body': body
        }
        entry = TakeNotes(title=title, body=body)
        entry.save()
        return render(request, 'note_saved.html', context)
    def get(self, request):
        return render(request, 'new_note.html')

def view_note(request, id):
    specific_note = TakeNotes.objects.get(id=id)
    title = specific_note.title
    body = specific_note.body
    create_time = specific_note.date_time
    context = {
        'title': title,
        "create_time" : create_time,
        "body" : body,
        "id":id
    }
    return render(request, 'view_note.html', context)

def delete_note(request, id):
    TakeNotes.objects.filter(id=id).delete()
    return render(request, 'delete_note.html')
    
# def get_search_results(request, search_string):
#     df = pd.DataFrame(list(TakeNotes.objects.all().vlaues()))
#     df['MatchScore'] = df['title'].apply(lambda x: bleu([x], search_string, smoothing_function=smoothie))
#     df.sort_values(by=['MatchScore'], ascending=False)
#     results = df.head(10)

#     context = {
#         'database': results
#     }
#     return render(request, 'search_results.html', context)


    

    