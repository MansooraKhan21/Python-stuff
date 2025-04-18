from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()

tasks = []

def show_menu():
    console.print("\n[bold magenta]== TO-DO LIST ==[/bold magenta]")
    console.print("1. 📋 View tasks")
    console.print("2. ➕ Add task")
    console.print("3. ❌ Remove task")
    console.print("4. 🚪 Quit")

def view_tasks():
    if not tasks:
        console.print("[italic yellow]No tasks found.[/italic yellow]")
        return
    table = Table(title="Your Tasks", header_style="bold green")
    table.add_column("No.", justify="right")
    table.add_column("Task", justify="left")
    for idx, task in enumerate(tasks, start=1):
        table.add_row(str(idx), task)
    console.print(table)

def add_task():
    task = Prompt.ask("Enter a new task").strip()
    if task:
        tasks.append(task)
        console.print(f"[green]Added:[/green] {task}")
    else:
        console.print("[red]Task can't be empty![/red]")

def remove_task():
    if not tasks:
        console.print("[italic yellow]Nothing to remove.[/italic yellow]")
        return
    view_tasks()
    try:
        idx = IntPrompt.ask("Enter task number to remove")
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            console.print(f"[red]Removed:[/red] {removed}")
        else:
            console.print("[red]Invalid task number.[/red]")
    except ValueError:
        console.print("[red]Please enter a valid number.[/red]")

def main():
    while True:
        show_menu()
        choice = Prompt.ask("Choose an option (1-4)")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            console.print("\n[bold cyan]Goodbye![/bold cyan] 👋")
            break
        else:
            console.print("[red]Invalid option. Choose between 1-4.[/red]")

if __name__ == "__main__":
    main()
