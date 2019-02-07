import math

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

class BlobGame:
    def __init__(self):
        self.blobs = []
        self.grid_height, self.grid_width = 0, 0
        self.grid = [[]]
        
    def play_game(self, blobs, render=False):
        self.init_grid(blobs)
        while True:
            if render:
                self.render_blobs()
            if not self.make_moves(): 
                break
            self.merge_blobs()
        return self.blobs

    def init_grid(self, blobs):
        self.blobs = blobs
        max_x, max_y = 0, 0
        for blob in self.blobs:
            if blob[0] > max_x:
                max_x = blob[0]
            if blob[1] > max_y:
                max_y = blob[1]
        self.grid_width, self.grid_height = max_x + 1, max_y + 1

    def make_moves(self):
        moved = False
        for index, blob in enumerate(self.blobs):
            target_blob = self.get_target(blob)
            if (target_blob is not None):
                self.move_toward(index, target_blob)
                moved = True
        return moved
    
    def merge_blobs(self):
        grid = [[0 for x in range(self.grid_width)] for y in range(self.grid_height)]
        for blob in self.blobs:
            coord_x, coord_y = blob[0], -(blob[1] + 1)
            grid[coord_y][coord_x] += blob[2]
        new_blobs = []
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                if grid[i][j] != 0:
                    new_blob = (j, -(i - self.grid_height + 1), grid[i][j])
                    new_blobs.append(new_blob)
        self.blobs = new_blobs

    # Return the blob which should be targeted.
    def get_target(self, blob):
        target_index = -1
        for index, candidate in enumerate(self.blobs):
            if candidate != blob and candidate[2] < blob[2]:
                if target_index == -1:
                    target_index = index
                    continue
                current_target = self.blobs[target_index]
                current_target_distance = self.distance(blob, current_target)
                candidate_distance = self.distance(blob, candidate)
                if candidate_distance < current_target_distance:
                    target_index = index
                elif candidate_distance == current_target_distance:
                    current_target_size = current_target[2]
                    candidate_size = candidate[2]
                    if candidate_size > current_target_size:
                        target_index = index
                    elif candidate_size == current_target_size:
                        if self.clockwise_comparison(blob, candidate, current_target) == 0:
                            target_index = index

        if target_index == -1:
            return None

        return self.blobs[target_index]

    def distance(self, blob_a, blob_b):
        return math.sqrt((blob_b[0] - blob_a[0])**2 + (blob_b[1] - blob_a[1])**2)


    # Returns 0 if target_a is more clockwise from blob than target_b, else 1.
    def clockwise_comparison(self, blob, target_a, target_b):
        
    # Moves the blob to the position which minimizes the distance between blob and target
    def move_toward(self, blob_index, target):
        blob = self.blobs[blob_index]
        move_index = 0
        for i in range(1, len(MOVES)):
            current_move_position = (blob[0] + MOVES[move_index][0], blob[1] + MOVES[move_index][1])
            candidate_position = (blob[0] + MOVES[i][0], blob[1] + MOVES[i][1])
            if self.distance(candidate_position, target) < self.distance(current_move_position, target):
                move_index = i
        move = MOVES[move_index]
        blob_list = list(self.blobs[blob_index])
        blob_list[0] = blob[0] + move[0]
        blob_list[1] = blob[1] + move[1]
        self.blobs[blob_index] = tuple(blob_list)

    def render_blobs(self):
        grid = [["X" for x in range(self.grid_width)] for y in range(self.grid_height)]
        for blob in self.blobs:
            grid[-(blob[1] + 1)][blob[0]] = str(blob[2])
        for i in range(self.grid_height):
            for j in range(self.grid_width):
                print(grid[i][j], end=' ')
            print()
        print()

game = BlobGame()
print(game.play_game([(4, 3, 4),(4, 6, 2),(8, 3, 2),(2, 1, 3)]))
            

