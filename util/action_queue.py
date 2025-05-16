class ActionQueue [T]:
    def __init__(self):
        self.curr_ptr = 0
        self.actual_container = list[T]()

    def push(self, element: T) -> None:
        self.actual_container.append(element)

    def next(self) -> T:
        if self.curr_ptr >= len(self.actual_container):
            self.curr_ptr = 0
        result =  self.actual_container[self.curr_ptr]
        self.curr_ptr += 1
        return result

    def remove_items(self, indices: list[int]) -> None:
        for index in indices:
            self.actual_container.pop(index)

    def get_actual_container(self) -> list[T]:
        return self.actual_container

    def __getitem__(self, item) -> T:
        return self.actual_container[item]

    def __len__(self) -> int:
        return len(self.actual_container)

