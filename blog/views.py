from django.shortcuts import render, redirect, get_object_or_404

from .models import QuillPost
from .forms import QuillPostForm

def model_form_view(request):
    if request.method == 'POST':
        form = QuillPostForm(request.POST)
        if form.is_valid():
            quillpost = form.save()
            return redirect('detail', quillpost_id=quillpost.id)

    else:
        form = QuillPostForm()
    return render(request, 'content/create_post.html', {'form': form})


def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    quill_content_html = quillpost.content.html
    return render(request, 'content/detail.html', {'quill_content_html': quill_content_html})


# def quillpost_detail(request, quillpost_id):
#     quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    
#     # Obtener el contenido HTML del campo Quill
#     quill_content_html = quillpost.content.html
    
#     # Analizar el contenido HTML usando BeautifulSoup
#     # soup = BeautifulSoup(quill_content_html, 'html.parser')
    
#     # Obtener todos los bloques de código
#     # code_blocks = soup.find_all('pre')
    
#     # # Procesar cada bloque de código
#     # for block in code_blocks:
#     #     # Obtener el lenguaje del bloque de código
#     #     language_class = block.get('class')
        
#     #     # Si hay una clase de lenguaje, agregamos 'language-*' a la lista de clases
#     #     if language_class:
#     #         language = language_class[0].split('-')[-1]
#     #         block['class'] = [f'language-{language}']
    
#     # # Obtener el contenido HTML modificado
#     # quill_content_html = str(soup)
    
#     return render(request, 'content/detail.html', {'quillpost': quillpost, 'quill_content_html': quill_content_html})

# # def quillpost_detail(request, quillpost_id):
# #     quillpost = get_object_or_404(QuillPost, pk=quillpost_id)
    
# #     # Obtener el contenido HTML del campo Quill
# #     quill_content_html = quillpost.content.html
    
# #     # Analizar el contenido HTML usando BeautifulSoup
# #     soup = BeautifulSoup(quill_content_html, 'html.parser')
    
# #     # Agregar clases de lenguaje a los bloques de código
# #     code_blocks = soup.find_all('pre')
# #     for block in code_blocks:
# #         block['class'] = 'language-python'  # Reemplaza 'language-html' con el lenguaje real del bloque de código si es necesario
    
# #     # Obtener el contenido HTML modificado
# #     quill_content_html = str(soup)
    
# #     return render(request, 'content/detail.html', {'quillpost': quillpost, 'quill_content_html': quill_content_html})




# # def form_view(request):
# #     if request.method == 'POST':
# #         # Si la solicitud es un POST, procesar los datos del formulario
# #         form = QuillFieldForm(request.POST)
# #         if form.is_valid():
# #             # Si el formulario es válido, obtener los datos del formulario
# #             content = form.cleaned_data['content']

# #             # Aquí puedes guardar los datos en la base de datos si lo deseas
# #             # Por ejemplo, si tienes un modelo llamado Post:
# #             post = QuillPost(content=content)
# #             post.save()

# #             # Redirigir a una URL de éxito después de procesar los datos
# #             return redirect('detail')
# #     else:
# #         # Si la solicitud no es un POST, renderizar el formulario vacío
# #         form = QuillFieldForm()
# #     return render(request, 'content/create_post.html', {'form': form})












# def form_view(request):
#     if request.method == 'POST':
#         # Si la solicitud es un POST, procesar los datos del formulario
#         form = QuillFieldForm(request.POST)
#         if form.is_valid():
#             # Si el formulario es válido, guardar los datos en la base de datos
#             form.save()
#             # Redirigir a una URL de éxito después de guardar los datos
#             return redirect('content/detail.html')
#     else:
#         # Si la solicitud no es un POST, renderizar el formulario vacío
#         form = QuillFieldForm()
#     return render(request, 'content/create_post.html', {'form': form})

# def detail(request):
#     return render(request, 'content/detail.html')












# from django.shortcuts import render
# from .forms import QuillFieldForm

# # Create your views here.

# def form_view(request):
#     return render(request, 'content/create_post.html', {'form': QuillFieldForm()})