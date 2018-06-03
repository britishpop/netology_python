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
    median = temperature_conversion("c", round(sum(templist)/len(templist)))
    return int(median[1])


def temperature_conversion(target_scale, input_temperature):
    client = Client("https://www.w3schools.com/xml/tempconvert.asmx?WSDL")
    if target_scale == "c":
        conversion = client.service.FahrenheitToCelsius(input_temperature)
        result = "\n{} по Фаренгейту это {} по Цельсию\n"\
        .format(input_temperature, conversion)
    elif target_scale == "f":
        conversion = client.service.CelsiusToFahrenheit(input_temperature)
        result = "\n{} по Цельсию это {} по Фаренгейту\n"\
        .format(input_temperature, conversion)
    else:
        result = "Что-то пошло не так, попробуйте еще раз"
    return [result, round(float(conversion))]


def travel_plan():
    client = Client("http://fx.currencysystem.com/webservices/CurrencyServer4"
                    ".asmx?WSDL")
    flights_sum = 0
    with open(os.path.join("input_files", "currencies.txt")) as f:
        for line in f:
            from_currency = line.split(":")[1].split()[1]
            amount_currency = int(line.split(":")[1].split()[0])
            flights_sum += client.service.ConvertToNum(
                                                        fromCurrency=from_currency,
                                                        toCurrency="RUB",
                                                        amount=amount_currency,
                                                        rounding=True
                                                    )
        return flights_sum


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
            print(temperature_conversion(target_scale, input_temperature)[0])
        elif answer == "file":
            print("\nСредняя температура за неделю - {} градусов по цельсию".\
                  format(median_temp()))
        elif answer == "travel":
            print("\nОбщая стоимость путешествия - {} рублей".\
                  format(travel_plan()))
        else:
            continue
