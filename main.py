from algorithms.BubbleSort.bubbleSort import BubbleSort
from algorithms.MergeSort.mergeSort import MergeSort
from framework.framework import SortingVisualizerFramework


def start():
    sorting_algorithms = {
        "Bubble Sort": BubbleSort(),
        "Merge Sort": MergeSort(),
        # "Insertion Sort": InsertionSort(),
        # "Selection Sort": SelectionSort(),
        # "Heap Sort": HeapSort(),
        # "Quick Sort": QuickSort(),
        # "Shell Sort": ShellSort(),
        # "Radix Sort": RadixSort()
    }
    # TODO: implement the speed similarly to the algo's
    # speed_selections = {
    #     "Slow": 0.3,
    #     "Medium": 0.1,
    #     "Fast": 0.001
    # }
    framework = SortingVisualizerFramework(sorting_algorithms)
    framework.start()


if __name__ == '__main__':
    start()
