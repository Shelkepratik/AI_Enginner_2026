from langchain_core.prompts import PromptTemplate


tmpl="write a poem about {subject} in a {tone} tone with {lines} lines"


prompt_obj=PromptTemplate(
    template=tmpl
)

prompt_obj.save("report_template.json")