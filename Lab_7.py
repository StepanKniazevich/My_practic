# Task 7.3.3

class Worker:

    # Constructor by to the task
    def __init__(self, last_name, first_name, info):
        self.last_name = last_name
        self.first_name = first_name
        self.dept_name = info['dept_name']
        self.position = info['position']
        self.birth_date = info['birth_date']
        self.experience = info['experience']

    def get_information(self):
        print("Last name: {}".format(self.last_name))
        print("First name: {}".format(self.first_name))
        print("Department: {}".format(self.dept_name))
        print("Position: {}".format(self.position))
        print("Year of birth: {}".format(self.birth_date))
        print("Experience in years: {}".format(self.experience))

    def __del__(self):
        del(self.last_name)
        del(self.first_name)
        del(self.dept_name)
        del(self.position)
        del(self.birth_date)
        del(self.experience)



# Main part

class App:

    workers = []

    # Menu positions
    menu = [
        'Add worker.',
        'Delete worker.',
        'Get information about the worker by last and first names.',
        'Search by the year of birth.',
        'Search by the position.',
    ]

    def __init__(self):
        self.map = {
            1: self.add_worker,
            2: self.del_worker,
            3: self.get_info,
            4: self.search_year,
            5: self.search_position,
        }
        self.loop()

    def loop(self):

        while(True):
            self.print_menu()
            self.menu_position = self.get_menu_position()
            self.process()

    def print_menu(self):
        print("\n------------------------------------------------")


        count = 1
        for item in self.menu:
            print("{}) {}".format(count, item))
            count += 1

        print("------------------------------------------------")

    def get_menu_position(self):
        count = input('Your choice -> ')

        cond_type = not count.isdigit()

        if(not cond_type):
            cond_menu = int(count) > len(self.menu)
        else:
            cond_menu = False

        while(cond_type or cond_menu):
            print('Invalid format. Try again.')
            return self.get_menu_position()

        return int(count)

    def process(self):
        func = self.map[self.menu_position]
        func()

    def add_worker(self):
        print("Adding new worker:")

        # Last name

        last_name = input('Input worker\'s last name -> ')

        while(last_name.isdigit() or last_name == ''):
            print('Invalid format. Try again.')
            last_name = input('Input worker\'s last name -> ')

        # First name

        first_name = input('Input worker\'s first name -> ')

        while(first_name.isdigit() or first_name == ''):
            print('Invalid format. Try again.')
            first_name = input('Input worker\'s first name -> ')

        # Info

        info = {}

        # Department name
        info['dept_name'] = input('Input department -> ')

        while(info['dept_name'].isdigit() or info['dept_name'] == ''):
            print('Invalid format. Try again.')
            info['dept_name'] = input('Input department -> ')

        # Position
        info['position'] = input('Input position -> ')

        while(info['position'].isdigit() or info['position'] == ''):
            print('Invalid format. Try again.')
            info['position'] = input('Input position -> ')

        # Birth year
        info['birth_date'] = input('Input year of birth -> ')

        while(not info['birth_date'].isdigit()):
            print('Invalid format. Try again.')
            info['birth_date'] = input('Input year of birth -> ')

        # Experience
        info['experience'] = input('Input experience in years -> ')

        while(not info['experience'].isdigit()):
            print('Invalid format. Try again.')
            info['experience'] = input('Input experience in years -> ')

        # New worker
        self.workers.append(Worker(last_name, first_name, info))

    def get_del_position(self):
        count = input('Your choice -> ')

        cond_type = not count.isdigit()

        if(not cond_type):
            cond_menu = int(count) > (len(self.workers) + 1)
        else:
            cond_menu = False

        while(cond_type or cond_menu):
            print('Invalid format. Try again.')
            return self.get_del_position()

        return int(count)

    def del_worker(self):
        print("Deleting worker:")

        count = 1
        for worker in self.workers:
            print("{}) {} {}.".format(count, worker.last_name, worker.first_name))
            count += 1

        print("{}) {}.".format(count, "Cancel"))
        print("------------------------------------------------")

        del_position = self.get_del_position()

        if(del_position == count):
            return 0

        self.workers.pop(del_position - 1)

    def get_info(self):
        print("Getting information about worker:")

        # Last name

        last_name = input('Input worker\'s last name -> ')

        while(last_name.isdigit() or last_name == ''):
            print('Invalid format. Try again.')
            last_name = input('Input worker\'s last name -> ')

        # First name

        first_name = input('Input worker\'s first name -> ')

        while(first_name.isdigit() or first_name == ''):
            print('Invalid format. Try again.')
            first_name = input('Input worker\'s first name -> ')

        # Search
        for worker in self.workers:
            if(worker.last_name == last_name and worker.first_name == first_name):
                worker.get_information()
                return 0

        print("No results.")


    def search_year(self):
        print("Searching worker by the year of birth:")

        # Birth year
        birth_date = input('Input year of birth -> ')

        while(not birth_date.isdigit()):
            print('Invalid format. Try again.')
            birth_date = input('Input year of birth -> ')

        # Search
        for worker in self.workers:
            if(worker.birth_date == birth_date):
                worker.get_information()
                return 0

        print("No results.")


    def search_position(self):
        print("Searching worker by position:")

        # Position
        position = input('Input position -> ')

        while(position.isdigit() or position == ''):
            print('Invalid format. Try again.')
            position = input('Input position -> ')

        # Search
        for worker in self.workers:
            if(worker.position == position):
                worker.get_information()
                return 0

        print("No results.")

App()
