import os
import sys
# 请在此输入您的代码
a=2025
sum=0
count=0
while sum<a:
  count+=1
  sum+=5
  if count%2!=0:
    sum+=15
  if count%2==0:
    sum+=2
  if count%3==2:
    sum+=10
  if count%3==1:
    sum+=2
  if count%3==0:
    sum+=7
print(count)