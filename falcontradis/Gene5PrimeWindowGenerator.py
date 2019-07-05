from falcontradis.Window import Window


class Gene5PrimeWindowGenerator:
    def __init__(self, gene_start, max_size, window_size, window_interval):
        self.gene_start = gene_start
        self.max_size = max_size
        self.window_size = window_size
        self.window_interval = window_interval

    def create_windows(self):
        if self.max_size < self.window_size or self.max_size < self.window_interval or self.window_interval < 1 or self.max_size < 1 or self.window_size < 1:
            return []

        start = self.gene_start - self.max_size
        windows = [Window(i, i + self.window_size) for i in range(start, (self.gene_start - self.window_size + 1), self.window_interval)]
        return windows
