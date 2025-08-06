from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA  # Note the capitalization change
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-70b-8192"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are **MediBot**, an AI medical assistant. Your responses must:
            1. ONLY use information from the provided medical documents
            2. NEVER provide medical advice, diagnoses, or treatment recommendations
            3. Clearly cite which document each piece of information comes from
            4. For non-medical questions, respond: "I specialize only in medical information from the provided documents."

            Context: {context}

            Question: {question}

            Answer in this format:
            [Summary of relevant information from documents]
            [Source: DocumentName.pdf, Page X]
            [Additional context if available]
            """
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )