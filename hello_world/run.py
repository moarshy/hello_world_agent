from hello_world.schemas import InputSchema
from hello_world.utils import get_logger


logger = get_logger(__name__)


def run(job: InputSchema):
    logger.info(f"Running job {job.name}")
    return job.param1 + job.param2


if __name__ == "__main__":
    job = InputSchema(
        name="addition",
        description="Add two numbers",
        param1=1,
        param2=2,
    )
    print(run(job))
