from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
score = 0 # 점수 초기화
pos = mc.player.getTilePos() # 사용자의 위치 입력 받음
x = pos.x
y = pos.y
z = pos.z
blockType = 80 # 눈 블럭 이용( 블럭 id = 80 )
mc.setBlocks(x-3, y, z-3, x+3, y, z+3, blockType) # 눈 바닥 생성
while(True): 
    for i in range(5): 
        sec = 5-i
        print(str(sec)+ "초 뒤에 타일이 사라집니다!")
        time.sleep(1)
    for j in range(30): # 랜덤으로 공기 타일로 바꿀 30개의 좌표 뽑음
        blockX = random.randint(x-3, x+3)
        blockZ = random.randint(z-3, z+3) 
        mc.setBlock(blockX, y, blockZ, 0) # 공기블럭으로 바뀜
    time.sleep(1) # 타일이 없어진 후 1초 기다림
    pos = mc.player.getTilePos() 
    if (blockType == mc.getBlock(pos.x, pos.y - 1, pos.z)): # 사용자가 밟고 있는 블록이 눈 블록이라면
        score += 1 # 스코어 상승
    else:
        break # 눈 블록이 아닐 경우 while문에서 빠져나옴 = 게임 종료 
    mc.setBlocks( x-3, y, z-3, x+3, y, z+3, blockType ) # 눈 바닥 재생성
message = "총 점수는 " + str(score) + "점 입니다." 
print(message)
