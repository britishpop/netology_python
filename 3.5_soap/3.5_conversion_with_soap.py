from zeep import Client
import os

def open_file(filename):
    file = []
    with open(os.path.join("input_files", filename)) as f:
        for line in f:
            file.append(line.strip())
    return file


def median_temp():
    data = open_file("temps.txt")
    templist = []
    for day_temp in data:
        templist.append(int(day_temp.strip(" F\n")))
    median = sum(templist)/len(templist)
    return median


def temperature_conversion(target_scale, input_temperature):
    client = Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL")
    if target_scale == "c":
        result = "\n{} по Фаренгейту это {} по Цельсию\n"\
        .format(input_temperature,
                client.service.FahrenheitToCelsius(input_temperature))
    elif target_scale == "f":
        result = "\n{} по Цельсию это {} по Фаренгейту\n"\
        .format(input_temperature,
                client.service.CelsiusToFahrenheit(input_temperature))
    else:
        result = "Что-то пошло не так, попробуйте еще раз"
    return result


def temperature_file():
    pass


if __name__ == "__main__":
    answer = ""
    while answer != "q":
        answer = input("\nПривет! Мы используем SOAP, чтобы управлять сторонними"
                       " сервисами. Выберите, что вы хотите сделать\n"
                       "Перевести температуру - команда temp\n"
                       "Обработать файл temps.txt - команда file\n"
                       "Спланировать путешествие - команда travel\n"
                       "Чтобы выйти - команда q\n")
        if answer == "temp":
            input_temperature = input("\nВведите количество градусов\n")
            try:
                int(input_temperature)
            except ValueError:
                print("\nКажется, вы ввели буквы вместо цифр, начнем сначала\n")
                continue
            target_scale = input("\nМы можем перевести это значение в градусы по"
                                " Фаренгейту или в градусы по Цельсию\n"
                                "Введите 'f' (celsius->fahrenheit) или 'c' (fah"
                                "renheit->celsius)\n")
            print(temperature_conversion(target_scale, input_temperature))
        elif answer == "file":
            median_temp()
        elif answer == "travel":
            pass
        else:
            continue
