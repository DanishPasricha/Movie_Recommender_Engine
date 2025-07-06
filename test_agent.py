from judgeval import JudgmentClient
from judgeval.data import Example
from judgeval.scorers import FaithfulnessScorer
from agent import movie_recommender_workflow
from judgeval.common.tracer import Tracer
import datetime

tracer = Tracer(project_name="movie-recommender-agent")
client = JudgmentClient()

# Mock retrieval context for testing
retrieval_context = [
    "Mission Impossible: Fallout - Action thriller starring Tom Cruise",
    "Top Gun: Maverick - Action drama starring Tom Cruise", 
    "Edge of Tomorrow - Sci-fi action starring Tom Cruise",
    "Jack Reacher - Action thriller starring Tom Cruise",
    "The Last Samurai - Action drama starring Tom Cruise"
]

example = Example(
    input={"genre": "Action", "actor": "Tom Cruise", "recent": "Mission Impossible"},
    actual_output="Based on your preferences, here are 5 action movies starring Tom Cruise: 1. Mission Impossible: Fallout 2. Top Gun: Maverick 3. Edge of Tomorrow 4. Jack Reacher 5. The Last Samurai",
    retrieval_context=retrieval_context
)

# Create unique evaluation run name with timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
eval_run_name = f"movie_recommender_test_{timestamp}"

results = client.run_evaluation(
    examples=[example],
    scorers=[FaithfulnessScorer(threshold=0.5)],
    model="gpt-4o",
    project_name="movie-recommender-agent",
    eval_run_name=eval_run_name,
    override=True
)
print(results)
