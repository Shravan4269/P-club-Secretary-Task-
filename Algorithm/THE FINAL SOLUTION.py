# %%
import random
import csv
import time as tm
start_time = tm.time()

N = 2000
reallocation_factor = 0
layover_factor = 10
timediff_factor = 100000000
output_variable = 1000
for z in range(N):
    # %%
    passenger_list = []
    number_of_rows = 400
    for i in range(number_of_rows):
        passenger_list.append([])

    # %%
    with open('passengers.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            k = int(row[1])
            if k >= number_of_rows:
                # If k is larger than the current size of passenger_list, resize it
                passenger_list.extend([[] for _ in range(k - number_of_rows + 1)])
                number_of_rows = len(passenger_list)
            #passenger_list[k].append(12)
            passenger_list[k].append(int(row[0]))
        

    # %%
    no_of_passengers = []
    for flights in passenger_list:
        no_of_passengers.append(len(flights))

    # %%
    cancelled = []
    cancel = {}
    with open('canceled.csv','r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cancelled.append(int(row[0]))
    capacity = []
    vacancy = []
    time = []
    flights = {}
    with open('flights.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)        
        maxm = 0
        for row in reader:
            k = int(row[0])
            capacity.append(int(row[3]))
            time.append((int(row[4]),int(row[5])))
            vacancy.append(capacity[k]-no_of_passengers[k])
            if k in cancelled:
                cancel[k] = ((int(row[1]),int(row[2])))
                continue
            if not (int(row[1]),int(row[2])) in flights:
                flights[(int(row[1]),int(row[2]))] = []
            maxm = max(maxm,int(row[1]))    
            
            flights[(int(row[1]),int(row[2]))].append(k)
            

    # %%
    n = maxm+1
    graph = {}
    for i in range(n):
        graph[i] = []

    for (u,v) in flights:
        graph[u].append(v)

    # %%
    possible_direct = {}
    possible_2_layoff = {}
    possible_3_layoff = {}
    for c in cancel:
        A,B = cancel[c]
        possible_direct[c] = []
        possible_2_layoff[c] = []
        possible_3_layoff[c] = []
        if B in graph[A]: possible_direct[c].append("YES")
        for i in graph[A]:
            if B in graph[i]:
                possible_2_layoff[c].append(i)
        for i in graph[A]:
            for j in graph[i]:
                if  B in graph[j]:
                    if(j==A): continue
                    possible_3_layoff[c].append((i,j))
                    

    # %%
    replace_flights = {}
    for c in cancelled:
        replace_flights[c] = [],[]
        A,B = cancel[c]
        for i in possible_2_layoff[c]:
            for j in flights[A,i]:
                
                    for k in flights[i,B]:
                        if time[k][0]-time[j][1] >=3600:
                            replace_flights[c][0].append((j,k))
        for (i,j) in possible_3_layoff[c]:
            for k in flights[A,i]:
                
                    for l in flights[i,j]:
                        if time[l][0]-time[k][1] >=3600:
                            for m in flights[j,B]:
                                if time[m][0]-time[l][1] >=3600:
                                    replace_flights[c][1].append((k,l,m))
                        

    # %%
    cnt = {}
    for c in cancelled:
        count =0
        for (u,v) in replace_flights[c][0]:
            count += min(vacancy[u],vacancy[v])
        for (u,v,w) in replace_flights[c][1]:
            count += min(vacancy[u],vacancy[v],vacancy[w])
        cnt[c] = count
    for c in cancel:
        if possible_direct[c] :
            for  i in flights[cancel[c]]:
                cnt[c] += vacancy[i]    
                

    # %%
    # random.shuffle(cancelled)
    def custom_key(item):
        return int(cnt[item]) - int(no_of_passengers[item])
    cancelled = sorted(cancelled,key =custom_key)

    # %%
    for key, value in replace_flights.items():
        for inner_list in value:
            random.shuffle(inner_list)
    # def sort_tuples(tuples_list,c):
    #     return sorted(tuples_list, key = lambda x: abs(time[c][1]-time[x[-1]][1]))

    # replace_flights = {key:[sort_tuples(lst,key) for lst in value] for key , value in replace_flights.items()}

    # %%
    no_of_affected = 0
    managed_reallocation = 0
    for i in cancelled:
        no_of_affected += no_of_passengers[i]

    # %%
    layover_count = 0
    absolute_time_diffrence = 0
    PID = {}
    average_time_diffrence = []

    # %%
    ABC = []
    countttt = 0

    # %%
    for c in cancelled:
        reallocation_required = no_of_passengers[c]
        reallocated = 0
        A,B = cancel[c]
        if possible_direct[c]:
            for i in flights[A,B]:        
                FID = i
                cnt = 0
                for x in range(vacancy[FID]):
                    Passenger_reallocating = passenger_list[c][0]
                    del passenger_list[c][0]
                    passenger_list[FID].append(Passenger_reallocating)
                    reallocated += 1
                    layover_count +=0
                    absolute_time_diffrence += abs(time[c][1]-time[FID][1])
                    average_time_diffrence.append(absolute_time_diffrence)
                    ABC.append(Passenger_reallocating)
                    PID[Passenger_reallocating] = []
                    PID[Passenger_reallocating].append(0)
                    PID[Passenger_reallocating].append((FID))
                    cnt = cnt+1
                    if(reallocated==reallocation_required):
                        break       
                
                vacancy[FID] = vacancy[FID]-cnt
                no_of_passengers[c] = no_of_passengers[c]-cnt
                    
        for (u,v) in replace_flights[c][0]:
            FID1 = u
            FID2 = v
            cnt = 0
            minimum = min(vacancy[FID1],vacancy[FID2])
            for x in range(minimum):
                Passenger_reallocating = passenger_list[c][0]
                del passenger_list[c][0]
                passenger_list[FID1].append(Passenger_reallocating)
                passenger_list[FID2].append(Passenger_reallocating)
                layover_count +=0
                reallocated += 1
                absolute_time_diffrence += abs(time[c][1]-time[FID2][1])
                average_time_diffrence.append(absolute_time_diffrence)
                ABC.append(Passenger_reallocating)
                PID[Passenger_reallocating] = []
                PID[Passenger_reallocating].append(1)
                PID[Passenger_reallocating].append(FID1)
                PID[Passenger_reallocating].append(FID2)
                cnt = cnt+1
                if(reallocated==reallocation_required):
                    break   
                
            vacancy[FID1] = vacancy[FID1]-cnt  
            vacancy[FID2] = vacancy[FID2]-cnt
            no_of_passengers[c] = no_of_passengers[c]-cnt     
    #     managed_reallocation += reallocated 
        
    # for c in cancelled:  
    #     reallocation_required = no_of_passengers[c]
    #     reallocated = 0  
        for (u,v,w) in replace_flights[c][1]:
            FID1 = u
            FID2 = v
            FID3 = w
            cnt = 0
            minimum = min(vacancy[FID1],vacancy[FID2],vacancy[FID3])
            for x in range(minimum):
                Passenger_reallocating = passenger_list[c][0]
                del passenger_list[c][0]
                passenger_list[FID1].append(Passenger_reallocating)
                passenger_list[FID2].append(Passenger_reallocating)
                passenger_list[FID2].append(Passenger_reallocating)
                layover_count +=2
                reallocated += 1
                absolute_time_diffrence += abs(time[c][1]-time[FID3][1])
                average_time_diffrence.append(absolute_time_diffrence)
                ABC.append(Passenger_reallocating)
                PID[Passenger_reallocating] = []
                PID[Passenger_reallocating].append(2)
                PID[Passenger_reallocating].append(FID1)
                PID[Passenger_reallocating].append(FID2)
                PID[Passenger_reallocating].append(FID3)
                cnt = cnt+1
                if(reallocated==reallocation_required):
                    break   
                
            vacancy[FID1] = vacancy[FID1]-cnt  
            vacancy[FID2] = vacancy[FID2]-cnt
            vacancy[FID3] = vacancy[FID3]-cnt
            no_of_passengers[c] = no_of_passengers[c]-cnt    
        managed_reallocation += reallocated 
    
    l = layover_count/managed_reallocation
    a = absolute_time_diffrence/managed_reallocation
    
    reallocation_factor = max(reallocation_factor,managed_reallocation)
    timediff_factor = (timediff_factor*z + a)/(z+1)
    layover_factor = (layover_factor*z + l)/(z+1)
    new_output = 200*(l/layover_factor + a/timediff_factor) 
    print(z,output_variable,new_output)           
    if z <1000:
        output_variable = min(output_variable,new_output)
    else:
        if abs(new_output-output_variable)<=4 and reallocation_factor==managed_reallocation:
            break
    # %%   


# %%


end_time = tm.time()
time_taken = 1000*(end_time - start_time)
time_taken

# %%
with open('stats.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["AFFECTED", "REALLOCATED", "AVERAGE LAYOUT","AVERAGE TIME DIFFRENCE","SOL TIME"])
        writer.writerow([no_of_affected , managed_reallocation , l , a , time_taken])

with open('allot.csv', 'w') as f:
        writer = csv.writer(f)
        for x in PID:
                if PID[x][0] == 0:
                        writer.writerow([x,PID[x][0],PID[x][1]])
                if PID[x][0] == 1:
                        writer.writerow([x,PID[x][0],PID[x][1],PID[x][2]])  
                if PID[x][0] == 2:
                        writer.writerow([x,PID[x][0],PID[x][1],PID[x][2],PID[x][3]])         
        for c in cancelled:
                for x in range(no_of_passengers[c]):
                        writer.writerow([passenger_list[c][x],0])                

# %%

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%



