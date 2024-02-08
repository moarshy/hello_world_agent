from hello_world_daimon_template.schema import JobRequestSchema
from hello_world_daimon_template.utils import get_logger


logger = get_logger(__name__)


def run(job: JobRequestSchema):
    logger.info(f"Running job {job.name}")
    return job.param1 + job.param2


if __name__ == "__main__":
    job = JobRequestSchema(
        name="addition",
        description="Add two numbers",
        param1=1,
        param2=2,
    )
    print(run(job))
