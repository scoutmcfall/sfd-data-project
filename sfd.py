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
    data = sfd_report.readlines()
    responses = []
    dates = []
    
def search(data, add):    
    for line in data:
        if add in line:
            columns = line.split(",")    
            responses.append(columns[1])
            datetimes = columns[2].split(" ")
            dates.append(datetimes[0][-4:])
    result = Counter(responses)
    # pprint.pprint(result)
    # dates.sort() 
    dateresult = Counter(dates)
    # pprint.pprint(dateresult)
    return str(dateresult)

total = []
# print(search(data, "2519 1st Av"))
#THERES SOMETHING HAPPENING HERE THAT'S MAKING THE NUMBERS HUGE WHAT IS GOING ON
for add in str_adds:
    total.append(add)
    res = search(data, add)
    total.append(res)
    total.append("\n")
print(total)


# f = open('unsorted_date_results_by_address.csv', 'w')
# for res in total:
#     f.write(res)
# f.close()




# def get_calls_by_address():
#     for record in data:
#         if "903 Union" in record:
#             print(record)


# def call_api():
#     res = requests.get("https://data.seattle.gov/resource/kzjm-xkqj.json")
#     res2 = res.json()
#     for record in res2:
#         if "903 Union" in record:
#             print(record)
