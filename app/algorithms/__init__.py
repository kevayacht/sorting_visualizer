import inspect
import sys
import importlib
import re

from app.algorithms.algorithm import Algorithm
from app.algorithms.BubbleSort.bubbleSort import BubbleSort
from app.algorithms.MergeSort.mergeSort import MergeSort
from app.algorithms.QuickSort.quickSort import QuickSort
from app.algorithms.SelectionSort.selectionSort import SelectionSort
from app.algorithms.ShellSort.shellSort import ShellSort
from app.algorithms.InsertionSort.insertionSort import InsertionSort
from app.algorithms.CountingSort.countingSort import CountingSort
from app.algorithms.OpiBubbleSort.optiBubbleSort import OptiBubbleSort


def get_sorting_algorithms() -> dict:
    classMembers = inspect.getmembers(
        sys.modules[__name__],
        lambda x: inspect.isclass(x) and issubclass(x, Algorithm)
    )

    importlib.import_module("app.algorithms", "algorithms")
    sorting_algorithms = {}
    for item in classMembers:
        print(item)
        if item[0] == Algorithm.__name__:
            continue
        sorting_algorithms[re.sub(r"(\w)([A-Z])", r"\1 \2", item[0])] = item[1]()

    return sorting_algorithms


def print_classes():
    classMembers = inspect.getmembers(
        sys.modules[__name__],
        lambda x: inspect.isclass(x) and issubclass(x, Algorithm)
    )

    for item in classMembers:
        if item[0] == Algorithm.__name__:
            continue
        print(re.sub(r"(\w)([A-Z])", r"\1 \2", item[0]))
