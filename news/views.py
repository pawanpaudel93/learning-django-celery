from django.views.generic.list import ListView

from news.models import News
from feedback.forms import FeedbackForm


class NewsView(ListView):
    model = News
    template_name = 'news/news_list.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['form'] = FeedbackForm()
        return context
