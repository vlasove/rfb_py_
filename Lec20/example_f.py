"""
Запись строки в файл
"""

message = "10"
fh = open(file="output.txt", mode="a")
fh.write(message)
fh.close()