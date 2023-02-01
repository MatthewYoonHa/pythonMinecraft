from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time 
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
stone = 98
lava = 10
mc.postToChat("the floor is lava!")
mc.setBlocks(x-2,y-2,z-2,x+2,y-1,z+2,stone)
mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,lava)
time.sleep(3)
pos = mc.player.getTilePos()
blockType = mc.getBlock(pos.x,pos.y,pos.z)
ans = str(bool(blockType == lava))
mc.postToChat(ans)