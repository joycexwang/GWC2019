# define function below
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# ask player to say a number
number = input("Choose a number ")
number = int(number)
answer = is_even(number)
print(answer)
print(is_even(7))

def calc_total(list):
    for num in list:
        sum += num
    return sum
print(calc_total([1,2,3]))
