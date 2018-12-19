def find_power_level(x, y, serial_num):
    rack_ID = x + 10
    power_level = ((rack_ID * y) + serial_num) * rack_ID
    if len(str(power_level)) >= 3:
        power_level = int(str(power_level)[-3])
    elif len(str(power_level)) < 3:
        power_level = 0
    power_level = power_level - 5
    return power_level

# print(find_power_level(101,153,71))

def total_power_level_of_3x3_square(top_left_x, top_left_y, serial_num):
    total_power_level = 0
    for x in range(top_left_x, top_left_x + 3):
        for y in range(top_left_y, top_left_y + 3):
            total_power_level += find_power_level(x,y,serial_num)
    return total_power_level

# print(total_power_level_of_3x3_square(21,61,42))

def find_largest_total_power_coords(serial_num):
    largest_total_power = 0
    for x in range(1,299):
        for y in range(1,299):
            if total_power_level_of_3x3_square(x,y,serial_num) > largest_total_power:
                largest_total_power = total_power_level_of_3x3_square(x,y,serial_num)
                x_coord = x 
                y_coord = y
    identifier = [x_coord,y_coord]
    return (identifier,largest_total_power)

print(find_largest_total_power_coords(9424))
