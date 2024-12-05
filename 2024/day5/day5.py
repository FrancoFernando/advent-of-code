from collections import defaultdict

class Solution:

    def __init__(self):
        self.rules = defaultdict(set)
        self.updates = []
        self.valid_updates = []
        self.invalid_updates = []
        self.parse_input()

    def parse_input(self):
        
        with open("input.txt", 'r') as file:
            # Parse rules
            for line in file:
                if line.strip() == "":
                    break
                a, b = map(int, line.strip().split('|'))
                self.rules[a].add(b)
            
            # Parse updates
            for line in file:
                self.updates.append(list(map(int, line.strip().split(','))))

    def topological_sort(self, graph, nodes):
        in_degree = {node: 0 for node in nodes}
        for node in nodes:
            for neighbor in graph[node]:
                if neighbor in nodes:
                    in_degree[neighbor] += 1
        
        queue = [node for node in nodes if in_degree[node] == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor in nodes:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
        
        return result if len(result) == len(nodes) else None


    def part_one(self): 

        result = 0
    
        for update in self.updates:
            subgraph = {page: self.rules[page].intersection(set(update)) for page in update}
            sorted_pages = self.topological_sort(subgraph, update)
            
            if sorted_pages == update:
                mid_index = len(update) // 2
                result += update[mid_index]
                self.valid_updates.append(update)
            else:
                self.invalid_updates.append(update)

        print(result)
        return result
    
    def order_update(self, update):
        
        # If topological sort fails, use a greedy approach
        remaining = set(update)
        ordered = []
        while remaining:
            # Find a page that has no predecessors in the remaining set
            for page in remaining:
                if not any(pred in remaining for pred in self.rules if page in self.rules[pred]):
                    ordered.append(page)
                    remaining.remove(page)
                    break
            else:
                # If no such page is found, we have a cycle. Break it arbitrarily.
                page = remaining.pop()
                ordered.append(page)

        return ordered
    
    def part_two(self):
        result = 0

        for update in self.invalid_updates:
            reordered_update = self.order_update(update)
            mid_index = len(reordered_update) // 2
            result += reordered_update[mid_index]

        print(result)
        return result
        
if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()