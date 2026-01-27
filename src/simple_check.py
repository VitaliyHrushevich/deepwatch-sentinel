import sqlite3
import os

# ПУТЬ: Убедись, что этот путь верен для твоего Mac
DB_PATH = "/Users/vitaliyhrushevich/Desktop/Projects/LFD/Portfolio(ML)/StatGuard-Metric/data/experiments.db"


def get_ai_analytic_report():
    """Инструмент 1: Детальный отчет по последнему тесту"""
    if not os.path.exists(DB_PATH):
        return "❌ Error: Database StatGuard not found."

    conn = sqlite3.connect(DB_PATH)
    # Позволяет обращаться к колонкам по именам
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT test_name, p_value, lift FROM experiment_logs ORDER BY timestamp DESC LIMIT 1")
        row = cursor.fetchone()

        if not row:
            return "📭 No experiments found in database."

        name, p, lift = row['test_name'], row['p_value'], row['lift']

        # Экспертная логика (Rule-based)
        significance = "СТАТИСТИЧЕСКИ ЗНАЧИМО" if p < 0.05 else "НЕЗНАЧИМО"
        impact = "ВЫСОКИЙ" if lift > 2.0 else "УМЕРЕННЫЙ" if lift > 0.5 else "НИЗКИЙ"

        return (
            f"Анализ теста: '{name}'\n"
            f"- Результат: {significance} (p={p:.4f})\n"
            f"- Влияние (Lift): {impact} ({lift:.2f}%)"
        )
    finally:
        conn.close()


def get_all_significant_tests():
    """Инструмент 2: Сводка всех успешных тестов для анализа трендов"""
    if not os.path.exists(DB_PATH):
        return "Error: Database not found."

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT test_name, lift FROM experiment_logs WHERE is_significant = 1")
        rows = cursor.fetchall()
        if rows:
            results = [f"Test: {r['test_name']}, Lift: {r['lift']:.2f}%" for r in rows]
            return "\n".join(results)
        return "No successful tests in history yet."
    finally:
        conn.close()
