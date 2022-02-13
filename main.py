from app.algorithms import get_sorting_algorithms
from app.framework.sortingVisualizer import SortingVisualizerFramework


def start():
    speed_selections = {
        "Slowest": 0.6,
        "Slow": 0.3,
        "Medium": 0.1,
        "Fast": 0.01,
        "Faster": 0.001,
        "Fastest": 0.0001,
    }
    data_range = {}  # introduce a data range selection.
    framework = SortingVisualizerFramework(get_sorting_algorithms(), speed_selections)
    framework.start()


if __name__ == '__main__':
    start()
