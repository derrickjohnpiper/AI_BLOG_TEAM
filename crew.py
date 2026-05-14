How to Run It (Basic Python File)
In your main crew file (usually src/blog_writer/crew.py or similar), it should look something like this after the CLI scaffold:

from crewai.project import CrewBase, agent, crew, task
from crewai import Crew

@CrewBase
class BlogWriter:
    """Blog writing crew powered by your style"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process="sequential",   # or "hierarchical"
            verbose=2,
        )
