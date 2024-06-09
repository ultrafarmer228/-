def filter_short_strings(input_array):
    result = []
    for string in input_array:
        if len(string) <= 3:
            result.append(string)
    return result

if __name__ == "__main__":
    # Пример использования
    input_array = ["Hello", "2", "world", ":-)"]
    output_array = filter_short_strings(input_array)
    print(output_array)
