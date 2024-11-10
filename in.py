def double_directory_size(self):
    total_size = 0
    for item in self.listdir():
        if item.is_file():
            total_size += item.size() * 2
        elif item.is_dir():
            total_size += item.size() * 2
            total_size += self.double_directory_size(item)
    return total_size
