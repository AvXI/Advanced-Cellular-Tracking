import pandas as pd
from sklearn.cluster import KMeans
import folium

# Load the cellular tower data
tower_data = pd.read_csv('cell_tower_data.csv')

# Load the GPS data
gps_data = pd.read_csv('gps_data.csv')

# Preprocess the data
tower_data['signal_strength'] = tower_data['signal_strength'].apply(lambda x: -x)
merged_data = pd.merge(tower_data, gps_data, on='user_id')
X = merged_data[['latitude', 'longitude', 'signal_strength']].values

# Cluster the data using KMeans algorithm
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)
labels = kmeans.predict(X)
merged_data['label'] = labels

# Visualize the results on a map
center_lat, center_lon = merged_data[['latitude', 'longitude']].mean().values
map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
for label in range(kmeans.n_clusters):
    data = merged_data[merged_data['label'] == label]
    for index, row in data.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['user_id']).add_to(map)
map.save('map.html')