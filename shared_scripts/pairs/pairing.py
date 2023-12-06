from shared_scripts import LengthCheck


class MakePairs:
    def __init__(self, list_of_items: list):
        LengthCheck.check(list_of_items, desired_length=2)
        self.__pairs = []
        self.__list_of_items = list_of_items

    def __draw(self):
        current_index = 0
        end_index = len(self.__list_of_items)

        while current_index < end_index:
            item1 = self.__list_of_items[current_index]

            for item2 in self.__list_of_items[current_index + 1:]:
                self.__pairs.append((item1, item2))
            current_index += 1
        return self

    def get_pairs(self):
        self.__draw()
        return self.__pairs
