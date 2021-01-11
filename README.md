# K-Means Clustering Sample
### Short Summary for K-means clustering
K-means clustering is one of the simplest and popular unsupervised machine learning algorithms. To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs iterative (repetitive) calculations to optimize the positions of the centroids. It halts creating and optimizing clusters when either:
- The centroids have stabilized — there is no change in their values because the clustering has been successful.
- The defined number of iterations has been achieved.

### Summary for my basic project
In my project, I created very basic dataFrame to understand how K-means clustering seperate unlabelled features and how it looks like.

### Choosing the best value from elbow graph

![elbow](https://user-images.githubusercontent.com/44119225/104195704-05f66b00-5434-11eb-987d-a1f6b9787fd8.png)

Here, I found the best value for my clusters' amount(k) and it's 3.

### Visualization 

![clusters](https://user-images.githubusercontent.com/44119225/104195863-3211ec00-5434-11eb-834d-6cede41bb874.png)

Finally, as you can see, K-means algorithm worked and it seperated unlabelled features very well. For the last step I plotted centers of the clusters.
