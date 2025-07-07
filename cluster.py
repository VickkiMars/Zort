from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from kneed import KneeLocator
from retrieve_data import Files
import numpy as np
from sklearn.preprocessing import StandardScaler

model = SentenceTransformer('all-mpnet-base-v2')
model.save('my_local_model')  # Saves to a folder called 'my_local_model'

class Cluster:
    def __init__(self, data):
        self.data = data
        print("Loading model..🎉🎉")
        self.model = SentenceTransformer('my_local_model')
        print("Model:", self.model)
        print("Generating embeddings...🎉🎉🎉")
        self.embeddings = self.generateEmbeddings()
        print(type(self.embeddings))

        print("Finding optimal number of folders 🔃🔃")
        self.optimal_k = self.findOptimalK(self.embeddings)

        self.clusters = self.showClusters()

    def generateEmbeddings(self):
        print(len(self.data))
        embeddings = self.model.encode(self.data, show_progress_bar=True)
        print("Shape of the embeddings: ", embeddings.shape)
        return embeddings

    def findOptimalK(self, data):
        k_range = (2, int(len(self.data)/2))
    # Standardize if needed
        #data = StandardScaler().fit_transform(data)
        if len(data) < 2:
            data = data.reshape(1, -1)

        print(f"Shape of the data: {data.shape}")
        inertias = []
        ks = list(range(k_range[0], k_range[1] + 1))
        for k in ks:
            kmeans = KMeans(n_clusters=k, random_state=1334, n_init='auto')
            kmeans.fit(data)
            inertias.append(kmeans.inertia_)
        
        kn = KneeLocator(ks, inertias, curve='concave', direction='decreasing')

        if kn.elbow is None:
            print("⚠️ Warning: Elbow not found, defaulting to minimum k")
        
        return kn.elbow or ks[0]
    
    def clusterText(self):
        kmeans = KMeans(n_clusters=self.optimal_k, random_state=1334)
        if self.data is None or len(self.data) == 0:
            raise ValueError("No embeddings provided — check input data or model encoding.")
        labels = kmeans.fit_predict(self.embeddings)

        return labels

    def showClusters(self):
        cluster_dict = {}
        clusters = self.clusterText()
        print(self.optimal_k)

        for i in range(self.optimal_k):
            cluster_dict[f"Cluster {i}"] = []
            for j, doc in enumerate(self.data):
                if clusters[j] == i:
                    cluster_dict[f"Cluster {i}"].append(doc)
        return cluster_dict



    
if __name__ == "__main__":
    print("Running its ass off 🎉🎉🎉")
    fileins = Files("")
    data = ""
    print("Data received from sendData: ", data, len(data))
    ins = Cluster(list(data))
    ins.showClusters()





    


