class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size
    
    def __del__(self):
        print(f"Файл {self.name}.{self.extension} видалено.")
    
    def __str__(self):
        return f"Файл: {self.name}.{self.extension}, Розмір: {self.size} байт"
    

class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []
    
    def __del__(self):
        print(f"Папка {self.name} видалена.")

    def __str__(self):
        content_list = "\n".join([str(item) for item in self.contents])
        return f"Папка: {self.name}\nВміст:\n{content_list if content_list else 'Порожня'}"
    
    def add_item(self, item):
        self.contents.append(item)
    
    def print_tree(self, level=0):
        indent = "  " * level
        print(f"{indent}Папка: {self.name}")
        for item in self.contents:
            if isinstance(item, Folder):
                item.print_tree(level + 1)
            else:
                print(f"{indent}  - {item}")
    
    def longest_path(self, current_path="/"):
        longest = current_path + self.name
        for item in self.contents:
            if isinstance(item, Folder):
                longest_subfolder = item.longest_path(current_path + self.name + "/")
                if len(longest_subfolder) > len(longest):
                    longest = longest_subfolder
            else:
                longest_file = current_path + self.name + "/" + item.name + "." + item.extension
                if len(longest_file) > len(longest):
                    longest = longest_file
        return longest
    def find_folder(self, name):
        if self.name == name:
            return self
        for item in self.contents:
            if isinstance(item, Folder):
                found = item.find_folder(name)
                if found:
                    return found
        return None


def main():
    file1 = File("file1", "txt", 120)
    file2 = File("file2", "jpg", 1500)
    file3 = File("file3", "pdf", 230)
    
    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    folder3 = Folder("folder3")
    
    folder1.add_item(file1)
    folder1.add_item(file2)
    folder2.add_item(file3)
    
    folder3.add_item(folder1)
    folder3.add_item(folder2)
    
    print("Дерево файлів:")
    folder3.print_tree()
    
    print("\nНайдовший шлях до об'єкту:")
    print(folder3.longest_path())

    print("\nІнформація про папку:")
    print(folder3)
    while True:
        folder_name = input("\nВведіть назву папки, яку ви хочете вивести:")
        if folder_name.lower() == "вихід":
            print("Завершення роботи.")
            break
        found_folder = folder3.find_folder(folder_name)
        if found_folder:
            print("\nДерево вибраної папки:")
            found_folder.print_tree()
        else:
            print(f"Папка з назвою '{folder_name}' не знайдена.")

    


main()