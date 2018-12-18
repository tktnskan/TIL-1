import requests
import random

url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url, verify=False)
lotto_data = response.json()

real_numbers = []
for key, value in lotto_data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

real_numbers.sort()
bonus_number = lotto_data['bnusNo']

numbers = list(range(1, 46))

my_numbers = random.sample(numbers, 6)
my_numbers.sort()

# my_numbers, real_numbers, bonus_number
# 1 등: my_numbers == real_numbers
# 2 등: real & my 가 5개가 같고, my의 나머지 하나가 bonus_number
# 3 등: real & my 가 5개가 같다
# 4 등: real & my 가 4개가 같다
# 5 등: real & my 가 3개가 같다
# 꽝