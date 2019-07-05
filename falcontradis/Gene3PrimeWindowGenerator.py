from falcontradis.Window import Window


class Gene3PrimeWindowGenerator:
    def __init__(self, gene_end, max_size, window_size, window_interval):
        self.gene_end = gene_end
        self.max_size = max_size
        self.window_size = window_size
        self.window_interval = window_interval

    def create_windows(self):
        if self.max_size < self.window_size or self.max_size < self.window_interval or self.window_interval < 1 or self.max_size < 1 or self.window_size < 1:
            return []

        end = self.gene_end + self.max_size - self.window_size + 1
        windows = [Window(i, i + self.window_size) for i in range(self.gene_end, end, self.window_interval)]
        return windows
