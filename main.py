# calori = Metabolisme(int)*berat(kg)*time(hours)
# jika waktu lebih 2 jam saran kepada user mengurangi jam, kurang dari 30 menit sarankan user menambah jam ke 2 jam
# pandas
# numpy
# matplotlib

def main():
    print(1)
    gender = input('Anda laki (l) atau perempuan (p) ? ')
    weight = int(input('Berat badan (kg) ? '))
    height = int(input('Tinggi badan (cm) ? '))
    age = int(input('Umur ? '))
    activity = input('Tidak pernah olahraga (y/n)')
    intensity = 1.2

    if activity == 'n':
        activity = input('Sering olahraga atau jarang (y/n) ? ')

        if activity == 'y':
            intensity = 1.4
        else:
            intensity = 1.3

    result = calc(gender, weight, height, age, intensity)

    print(f'Kebutuhan kalori anda per hari yaitu {result} kkal')


def calc(gender, weight, height, age, intensity):
    result = 0

    if gender == 'l':
        result = 66.5 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif gender == 'p':
        result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    if result > 0:
        result *= intensity

    return round(result)


if __name__ == '__main__':
    main()
