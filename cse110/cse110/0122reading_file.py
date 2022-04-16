"""
Author: Caio Sa

Purpose: Practice finding items in files.
"""

with open("books_and_chapters.txt") as something:
    
    largest_chapter = 0
    
    largest_book = "" 
        
    for count,line in enumerate(something):
        if int(line.split(":")[1]) > largest_chapter:
            largest_chapter = int(line.split(":")[1])
            largest_book = line.split(":")[0]
        book = line.split(":")[0].strip()
        scripture = line.split(":")[2].strip()
        chapters = line.split(":")[1].strip()

        print(f"{count} Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

    print(f"The largest book is the book of {largest_book} with {largest_chapter} chapters")
