from fasthtml.common import *
from starlette.testclient import TestClient

def render():
    return Li(f"{users.username} - {users.password} | {A(f"{users.website}", href=users.website)}", 
              A("Remove", hx_delete=f"/{users.id}", hx_swap="OuterHTML", target_id=f"contact-{users.id}", id=f"contact-{users.id}"))

app, rt, users, Task = fast_app(
    'users.db',
    render = render,
    username = str,
    passowrd = str,
    website = str,
    id = int,
    pk = "id"
)

def CreateUsername():
    return Input(id="username", placeholder="Username")

@rt("/")
def Home():
    return P("Hello World!")



serve()