from ask_gem import call

def name(clusters):
    main_clusters = {}
    for cluster in clusters:
        folder_name = call(cluster)
        if len(folder_name) > 3:
            main_clusters[folder_name] = cluster

    return main_clusters