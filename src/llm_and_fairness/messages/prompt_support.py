from langchain_core.prompts import PromptTemplate

class PromptSupport:

    @staticmethod
    def get_resolved_message(amessage):
       prompt = PromptTemplate(template=amessage.getMessageTemplate())
       string_rep = prompt.invoke(amessage.getParameters()).to_string()
       return string_rep
