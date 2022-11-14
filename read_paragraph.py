import re



txt = """La logística Digital es un \n
        concepto que surge de la integración entre la logística tradicional\n
        y la era digital. Con el auge del correo electrónico y las descargas\n
        digitales reemplazando productos físicos, podríamos estar hablando\n
        de un golpe devastador para la industria de la logística, pero,\nd
        e hecho, ha ocurrido algo muy diferente. El sector de la logística ha\n
        introducido las innovaciones digitales."""

def read_paragraph(word='logística', paragraph= txt):
    
    pattern = re.compile(r'\b\{word\}\b)')
    count = len(re.findall(pattern,paragraph))
    print(f'{count} ocurrencias encontradas.')
    return count