informacion = [
    {
        "name": {
            "common": "Mexico",
            "official": "United Mexican States",
            "nativeName": {
                "spa": {
                    "official": "Estados Unidos Mexicanos",
                    "common": "México"
                }
            }
        },
        "tld": [".mx"],
        "cca2": "MX",
        "ccn3": "484",
        "cca3": "MEX",
        "cioc": "MEX",
        "independent": True,
        "status": "officially-assigned",
        "unMember": True,
        "currencies": {
            "MXN": {
                "name": "Mexican peso",
                "symbol": "$"
            }
        },
        "idd": {
            "root": "+5",
            "suffixes": ["2"]
        },
        "capital": ["Mexico City"],
        "altSpellings": ["MX", "Mexicanos", "United Mexican States", "Estados Unidos Mexicanos"],
        "region": "Americas",
        "subregion": "North America",
        "languages": {"spa": "Spanish"},
        "translations": {
            "ara": {"official": "الولايات المتحدة المكسيكية", "common": "المسكيك"},
            "bre": {"official": "Stadoù-Unanet Mec'hiko", "common": "Mec'hiko"},
            "ces": {"official": "Spojené státy mexické", "common": "Mexiko"},
            "cym": {"official": "United Mexican States", "common": "Mexico"},
            "deu": {"official": "Vereinigte Mexikanische Staaten", "common": "Mexiko"},
            "est": {"official": "Mehhiko Ühendriigid", "common": "Mehhiko"},
            "fin": {"official": "Meksikon yhdysvallat", "common": "Meksiko"},
            "fra": {"official": "États-Unis du Mexique", "common": "Mexique"},
            "hrv": {"official": "Sjedinjene Meksičke Države", "common": "Meksiko"},
            "hun": {"official": "Mexikói Egyesült Államok", "common": "Mexikó"},
            "ita": {"official": "Stati Uniti del Messico", "common": "Messico"},
            "jpn": {"official": "メキシコ合衆国", "common": "メキシコ"},
            "kor": {"official": "멕시코 합중국", "common": "멕시코"},
            "nld": {"official": "Verenigde Mexicaanse Staten", "common": "Mexico"},
            "per": {"official": "ایالات متحد مکزیک", "common": "مکزیک"},
            "pol": {"official": "Meksykańskie Stany Zjednoczone", "common": "Meksyk"},
            "por": {"official": "Estados Unidos Mexicanos", "common": "México"},
            "rus": {"official": "Мексиканские Соединённые Штаты", "common": "Мексика"},
            "slk": {"official": "Spojené štášy mexické", "common": "Mexiko"},
            "spa": {"official": "Estados Unidos Mexicanos", "common": "México"},
            "srp": {"official": "Сједињене Мексичке Државе", "common": "Мексико"},
            "swe": {"official": "Mexikos förenta stater", "common": "Mexiko"},
            "tur": {"official": "Birleşik Meksika Devletleri", "common": "Meksika"},
            "urd": {"official": "ریاستہائے متحدہ میکسیکو", "common": "میکسیکو"},
            "zho": {"official": "墨西哥合众国", "common": "墨西哥"}
        },
        "latlng": [23.0, -102.0],
        "landlocked": False,
        "borders": ["BLZ", "GTM", "USA"],
        "area": 1964375.0,
        "demonyms": {
            "eng": {"f": "Mexican", "m": "Mexican"},
            "fra": {"f": "Mexicaine", "m": "Mexicain"}
        },
        "flag": "\uD83C\uDDF2\uD83C\uDDFD",
        "maps": {
            "googleMaps": "https://goo.gl/maps/s5g7imNPMDEePxzbA",
            "openStreetMaps": "https://www.openstreetmap.org/relation/114686"
        },
        "population": 128932753,
        "gini": {"2018": 45.4},
        "fifa": "MEX",
        "car": {
            "signs": ["MEX"],
            "side": "right"
        },
        "timezones": ["UTC-08:00", "UTC-07:00", "UTC-06:00"],
        "continents": ["North America"],
        "flags": {
            "png": "https://flagcdn.com/w320/mx.png",
            "svg": "https://flagcdn.com/mx.svg",
            "alt": "The flag of Mexico is composed of three equal vertical bands of green, white and red, with the national coat of arms centered in the white band."
        },
        "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/mx.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/mx.svg"
        },
        "startOfWeek": "monday",
        "capitalInfo": {
            "latlng": [19.43, -99.13]
        },
        "postalCode": {
            "format": "#####",
            "regex": "^(\\d{5})$"
        }
    }
]

informacion_en_diccionario = informacion[0]
latitud_longitud = informacion_en_diccionario["latlng"]
paises_fronterizos = informacion_en_diccionario["borders"]
nombre = informacion_en_diccionario["name"]["common"]
capital = informacion_en_diccionario["capital"]

print(nombre, capital, latitud_longitud, paises_fronterizos)