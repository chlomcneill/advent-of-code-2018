def find_power_level(x, y, serial_num):
    rack_ID = x + 10
    power_level = ((rack_ID * y) + serial_num) * rack_ID
    if len(str(power_level)) >= 3:
        power_level = int(str(power_level)[-3])
    elif len(str(power_level)) < 3:
        power_level = 0
    power_level = power_level - 5
    return power_level

def total_power_level_of_nxn_square(top_left_x, top_left_y, n, serial_num):
    total_power_level = 0
    for x in range(top_left_x, top_left_x + n):
        for y in range(top_left_y, top_left_y + n):
            total_power_level += find_power_level(x,y,serial_num)
    return total_power_level

def find_highest_total_power_coords_for_nxn_square(serial_num, n):
    largest_total_power = 0
    for x in range(1,302-n):
        for y in range(1,302-n):
            if total_power_level_of_nxn_square(x,y,n,serial_num) > largest_total_power:
                largest_total_power = total_power_level_of_nxn_square(x,y,n,serial_num)
                x_coord = x 
                y_coord = y
                size = n
    return ([x_coord,y_coord,size],largest_total_power)

def find_size_of_highest_total_power_square(serial_num):
    largest_total_powers = []
 
    for n in range(1,301):
        largest_total_powers.append(find_highest_total_power_coords_for_nxn_square(serial_num, n))
    # max_largest_total_power = max(largest_total_powers)
    # if max_largest_total_power == find_highest_total_power_coords_for_nxn_square(serial_num, n)[-1]:
    #     x_coord = find_highest_total_power_coords_for_nxn_square(serial_num, n)[0][0]
    #     y_coord = find_highest_total_power_coords_for_nxn_square(serial_num, n)[0][1]
    #     size = find_highest_total_power_coords_for_nxn_square(serial_num, n)[0][2]
    # return ([x_coord,y_coord,size],max_largest_total_power)   
    return largest_total_powers


print(find_size_of_highest_total_power_square(18))
