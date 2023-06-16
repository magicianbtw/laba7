import time


def log_function_call(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print("-------------------------")
        print("Функция:", func.__name__)
        print("Расстояние (километры):", args[0])
        print("Результат:", round(result, 2))
        print("Время выполнения:", execution_time, "секунд")
        print("-------------------------")

        return result

    return wrapper


@log_function_call
def Calculating_the_cost_of_a_taxi(distance):
    base_fare = 4.00
    fare_per_meter = 0.25 / 140
    distance_in_meters = distance * 1000
    total_fare = base_fare + fare_per_meter * distance_in_meters

    return total_fare


distance_km = float(input("Введите расстояние в километрах: "))
fare = Calculating_the_cost_of_a_taxi(distance_km)
print("Ваша стоимость составляет:", round(fare, 2), "$")