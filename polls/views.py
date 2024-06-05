from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.shortcuts import get_object_or_404
 # Create your views here.
def index(request):
 """
 Displays the latest polls
 """
 latest_question_list = Question.objects.order_by('-pub_date')[:5]
 context = {'latest_question_list': latest_question_list}
 return render(request, "polls/poll.html", context)

def detail(request, question_id):
 """
 Displays a particular polls details
 """
 question = get_object_or_404(Question, pk=question_id)
 return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
 """
 Displays the result of a particular poll
 """
 question = get_object_or_404(Question, pk=question_id)
 return render(request, 'polls/results.html', {'question': question})



def vote(request, question_id):
 """
 Performs the vote for a poll made by a user.
 """
 question = get_object_or_404(Question, pk=question_id)
 try:
     selected_choice = question.choice_set.get(
     pk=request.POST['choice']
     )
 except (KeyError, Choice.DoesNotExist):
 # Redisplay the question voting form
     return render(request, 'polls/detail.html', {
     'question': question,
     'error_message': "You didn't select a choice."
     })
 else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully
    # dealing with POST data. This prevents data from being
    # posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(
    reverse('polls:results', args=(question_id,))
    )



