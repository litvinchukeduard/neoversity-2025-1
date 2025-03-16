# return [float(temp.strip()) for temp in temperature_data if temp.strip()] у коді нижче

def load_data(filename: str) -> list[str]:
    with open(filename, "r") as file:
        return file.readlines()

def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]

temperature_data = ['10.3', '12.5', '15.0', '', '', '']

result_one_list = [float(temp.strip()) for temp in temperature_data if temp.strip()]

result_list = []
for temp in temperature_data:
    if temp.strip():
        result_list.append(float(temp.strip()))

print(result_one_list)
print(result_list)
