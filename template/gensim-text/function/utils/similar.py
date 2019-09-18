def find_similar(cui, tn):
    return model.most_similar(cui, topn=tn)
