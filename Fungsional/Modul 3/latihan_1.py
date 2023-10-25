def convert_to_minutes(data):
    result = []
    for item in data:
        weeks, days, hours, minutes = 0, 0, 0, 0
        parts = item.split()
        for i in range(0, len(parts), 2):
            if parts[i+1] == 'minggu':
                weeks = int(parts[i])
            elif parts[i+1] == 'hari':
                days = int(parts[i])
            elif parts[i+1] == 'jam':
                hours = int(parts[i])
            elif parts[i+1] == 'menit':
                minutes = int(parts[i])
        total_minutes = weeks*7*24*60 + days*24*60 + hours*60 + minutes
        result.append(total_minutes)
    return result

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

print(convert_to_minutes(data))
