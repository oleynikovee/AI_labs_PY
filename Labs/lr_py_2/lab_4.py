N=int(input())
words="Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення (в простіших випадках — окремих програм) для програмованих пристроїв, які, як правило містять один процесор чи більше"
output=""
array=words.split()
first=array[N]
num=20-N
last=array[num]
array[N]=last
array[num]=first
for val in array:
    output+=val+" "
print("Слова: "+str(output))
