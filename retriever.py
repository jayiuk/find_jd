from vectorstore import load_vectorstore

vec_path = './jd_vec'
vecdb = load_vectorstore(vec_path)

# def find_relevant(query):
#     retriever = vecdb.as_retriever(search_kwargs={'k' : 1})
#     result = retriever.get_relevant_documents(query)
#     return result

class Retriever():
    def __init__(self):
        self.retriever = vecdb.as_retriever(search_kwargs={'k' : 1})
    
    def find_relevant(self, query):
        result = self.retriever.get_relevant_documents(query)
        return result