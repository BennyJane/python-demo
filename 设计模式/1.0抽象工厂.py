# -*- coding: utf-8 -*-
# @Time : 2020/11/2
# @Author : Benny Jane
# @Email : 暂无
# @File : 抽象工厂.py
# @Project : Python-Exercise


class PetShop:

    def __init__(self, animal_factory=None):
        """PetShop 本身就是一个抽象工厂"""
        self.pet_factory = animal_factory

    def show_pet(self):
        """animal_factory 需要实现的三个接口：get_pet， speak，get_food"""
        pet = self.pet_factory.get_pet()
        print("This is a lovely", pet)
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())


class Dog:
    """Dog 类自身没有实现PetShop所需要的接口"""

    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"

# todo 非继承方式 ==》 可以通过继承实现同样的效果
class DogFactory:
    """当原始类不方便修改的时候，可以使用该工厂模式"""

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


if __name__ == '__main__':
    shop = PetShop()
    shop.pet_factory = DogFactory()
    shop.show_pet()
    print("=" * 20)
