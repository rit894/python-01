'''In system administration, you often need to parse log files to find the first occurrence of a problem. Log
 entries are often stored or processed as tuples because they represent a fixed structure (e.g., timestamp,
 log level, message) that shouldn’t change.
 Write a Python function named find
 first
 a tuple with three elements:
 • timestamp (string)
 • log
 error that takes a list of log entries. Each log entry is
 level (string, e.g., ’INFO’, ’WARN’, ’ERROR’)
 • message (string)
 Your function should iterate through the list and return the timestamp (a string) of the very first log
 entry where the log
 level is ’ERROR’. If no ’ERROR’ entries are found in the list, the function should
 return None.'''
import datetime as dt
def list_input():
    log_entries=[]
    noof_enteries=int(input("Enter number of log entries: "))
    for i in range(noof_enteries):
        log_entrie1=[]
        timestamp=dt.datetime.now().time()
        log_level=input("Enter log level (INFO/WARN/ERROR): ")
        message=input("Enter message: ")
        log_entrie1.append(str(timestamp))
        log_entrie1.append(log_level)
        log_entrie1.append(message)
        log_entries.append(tuple(log_entrie1))
    return log_entries

def find_first_error(log_entries):
    for entry in log_entries:
        if entry[1]=='ERROR':
            return entry[0]
    return None
logs=list_input()
print(find_first_error(logs))
        