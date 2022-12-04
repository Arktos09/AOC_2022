import os
import re
dir = os.path.dirname(__file__)
os.chdir(dir)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

lines = [x for x in read_input_lines()]

count = 0
for i in lines:
    nums = [int(x) for x in re.findall('[0-9]+', i)]
    a = set([x for x  in range(nums[0],nums[1]+1)])
    b = set([x for x  in range(nums[2],nums[3]+1)])
    common = a&b
    if len(common) == len(a) or len(common) == len(b):
        count+=1
print(count)

count = 0
for i in lines:
    nums = [int(x) for x in re.findall('[0-9]+', i)]
    a = set([x for x  in range(nums[0],nums[1]+1)])
    b = set([x for x  in range(nums[2],nums[3]+1)])
    common = a&b
    if len(common)>0:
        count+=1
print(count)