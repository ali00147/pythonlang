from collections import Counter
from collections import defaultdict

fruits=["apple","apple", "apple","orange","orange",
        "tomato","tomato","pen","pen","mas"]

count_fruits = {fruit: fruits.count(fruit) for fruit in fruits}
fruits:list[str]
print(count_fruits)

#//--------using the counter libary-----------//
print("-"*70)
count_fruits2 = Counter(fruits)
print(count_fruits2)

#//---------using collections defaultdict------//

count_fruits = defaultdict(int)
for fruit in fruits:
    count_fruits[fruit] += 1

print("-"*70)
print("defaultdict:",dict(count_fruits))