measurements = [4.3, 5.7, 5.1, 6.4, 7.9, 12.8]

#def stableMeasurements(measurements):
#    return []

#print(stableMeasurements(measurements) == [])

for i in range(1, len(measurements) - 1):
    m = measurements[i]
    before = max(measurements[:i])
    after = min(measurements[i+1:])

    condition = (before < m )and (m < after)
    if condition:
        print(measurements[i:])
        break

#print(before, "**", m, "**", after, condition)

#def stateDurations(states, timestamps):
#    return []

#print(stateDurations([1,2,0], [0,243,565])
#      == [0, 243, 322])

#print(stateDurations([2, 1, 2, 0], [0, 300, 900, 1000])
#        == [0, 600, 400])

states = [1, 2, 0]
timestamps = [0, 243, 565]

durations = [0, 0, 0]

for i in range(len(states)-1):
    state = states[i]
    starts = timestamps[i]
    ends = timestamps[i+1] 
    duration = timestamps[i+1] - timestamps[i]
    print(state, "starts at", starts, "and ends at", ends)
    print("duration:", duration)

    if state == 0:
        durations[0] = durations[0] + duration
    if state == 1:
        durations[1] = durations[1] + duration
    if state == 2:
        durations[2] = durations[2] + duration

print(durations)
