import os
from dotenv import load_dotenv
from openai import OpenAI
from tavily import TavilyClient
from judgeval.common.tracer import Tracer, wrap
from judgeval import JudgmentClient
from judgeval.scorers import FaithfulnessScorer

load_dotenv()

# Wrap the OpenAI client for tracing
client = wrap(OpenAI())
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
judgment = Tracer(
    api_key=os.getenv("JUDGMENT_API_KEY"),
    project_name="movie-recommender-agent",
    enable_monitoring=True
)

@judgment.observe(span_type="function")
def movie_recommender_workflow():
    print(" Welcome to Movie Recommender!")
    genre = input("Favorite genre? ")
    actor = input("Favorite actor? ")
    recent = input("Recent movie you liked? ")

    # Tavily search
    search_query = f"Movies like {recent} starring {actor} in {genre}"
    search_results = tavily.search(query=search_query, max_results=5)

    # Prepare retrieval context for evaluation
    retrieval_context = []
    context = "Search Results:\n"
    for result in search_results.get("results", []):
        context += f"- {result['title']}: {result['url']}\n"
        retrieval_context.append(f"{result['title']}: {result.get('content', '')}")

    prompt = f"""
    Suggest 5 movies based on:
    - Genre: {genre}
    - Actor: {actor}
    - Similar to: {recent}

    Context:
    {context}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a movie expert."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content
    print("\n🎥 Recommendations:")
    print(output)

    # Evaluate faithfulness to search results
    judgment.async_evaluate(
        input=prompt,
        actual_output=output,
        retrieval_context=retrieval_context,
        scorers=[FaithfulnessScorer(threshold=0.5)],
        model="gpt-4o"
    )

    return output

if __name__ == "__main__":
    movie_recommender_workflow()
