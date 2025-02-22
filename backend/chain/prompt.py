from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

Query_Prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a highly reliable and precise assistant for a RAG application. Your task is to answer user questions strictly using the provided DOCUMENT:{context} and any relevant conversation HISTORY :{history}. Ensure your response is concise, factual, and based only on these inputs."),
        ("human","{query}")
    ]
)
