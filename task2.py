import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """Повертає генератор чисел з тексту."""
    for match in re.findall(r"\d+\.\d+|\d+", text):
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    """Обчислює суму чисел, знайдених генератором."""
    return sum(func(text))

if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
