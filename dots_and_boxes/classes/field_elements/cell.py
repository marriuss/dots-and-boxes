class Cell:
    def __init__(self, edges, gui):
        self.possible_edges = set(edges)
        self.centre(edges[0], edges[2])
        self.edges = set()
        self.is_filled = False
        self.color = None
        self.gui = gui

    def make_edge(self, edge, color):
        if not self.is_filled:
            if self.contains(edge) and edge not in self.edges:
                self.edges.add(edge)
                edge.fill(color)
                if len(self.edges) == 4:
                    self.fill(color)

    def cell(self):
        return self, self.is_filled, self.color

    def fill(self, color):
        self.is_filled = True
        self.color = color
        self.gui.draw_dot(self.color, self.centre)

    def centre(self, top, bottom):
        l_corner = (top.dot1.x, top.dot1.y)
        r_corner = (bottom.dot2.x, bottom.dot2.y)
        self.centre = ((l_corner[0] + r_corner[0]) / 2, (l_corner[1] + r_corner[1]) / 2)

    def contains(self, edge):
        return edge in self.possible_edges

    def reset(self):
        self.is_filled = False
        self.color = None
        self.edges = set()
