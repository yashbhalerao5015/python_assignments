dict1={
    "name":"Yash Bhalerao",
    "roll_no":565
}

dict2={
    "name":"Simba",
    "age":5
}

dict3={
    "location":"Pune",
    "mobile_no":9123456789
}

merged_dict = {**dict1,**dict2,**dict3}

print(merged_dict)