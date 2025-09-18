from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.vector_stores import SimpleVectorStore
from llama_index.core.storage.index_store import SimpleIndexStore

# 详细内容参考文档 https://developers.llamaindex.ai/python/framework/module_guides/deploying/query_engine

persist_path = "./llamaindex_index_store"

# 加载多个index json文件
storage_context = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(persist_dir=persist_path),
    vector_store=SimpleVectorStore.from_persist_dir(persist_dir=persist_path),
    index_store=SimpleIndexStore.from_persist_dir(persist_dir=persist_path),
)

# 使用最简单的query方法
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()
response = query_engine.query("Who is 张三.")

print(response)
