
employee_Detail = {
    "emp_id" : 1001,
    "emp_name" : "Vinay",
    "age" : 28,
    "designation" : "SSE",
    "personal_details" : {
        "qualification" : "MCA",
        "phone_no" : 9154549566,
        "location" : "Bangalore",
        "additional_details" : {
            "mother" : "Jyothi",
            "father" : "Raghu",
            "gender" : "male",
            "blood group" : "B+"
        }
    }
}

shallow_dict = {}

# recursion -> creating a shallow copy of nested dictionary
def recursion(employee_Detail):
    if(type(employee_Detail) == dict):
        for key in list(employee_Detail.keys()):
            if(type(employee_Detail[key]) != dict):
                shallow_dict[key] = employee_Detail[key]
                print(key, " : ", employee_Detail[key])
            if(type(employee_Detail[key]) == dict):
                recursion(employee_Detail[key])

recursion(employee_Detail)