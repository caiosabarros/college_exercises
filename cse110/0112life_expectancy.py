
#Open the file

year = int(input("Enter the year of interest: "))
lattest_year = 0

with open("life-expectancy.csv") as data:

    max_expectancy_for_the_year = 0
    min_expectancy_for_the_year = 100
    year_for_max_expectancy = 0
    year_for_min_expectancy = 0
    country_max = ""
    country_min = ""
    sum_of_life_expectancies = 0
    

    for count,line in enumerate(data):
        if count > 0:
            sum_of_life_expectancies += float(line.strip().split(",")[3])
            if float(line.strip().split(",")[3]) > max_expectancy_for_the_year:
                max_expectancy_for_the_year = float(line.strip().split(",")[3])    
                year_for_max_expectancy = line.split(",")[2]
                country_max = line.split(",")[0]
            if float(line.strip().split(",")[3]) < min_expectancy_for_the_year:
                min_expectancy_for_the_year = float(line.strip().split(",")[3])
                year_for_min_expectancy = line.split(",")[2]
                country_min = line.split(",")[0]

    print(f"The overall max life expectancy is: {max_expectancy_for_the_year} from {country_max} in {year_for_max_expectancy}")
    print(f"The overall min life expectancy is: {min_expectancy_for_the_year} from {country_min} in {year_for_min_expectancy}")

with open("life-expectancy.csv") as data:

    max_expectancy_for_the_year = 0
    min_expectancy_for_the_year = 100
    year_for_max_expectancy = 0
    year_for_min_expectancy = 0
    country_max = ""
    country_min = ""
    sum_of_life_expectancies = 0
    counter = 0 

    for count,line in enumerate(data):
        if count > 0:
            if int(line.strip().split(",")[2]) == year:
                counter += 1
                sum_of_life_expectancies += float(line.strip().split(",")[3])
                if float(line.strip().split(",")[3]) > max_expectancy_for_the_year:
                    max_expectancy_for_the_year = float(line.strip().split(",")[3])    
                    country_max = line.split(",")[0]
                if float(line.strip().split(",")[3]) < min_expectancy_for_the_year:
                    min_expectancy_for_the_year = float(line.strip().split(",")[3])
                    country_min = line.split(",")[0]


    print(f"The average life expectancy across all countries was {round(sum_of_life_expectancies/counter,2)}")
    print(f"The max life expectancy was in {country_max} with {max_expectancy_for_the_year}")
    print(f"The min life expectancy was in {country_min} with {min_expectancy_for_the_year}")

with open("life-expectancy.csv") as data:

    max_expectancy_for_the_year = 0
    min_expectancy_for_the_year = 100
    year_for_max_expectancy = 0
    year_for_min_expectancy = 0
    country_max = ""
    country_min = ""
    sum_of_life_expectancies = 0
    counter = 0 

    newest_year = 0

    #find newest year
    for count,line in enumerate(data):
        if count > 0:
            if int(line.strip().split(",")[2]) > newest_year:
                newest_year = int(line.strip().split(",")[2])
    lattest_year = newest_year

with open("life-expectancy.csv") as data:
    for count,line in enumerate(data):
        if count > 0:
            if int(line.strip().split(",")[2]) == newest_year:
                counter += 1
                #sum_of_life_expectancies += float(line.strip().split(",")[3])
                if float(line.strip().split(",")[3]) > max_expectancy_for_the_year:
                    max_expectancy_for_the_year = float(line.strip().split(",")[3])    
                    country_max = line.split(",")[0]
                if float(line.strip().split(",")[3]) < min_expectancy_for_the_year:
                    min_expectancy_for_the_year = float(line.strip().split(",")[3])
                    country_min = line.split(",")[0]

    print(f"The lattest max life expectancy was in {country_max} with {max_expectancy_for_the_year}")
    print(f"The lattest min life expectancy was in {country_min} with {min_expectancy_for_the_year}")
