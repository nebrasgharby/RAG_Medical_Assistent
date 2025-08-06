from logger import logger

def query_chain(chain, user_input:str):
    try:
        logger.debug(f"Running chain for input: {user_input}")
        result = chain({"query": user_input})
        
        # Enhanced source tracking
        sources = []
        for doc in result["source_documents"]:
            source_info = {
                "document": doc.metadata.get("source", "unknown"),
                "page": doc.metadata.get("page", "N/A"),
                "excerpt": doc.page_content[:200] + "..."  # First 200 chars
            }
            sources.append(source_info)
        
        response = {
            "response": result["result"],
            "sources": sources
        }
        logger.debug(f"Chain response: {response}")
        return response
    except Exception as e:
        logger.exception("Error on query chain")
        raise