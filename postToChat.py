from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
mc. postToChat('HELLO!')

import time
pos = mc.player.getTilePos()
x = pos.x+1
y = pos.y
z = pos.z

block = 35

ingredients = [1,12,6,5,4,12,0,1]

index = 0

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

mc.setBlocks(x,y,z,x+3,y,z+3, block, ingredients[index])
time.sleep(1)
index +=1
y +=1

 

