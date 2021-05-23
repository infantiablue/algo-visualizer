import random
import sys
from prompt_toolkit import prompt
from rich.console import Console
from config import ARRAY_SIZE
from ui import algo_wrapper, visualize_compare, clear_screen, footer
console = Console()


@algo_wrapper
def BubbleSort(list):
    '''Buble Sort'''
    lastElementIndex = len(list)-1
    steps = 1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            visual = list.copy()
            visual[idx] = f'[ {visual[idx]} ]'
            visual[idx+1] = f'[ {visual[idx+1]} ]'
            visualize_compare(visual, idx, idx+1, steps)
            if list[idx] > list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
                visual = list.copy()
                visual[idx] = f' {visual[idx]} >>'
                visual[idx+1] = f'<< {visual[idx+1]} '
                visualize_compare(visual, idx, idx+1, steps)
            steps += 1
    result = {'list': list, 'steps': steps}
    return result


@algo_wrapper
def InsertionSort(list):
    '''Insertion Sort'''
    steps = 1
    for i in range(1, len(list)):
        visual = list.copy()
        j = i-1
        element_next = list[i]
        # Visualize
        visual[j] = f'[ {visual[j]} ]'
        visual[j+1] = f'[ {element_next} ]'
        visualize_compare(visual, j, j+1, steps)
        steps += 1

        while (list[j] > element_next) and (j >= 0):
            visual = list.copy()
            vj = j
            list[j+1] = list[j]
            j = j-1
            # Visualize
            visual[vj+1] = f'<< {element_next} '
            visual[vj] = f' {visual[vj]} >>'
            visualize_compare(visual, vj, vj+1, steps)
            steps += 1
        list[j+1] = element_next
    result = {'list': list, 'steps': steps}
    return result


@algo_wrapper
def ShellSort(list):
    '''Shell Sort'''
    steps = 1
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            visual = list.copy()
            visual[j] = f'[ {visual[j]} ]'
            visual[j-distance] = f'[ {visual[j-distance]} ]'
            visualize_compare(visual, j, j-distance, steps)
            steps += 1
            while j >= distance and list[j - distance] > temp:
                visual = list.copy()
                visual[j] = f' {list[j - distance]} >>'
                visual[j-distance] = f'<< {list[j]} '
                visualize_compare(visual, j, j-distance, steps)

                list[j] = list[j - distance]
                j = j-distance
                steps += 1
            list[j] = temp
        # Reduce the distance for the next element
        distance = distance//2
    result = {'list': list, 'steps': steps}
    return result


if __name__ == "__main__":
    while True:
        clear_screen()
        console.print("Algorithm Visualization", style='#a2d2ff')
        console.print("1. [bold]Bubble Sort[/bold]")
        console.print("2. [bold]Insertion Sort[/bold]")
        console.print("3. [bold]Shell Sort[/bold]")
        console.print("q. Quit", style="#e63946")
        print()
        randomlist = random.sample(range(1, 100), ARRAY_SIZE)
        ans = 48
        while ans != 113 and (ans < 49 or ans > 51):
            ans = prompt('Choose the algorithm to run or enter to exit: ',
                         bottom_toolbar=footer)
            if ans:
                ans = ord(ans)
            else:
                sys.exit()

        if ans == 113:
            sys.exit()
        else:
            if chr(ans) == '1':
                BubbleSort(randomlist)
            elif chr(ans) == '2':
                InsertionSort(randomlist)
            elif chr(ans) == '3':
                ShellSort(randomlist)
        try:
            print()
            input("Press enter to continue")
        except SyntaxError:
            pass
