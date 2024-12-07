from gigachat import GigaChat

def get_animal_description(animal: str) -> str:
  if animal == "" or animal is None:
    return "Не знаю такого зверя"
  with GigaChat(credentials="OWVmZDViNmYtODdlNy00ZGI4LWI1NmUtMDkxOTIxMDMxZTM1OmQxODJiZDRlLTRhZjgtNGUwYS05ZTMxLWM2YzJmYmUxZDRiYw==", verify_ssl_certs=False) as giga:
    response = giga.chat(f"Напиши подробное описание животного, внешний вид, место обитания и ежедневный рацион питания, а также другие интересные факты о животном: {animal}")
    return response.choices[0].message.content