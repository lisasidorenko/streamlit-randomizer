import random
import streamlit as st
from streamlit_server_state import server_state, server_state_lock

# Начальный список слов
words = ["Кринж", "Радость", "Грусть", "Страх", "Отвращение", "Удивление", 
         "Брезгливость", "Смущение", "Зависть", "ЧСВ", "Ностальгия", "Навязчивость"]

# Функция для загрузки оставшихся слов
def load_words():
    with server_state_lock:
        if "remaining_words" not in server_state:
            server_state.remaining_words = words.copy()  # Инициализируем список слов на сервере
        if "word_chosen" not in server_state:
            server_state.word_chosen = False  # Инициализируем состояние выбора слова
    return server_state.remaining_words

# Функция для сохранения обновлённого списка слов
def save_words(remaining_words):
    with server_state_lock:
        server_state.remaining_words = remaining_words

# Основная функция приложения
def main():
    st.title("Рандомайзер эмоций")
    st.write("Нажмите на кнопку, чтобы получить случайную эмоцию. Каждая эмоция выпадает только один раз для всех пользователей.")

    # Загружаем список оставшихся слов
    remaining_words = load_words()

    # Проверяем, есть ли оставшиеся слова
    if remaining_words:
        if st.button("Выбрать случайную эмоцию"):
            # Выбираем случайное слово и удаляем его из списка
            selected_word = random.choice(remaining_words)
            remaining_words.remove(selected_word)
            save_words(remaining_words)  # Сохраняем обновлённый список на сервере
 
             # Устанавливаем состояние выбора слова в True
            with server_state_lock:
                    server_state.word_chosen = True

            # Выводим выбранное слово
            st.success(f"Ваша эмоция: {selected_word}")
        else:
            st.warning("Уго! Обязательно запомни свою эмоцию, ведь тебе нужно будет её презентовать в субботу!;)")
    else:
        st.warning("Упс, кажется эмоций больше не осталось:(")

if __name__ == "__main__":
    main()