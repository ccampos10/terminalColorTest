#!/bin/python3
title = "  |   255-code   |    ansi-16   |   255-code   |    ansi-16   |"

print("Normal:")
print(' ','-'*(len(title)-2))
print(title)
print(' ','-'*(len(title)-2))
for i in range (8):
    print(f'  |  \033[38;5;{i}m    {"00"+str(i)}   \033[0m  |  \033[{30+i}m    {"0"+str(30+i)}   \033[0m  |  \033[48;5;{i}m    {"00"+str(i)}   \033[0m  |  \033[{40+i}m    {"0"+str(40+i)}   \033[0m  |')
print(' ','-'*(len(title)-2))

print("Bright:")
print(' ','-'*(len(title)-2))
print(title)
print(' ','-'*(len(title)-2))
for i in range (8):
    print(f'  |  \033[38;5;{8+i}m    {"00"+str(8+i) if i<2 else "0"+str(8+i)}   \033[0m  |  \033[{90+i}m    {"0"+str(90+i)}   \033[0m  |  \033[48;5;{8+i}m    {"00"+str(8+i) if i<2 else "0"+str(8+i)}   \033[0m  |  \033[{100+i}m    {str(100+i)}   \033[0m  |')
print(' ','-'*(len(title)-2))

