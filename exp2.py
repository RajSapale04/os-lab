import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority

def execute_algorithm(processes, algorithm, time_quantum=None):
    if algorithm == "FCFS":
        return fcfs(processes)
    elif algorithm == "SJF":
        return sjf(processes)
    elif algorithm == "RR":
        return rr(processes, time_quantum)
    elif algorithm == "Priority":
        return priority_scheduling(processes)
    else:
        print("Invalid algorithm choice!")
        return None

def fcfs(processes):
    print("Executing FCFS algorithm")
    processes.sort(key=lambda x: x.arrival_time)
    return execute_scheduling_algorithm(processes)

def sjf(processes):
    print("Executing SJF algorithm")
    processes.sort(key=lambda x: (x.burst_time,x.arrival_time))
    return execute_scheduling_algorithm(processes)

def rr(processes, time_quantum):
    print(f"Executing RR algorithm with time quantum {time_quantum}")
    return execute_scheduling_algorithm(processes, time_quantum)

def priority_scheduling(processes):
    print("Executing Priority Scheduling algorithm")
    processes.sort(key=lambda x: (x.priority,x.arrival_time))
    return execute_scheduling_algorithm(processes)

def execute_scheduling_algorithm(processes, time_quantum=None):
    current_time = 0
    wait_time_sum = 0
    turnaround_time_sum = 0
    gantt_chart = []
    total_processes = len(processes)
    

    while processes:
        next_process = get_next_process(processes, current_time)
        if next_process is None:
            current_time += 1
            continue

        wait_time = max(current_time - next_process.arrival_time, 0)
        execution_time = min(next_process.remaining_time, time_quantum) if time_quantum else next_process.remaining_time
        turnaround_time = wait_time + execution_time

        wait_time_sum += wait_time
        turnaround_time_sum += turnaround_time

        gantt_chart.append((next_process.pid, current_time, current_time + execution_time))
        current_time += execution_time
        next_process.remaining_time -= execution_time

        if next_process.remaining_time == 0:
            processes.remove(next_process)
    avg_wait_time = wait_time_sum / total_processes if total_processes != 0 else 0
    avg_turnaround_time = turnaround_time_sum / total_processes if total_processes != 0 else 0
    print(gantt_chart)
    return avg_wait_time, avg_turnaround_time, gantt_chart

def get_next_process(processes, current_time):
    for process in processes:
        if process.arrival_time <= current_time:
            return process
    return None

def draw_gantt_chart(gantt_chart, i):
    titles = ['First Come First Serve', 'Shortest Job First', 'Round Robin', 'Priority']
    fig, gnt = plt.subplots()
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    process_names = sorted(set(f'P{entry[0]}' for entry in gantt_chart))
    process_mapping = {name: i for i, name in enumerate(process_names)}

    for g in gantt_chart:
        process_name = f'P{g[0]}'
        execution_time = g[2] - g[1]       
        first_part = any(entry[1] == g[1] and entry[0] == g[0] for entry in gantt_chart)       
        gap = 0.1 if not first_part else 0
        gnt.barh(process_mapping[process_name], execution_time - gap, left=g[1], height=0.5, align='center', edgecolor='black')       
        if gap > 0 and g[2] < max(entry[2] for entry in gantt_chart):
            gnt.barh(process_mapping[process_name], gap, left=g[2], height=0.5, align='center', edgecolor='white')
    plt.yticks(range(len(process_names)), process_names)  
    plt.title(titles[i])
    plt.show()

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes_FCFC = []
    processes_SJF = []
    processes_RR = []
    processes_PS = []
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for Process {i}: "))
        burst_time = int(input(f"Enter burst time for Process {i}: "))
        priority = int(input(f"Enter priority for Process {i}: "))
        processes_SJF.append(Process(i, arrival_time, burst_time, priority))
        processes_PS.append(Process(i, arrival_time, burst_time, priority))
        processes_RR.append(Process(i, arrival_time, burst_time, priority))
        processes_FCFC.append(Process(i, arrival_time, burst_time, priority))
    time_quantum = int(input("Enter time quantum for Round Robin: "))

    
    algorithms = ["FCFS", "SJF", "RR", "Priority"]
    processes=[processes_FCFC,processes_SJF,processes_RR,processes_PS]
    for i in range(0,4):
        avg_wait_time, avg_turnaround_time, gantt_chart = execute_algorithm(processes[i], algorithms[i], time_quantum)
        
        if gantt_chart is not None:
            print(f"{algorithms[i]} results:")
            print("Average Wait Time:", avg_wait_time)
            print("Average Turnaround Time:", avg_turnaround_time)
            draw_gantt_chart(gantt_chart,i)

if __name__ == "__main__":
    main()
