# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:56:30 2019

@author: Haiounj
"""

from flask import render_template
from app import app
import random

@app.route('/')
@app.route('/index')
def index():
    cards = [
        {
             'name' : 'Benthide hypnotisant',
             'gametext':'Quand le Benthide hypnotisant arrive sur le champ de bataille, créez deux jetons de créature 0/2 bleue Illusion avec « À chaque fois que cette créature bloque une créature, celle-ci ne se dégage pas pendant la prochaine étape de dégagement de son contrôleur. » Le Benthide hypnotisant a la défense talismanique tant que vous contrôlez une illusion.',
             'image' :"http://www.magiccorporation.com/scan/ravnica_allegiance/vf/043.png"
                },
        {
             'name' : 'Ange de la grâce',
             'gametext':'Flash, Vol. Quand l Ange de la grâce arrive sur le champ de bataille, jusqu à la fin du tour, les blessures qui devraient réduire votre total de points de vie à moins de 1 le réduisent à 1 à la place. , exilez l Ange de la grâce de votre cimetière: Votre total de points de vie devient 10 .',
             'image' :"http://www.magiccorporation.com/scan/ravnica_allegiance/vf/001.png" 
                },
        {
             'name' : 'Engeance du chaos',
             'gametext':'...',
             'image' :"http://www.magiccorporation.com/scan/ravnica_allegiance/vf/085.png" 
                },
        {
             'name' : 'Escouflenfer skarrgan',
             'gametext':'...',
             'image' :"http://www.magiccorporation.com/scan/ravnica_allegiance/vf/114.png" 
                },
        {
             'name' : 'Limon biosynthétique',
             'gametext':'...',
             'image' :"http://www.magiccorporation.com/scan/ravnica_allegiance/vf/122.png" 
                }
        
            ]
    cards1_1=[];
    cards2_1=[];
    cards3_1=[];
    cards1_2=[];
    cards2_2=[];
    cards3_2=[];
    cards1_3=[];
    cards2_3=[];
    cards3_3=[];
    cards1_4=[];
    cards2_4=[];
    cards3_4=[];
    cards1_5=[];
    cards2_5=[];
    cards3_5=[];
    cards1_6=[];
    cards2_6=[];
    cards3_6=[];
    cards1_7=[];
    cards2_7=[];
    cards3_7=[];
    cards1_8=[];
    cards2_8=[];
    cards3_8=[];
    cards1_9=[];
    cards2_9=[];
    cards3_9=[];
    cards1_10=[];
    cards2_10=[];
    cards3_10=[];
    cards1_11=[];
    cards2_11=[];
    cards3_11=[];
    cards1_12=[];
    cards2_12=[];
    cards3_12=[];
    cards1_13=[];
    cards2_13=[];
    cards3_13=[];
    cards1_14=[];
    cards2_14=[];
    cards3_14=[];
    cards1_15=[];
    cards2_15=[];
    cards3_15=[];
    for i in range(60):
        cards1_1.append(cards[random.randrange(0, 5, 1)])

    
        
    
    return render_template('index.html', title='Home',cards = [cards1_1,cards1_2,cards1_3,cards1_4,cards1_5,cards1_6,cards1_7,cards1_8,cards1_9,cards1_10,cards1_11,cards1_12,cards1_13,cards1_14,cards1_15,cards2_1,cards2_2,cards2_3,cards2_4,cards2_5,cards2_6,cards2_7,cards2_8,cards2_9,cards2_10,cards2_11,cards2_12,cards2_13,cards2_14,cards2_15,cards3_1,cards3_2,cards3_3,cards3_4,cards3_5,cards3_6,cards3_7,cards3_8,cards3_9,cards3_10,cards3_11,cards3_12,cards3_13,cards3_14,cards3_15])