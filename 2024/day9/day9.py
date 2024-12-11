class Solution:

    def __init__(self):
        self.disk = []
        self.disk_copy = []
        self.total_space = 0
        self.file_positions = []
        self.parse_input()

    def parse_input(self):

        with open('input.txt') as file: 
            data = [int(char) for char in file.read().strip()]

        files = data[::2]
        spaces = data[1::2]
        current_position = 0
        for i, (file_len, space_len) in enumerate(zip(files, spaces)):
            self.file_positions.append((current_position, file_len, i))
            self.disk.extend([str(i)] * file_len)
            self.disk.extend(['.'] * space_len)
            self.total_space += space_len
            current_position += file_len + space_len

        if len(files) > len(spaces):
            self.disk.extend([str(len(files)-1)] * files[-1])
            self.file_positions.append((current_position, files[-1], len(files) - 1))

        self.disk_copy = self.disk.copy()


    def part_one(self):
        free_space_start = len(self.disk) - self.total_space
        for i in range(len(self.disk) - 1, -1, -1):
            if self.disk[i] != '.':
                for j in range(len(self.disk)):
                    if self.disk[j] == '.':
                        self.disk[j], self.disk[i] = self.disk[i], self.disk[j]
                        break

            if i == free_space_start:
                break  # All files are now contiguous

        checksum = sum(i * int(char) for i, char in enumerate(self.disk) if char != '.')
        print(checksum)
        return checksum

    def part_two(self):
        
        self.disk = self.disk_copy
        for file_start, file_len, file_id in reversed(self.file_positions):
            # Find the leftmost free space
            target_position = None
            for i in range(file_start):
                if all(self.disk[j] == '.' for j in range(i, i + file_len)):
                    target_position = i
                    break
            
            # Move the file if a suitable position was found
            if target_position is not None and target_position != file_start:
                file_content = self.disk[file_start:file_start + file_len]
                self.disk[target_position:target_position + file_len] = file_content
                self.disk[file_start:file_start + file_len] = ['.'] * file_len

        checksum = sum(i * int(char) for i, char in enumerate(self.disk) if char != '.')
        print(checksum)
        return checksum


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()

""" def compact_disk(input_str):
    # Parse the input string
    lengths = [int(char) for char in input_str]
    files = lengths[::2]
    spaces = lengths[1::2]

    # Create the initial disk layout
    disk = []
    for i, (file_len, space_len) in enumerate(zip(files, spaces)):
        disk.extend([str(i)] * file_len)
        disk.extend(['.'] * space_len)
    if len(files) > len(spaces):
        disk.extend([str(len(files)-1)] * files[-1])

    print(''.join(disk))  # Initial state

    # Compact the disk
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != '.':
            for j in range(len(disk)):
                if disk[j] == '.':
                    disk[j], disk[i] = disk[i], disk[j]
                    break
        print(''.join(disk))  # Print each step

    # Calculate checksum
    checksum = sum(i * int(char) for i, char in enumerate(disk) if char != '.')
    
    return checksum

# Test the function
input_str = "2333133121414131402"
result = compact_disk(input_str)
print(f"Checksum: {result}") """