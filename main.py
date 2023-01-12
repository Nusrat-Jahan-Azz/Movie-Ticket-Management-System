
class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = []
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self):
        self.id = input('ENTER THE MOVIE ID: ')
        self.movie_name = input('ENTER THE MOVIE NAME: ')
        self.time = input('ENTER THE MOVIE TIME: ')
        self.obj2 = Entry_Show(self.id, self.movie_name, self.time)
        self._show_list.append(self.obj2)
        self.seat2D = [['true' for i in range(self.cols)] for j in range(self.rows)]
        self.prepare_seat = TwoD_seat(self.id, self.seat2D)
        self.__seats.append(vars(self.prepare_seat))

    def book_seats(self):
        self.customer_Name = input('ENTER CUSTOMER NAME: ')
        self.__phone_num = input('ENTER CUSTOMER PHONE NUMBER: ')
        self.s_id = input('ENTER SHOW ID: ')
        show_flag = 1
        for shows in self._show_list:
            if self.s_id == shows.id:
                self.ticket_num = int(input('ENTER NUMBER OF TICKETS: '))
                self.Booked_T_list = []
                self.T_num = 0
                while(self.T_num != self.ticket_num):
                    self.seat_no = input('ENTER SEAT NO: ')
                    self.check_rows = (ord(self.seat_no[0]) - 65) + 1
                    self.check_cols = int(self.seat_no[1:])

                    if self.check_rows>self.rows or self.check_cols>self.cols:
                        print('-' * 50)
                        print("Invalid Seat Number!")
                        print('-' * 50)
                    else:
                        for shows_seat in self.__seats:
                            if shows_seat['id'] == self.s_id:
                                if shows_seat['seat2D'][self.check_rows-1][self.check_cols] == 'true':
                                    self.Booked_T_list.append(self.seat_no)
                                    shows_seat['seat2D'][self.check_rows-1][self.check_cols] = ' X'
                                    print('BOOKED')
                                    self.T_num += 1
                                else:
                                    print('SORRY!!! SEAT ALREADY BOOKED')
                    
                if len(self.Booked_T_list):
                    print()
                    print(f'{"#"*5} TICKET BOOKED SUCCESSFULLY!! {"#"*5}')
                    print('-' * 70)
                    print(f'NAME: {self.customer_Name}')
                    print(f'PHONE NUMBER: {self.__phone_num}')
                    print()
                    print(f'MOVIE NAME: {shows.movie_name}\t\tMOVIE TIME: {shows.time}')
                    #print(f'TICKETS: {self.Booked_T_list}')
                    print(f'TICKETS: ', end="")
                    for BTL in range(len(self.Booked_T_list)):
                        print(f'{self.Booked_T_list[BTL]} ', end="")
                    print(f'\nHALL NO: {self.hall_no}')
                    print('-' * 70)
                show_flag = 0
                break
        if show_flag:
            print('-' * 50)
            print("Id didn't match with any show!")
            print('-' * 50)
        print()

    def view_show_list(self):
        print()
        print('-' * 80)
        for movie in self._show_list:
            print(f'MOVIE NAME: {movie.movie_name}\t\tSHOW ID: {movie.id}\t\tTIME: {movie.time}')
        print('-' * 80)
        print()

    def view_available_seats(self):
        self.s_id = input('ENTER SHOW ID: ')
        print()
        flag = 1
        for shows in self._show_list:
            if self.s_id == shows.id:
                print(f'MOVIE NAME: {shows.movie_name}\t\tTIME: {shows.time}')
                print('X for already booked seats')
                print('-' * 50)
                for shows_seat in self.__seats:
                    if shows_seat['id'] == self.s_id:
                        for i in range(self.rows):
                            for j in range(self.cols):
                                if shows_seat['seat2D'][i][j] == 'true':
                                    print(f'{chr(65+i)}{j}\t', end="")
                                else:
                                    print(f"{shows_seat['seat2D'][i][j]}\t", end="")
                            print()
                        print('-' * 50)
                flag = 0
                break
        if flag:
            print('-' * 50)
            print("Id didn't match with any show!")
            print('-' * 50)
        print()


    
class Star_Cinema(Hall):
    __hall_list = []

    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__(rows, cols, hall_no)
        self.hall_info = Hall(rows, cols, hall_no)

    def entry_hall(self):
        self.__hall_list.append(self.hall_info)



class Entry_Show:
    def __init__(self, id, movie_name, time) -> None:
        self.id = id
        self.movie_name = movie_name
        self.time = time



class TwoD_seat:
    def __init__(self, id, seat2D) -> None:
        self.id = id
        self.seat2D = seat2D


# please, initially entry two show.
T_counter = Hall(3, 5, 1)
T_counter.entry_show()
T_counter.entry_show()
print()



while(True):
    print("1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET")
    choice = int(input('ENTER OPTION: '))
    if choice == 1:
        T_counter.view_show_list()
    elif choice == 2:
        T_counter.view_available_seats()
    elif choice == 3:
        T_counter.book_seats()
    else:
        break




