from heapq import heappush, heappop


class AdvancedList:
    def __init__(self):
        self.data = []
        self.small = []  # max heap for smaller half
        self.large = []  # min heap for larger half
        self.history = []
        self.redo_stack = []

    def _update_heaps(self):
        self.small, self.large = [], []
        for num in self.data:
            self._add_to_heaps(num)

    def _add_to_heaps(self, num):
        if len(self.small) == 0 or -self.small[0] > num:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)

        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
        elif len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def _save_state(self, action):
        self.history.append((action, self.data[:]))
        self.redo_stack.clear()

    def insert(self, index, value):
        self._save_state(('insert', index, value))
        self.data.insert(index, value)
        self._update_heaps()

    def delete_by_index(self, index):
        if 0 <= index < len(self.data):
            self._save_state(('delete', index, self.data[index]))
            del self.data[index]
            self._update_heaps()
            return True
        return False

    def get_median(self):
        if not self.data:
            return None
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (self.large[0] - self.small[0]) / 2

    def kth_smallest(self, k):
        if not 1 <= k <= len(self.data):
            return None
        return sorted(self.data)[k - 1]

    def undo(self):
        if not self.history:
            return False
        action = self.history.pop()
        self.redo_stack.append((action[0], self.data[:]))
        self.data = action[1]
        self._update_heaps()
        return True

    def redo(self):
        if not self.redo_stack:
            return False
        action = self.redo_stack.pop()
        self.history.append((action[0], self.data[:]))
        self.data = action[1]
        self._update_heaps()
        return True


def main():
    lst = AdvancedList()

    while True:
        print("\nAdvanced List Operations:")
        print("1. Insert number")
        print("2. Delete by index")
        print("3. Find kth smallest")
        print("4. Get median")
        print("5. Undo")
        print("6. Redo")
        print("7. Show list")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        try:
            if choice == '1':
                value = int(input("Enter number to insert: "))
                index = int(input("Enter position to insert (0 to append): "))
                if index == 0:
                    index = len(lst.data)
                lst.insert(index, value)
                print(f"Inserted {value} at position {index}")

            elif choice == '2':
                if not lst.data:
                    print("List is empty!")
                    continue
                print(f"Current list: {lst.data}")
                index = int(input("Enter index to delete: "))
                if lst.delete_by_index(index):
                    print(f"Deleted element at index {index}")
                else:
                    print("Invalid index!")

            elif choice == '3':
                if not lst.data:
                    print("List is empty!")
                    continue
                k = int(input(f"Enter k (1 to {len(lst.data)}): "))
                result = lst.kth_smallest(k)
                if result is not None:
                    print(f"The {k}th smallest element is: {result}")
                else:
                    print("Invalid k!")

            elif choice == '4':
                median = lst.get_median()
                if median is not None:
                    print(f"Median is: {median}")
                else:
                    print("List is empty!")

            elif choice == '5':
                if lst.undo():
                    print("Undo successful")
                else:
                    print("Nothing to undo!")

            elif choice == '6':
                if lst.redo():
                    print("Redo successful")
                else:
                    print("Nothing to redo!")

            elif choice == '7':
                print(f"Current list: {lst.data}")

            elif choice == '8':
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")


if __name__ == "__main__":
    main()