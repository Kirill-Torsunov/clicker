from django.contrib.auth.models import User
from django.db import models


class MainCycle(models.Model):
    user = models.ForeignKey(User, related_name='cycle', null=False, on_delete=models.CASCADE)
    coins_count = models.IntegerField(default=0)
    auto_click_power = models.IntegerField(default=0)
    click_power = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    def set_main_cycle(self, coins_count):
        self.coins_count = coins_count
        return self.check_level()

    def check_level(self):
        last_boost = Boost.objects.last()
        if self.coins_count > last_boost.default_price * 8:
            self.level += 1
            boost_type = 1
            if self.level % 2 == 0:
                boost_type = 0
            last_boost = Boost.objects.filter(main_cycle=self, boost_type=boost_type).last()
            if last_boost:
                new_price = last_boost.default_price * 9
                new_power = last_boost.power * 6
                boost = Boost(main_cycle=self, boost_type=boost_type, level=self.level, price=new_price,
                              default_price=new_price, power=new_power)
                boost.save()
            else:
                boost = Boost(main_cycle=self, boost_type=boost_type, level=self.level)
                boost.save()
            return True
        return False


class Boost(models.Model):
    main_cycle = models.ForeignKey(MainCycle, related_name='boosts', null=False, on_delete=models.CASCADE)
    level = models.IntegerField(null=False)
    power = models.IntegerField(default=1)
    price = models.IntegerField(default=10)
    boost_type = models.IntegerField(default=1)
    default_price = models.IntegerField(default=10)

    def upgrade(self):
        if self.main_cycle.coins_count >= self.price:
            self.main_cycle.coins_count -= self.price
            if self.boost_type == 1:
                self.main_cycle.click_power += self.power
                self.price = int(self.price * 1.5)
            else:
                self.main_cycle.auto_click_power += self.power
                self.price = int(self.price * 3)
        self.main_cycle.save()
        return self.main_cycle, self.level, self.price, self.power
