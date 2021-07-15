import Alice_active_listen, Alice_passive_listen

class VA:

    def answer_on_command(self, command, close_Alice, listen_type):
        self.command = command
        self.close_Alice = close_Alice
        self.listen_type = listen_type
        if 'выключить Алису' in self.command or 'выключить Алису' in self.command or 'выключить' in self.command:
            self.close_Alice = True
        if ('Алиса' in self.command) and (self.listen_type == 0):
            Alice_active_listen.main()
            self.listen_type = 1
        if ('Выйти из активного режима' in self.command or 'стоп' in self.command) and (self.listen_type == 1):
            Alice_passive_listen.main()
            self.listen_type = 0

Alice = VA()
Alice.listen_type = 0