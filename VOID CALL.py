import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def void_response(user_input):
    """Пустота возвращает искаженную версию сказанного"""
    words = user_input.split()
    if not words:
        return "..."
    
    # Перемешиваем слова
    random.shuffle(words)
    # Иногда убираем некоторые
    if random.random() > 0.6:
        words = words[:-1] if words else []
    # Иногда добавляем тишину
    if random.random() > 0.7:
        words.append("...")
    
    result = " ".join(words) if words else "..."
    
    # Делаем строчными
    return result.lower()

def main():
    clear()
    print("=" * 50)
    print("VOID CALL".center(50))
    print("=" * 50)
    print("\nТы звонишь в пустоту.")
    print("Она отвечает только тем, что ты ей дал.")
    print("Никто не придет. Только эхо.")
    print("\nВведите 'выход' чтобы завершить разговор.")
    print("-" * 50)
    
    log = []
    turn = 0
    
    while True:
        print()
        user_input = input("Ты: ")
        
        if user_input.lower() in ['выход', 'exit', 'quit', 'q']:
            break
        
        if not user_input.strip():
            continue
        
        log.append(f"Ты: {user_input}")
        
        # Имитация паузы
        time.sleep(random.uniform(0.8, 1.5))
        
        response = void_response(user_input)
        print(f"Пустота: {response}")
        log.append(f"Пустота: {response}")
        
        turn += 1
        
        # Иногда пустота "молчит"
        if random.random() > 0.85:
            time.sleep(1)
            print("...")
            log.append("...")
    
    # Сохраняем лог на рабочий стол
    import os
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    log_file = os.path.join(desktop, "void_call_log.txt")
    
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("=== VOID CALL LOG ===\n\n")
        f.write("\n".join(log))
        f.write("\n\n=== ЗАМЕТКА ===\n")
        f.write("Ты говорил с пустотой. Пустота ничего не добавила.\n")
        f.write("Всё, что ты услышал — это твои же слова, переставленные.\n")
    
    print("\n" + "=" * 50)
    print(f"[Разговор сохранен на рабочий стол: void_call_log.txt]")
    print("=" * 50)

if __name__ == "__main__":
    main()