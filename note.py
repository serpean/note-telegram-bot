class Note:
    def __init__(self, note_name):
        self.note_name = note_name
        self.item_list = []

    def add(self, note):
        self.item_list.append(note)

    def remove(self, value) -> bool:
        if value in self.item_list:
            self.item_list.remove(value)
            return True
        if value.isdigit() and int(value) > 0 and value not in self.item_list:
            self.item_list.pop(int(value) - 1)
            return True
        return False

    def clear(self):
        self.item_list = []

    def list_str(self):
        if len(self.item_list) == 0:
            return "No notes!"
        else:
            items = '\n'.join([str(i + 1) + '. ' + n for i, n in enumerate(self.item_list)])
            return "Notes: \n" + items
