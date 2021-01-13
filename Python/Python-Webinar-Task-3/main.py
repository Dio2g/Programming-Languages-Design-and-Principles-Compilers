
print('Enter a number: ');
num = int(input());
count = 0;

while num != 1:
  count = count +1
  if (num % 2) == 0:
    num = num/2;
  else:
    num = (num*3)+1;
  
print('Steps taken: ' + count);






