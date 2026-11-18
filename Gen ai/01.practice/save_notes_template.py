from langchain_core.prompts import PromptTemplate

templ="Explain {topic} for a {level} student in {points} bullet points"

prompt_obj=PromptTemplate(
    template=templ
)

save=prompt_obj.save("notes_template.json")