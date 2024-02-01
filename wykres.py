import matplotlib.pyplot as plt
import numpy as np

def rysuj_procentyle_wzrostu(plec, pomiary, imie):
    fig, ax = plt.subplots(figsize=(12, 12))    

    for percentyl in [5, 10, 25, 50, 75, 90, 95]:
        if plec == 'chłopiec':
            ax.plot(wiek_miesiace, chlopcy_wzrost_percentyle[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='--', marker='o')
        elif plec == 'dziewczynka':
            ax.plot(wiek_miesiace, dziewczyny_wzrost_percentyle[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='--', marker='s')

    wiek_pomiary = [pomiar.miesiace_zycia for pomiar in pomiary]
    wzrost_pomiary = [pomiar.wzrost for pomiar in pomiary]

    ax.plot(wiek_pomiary, wzrost_pomiary, label=f'{imie}', linestyle='-', marker='s')

    ax.set_title('Procentyle Wzrostu Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Procentyl Wzrostu')
    ax.legend()
    plt.show()


def rysuj_procentyle_wagi(plec, pomiary, imie):
    fig, ax = plt.subplots(figsize=(12, 12))
    
    for percentyl in [5, 10, 25, 50, 75, 90, 95]:
        if plec == 'chłopiec':
            ax.plot(wiek_miesiace, chlopcy_waga_percentyle[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='--', marker='o')
        elif plec == 'dziewczynka':
            ax.plot(wiek_miesiace, dziewczyny_waga_percentyle[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='--', marker='s')

    wiek_pomiary = [pomiar.miesiace_zycia for pomiar in pomiary]
    waga_pomiary = [pomiar.waga for pomiar in pomiary]

    ax.plot(wiek_pomiary, waga_pomiary, label=f'{imie}', linestyle='-', marker='s')

    ax.set_title('Procentyle Masy Ciała Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Procentyl Masy Ciała')
    ax.legend()
    plt.show()

# Example usage with placeholder data
wiek_miesiace = np.array([0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60])

# Placeholder data for boys and girls
chlopcy_wzrost_percentyle = {
    5: np.array([50, 63, 66, 69, 72, 76, 79, 82, 85, 87, 89]),
    10: np.array([52, 64, 67, 70, 73, 77, 80, 83, 86, 88, 91]),
    25: np.array([56, 66, 69, 72, 75, 78, 81, 84, 87, 89, 92]),
    50: np.array([60, 68, 71, 74, 77, 80, 83, 86, 89, 91, 94]),
    75: np.array([62, 71, 74, 77, 80, 83, 86, 89, 92, 94, 97]),
    90: np.array([68, 73, 76, 79, 82, 85, 88, 91, 94, 96, 99]),
    95: np.array([70, 74, 77, 80, 83, 86, 89, 92, 95, 97, 100])
}

dziewczyny_wzrost_percentyle = {
    5: np.array([48, 62, 65, 68, 71, 74, 77, 80, 83, 85, 88]),
    10: np.array([51, 63, 66, 69, 72, 75, 78, 81, 84, 86, 89]),
    25: np.array([54, 65, 68, 71, 74, 77, 80, 83, 86, 88, 91]),
    50: np.array([58, 67, 70, 73, 76, 79, 82, 85, 88, 90, 93]),
    75: np.array([61, 70, 73, 76, 79, 82, 85, 88, 91, 93, 96]),
    90: np.array([64, 72, 75, 78, 81, 84, 87, 90, 93, 95, 98]),
    95: np.array([67, 73, 76, 79, 82, 85, 88, 91, 94, 96, 99])
}

chlopcy_waga_percentyle = {
    5: np.array([3, 5.5, 6.2, 7.0, 7.8, 8.7, 9.6, 10.6, 11.6, 12.6, 13.6]),
    10: np.array([3.2, 6.0, 6.7, 7.5, 8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4]),
    25: np.array([3.5, 6.8, 7.6, 8.5, 9.4, 10.4, 11.4, 12.5, 13.5, 14.5, 15.5]),
    50: np.array([3.7, 7.8, 8.7, 9.7, 10.7, 11.8, 12.9, 14.0, 15.1, 16.1, 17.1]),
    75: np.array([4.0, 9.0, 9.9, 11.0, 12.1, 13.3, 14.5, 15.7, 16.9, 18.1, 19.3]),
    90: np.array([5.5, 9.8, 10.8, 11.9, 13.1, 14.3, 15.5, 16.8, 18.0, 19.2, 20.4]),
    95: np.array([6.2, 10.5, 11.6, 12.8, 14.0, 15.3, 16.6, 17.9, 19.2, 20.5, 21.8])
}

dziewczyny_waga_percentyle = {
    5: np.array([3, 5.3, 6.0, 6.8, 7.6, 8.5, 9.4, 10.3, 11.2, 12.1, 13.1]),
    10: np.array([3.2, 5.8, 6.5, 7.3, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1]),
    25: np.array([3.4, 6.6, 7.4, 8.3, 9.2, 10.2, 11.2, 12.3, 13.3, 14.3, 15.3]),
    50: np.array([3.7, 7.6, 8.5, 9.5, 10.5, 11.6, 12.7, 13.8, 14.9, 15.9, 17.0]),
    75: np.array([4.2, 8.8, 9.7, 10.8, 11.9, 13.1, 14.3, 15.5, 16.7, 17.9, 19.1]),
    90: np.array([4.9, 9.6, 10.7, 11.8, 13.0, 14.2, 15.4, 16.7, 17.9, 19.1, 20.3]),
    95: np.array([5.2, 10.3, 11.4, 12.6, 13.8, 15.1, 16.4, 17.7, 18.9, 20.2, 21.5])
}
