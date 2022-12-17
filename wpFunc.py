def wp_list(dicts):
    first_line = '<!-- wp:list --><ul>'
    for key,value in dicts.items():
        code = f'<!-- wp:list-item --><li><strong>{key.title()} </strong>: {value.title()}</li><!-- /wp:list-item -->'
        first_line += code
    last_line = '</ul><!-- /wp:list -->'
    first_line += last_line
    return first_line


def slugify(text):
    while '  ' in text:
        text = text.replace('  ',' ')
    code = text.strip().lower().replace(' ','-')
    return code