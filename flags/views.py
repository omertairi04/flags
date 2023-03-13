from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
import random

from .models import Flag , Score

def selectingGame(request):
    # Get a random flag from the database
    flag = Flag.objects.order_by('?').first()

    # Redirect the user to the "play" view for the selected flag
    return redirect('play', pk=flag.pk)

def index(request , pk):
    # Get the flag corresponding to the given primary key
    flag = Flag.objects.get(pk=pk)

    # Retrieve the current session
    session = Session.objects.get(session_key=request.session.session_key)

    # Retrieve the score object for the current session, creating it if it doesn't exist
    score, created = Score.objects.get_or_create(session=session)

    # Initialize the guessed flag to False
    guessed = False

    # If the user submitted a guess, check if it is correct and update the score accordingly
    if request.method == 'POST':
        flag_guess = request.POST.get('flag_guess')
        if flag_guess.lower() == flag.name.lower():
            guessed = True
            score.score += 1
            score.save()
            messages.success(request, 'Bravo!')
            return redirect('selecting')
        else:
            guessed = False
            score.score = 0
            score.save()
            messages.error(request, 'Try again!')

    # Pass the flag, guessed flag, and score to the template
    context = {
        'flag': flag,
        'guessed': guessed,
        'score': score.score,
    }

    return render(request , 'index.html' , context)
