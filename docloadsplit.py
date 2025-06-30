from langchain_community.document_loaders import JSONLoader

def jsonloader(path):
    loader = JSONLoader(
        file_path = path,
        jq_schema = ".",
        content_key = "company",
        text_content = False
    )
    doc = loader.load_and_split()
    return doc

# def jsonsplitter(doc):
#     splitter = RecursiveJsonSplitter(max_chunk_size=500, min_chunk_size=100)