import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def rysuj_tabele(pomiary, imie):
    data = {
        'Wiek': [pomiar.wiek_dziecka() for pomiar in pomiary],
        'Waga (kg)': [pomiar.waga for pomiar in pomiary],
        'Wzrost (cm)': [pomiar.wzrost for pomiar in pomiary],
        'Data': [pomiar.data for pomiar in pomiary],
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('off')

    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 1.5) 

    plt.title(imie, fontsize=14)
    plt.show()

def rysuj_procentyle_wzrostu(plec, pomiary, imie):
    fig, ax = plt.subplots(figsize=(12, 12))    

    for percentyl in [3, 15, 50, 85, 97]:
        if plec == 'chłopiec':
            ax.plot(wiek_miesiace, chlopcy_wzrost_percentyle[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='-')
        elif plec == 'dziewczynka':
            ax.plot(wiek_miesiace, dziewczyny_wzrost_percentyle[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='-')

    wiek_pomiary = [pomiar.miesiace_zycia for pomiar in pomiary]
    wzrost_pomiary = [pomiar.wzrost for pomiar in pomiary]

    ax.plot(wiek_pomiary, wzrost_pomiary, label=f'{imie}', linestyle='-', marker='s')

    ax.set_title('Percentyle Wzrostu Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Wzrost (cm)')
    ax.legend()
    plt.show()


def rysuj_procentyle_wagi(plec, pomiary, imie):
    fig, ax = plt.subplots(figsize=(12, 12))
    
    for percentyl in [3, 15, 50, 85, 97]:
        if plec == 'chłopiec':
            ax.plot(wiek_miesiace, chlopcy_waga_percentyle[percentyl], label=f'Chłopcy {percentyl} percentyl', linestyle='-')
        elif plec == 'dziewczynka':
            ax.plot(wiek_miesiace, dziewczyny_waga_percentyle[percentyl], label=f'Dziewczyny {percentyl} percentyl', linestyle='-')

    wiek_pomiary = [pomiar.miesiace_zycia for pomiar in pomiary]
    waga_pomiary = [pomiar.waga for pomiar in pomiary]

    ax.plot(wiek_pomiary, waga_pomiary, label=f'{imie}', linestyle='-', marker='s')

    ax.set_title('Percentyle Masy Ciała Dzieci W Czasie')
    ax.set_xlabel('Wiek (miesiące)')
    ax.set_ylabel('Masa Ciała (kg)')
    ax.legend()
    plt.show()

# Example usage with placeholder data
wiek_miesiace = np.array([0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60])

# Placeholder data for boys and girls
chlopcy_wzrost_percentyle = {
    3: np.array([45.7, 64.4, 75.6, 78.9, 83.5, 87.0, 89.9, 92.3, 94.4, 96.2, 97.9]),
    15: np.array([49.9, 68.7, 77.1, 83.4, 88.2, 91.8, 94.8, 97.2, 99.4, 101.3, 103.1]),
    50: np.array([54.4, 73.8, 82.3, 88.9, 93.9, 97.6, 100.7, 103.2, 105.4, 107.3, 109.1]),
    85: np.array([59.4, 79, 87.7, 94.5, 99.8, 103.6, 106.8, 109.5, 111.8, 113.8, 115.7]),
    97: np.array([63.7, 83.1, 92, 99, 104.4, 108.4, 111.8, 114.8, 117.4, 119.6, 121.7]),
}

dziewczyny_wzrost_percentyle = {
    3: np.array([45.5, 63.5, 71, 76.5, 80.4, 83.6, 86.3, 88.7, 90.8, 92.7, 94.5]),
    15: np.array([49.7, 67.8, 75.6, 81.1, 85.1, 88.5, 91.3, 93.9, 96.2, 98.3, 100.4]),
    50: np.array([54.1, 72.7, 80.8, 86.3, 90.5, 93.9, 96.7, 99.3, 101.7, 103.8, 105.9]),
    85: np.array([59, 78.1, 86.5, 92.1, 96.4, 99.8, 102.8, 105.5, 108.1, 110.4, 112.5]),
    97: np.array([63.2, 82.2, 91.1, 96.8, 101.2, 104.7, 107.8, 110.5, 113.1, 115.4, 117.6]),
}

chlopcy_waga_percentyle = {
    3: np.array([2.5, 7.2, 9.2, 10.6, 11.8, 13, 13.9, 14.8, 15.6, 16.4, 17.1]),
    15: np.array([2.9, 7.9, 10.2, 11.8, 13.2, 14.5, 15.6, 16.7, 17.7, 18.7, 19.7]),
    50: np.array([3.4, 8.8, 11.5, 13.2, 14.8, 16.3, 17.6, 18.8, 20, 21.2, 22.4]),
    85: np.array([3.9, 9.8, 12.9, 14.8, 16.6, 18.3, 19.8, 21.2, 22.5, 24, 25.4]),
    97: np.array([4.4, 10.6, 13.9, 15.9, 17.8, 19.7, 21.2, 22.8, 24.2, 25.8, 27.3]),
}

dziewczyny_waga_percentyle = {
    3: np.array([2.5, 6.7, 8.6, 9.8, 10.9, 11.9, 12.7, 13.5, 14.1, 14.8, 15.4]),
    15: np.array([2.9, 7.5, 9.7, 11, 12.2, 13.3, 14.2, 15, 15.8, 16.5, 17.2]),
    50: np.array([3.4, 8.4, 11, 12.4, 13.7, 15, 16, 16.9, 17.8, 18.6, 19.4]),
    85: np.array([3.9, 9.5, 12.4, 14, 15.5, 16.9, 18.1, 19.1, 20.1, 21, 22]),
    97: np.array([4.5, 10.3, 13.5, 15.2, 16.9, 18.4, 19.7, 20.9, 22, 23, 24.1]),
}
