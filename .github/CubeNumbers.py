#第一个方法
#Numbers = list(range(1,20))
#for CubeNumbers in Numbers:
 #   CubeNumbers = CubeNumbers ** 3
  #  print(CubeNumbers)
  
  # 第二个方法
#CubeNumbers = []
#for number in range(1,20):
 #   CubeNumber = number ** 3
  #  CubeNumbers.append(CubeNumber)
#print(CubeNumbers)

#列表解析方法
CubeNumbers = [ number ** 3 for number in range(1,11)]
print(CubeNumbers)           

