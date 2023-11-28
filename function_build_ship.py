def build_ship(bottle):
    total_bottles=0
    for week in range(1,53):
        total_bottles=total_bottles + bottle
        print('Week %s = %s bottles' % (week,total_bottles))
build_ship(2)