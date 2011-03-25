from django.template import Library, Node
from contact_form.views import contact_form as contact_form_view 
from contact_form.forms import ContactForm

register = Library()

@register.inclusion_tag('contact_form/contact_form_tag.html',takes_context=True)
def contact_form(context):
	form = ContactForm(request=context['request'])
	return {'form': form, 'context': context }
