from os import system, name
import time
import click
from prompt_toolkit.formatted_text import HTML
from rich.console import Console
from config import SPEED

console = Console()


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def algo_wrapper(func):
    def wrapper(*args, **kwargs):
        clear_screen()
        algo_name = func.__doc__
        input = args[0]
        console.print(algo_name, style='#5CB270')
        console.print(input)
        print('', end="\r")
        time.sleep(SPEED)
        result = func(*args, **kwargs)
        time.sleep(SPEED)

        print('', end='\r')
        print(input, end='\r')
        console.print(
            f'The [bold]{algo_name}[bold] has been completed in [{result["steps"]-1}] steps.', style='#EDE342')
        console.print(result['list'], style='#E85C90')
    return wrapper


def visualize_compare(list, m, n, steps):
    print('\r', end='')
    click.secho(f'{steps}', nl=False, fg='red')
    for i in range(len(list)):
        if i == m or i == n:
            click.secho(f' {list[i]} ', nl=False, fg='blue')
        else:
            click.secho(f' {list[i]} ', nl=False, fg='green')
    time.sleep(SPEED)


def footer():
    return HTML('Made with 🧡 by <a href="https://techika.com">Truong Phan</a>')
