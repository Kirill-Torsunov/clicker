from backend.forms import UserForm
from backend.models import MainCycle, Boost
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return True, 'index', {}
        else:
            return False, 'login.html', {'invalid': True}
    else:
        return False, 'login.html', {'invalid': False}


def user_logout(request):
    logout(request)
    return 'login'


def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            main_cycle = MainCycle(user=user)
            main_cycle.save()
            first_boost = Boost(main_cycle=main_cycle, level=0)
            first_boost.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return True, 'index', {}
        else:
            return False, 'registration.html', {'invalid': True, 'form': form}
    else:
        form = UserForm()
        return False, 'registration.html', {'invalid': False, 'form': form}
