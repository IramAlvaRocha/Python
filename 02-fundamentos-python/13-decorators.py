def require_auth(func):
    def wrapper(user):
        if user == "admin":
            return func(user);
        else:
            print("Acceso denegado")
    return wrapper

@require_auth
def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"

auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard("admin"))


