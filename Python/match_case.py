# Match-case statement (switch) = An alternative to many elif statement
#                                 Execute some code if a value matches a case
#                                 Benefits: cleaner and syntax is more readable

def dayOfWeek(day):
    match day:
        case 1 | 2:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4: 
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: # Wild-card case
            return "Not a Valid day"

print(dayOfWeek(3))


