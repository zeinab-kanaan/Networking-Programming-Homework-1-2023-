primsry_numbers = [x for x in range(1,1000) if 0 not in [x%i for i in range(2,x//2)]]
print(primsry_numbers)