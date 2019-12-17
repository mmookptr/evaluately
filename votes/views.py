from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import *


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Criteria.objects.order_by('-pub_date')[:30]

class FinalView(generic.ListView):
    template_name = 'polls/final_results.html'
    context_object_name = 'criterian'

    def get_queryset(self):
        """Return the last five published questions."""
        return Criteria.objects.order_by('-pub_date')[:30]

class DetailView(generic.DetailView):
    model = Criteria
    template_name = 'polls/detail.html'
    context_object_name = 'criteria'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Criteria.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Criteria
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Criteria, pk=question_id)
    try:
        selected_choice = question.entrant_set.get(pk=request.POST['choice'])
    except (KeyError, Entrant.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Criteria.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
