from langchain_community.llms import HuggingFaceEndpoint
import os
from langchain_core.tracers.context import tracing_v2_enabled
#from dotenv import load_dotenv

def refined_output(text):
    # Load environment variables from .env file
    # load_dotenv()
    
    # Get the Hugging Face token from the environment variable
    # hugging_face_token = os.getenv('HUGGING_FACE_TOKEN')
    unique_id="a3aff21a-ffa9-4a7e-a870-b2679735e9b6"
    #Langsmith Tracing
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
    os.environ["LANGCHAIN_API_KEY"] = "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"

    

    hugging_face_token = "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"
    
    # Ensure the token is available
    if hugging_face_token is None:
        raise ValueError("Hugging Face token not found. Please set it in the .env file.")
    
    # Set the Hugging Face token for the Transformers library
    #os.environ['HUGGING_FACE_HUB_TOKEN'] = hugging_face_token
    
    # Initialize the Hugging Face endpoint
    llm2 = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2",huggingfacehub_api_token="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", top_k=1)
    
    from langchain.chains import LLMChain
    from langchain_core.prompts import PromptTemplate
    
    # Define the prompt template
    template = """You are a pharmacy expert. Tell me the name of medicine and its dosage only from the Prescription: {text}
    """
    
    prompt = PromptTemplate.from_template(template)
    
    # Create an LLM chain
    llm_chain = LLMChain(prompt=prompt, llm=llm2)
    
    # Run the LLM chain with the input text
    refined_text = llm_chain.run(text)
    
    # Print and return the refined text
    print(refined_text)
    return refined_text
