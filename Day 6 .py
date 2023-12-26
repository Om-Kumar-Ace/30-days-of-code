def print_even_odd_characters(s):
    even_chars = s[::2]  
    odd_chars = s[1::2] 
    print(even_chars, odd_chars)


t = int(input())

for _ in range(t):
    
    s = input()
    print_even_odd_characters(s)
