from django import template
from django.utils.safestring import mark_safe

register=template.Library()

@register.filter
def redo_class(field,css_class):
    if css_class:
        field.field.widget.attrs['class']=css_class
        
    return field


@register.filter
def redo_holder(field,placeholder):
    if placeholder:
        field.field.widget.attrs['placeholder']=placeholder
        
    return field

@register.filter
def is_input(field):
    field.field.widget.attrs['class']="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500"
    
 
 
 
    
@register.simple_tag
def seo_tags(meta_title, meta_description, follow='follow'):
    # Escape any HTML in the meta_title and meta_description
    meta_title = meta_title.strip()
    meta_description = meta_description.strip()
    
    # Define a dictionary to map follow values to robots meta tag content
    robot_tags = {
        'follow': 'index, follow, max-snippet:-1, max-video-preview:-1',
        'nofollow': 'noindex, nofollow',
    }
    
    # Use the dictionary to get the appropriate robot tag content
    robot_content = robot_tags.get(follow, robot_tags['follow'])
    
    html = f'<title>{meta_title}</title><meta name="description" content="{meta_description}">'
    html += f'<meta name="robots" content="{robot_content}" />'
    
    return mark_safe(html)


@register.simple_tag
def twitter_card(title, description, image_url):
    title = title.strip()
    description = description.strip()
    image_url = image_url.strip()

    html = f'<meta name="twitter:card" content="summary" />' \
           f'<meta name="twitter:title" content="{title}" />' \
           f'<meta name="twitter:description" content="{description}" />' \
           f'<meta name="twitter:image" content="{image_url}" />' \
           '<meta name="twitter:image:alt" content="Image Alt Text" />'\
            '<meta name="twitter:site" content="@redodevs" />'
   

    return mark_safe(html)


@register.simple_tag
def og_tags(title, description, image_url, og_type='website'):
    title = title.strip()
    description = description.strip()
    image_url = image_url.strip()


    html = f'<meta property="og:title" content="{title}" />' \
           f'<meta property="og:description" content="{description}" />' \
           f'<meta property="og:image" content="{image_url}" />' \
           f'<meta property="og:type" content="{og_type}" />' \

    return mark_safe(html)