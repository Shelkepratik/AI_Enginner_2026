from langchain_core.prompts import load_prompt

prompt=load_prompt("report_template.json")

complate_prompt=prompt.invoke( {
        "subject":"AI",
        "tone":"fnuuy",
        "lines":10
    })

print(complate_prompt.text)