import PyPDF2
from django.conf import settings
from langchain_community.chat_models import ChatCohere
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document


def parse_pdf(pdf_file):
    pdf_text = ""
    try:
        with open(pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_text += page.extract_text()
    except Exception as e:
        # Обробка помилок при парсингу PDF
        print("Помилка при парсингу PDF:", e)
    return pdf_text


def get_cohere_answer(pdf_path, question):
    COHERE_API_KEY = settings.COHERE_API_KEY
    llm = ChatCohere()
    page_content = parse_pdf(pdf_path)
    prompt = ChatPromptTemplate.from_template(
        """Answer the following question based only on the provided context :

    <context>
    {context}
    </context>

    Question: {input}
    
    Specify the section of the text where the answer can be found."""
    )

    document_chain = create_stuff_documents_chain(llm, prompt)

    return document_chain.invoke({
        "input": question,
        "context": [Document(page_content=page_content)]
    })
