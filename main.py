from app.algorithms.BubbleSort.bubbleSort import BubbleSort
from app.algorithms.InsertionSort import InsertionSort
from app.algorithms.MergeSort.mergeSort import MergeSort
from app.framework.sortingVisualizer import SortingVisualizerFramework


def start():
    sorting_algorithms = {
        "Bubble Sort": BubbleSort(),
        "Merge Sort": MergeSort(),
        "Insertion Sort": InsertionSort,
        # "Selection Sort": SelectionSort(),
        # "Heap Sort": HeapSort(),
        # "Quick Sort": QuickSort(),
        # "Shell Sort": ShellSort(),
        # "Radix Sort": RadixSort()
    }
    speed_selections = {
        "Slowest": 0.6,
        "Slow": 0.3,
        "Medium": 0.1,
        "Fast": 0.01,
        "Faster": 0.001,
        "Fastest": 0.0001,
    }
    framework = SortingVisualizerFramework(sorting_algorithms, speed_selections)
    framework.start()


if __name__ == '__main__':
    start()
