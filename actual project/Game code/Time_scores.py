def get_best_times():#retrieves the best time scores for the 3 levels and puts them in alist format.
    times=open("best_times.txt","r")
    time_list=(times.read()).split()
    return time_list

def set_new_best_times(new_best_times):#best time scores text in file is overwirtten with new best scores
    times=open("best_times.txt","w")
    times.write(new_best_times)















