print('Bus Ticket')
bus_name='akshay travels'
seat_number=1
destination='pune'
departure_time=10.00
payment='done'
if (bus_name=='akshay travels'):
    if seat_number==1:
        if destination=='pune':
            if (departure_time==10.00):
                if payment=='done':
                    print('ticket booked succesfully' )
                    print('bus_name= akshay travels')
                    print('seat_number=1')
                    print('destination=pune')
                    print('departure_time=10.00')
                    print('payment=done')
                    print('1200/- payment done')
                else:
                    print('payment not done')
            else:
                print('departure time missmatch')
        else:
            print('wrong destination')
    else:
        print('wrong seat number')
else:
    print('invalid bus name')