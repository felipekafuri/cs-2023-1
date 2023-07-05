# INSTALL: pip install babel

import locale
from babel import Locale
from babel.numbers import get_currency_symbol
from datetime import datetime


def print_country_data(country_code, language_code, windows_codepage, currency_code):
    try:
        locale_code = f"{language_code}_{country_code}.UTF-8"
        locale.setlocale(locale.LC_ALL, locale_code)
    except locale.Error:
        print(f"Locale {locale_code} não disponível. Usando o padrão.")
        locale.setlocale(locale.LC_ALL, "")  # Use a localidade padrão do sistema
        locale_code = locale.getdefaultlocale()[0] or "en_US.UTF-8"

    babel_locale = Locale.parse(locale_code)

    print(f"Nome do País: {babel_locale.territories[country_code]}")
    print(f"Linguagem: {babel_locale.get_language_name(language_code)}")

    date_format = babel_locale.date_formats["short"].pattern
    now = datetime.now()
    print(f"Data no formato curto: {now.strftime(date_format)}")

    date_format = babel_locale.date_formats["long"].pattern
    print(f"Data no formato longo: {now.strftime(date_format)}")

    time_format = babel_locale.time_formats["short"].pattern
    print(f"Formato de hora: {now.strftime(time_format)}")

    print(
        f"Símbolo da moeda local: {get_currency_symbol(currency_code, locale=locale_code)}"
    )
    print(f"Separador de decimal: {babel_locale.number_symbols['decimal']}")
    print(f"Separador de milhar: {babel_locale.number_symbols['group']}")
    print(f"Código de página windows: {windows_codepage}")
    print("\n")


# Use os códigos de país e idioma corretos.
# Os códigos de página do Windows e códigos de moeda devem ser pesquisados ​​separadamente.
print_country_data("US", "en", "1252", "USD")  # Estados Unidos
print_country_data("JP", "ja", "932", "JPY")  # Japão
print_country_data("CN", "zh", "936", "CNY")  # China
print_country_data("IN", "hi", "1252", "INR")  # Índia
print_country_data("BR", "pt", "1252", "BRL")  # Brasil
print_country_data("FR", "fr", "1252", "EUR")  # França
print_country_data("DE", "de", "1252", "EUR")  # Alemanha
print_country_data("IT", "it", "1252", "EUR")  # Itália
print_country_data("RU", "ru", "1251", "RUB")  # Rússia
print_country_data("ES", "es", "1252", "EUR")  # Espanha
