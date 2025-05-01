from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Plus", "+79601111111"),
    Smartphone("Samsung", "Galaxy S25 Ultra", "+79602222222"),
    Smartphone("Huawei", "nova Y72", "+79603333333"),
    Smartphone("POCO", "F7 pro", "+79604444444"),
    Smartphone("Xiaomi", "15pro", "+79605555555")
]


for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. "
          f"{smartphone.number}")
