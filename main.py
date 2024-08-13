import pgzrun

import pgzero.game
import pgzero.keyboard
from pgzero.actor import Actor
from pgzero.animation import animate
from pgzero.clock import schedule_interval
from pgzero.constants import mouse

keyboard: pgzero.keyboard.keyboard
screen: pgzero.game.screen

WIDTH = 600 # Ширина окна
HEIGHT = 300 # Высота окна

TITLE = "Приключения Coddy" # Заголовок окна игры
FPS = 30 # Количество кадров в секунду

#Переменные с графикой
fon = Actor('fon_city')
coddy = Actor('coddy', (50,240))
fireball = Actor('fireball', (700, 240))

#Отрисовка
def draw():
    fon.draw()
    coddy.draw()
    fireball.draw()
    
#Перемещение
def update(dt):
    coddy.x = coddy.x + 2
    #Напиши код движения для огненного шара
    fireball.x = fireball.x - 5
    fireball.angle += 3
    
pgzrun.go()