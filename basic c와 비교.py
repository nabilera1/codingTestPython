
C언어 자료형 선언
int n;
char ch[50];
double d;

파이썬
n
ch 또는 ch=[]
d

#include <stdio.h>
void Hello(){
	printf("안녕하세요\n");
}

void Hello1(char s[]){
	printf("%s\n", s);
}

int main(){
	Hello();
	Hello1("안녕하세요");
	return 0;
}


def  Hello():
    print("안녕하세요")

def  Hello1(x):
    print(x)

Hello()
Hello("안녕하세요")



int plus(int a, int b){
    return a + b;
}

파이썬
def plus(a,b):
    return a+b
n=plus(a,b)
또는
plus=lambda a,b:a+b

C언어
#include <stdio.h>
int main(){
	int a[5] = { 1, 2, 3, 4, 5 };
	int i, sum = 0;
	double avg = 0.0F;

	for (i = 0; i < 5; i++){
		printf("%d ", a[i]);
		sum += a[i];
	}
    printf("\n");
	avg = (float)sum / 5;
	printf("합: %d\n", sum);
	printf("평균: %.2f\n", avg);
	return 0;
}

파이썬
sum=0
a = [ 25, 7, 9, 15, 22 ]
for  i  in  range(0,5):
    print(a[i], end=' ')
    sum += a[i]
avg = sum / 5
print("합: ", sum);
print("평균: ", avg);


C언어
#include <stdio.h>
int main(){
	int n;
	printf("점수입력 : ");
	scanf_s("%d", &n);
	if (n >= 90)
		printf("A학점\n");
	else if (n >= 80)
		printf("B학점\n");
	else if (n >= 70)
		printf("C학점\n");
	else if (n >= 60)
		printf("C학점\n");
	else
		printf("F학점\n");
	return 0;
}


파이썬
n = int(input("점수 입력 : "))
if (n >=90):
    print("A학점.")
elif (n >=80):
    print("B학점.")
elif (n >=70):
    print("C학점.")
elif (n >=60):
    print("D학점.")
else:
    print("F학점.")


C언어
while (1)
{
	scanf_s("%d", &n);
	if (n < 0)
        break;
	sum += n;
	i++;
}

파이썬
while True:
    n = int(input())
    if n < 0:
        break;
    sum += n
    i+=1


