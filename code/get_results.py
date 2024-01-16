import time
import random
import signal

len_seeds = 10

seeds = []
random.seed(42)
for i in range(len_seeds):
    seed = random.randint(0,1000)
    seeds.append(seed)

def handler(signum, frame):
    raise Exception("TIMEOUT")

signal.signal(signal.SIGALRM, handler)





### BABY HUMMER
#solution = cegis(setting, target, length, heuristic)

from bh_synthesis import cegis as straight_cegis
from bh_synthesis_stochastic import cegis as stochastic_cegis
from bh_grammar import turntop, turntop2, toptobottom, top2tobottom, cut

timeout = 600
f = open("bh.txt", "w")

# Time to find one solution

print('Time to find one solution:')
f.write('Time to find one solution:' + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 20, 'BFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 20, 'DFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 20, '%Success')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(1, [], 20, '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(1, [], 20, 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times) + '\n')



    
# Time to find meaningful solution

print('Time to find meaningful solution:')
f.write('Time to find meaningful solution:' + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(2, [], 20, 'BFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(2, [], 20, 'DFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(2, [], 20, '%Success')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(2, [], 20, '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(2, [], 20, 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times) + '\n')




# Time to find specific solutions

targets = [[toptobottom,turntop,cut,turntop,toptobottom,turntop2,toptobottom,turntop,toptobottom],
           [turntop2,turntop,cut,turntop,top2tobottom,turntop,cut],
           [turntop2,top2tobottom,turntop,cut],
           [toptobottom,turntop,cut,turntop2,cut,turntop,toptobottom,turntop,turntop2],
           [toptobottom,turntop,cut,turntop2,cut,turntop,toptobottom,turntop,turntop2],
           [toptobottom,top2tobottom,turntop,cut]]

for target in targets:

    print("Target: " + str(target))
    f.write("Target: " + str(target) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 20, 'BFS')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 20, 'DFS')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 20, '%Success')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        signal.alarm(timeout)
        start = time.time()
        try:
            solution = stochastic_cegis(3, target, 20, '%Success')
            end = time.time()
            times.append(round(end - start, 3))
        except Exception:
            times.append("TIMEOUT")
    f.write(str(times) + '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        signal.alarm(timeout)
        start = time.time()
        try:
            solution = stochastic_cegis(3, target, 20, 'Adapted')
            end = time.time()
            times.append(round(end - start, 3))
        except Exception:
            times.append("TIMEOUT")
    f.write(str(times) + '\n')

f.close()
    




### ELMSLEY SHUFFLES
#solution = cegis(setting, target, length, target_pos, heuristic)

from es_synthesis import cegis as straight_cegis
from es_synthesis_stochastic import cegis as stochastic_cegis
f = open("es.txt", "w")

# Time to find one solution

print('Time to find one solution:')
f.write('Time to find one solution:' + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(1, [], 10, position, 'BFS')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(1, [], 10, position, 'DFS')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(1, [], 10, position, '%Success')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(1, [], 10, position, '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    times_pos.append(times)
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(1, [], 10, position, 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    times_pos.append(times)
f.write(str(times_pos) + '\n')





# Time to find meaningful solution

print('Time to find meaningful solution:')
f.write('Time to find meaningful solution:' + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(2, [], 10, position, 'BFS')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(2, [], 10, position, 'DFS')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    start = time.time()
    solution = straight_cegis(2, [], 10, position, '%Success')
    end = time.time()
    times_pos.append(round(end - start, 3))
f.write(str(times_pos) + '\n')

times_pos = []
for position in range(8):
    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(2, [], 10, position, '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    times_pos.append(times)
f.write(str(times_pos) + '\n')
 
times_pos = []
for position in range(8):
    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(2, [], 10, position, 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    times_pos.append(times)
f.write(str(times_pos) + '\n')





# Time to find specific solutions

targets = [(["inS","inS","outS"], 6),
           (["inS","outS","outS","outS","inS","outS"], 6),
           (["inS","outS","inS"], 5),
           (["inS","outS","outS","outS","outS","inS"], 5)]

for target in targets:

    print("Target: " + str(target))
    f.write("Target: " + str(target) + '\n')
    
    start = time.time()
    solution = straight_cegis(3, target[0], 10, target[1], 'BFS')
    end = time.time()
    avg_time = round(end - start, 3)
    f.write(str(avg_time) + '\n')

    start = time.time()
    solution = straight_cegis(3, target[0], 10, target[1], 'DFS')
    end = time.time()
    avg_time = round(end - start, 3)
    f.write(str(avg_time) + '\n')

    start = time.time()
    solution = straight_cegis(3, target[0], 10, target[1], '%Success')
    end = time.time()
    avg_time = round(end - start, 3)
    f.write(str(avg_time) + '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(3, target[0], 10, target[1], '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    f.write(str(times) + '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        start = time.time()
        solution = stochastic_cegis(3, target[0], 10, target[1], 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    f.write(str(times) + '\n')

f.close()

    



### MIND READING
#solution = cegis(setting, target, audience, heuristic)

from mr_synthesis import cegis as straight_cegis
from mr_synthesis_stochastic import cegis as stochastic_cegis

timeout = 1800
f = open("mr.txt", "w")

# Time to find one solution - 3 audience members

print('Time to find one solution - 3 audience members:')
f.write('Time to find one solution - 3 audience members:' + '\n')

start = time.time()
solution = straight_cegis(1, [], 3, 'BFS')
end = time.time()
avg_time = round(end - start, 3)
f.write(str(avg_time) + '\n')

start = time.time()
solution = straight_cegis(1, [], 3, 'DFS')
end = time.time()
avg_time = round(end - start, 3)
f.write(str(avg_time) + '\n')

start = time.time()
solution = straight_cegis(1, [], 3, '%Success')
end = time.time()
avg_time = round(end - start, 3)
f.write(str(avg_time) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    start = time.time()
    solution = stochastic_cegis(1, [], 3, '%Success')
    end = time.time()
    times.append(round(end - start, 3))
f.write(str(times) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    start = time.time()
    solution = stochastic_cegis(1, [], 3, 'Adapted')
    end = time.time()
    times.append(round(end - start, 3))
f.write(str(times) + '\n')





# Time to find one solution - 5 audience members

print('Time to find one solution - 5 audience members:')
f.write('Time to find one solution - 5 audience members:' + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 5, 'BFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 5, 'DFS')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

signal.alarm(timeout)
start = time.time()
try:
    solution = straight_cegis(1, [], 5, '%Success')
    end = time.time()
    avg_time = round(end - start, 3)
except Exception:
    avg_time = "TIMEOUT"
f.write(str(avg_time) + '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(1, [], 5, '%Success')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times)+ '\n')

times = []
for seed in seeds:
    random.seed(seed)
    signal.alarm(timeout)
    start = time.time()
    try:
        solution = stochastic_cegis(1, [], 5, 'Adapted')
        end = time.time()
        times.append(round(end - start, 3))
    except Exception:
        times.append("TIMEOUT")
f.write(str(times)+ '\n')





# Time to find specific solutions

targets = [[list("rrrrrbrbrrbrrrbbbbbrbbbrrbbrbrbb")],
           [list("rrrrrbrrbrbbrrbbbbbrrrbbrbbbrbrb")]]

for target in targets:

    print("Target: " + str(target))
    f.write("Target: " + str(target) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 5, 'BFS')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 5, 'DFS')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    signal.alarm(timeout)
    start = time.time()
    try:
        solution = straight_cegis(3, target, 5, '%Success')
        end = time.time()
        avg_time = round(end - start, 3)
    except Exception:
        avg_time = "TIMEOUT"
    f.write(str(avg_time) + '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        signal.alarm(timeout)
        start = time.time()
        try:
            solution = stochastic_cegis(3, target, 5, '%Success')
            end = time.time()
            times.append(round(end - start, 3))
        except Exception:
            times.append("TIMEOUT")
    f.write(str(times)+ '\n')

    times = []
    for seed in seeds:
        random.seed(seed)
        signal.alarm(timeout)
        start = time.time()
        try:
            solution = stochastic_cegis(3, target, 5, 'Adapted')
            end = time.time()
            times.append(round(end - start, 3))
        except Exception:
            times.append("TIMEOUT")
    f.write(str(times)+ '\n')

f.close()





##### NUMBER OF SOLUTIONS

f = open("number.txt", "a")

from bh_synthesis import cegis as straight_cegis
from bh_synthesis_stochastic import cegis as stochastic_cegis
from bh_grammar import turntop, turntop2, toptobottom, top2tobottom, cut

timeout = 600
f.write("Baby Hummer:\n")

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 20, 'BFS')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 20, 'DFS')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 20, '%Success')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

counts = []
for seed in seeds:
    random.seed(seed)
    temp = open("temp.txt","w")
    temp.write("a")
    temp.close()
    signal.alarm(timeout)
    try:
        stochastic_cegis(4, [], 20, '%Success')
    except Exception:
        pass
    temp = open("temp.txt", "r")
    counts.append(len(temp.readlines()[0])-1)
    temp.close()
f.write(str(counts) + '\n')

counts = []
for seed in seeds:
    random.seed(seed)
    temp = open("temp.txt","w")
    temp.write("a")
    temp.close()
    signal.alarm(timeout)
    try:
        stochastic_cegis(4, [], 20, 'Adapted')
    except Exception:
        pass
    temp = open("temp.txt", "r")
    counts.append(len(temp.readlines()[0])-1)
    temp.close()
f.write(str(counts) + '\n')





from mr_synthesis import cegis as straight_cegis
from mr_synthesis_stochastic import cegis as stochastic_cegis

timeout = 600
f.write("Mind Reading:\n")

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 5, 'BFS')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 5, 'DFS')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

temp = open("temp.txt","w")
temp.write("a")
temp.close()
signal.alarm(timeout)
try:
    straight_cegis(4, [], 5, '%Success')
except Exception:
    pass
temp = open("temp.txt", "r")
f.write(str(len(temp.readlines()[0])-1) + '\n')
temp.close()

counts = []
for seed in seeds:
    random.seed(seed)
    temp = open("temp.txt","w")
    temp.write("a")
    temp.close()
    signal.alarm(timeout)
    try:
        stochastic_cegis(4, [], 5, '%Success')
    except Exception:
        pass
    temp = open("temp.txt", "r")
    counts.append(len(temp.readlines()[0])-1)
    temp.close()
f.write(str(counts) + '\n')

counts = []
for seed in seeds:
    random.seed(seed)
    temp = open("temp.txt","w")
    temp.write("a")
    temp.close()
    signal.alarm(timeout)
    try:
        stochastic_cegis(4, [], 5, 'Adapted')
    except Exception:
        pass
    temp = open("temp.txt", "r")
    counts.append(len(temp.readlines()[0])-1)
    temp.close()
f.write(str(counts) + '\n')

f.close()
