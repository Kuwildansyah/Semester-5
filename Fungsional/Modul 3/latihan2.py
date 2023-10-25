def convert_to_minutes(data):
    result = []
    for item in data:
        parts = item.split()
        # Use filter to get only integer values
        parts = list(filter(lambda x: x.isdigit(), parts))
        weeks, days, hours, minutes = map(int, parts)
        total_minutes = [weeks, days, hours, minutes]
        result.append(total_minutes)
    return result

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

print(convert_to_minutes(data))
