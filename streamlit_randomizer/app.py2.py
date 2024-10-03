import random  # Для генерации случайных чисел
import streamlit as st  # Для создания веб-интерфейса
from streamlit_server_state import server_state, server_state_lock

# Имя файла, в котором будет храниться список оставшихся слов
FILE_NAME = "remaining_words.txt"

# Заранее заданный список слов
words = ["Кринж", "Радость", "Грусть", "Страх", "Отвращение", "Удивление", "Брезгливость", "Смущение", "Зависть", "ЧСВ", "Ностальгия", "Навязчивость"]

# Функция для загрузки оставшихся слов
def load_words():
    with server_state_lock:
        if "remaining_words" not in server_state:
            server_state.remaining_words = words.copy()  # Инициализируем список слов на сервере
    return server_state.remaining_words

# Функция для сохранения обновлённого списка слов
def save_words(remaining_words):
    with server_state_lock:
        server_state.remaining_words = remaining_words
        
# Основная функция приложения
def main():
    # Заголовок приложения
    st.title("Рандомайзер эмоций")
    st.write("Нажмите на кнопку, чтобы получить случайную эмоцию. Каждая эмоция может выпасть только один раз.")

    # Загружаем список оставшихся слов
    remaining_words = load_words()

   # Проверяем, есть ли оставшиеся слова
    if remaining_words:
        if st.button("Выбрать случайное слово"):
            # Выбираем случайное слово и удаляем его из списка
            selected_word = random.choice(remaining_words)
            remaining_words.remove(selected_word)
            save_words(remaining_words)  # Сохраняем обновлённый список на сервере
            
            # Выводим выбранное слово
            st.success(f"Выбранное слово: {selected_word}")
        else:
            st.info("Нажмите кнопку, чтобы выбрать слово.")
    else:
        st.warning("Все слова были выбраны! Обновите страницу, чтобы начать заново.")

# Запуск главной функции приложения
if __name__ == "__main__":
    main()