# Advanced-Cellular-Tracking
In this code, we first load the cellular tower data and GPS data into pandas dataframes. We then preprocess the data by taking the negative of signal strength and merging the two dataframes based on the user ID.
Next, we use the KMeans algorithm from scikit-learn library to cluster the data into 5 groups based on latitude, longitude, and signal strength features. We then add a new column to the merged dataframe to indicate the cluster label.
Finally, we visualize the results on a map using the folium library. We first calculate the mean latitude and longitude values of all data points and center the map around these coordinates. We then iterate over each cluster and add markers to the map for each data point in that cluster.
