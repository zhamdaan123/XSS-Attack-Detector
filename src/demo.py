from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse


demo = APIRouter(prefix="/demo", tags=['Demo'], include_in_schema=False)


def get_content(request: Request):
    return request.session.get('content', []) or []


@demo.get('/content')
def show_content(request: Request):
    content = get_content(request)
    page = """
    <h1>Saved Content</h1>
    <a href="/">Go back</a>
    <span style="margin: 0 .5rem;">|</span>
    <a href="/demo/content/clear">Clear Content</a>
    <br>
    """
    for i in content:
        page += i + '<br>'
    return HTMLResponse(content=page)


@demo.post('/content')
def add_content(request: Request, content=Form(...)):
    saved_content: list = get_content(request)
    saved_content.append(content)
    request.session['content'] = saved_content
    return RedirectResponse(url='/', status_code=303)


@demo.get('/content/clear')
def show_content(request: Request):
    request.session.pop('content', None)
    return RedirectResponse(url='/demo/content', status_code=303)
