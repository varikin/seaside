from django.template import Library, Node, TemplateSyntaxError
from seaside.pages.models import NavItem

register = Library()

@register.tag(name='get_menu_nav_items')
def do_get_menu_nav_items(parser, token):
    return get_nav_items(token, True)

@register.tag(name='get_nav_items')
def do_get_nav_items(parser, token):
    return get_nav_items(token, False)
    
def get_nav_items(token, is_menu):
    tokens = token.contents.split()
    if len(tokens) != 3:
        raise TemplateSyntaxError('Incorrect format, got %r' % tokens)
    return NavItemNode(tokens[2], is_menu)

class NavItemNode(Node):
    def __init__(self, var, is_menu):
        self.var = var
        self.is_menu = is_menu

    def render(self, context):
        context[self.var] = NavItem.objects.filter(is_menu=self.is_menu)
        return u''
    