# Проект "Бронирование мест"
def book_seat():
    seat_name=input("Введите место для бронирования (от Б1 до Б9): ")
    try:
        i=seats.index([seat_name, "свободно"])
        seats[i][1] = "забронировано"
        print(f"Место {seat_name} успешно забронировано.")
    except ValueError:
        print(f"Место {seat_name} уже забронировано или не существует.")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")
seats = [[f"Б{i}", "свободно"] for i in range(1,10)]
#print(seats)

while True:
    book_seat()
    booking= input("Хотите забронировать еще одно место? (да/нет):")
    if booking.lower() != "да":
        break
print("Итоговое состояние бронирование мест.")

for seat in seats:
    print(f"{seat[0]}:{seat[1]}")