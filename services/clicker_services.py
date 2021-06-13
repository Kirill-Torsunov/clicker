from django.contrib.auth.models import User
from backend.models import MainCycle, Boost
from backend.serializers import BoostSerializer


def main_page(request):
    user = User.objects.filter(id=request.user.id).first()
    if user:
        main_cycle = MainCycle.objects.get(user=request.user)
        return False, 'index.html', {'user': user, 'main_cycle': main_cycle}
    else:
        return True, 'login', {}


def set_main_cycle(request):
    main_cycle = MainCycle.objects.get(user=request.user)
    is_level_up = main_cycle.set_main_cycle(int(request.data['coins_count']))
    boosts_query = Boost.objects.filter(main_cycle=main_cycle)
    boosts = BoostSerializer(boosts_query, many=True).data
    main_cycle.save()
    if is_level_up:
        return main_cycle.coins_count, boosts
    return main_cycle.coins_count, None


def upgrade_boost(request):
    boost_level = request.data['boost_level']
    cycle = MainCycle.objects.get(user=request.user)
    boost = Boost.objects.get(main_cycle=cycle, level=boost_level)
    main_cycle, level, price, power = boost.upgrade()
    boost.save()
    return {'click_power': main_cycle.click_power,
            'coins_count': main_cycle.coins_count,
            'auto_click_power': main_cycle.auto_click_power,
            'level': level,
            'price': price,
            'power': power}
