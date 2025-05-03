from mine.pygame_template import *

GRID_W, GRID_H = 50, 50
CELL_SIZE = 17



# ENTER for manual stepping
# SPACE for run toggle
# click to activate or deactivate cell



class run(APP):
    def init(self):
        self.WIDTH = GRID_W * CELL_SIZE
        self.HEIGHT = GRID_H * CELL_SIZE

    def setup(self):
        self.array = [[False for i in range(GRID_W)] for j in range(GRID_H)]
        self.buffer_array = [row.copy() for row in self.array]

        self.should_run = False
        self.continue_run = False
        self.update_event = pygame.USEREVENT
        pygame.time.set_timer(self.update_event, 50)

    def update(self):
        m_pos = V2(pygame.mouse.get_pos())
        m_down = pygame.mouse.get_just_pressed()[0]

        m_pos /= CELL_SIZE
        if m_down:
            self.array[int(m_pos.y)][int(m_pos.x)] = not self.array[int(m_pos.y)][int(m_pos.x)]
        self.handle_life()

    def handle_life(self):
        key = pygame.key.get_just_pressed()
        if key[pygame.K_RETURN] or self.should_run:
            self.buffer_array = [row.copy() for row in self.array]
            for j in range(GRID_H):
                for i in range(GRID_W):
                    count = self.count_neighbours(i, j)
                    if self.array[j][i]:
                        if count < 2 or count > 3: self.buffer_array[j][i] = False
                        else: self.buffer_array[j][i] = True
                    else:
                        if count == 3: self.buffer_array[j][i] = True
                        else: self.buffer_array[j][i] = False
            self.array = [row.copy() for row in self.buffer_array]
            self.should_run = False

    def count_neighbours(self, i, j):
        count = 0
        for dj in range(-1, 2):
            for di in range(-1, 2):
                if di == 0 and dj == 0: continue
                ni, nj = i + di, j + dj
                if 0 <= ni < GRID_W and 0 <= nj < GRID_H:
                    if self.array[nj][ni]: count += 1
        return count

    def draw(self):
        for j in range(GRID_H):
            for i in range(GRID_W):
                if self.array[j][i]:
                    pygame.draw.rect(self.screen, Color.deeppink, (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0, 4)
                else:
                    pygame.draw.rect(self.screen, Color.lightpink, (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0, 4)
                pygame.draw.rect(self.screen, Color.maroon, (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1, 4)

    def event(self, e):
        if e.type == self.update_event and self.continue_run:
            self.should_run = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            self.continue_run = not self.continue_run

run()
