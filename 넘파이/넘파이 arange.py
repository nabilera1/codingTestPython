import numpy as np
n=50
print(np.arange(n))

# import numpy as np
np.arange(30)  #0~29 값이 저장된 30개 공간의 Array
np.arange(0, 10, 0.5) #실수 간격 가능

arr=np.arange(30)
resh=arr.reshape(5,6)  #5행 6열
print(resh)

resh=arr.reshape(-1,5)  #6행 5열
print(resh)

resh=arr.reshape(-1,)  #1차원 배열
print(resh)
print(resh[0]) #0
resh=arr.reshape(-1,1)  #2차원 배열
print(resh)
print(resh[0]) #[0]이