import os
from embedchain import App

# Replace this with your OpenAI key
os.environ["OPENAI_API_KEY"] = "sk-proj-CK9lJWrqrnC0XXxHrVgWT3BlbkFJzWdPza7eWiy9vfUCfpzq"


app = App()


app.add('commercial books law_formatted.txt')
try:
    while True:
        # Ask the user for a query
        user_query = input("Enter your query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        # Process the query
        answer = app.query(user_query)
        print(f"Answer: {answer}")

except KeyboardInterrupt:
    print("Loop has been stopped manually.")

