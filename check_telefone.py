import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato +55[DDD]0000000000 \n                             ")
phone_numbers = phonenumbers.parse(phone)

print("\n> ", geocoder.description_for_number(phone_numbers, "pt"), "\n")
