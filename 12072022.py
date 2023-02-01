from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
sand = 12
sandState = 1
x = pos.x +1
y = pos.y
z = pos.z
floor = int(input("몆 층짜리 피라미드를 만들까요?"))
width = floor * 2 - 1
for i in range(floor):
    mc.setBlocks(x+i, y+i, z+i, x+width-1+i, y+i, z+width-1-i, sand, sandState)
    width = width - 2