# PATHS
# from pathlib import Path
# path = Path("ecommerce/__init__.py")

# path.exists()
# path.is_file()
# path.is_dir()
# print(path.suffix)
# print(path.stem)
# print(path.parent)
# path = path.with_name("text.txt")
# print(path)

# WORKING WITH DIRECTORIES
# from pathlib import Path
# path = Path("ecommerce")
# # path.mkdir()
# # path.exists()
# # path.rmdir()
# # path.rename("ecommerce2")

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)

# import csv

# # WRITING TO A CSV FILE
# # with open("data.csv", "w") as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["transaction_id", "product_id", "product_quantity"])
# #     writer.writerow([1001, 2, 15])
# #     writer.writerow([1000, 1, 5])
# # READIND FROM A CSV FILE
# with open("data.csv") as file:
#     reader = csv.reader(file)
#     # print(list(reader))
#     # iterating over the file
#     for row in reader:
#         print(row)

# WORKING WITH JSON FILE
# import json
# from pathlib import Path
# # WRITING JSON DATA
# # movies = [
# #     {"id": 1, "title": "Terminator", "year": 1989},
# #     {"id": 2, "title": "Kingdergarten cop", "year": 1993}
# # ]

# # data = json.dumps(movies)
# # print(data)

# # Path("movies.json").write_text(data)
# # READING JSON DATA
# data = Path("movies.json").read_text()
# movies = json.loads(data)
# print(movies)

# WORKING WITH A SQLITE DATABASE
import sqlite3
import json
from pathlib import Path
movies = json.loads(Path("movies.json").read_text())
print(movies)
