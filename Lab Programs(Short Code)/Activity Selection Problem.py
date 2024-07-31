def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort activities by finish time
    selected_activities = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected_activities[-1][1]:
            selected_activities.append(activities[i])

    return selected_activities

def main():
    activities = []
    
    n = int(input("Enter the number of activities: "))

    for i in range(n):
        start, finish = map(int, input(f"Enter start and finish time for activity {i + 1} (separated by space): ").split())
        activities.append((start, finish))

    selected_activities = activity_selection(activities)

    print("Selected activities:")
    for activity in selected_activities:
        print(f"Activity {activities.index(activity) + 1}: Start time = {activity[0]}, Finish time = {activity[1]}")

if __name__ == "__main__":
    main()
