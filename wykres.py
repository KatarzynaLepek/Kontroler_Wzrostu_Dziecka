import matplotlib.pyplot as plt
import numpy as np

def rysuj_procentyle_wzrostu(wiek_miesiace, plec, dane_chlopcow, dane_dziewczat):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for percentyl in [5, 10, 25, 50, 75, 90, 95]:
        if plec == 'chlopcy':
            ax.plot(wiek_miesiace, dane_chlopcow[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='--', marker='o')
        elif plec == 'dziewczyny':
            ax.plot(wiek_miesiace, dane_dziewczat[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='--', marker='s')

    ax.set_title('Procentyle Wzrostu Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Procentyl Wzrostu')
    ax.legend()
    plt.show()


def rysuj_procentyle_wagi(wiek_miesiace, plec, dane_chlopcow, dane_dziewczat):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for percentyl in [5, 10, 25, 50, 75, 90, 95]:
        if plec == 'chlopcy':
            ax.plot(wiek_miesiace, dane_chlopcow[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='--', marker='o')
        elif plec == 'dziewczyny':
            ax.plot(wiek_miesiace, dane_dziewczat[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='--', marker='s')

    ax.set_title('Procentyle Masy Ciała Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Procentyl Masy Ciała')
    ax.legend()
    plt.show()

# Example usage with placeholder data
wiek_miesiace = np.array([6, 12, 18, 24, 30, 36, 42, 48, 54, 60])

# Placeholder data for boys and girls
chlopcy_wzrost_percentyle = {
    5: np.array([63, 66, 69, 72, 76, 79, 82, 85, 87, 89]),
    10: np.array([64, 67, 70, 73, 77, 80, 83, 86, 88, 91]),
    25: np.array([66, 69, 72, 75, 78, 81, 84, 87, 89, 92]),
    50: np.array([68, 71, 74, 77, 80, 83, 86, 89, 91, 94]),
    75: np.array([71, 74, 77, 80, 83, 86, 89, 92, 94, 97]),
    90: np.array([73, 76, 79, 82, 85, 88, 91, 94, 96, 99]),
    95: np.array([74, 77, 80, 83, 86, 89, 92, 95, 97, 100])
}

dziewczyny_wzrost_percentyle = {
    5: np.array([62, 65, 68, 71, 74, 77, 80, 83, 85, 88]),
    10: np.array([63, 66, 69, 72, 75, 78, 81, 84, 86, 89]),
    25: np.array([65, 68, 71, 74, 77, 80, 83, 86, 88, 91]),
    50: np.array([67, 70, 73, 76, 79, 82, 85, 88, 90, 93]),
    75: np.array([70, 73, 76, 79, 82, 85, 88, 91, 93, 96]),
    90: np.array([72, 75, 78, 81, 84, 87, 90, 93, 95, 98]),
    95: np.array([73, 76, 79, 82, 85, 88, 91, 94, 96, 99])
}

chlopcy_waga_percentyle = {
    5: np.array([5.5, 6.2, 7.0, 7.8, 8.7, 9.6, 10.6, 11.6, 12.6, 13.6]),
    10: np.array([6.0, 6.7, 7.5, 8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4]),
    25: np.array([6.8, 7.6, 8.5, 9.4, 10.4, 11.4, 12.5, 13.5, 14.5, 15.5]),
    50: np.array([7.8, 8.7, 9.7, 10.7, 11.8, 12.9, 14.0, 15.1, 16.1, 17.1]),
    75: np.array([9.0, 9.9, 11.0, 12.1, 13.3, 14.5, 15.7, 16.9, 18.1, 19.3]),
    90: np.array([9.8, 10.8, 11.9, 13.1, 14.3, 15.5, 16.8, 18.0, 19.2, 20.4]),
    95: np.array([10.5, 11.6, 12.8, 14.0, 15.3, 16.6, 17.9, 19.2, 20.5, 21.8])
}

dziewczyny_waga_percentyle = {
    5: np.array([5.3, 6.0, 6.8, 7.6, 8.5, 9.4, 10.3, 11.2, 12.1, 13.1]),
    10: np.array([5.8, 6.5, 7.3, 8.1, 9.1, 10.1, 11.1, 12.1, 13.1, 14.1]),
    25: np.array([6.6, 7.4, 8.3, 9.2, 10.2, 11.2, 12.3, 13.3, 14.3, 15.3]),
    50: np.array([7.6, 8.5, 9.5, 10.5, 11.6, 12.7, 13.8, 14.9, 15.9, 17.0]),
    75: np.array([8.8, 9.7, 10.8, 11.9, 13.1, 14.3, 15.5, 16.7, 17.9, 19.1]),
    90: np.array([9.6, 10.7, 11.8, 13.0, 14.2, 15.4, 16.7, 17.9, 19.1, 20.3]),
    95: np.array([10.3, 11.4, 12.6, 13.8, 15.1, 16.4, 17.7, 18.9, 20.2, 21.5])
}

# Plot height percentiles for boys
rysuj_procentyle_wzrostu(wiek_miesiace, 'chlopcy', chlopcy_wzrost_percentyle, dziewczyny_wzrost_percentyle)

# Plot weight percentiles for girls
rysuj_procentyle_wagi(wiek_miesiace, 'dziewczyny', chlopcy_waga_percentyle, dziewczyny_waga_percentyle)
