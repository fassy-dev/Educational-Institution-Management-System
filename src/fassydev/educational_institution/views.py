from .logger import logger
from .models import StudentsManagement


def main_loop():
    logger.info("=== Программа запущена ===")

    school = StudentsManagement(
        "Лицей №42",
        "ул. Ау да здравствует Санкт-Петербург",
        "Университет",
        "52-67"
    )

    while True:
        print(f"\n\n--- Меню управления: {school.name} ---")
        print("1. Показать информацию об учреждении")
        print("2. Показать список студентов")
        print("3. Показать список учителей")
        print("4. Зачислить студента")
        print("5. Отчислить студента")
        print("6. Нанять учителя")
        print("7. Уволить учителя")
        print("0. Выход")

        try:
            choice = input("\nВыберите действие (0-7): ").strip()
        except KeyboardInterrupt:
            print("\n Обнаружено прерывание (Ctrl+C). Завершаем работу...")
            logger.warning("Программа была прервана пользователем (Ctrl+C)")
            break

        try:
            if choice == "1":
                print(school)
                logger.debug("Пользователь запросил информацию об учреждении")

            elif choice == "2":
                if school.students:
                    print("\nСписок студентов:")
                    for s_id, name in school.students.items():
                        print(f"ID: {s_id} | Имя: {name}")
                else:
                    print("\nСтудентов пока нет.")
                logger.debug("Показан список студентов")

            elif choice == "3":
                if school.teachers:
                    print("\nСписок учителей:")
                    for t_id, name in school.teachers.items():
                        print(f"ID: {t_id} | Имя: {name}")
                else:
                    print("\nУчителей пока нет.")
                logger.debug("Показан список учителей")

            elif choice == "4":
                s_id = input("Введите ID нового студента: ").strip()
                name = input("Введите ФИО нового студента: ").strip()
                try:
                    school.enroll_student(s_id, name)
                    msg = f"Студент {name} успешно зачислен."
                    print(msg)
                    logger.info(f"Студент зачислен: ID={s_id}, Имя={name}")
                except ValueError as e:
                    err_msg = f"Ошибка: {e}"
                    print(err_msg)
                    logger.warning(err_msg)

            elif choice == "5":
                s_id = input("Введите ID студента для отчисления: ").strip()
                if school.expel_student(s_id):
                    msg = f"Студент с ID {s_id} отчислен."
                    print(msg)
                    logger.info(f"Студент отчислен: ID={s_id}")
                else:
                    print("Студент с таким ID не найден.")
                    logger.debug(f"Попытка отчисления несуществующего студента: ID={s_id}")

            elif choice == "6":
                t_id = input("Введите ID нового учителя: ").strip()
                name = input("Введите ФИО нового учителя: ").strip()
                try:
                    school.hire_teacher(t_id, name)
                    msg = f"Учитель {name} устроен на работу."
                    print(msg)
                    logger.info(f"Учитель нанят: ID={t_id}, Имя={name}")
                except ValueError as e:
                    err_msg = f"Ошибка: {e}"
                    print(err_msg)
                    logger.warning(err_msg)

            elif choice == "7":
                t_id = input("Введите ID учителя для увольнения: ").strip()
                if school.fire_teacher(t_id):
                    msg = f"Учитель с ID {t_id} уволен."
                    print(msg)
                    logger.info(f"Учитель уволен: ID={t_id}")
                else:
                    print("Учитель с таким ID не найден.")
                    logger.debug(f"Попытка увольнения несуществующего учителя: ID={t_id}")

            elif choice == "0":
                print("Выход из программы. До свидания!")
                logger.info("Пользователь инициировал выход из программы")
                break

            else:
                print("Неверный ввод. Попробуйте снова (числа от 0 до 7).")
                logger.debug(f"Неверный ввод пользователя: '{choice}'")

        except KeyboardInterrupt:
            print("\nНеожиданное прерывание во время операции.")
            logger.error("Операция прервана пользователем")
            break
        except Exception as e:
            print(f"\nПроизошла непредвиденная ошибка: {e}")
            logger.critical(f"Критическая ошибка в цикле меню: {e}", exc_info=True)
            break

    logger.info("Программа завершена")
