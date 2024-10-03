import random  # Для генерации случайных чисел
import streamlit as st  # Для создания веб-интерфейса
import os
# Имя файла, в котором будет храниться список оставшихся слов
FILE_NAME = "remaining_words.txt"

# Заранее заданный список слов
words = ["Кринж", "Радость", "Грусть", "Страх", "Отвращение", "Удивление", "Брезгливость", "Смущение", "Зависть", "ЧСВ", "Ностальгия", "Навязчивость"]

# Функция для чтения оставшихся слов из файла
def load_words():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            remaining_words = file.read().splitlines()
    else:
        remaining_words = words.copy()  # Если файла нет, используем исходный список слов
        save_words(remaining_words)  # Сохраняем его в файл
    return remaining_words

# Функция для сохранения оставшихся слов в файл
def save_words(remaining_words):
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(remaining_words))
        
# Основная функция приложения
def main():
    # Заголовок приложения
    st.title("Рандомайзер эмоций")
    st.write("Нажмите на кнопку, чтобы получить случайную эмоцию. Каждая эмоция может выпасть только один раз.")

    # Загружаем список оставшихся слов
    remaining_words = load_words()

    # Проверяем, есть ли оставшиеся слова
    if remaining_words:
        if st.button("Выбрать"):
            # Выбираем случайное слово и удаляем его из списка
            selected_word = random.choice(remaining_words)
            remaining_words.remove(selected_word)
            save_words(remaining_words)  # Сохраняем обновлённый список в файл

            # Выводим выбранное слово
            st.success(f"Эмоция: {selected_word}")
        else:
            st.info("Нажмите кнопку, чтобы выбрать слово.")
    else:
        st.warning("Упс, кажется все эмоции уже разобрали:(")
    
# Запуск главной функции приложения
if __name__ == "__main__":
    main()
    
