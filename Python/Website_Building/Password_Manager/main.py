from fasthtml.common import *
from starlette.testclient import TestClient

def render(user):
    return Li(f"{user.username} - {user.password} | {A(f"{user.website}", href=user.website)}", 
              A("Remove", hx_delete=f"/{user.id}", hx_swap="outerHTML", target_id=f"contact-{user.id}", id=f"contact-{user.id}"))

app, rt, users, User = fast_app(
    'users.db',
    render = render,
    username = str,
    password = str,
    website = str,
    id = int,
    pk = "id"
)

def CreateUsername():
    return Input(id="username", placeholder="Username")
def CreatePassword():
    return Input(id="password", placeholder="Password")
def CreateWebsite():
    return Input(id="website", placeholder="Website: https://example.com")

@rt("/")
def Home():
    return Titled("Password Manager"), Div(
        Ul(*users(), id="user_list"),
        Form(
            CreateUsername(),
            CreatePassword(),
            CreateWebsite(),
            Button("Add User", hx_post="/", target_id="user_list", hx_swap="beforeend")
        )
    )

@rt("/")
def PostUser(user: User):
    users.insert(user)
    return users

serve()