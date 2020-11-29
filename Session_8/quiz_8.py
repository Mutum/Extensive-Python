# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 21:44:30 2020

@author: Mutum
"""

# A webpage has 4 buttons - 1,2,3,4
# Write a fn/closure such that we can track how many times each button was pressed. To simulate different users, pass on/maintain seperate
# dictionaries.

# Assume a function called onClick(4) will be called when 4th button is presses, and so on


track_click = dict()



def onClick():
    
    count= 0
    
    def click(a,*kwargs):
        nonlocal count
        count += 1
        
        track_click[a] = count
        
    return click

onClick = onClick()

onClick.__closure__
onClick.__code__.co_freevars
 

onClick(3)
onClick(4)
onClick(4)



track_click

track = {}

def onclick():
     
    def users(number):
        count = 0
        
        def click():
            nonlocal count
            count += 1
            track[number] = count
        return click
    return users
            
onclick = onclick()           

onclick.__closure__

onclick(1)
onclick(2)
    

[{y:0} for x,y in enumerate(range(1,5))]

click_track = {}

# count = [{user:0} for index,user in enumerate(range(1,5))]

def website():
    
    count = [{user:0} for index,user in enumerate(range(1,5))] 
    
    def on_click(user):
        nonlocal count
        click_number = count[user -1][user] + 1
        count[user -1][user] = click_number
        click_track[user] = click_number
        
    return on_click
        
On_Click = website()

On_Click(1)
On_Click(1)
On_Click(2)
On_Click(2)
On_Click(3)
On_Click(4)
On_Click(4)
On_Click(4)



click_track
