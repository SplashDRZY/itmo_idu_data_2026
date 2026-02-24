import pandas as pd
from shapely.geometry import Point

def main():
    df = pd.DataFrame({
        'name': ['Промзона', 'Трасса', 'Трек'],
        'score': [75, 45, 95]
    })
    print(f"Анализ завершен. Лучшая: {df.loc[df['score'].idxmax(), 'name']}")

if __name__ == "__main__":
    main()  