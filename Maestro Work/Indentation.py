def check(num):
    if num > 5:
        print("big")
    else:
        print("small")



numbers = ( 1 + 2 + 3 + 4 +
            5 + 6 + 7 + 8 +
            9 + 10 + 11 + 12
            )


def total( x , y ):
    v = ( x + y + 4 +
          5 + 6 + 7 +
          8 + 9 + 10 +
          11 + 12
         )
    if v > 50 :
        print( "Above limit" )
    else :
        print( "Below" )
    return v


def string_division(x):

    total_string_character_sum = sum(x)
    total_string_character_length = len(x)

    "to calculate the average of characters in a string "

    return total_string_character_sum / total_string_character_length


def get_grade(points):
    """
    calculating the average grade for each student
    """

def total_string_length_calculation(x):
    """
    setting up a counter parameter to go through the string
    """
    y=0
    for i in x:
        y += i
        total_string_length = len(x)
        average = y / total_string_length

        if i < average:
            print('below average')
        else:
            print('above average')