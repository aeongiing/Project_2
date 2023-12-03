import pandas as pd

df = pd.read_csv('/Users/jeong-yewon/Downloads/2019_kbo_for_kaggle_v2.csv')
for year in range(2015, 2019):
    data = df[df['year'] == year]
    for column in ['H', 'avg', 'HR', 'OBP']:
        print(f"년도: {year}, 항목: {column}")
        print(data[['batter_name', column]].sort_values(column, ascending=False).head(10))
        print()

data = df[df['year'] == 2018]
positions = ['포수', '1루수', '2루수', '3루수', '유격수', '좌익수', '중견수', '우익수']
for position in positions:
    players = data[data['cp'] == position]
    top_player = players[['batter_name', 'war']].sort_values('war', ascending=False).head(1)
    print(f"포지션: {position}, 선수: {top_player['batter_name'].values[0]}, 승리 기여도: {top_player['war'].values[0]}")

correlations = df[columns + ['salary']].corr()['salary'].drop('salary')
print(correlations.idxmax(), correlations.max())