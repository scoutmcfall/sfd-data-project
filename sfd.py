import requests
from collections import Counter
import pprint

#used this to format bellwether housing addresses
#     street_nums = []
#     for line in adds:
#         nums = line.split(",")
#         street_nums.append(nums[1])
#     for num in street_nums:
#         print(num)

#get a list of unique response codes to use as column headers
# with open("/home/hackbright/src/practice/address_results - Sheet2 (1).csv") as categories:
#     cats = categories.readlines()
#     catlst = []
#     for line in cats:
#         codes = line.split(",")
#         for code in codes:
#             inner_code = code.split(",")
#             for response in inner_code:
#                 if response not in catlst:
#                     catlst.append(code)
#                     catlst.append("\n")
    
# f = open('unique_codes.csv', 'w')
# for code in catlst:
#     f.write(code)
# f.close()

# with open("/home/hackbright/src/practice/unique_codes.csv", 'r') as codes:
#     formatted_codes = []
#     codelst = codes.readlines()
#     for code in codelst:
#         code.replace("'", "")
#     # print(codelst)

# f = open('formatted_codes.csv', 'w')
# for code in codelst:
#     f.write(code)
# f.close()
#******************************************************

with open("/home/hackbright/src/sfd-data-project/add_to_check.csv", 'r') as addresses:
    adds = addresses.readlines()
    str_adds = []
   
    for line in adds:
        chars = line.split("\n")
        str_adds.append(""+chars[0]+"")


with open("/home/hackbright/src/Seattle_Real_Time_Fire_911_Calls.csv", 'r') as sfd_report:
    sfd_data = sfd_report.readlines()
   

def code_search(call_data, add):  
    # print("code search: " + add)
    responses = []
    for record in call_data:
        if add in record:
            columns = record.split(",")
            
            responses.append(columns[1])
    result = Counter(responses)
    # pprint.pprint(result)
    # print("-----------------------------")
    # print("\n")
    return str(result)

def date_search(call_data, add):   
    # print("date search: " + add)
    dates = []
    year_counts = {}
    for record in call_data:
        if add in record:
            columns = record.split(",")
            datetimes = columns[2].split(" ")
            dates.append(datetimes[0][-4:])
    #instead of using counter, which sorts by count instead of key
    #i'll populate my year counts dict using .get()
    year_rang = list(range(2003,2023))

    for year in year_rang:
        year_counts[str(year)] = year_counts.get(year, 0)
    #now i have a dict where keys are the years from 2003-2022
    for date in dates:
        year_counts[date] = year_counts.get(date, 0)+1
    
    
    # #now sort the dictionary by key
    # year_counts_keys = year_counts.items()
    # sorted_keys = sorted(year_counts_keys)
    # print(sorted_keys)
    
    #dateresult = Counter(dates)
    #return str(dateresult)
    #have to make it a string so it can be written to a file
    return str(year_counts)

# print(" test  ")
# date_search(sfd_data, '1601 2nd Av')


codes_total = []
dates_total = []

for val in str_adds:
    dates_total.append("\n")
    dates_total.append(val)
    dates_total.append(date_search(sfd_data, val))
  
#     codes_total.append("\n")
#     codes_total.append(val)
#     codes_total.append(code_search(sfd_data, val))
  
#write sorted date list from date_search specifically to a file
f = open("sorted_dates_by_year_address.csv", "w")
for dres in dates_total:
    f.write(dres)
f.close()

# #write all the codes/dates results to a file
# f = open('date_and_code_results_by_address.csv', 'w')
# for res in codes_total:
#     # res_st = str(res)
#     f.write(res)
# for dres in dates_total:
#     # dres_st = str(dres)
#     f.write(dres)
# f.close()

#get all dates in a doc so i can sort them
# f = open('date_to_sort.csv', 'w')
# for dres in dates_total:
#     # dres_st = str(dres)
#     f.write(dres)
# f.close()

# with open("/home/hackbright/src/sfd-data-project/date_to_sort.csv", "r") as calls_by_year:
#     call_info = calls_by_year.readlines()
#     address_calls_per_year = {}
#     for line in call_info:
#         linevals = line.split("Counter")
#         #at this point linevals[-1] is an unsorted dictionary of year:# call values
#         #I want to sort the years in order and then store the whole thing as a alue keyed to the address        
        
#         address_calls_per_year[linevals[0]] = linevals[-1]
# #print(address_calls_per_year)




# def get_calls_by_address():
#     for record in data:
#         if "903 Union" in record:
#             print(record)

