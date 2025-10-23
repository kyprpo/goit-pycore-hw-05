import sys
from pathlib import Path

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
        return logs
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до файлу логів.")
        sys.exit()

    log_path = Path(sys.argv[1])
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(log_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")
