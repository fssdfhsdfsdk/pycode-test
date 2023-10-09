def my_function(school, standard, city, name):
    schoolName  = school
    cityName = city
    standardName = standard
    studentName = name
    print(schoolName, cityName, standardName, studentName)
    
def my_function2(school, standard):
    schoolName  = school
    standardName = standard
    print(schoolName, standardName)
    
# TypeError: my_function() got an unexpected keyword argument
data = {'school':'DAV', 'standard': '7', 'name': 'abc', 'city': 'delhi'}
my_function(**data)

logBlock_handle_tables = {
  "f1": {
    "func" : my_function,
    "args": data
  },
  
  "f2": {
    "func" : my_function2,
    "args": {'school':'USA', 'standard': '71'}
  }
}

logBlock_handle_tables["f1"]["func"](**logBlock_handle_tables["f1"]["args"])
logBlock_handle_tables["f2"]["func"](**logBlock_handle_tables["f2"]["args"])



