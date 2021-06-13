import services
from django.shortcuts import render, redirect


def main(request):
    relocate, template, params = services.clicker_services.main_page(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)


def registration(request):
    relocate, template, params = services.auth_services.user_registration(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)


def login(request):
    relocate, template, params = services.auth_services.user_login(request)
    if relocate:
        return redirect(template)
    return render(request, template, params)


def logout(request):
    template = services.auth_services.user_logout(request)
    return redirect(template)
