from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class BaseTemplatePerModuleMixin():
    """
    TEMPLATE_DIR is template directory.
    template_filename is template html file.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verify()

    def verify(self):
        if not hasattr(self, 'TEMPLATE_DIR'):
            raise ImproperlyConfigured('To subclass this class, TEMPLATE_DIR needed to be set.')
        if not hasattr(self, 'template_filename'):
            raise ImproperlyConfigured('To subclass this class, template_filename needed to be set.')

    def get_template_names(self):
        """
        Dynamically returns the full template path.
        """
        if self.template_filename:
            return [f'{self.TEMPLATE_DIR}/{self.template_filename}']
        
        # Fallback to the default Django template name convention
        # (e.g., myapp/project_list.html)
        return super().get_template_names()
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response  
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({"active": self.TEMPLATE_DIR})
        return kwargs

    

class LandingView(BaseTemplatePerModuleMixin, TemplateView):
    TEMPLATE_DIR = 'base'
    template_filename = 'home.html'
