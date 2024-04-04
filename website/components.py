from reactpy import component, html

@component
def container():
    return html.div(

    )

@component
def login_form():
    return html.div(
        html.h1("Login"),
        html.br(),
        html.div(
            {"class_name": "mb-3"},
            html.input(
                {
                    "type": "text",
                    "class_name": "form-control",
                    "name": "username",
                    "placeholder": "Username",
                    "required": "true",
                }
            ),
        ),
        html.div(
            {"class_name": "mb-3"},
            html.input(
                {
                    "type": "password",
                    "class_name": "form-control",
                    "name": "password",
                    "placeholder": "Password",
                    "required": "true",
                }
            ),
        ),
        html.br(),
        html.button({"class_name": "btn btn-secondary", "type": "submit"}, "Login"),
    )

@component 
def cards(title, data, img ):
    return html.div(
        {"class_name": "col"},
        html.div(
            {"class_name": "card"},
            html.img(
                {"src": img, "class_name": "card-img-top"}
            ),
            html.div(
                {"class_name": "card-body"},
                html.h5({"class_name": "card-title"}, title),
                html.p({"class_name": "card-text"}, data),
            ),
        )
    )

@component
def pop_message(value):
    return html.div(
        {
            "class_name": "alert alert-warning alert-dismissible fade show",
            "role": "alert",
        },
        value,
        html.button(
            {
                "class_name": "btn-close",
                "type": "button",
                "data-bs-dismiss": "alert",
                "aria-label": "Close",
            }
        ),
    )

@component
def post_post():
    return html.div(
        html.h1("Public Post"),
        html.br(),
        html.div(
            {"class_name": "mb-3"},
            html.input(
                {
                    "type": "text",
                    "class_name": "form-control",
                    "name": "title",
                    "placeholder": "Title",
                    "required": "true",
                }
            ),
        ),
        html.div(
            {"class_name": "mb-3"},
            html.input(
                {
                    "type": "text",
                    "class_name": "form-control",
                    "name": "description",
                    "placeholder": "Description",
                    "required": "true",
                }
            ),
        ),
        html.div(
            {"class_name": "mb-3"},
            html.input(
                {
                    "type": "file",
                    "name": "img",
                    "class_name": "form-control",
                    "placeholder": "Password",
                    "required": "true",
                }
            ),
        ),
        html.br(),
        html.button({"class_name": "btn btn-secondary", "type": "submit"}, "Send"),
    )
