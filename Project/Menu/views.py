from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'Menu/somepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context