# SV: You receieve a list of business data from multiple sources with differing priorities.
#  You need to create a result that holds an entry for each business and takes attributes 
# from each of the inputs depending on priority.

# Input = [ {"name": "Starbucks", "phone_number": "12345"},
#     {"name": "Starbucks", "is_open": "true"},
#     {"name": "Dunkin", "is_open": "false"},  ] 

# Returns: [{"name": "Starbucks", "phone_number": "12345", "is_open": "true"}, {"name": "Dunkin", "is_open": "false"} ]

# 
def check_priority(array):
   
   for index in range(len(array)):
       


a = [ {"name": "Starbucks", "phone_number": "12345"},
{"name": "Starbucks", "is_open": "true"},
{"name": "Starbucks", "is_closed": "false"},
{"name": "Dunkin", "is_open": "false"}, 
{"name": "Dunkin", "phone_number": "378"},  ] 

print(check_priority(a))