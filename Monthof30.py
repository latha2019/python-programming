
def freedays(booked, travel):
    """ function to takes two lists as parameters and
    returns a list of days those are free to study
    """
    occupied = booked + travel
    print("occupied dates for the month:", occupied)
    study = []
    for days in range(1, 31):
        if days not in occupied:
            study.append(days)
    return study

booked = [ 1, 3, 9, 12, 13, 18, 26, 27, 28, 29 ]
travel = [ 4, 5, 15, 16, 21, 22 ]
res = freedays(booked, travel)
print(" list of days free to study in the month: ", res)
