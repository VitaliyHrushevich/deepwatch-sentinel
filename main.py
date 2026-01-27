import sys
import os

# Добавляем src в пути поиска модулей
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.core.llm_client import ask_ollama
from src.simple_check import get_ai_analytic_report, get_all_significant_tests


def start_sentinel():
    print("🛰️ DeepWatch Sentinel System: Booting...")

    # 1. Сбор данных (Context Collection)
    print("🔍 Collecting metrics and historical trends...")
    latest_report = get_ai_analytic_report()
    history = get_all_significant_tests()

    # Формируем полный контекст для ИИ
    full_context = (
        f"ДАННЫЕ ПОСЛЕДНЕГО ЭКСПЕРИМЕНТА:\n{latest_report}\n\n"
        f"ИСТОРИЯ УСПЕШНЫХ ЭКСПЕРИМЕНТОВ:\n{history}"
    )

    # 2. Формируем запрос
    question = (
        "Сравни последний результат с историей прошлых тестов. "
        "Насколько стабильно мы улучшаем систему? "
        "Дай краткий вердикт: готовы ли мы к релизу обновления?"
    )

    print("🤖 AI Agent is analyzing data patterns...")

    try:
        # 3. Вызов ИИ (Убедись, что модель llama3 скачана)
        response = ask_ollama(
            user_query=question,
            context_data=full_context,
            model="llama3"
        )

        print("\n" + "—" * 50)
        print("🟢 SENTINEL FINAL VERDICT:")
        print(response)
        print("—" * 50)

    except Exception as e:
        print(f"❌ System Error: {e}")


if __name__ == "__main__":
    start_sentinel()
