#!/usr/bin/env python

from hello_world_agent.schemas import InputSchema
from naptha_sdk.utils import get_logger

logger = get_logger(__name__)

def run(inputs: InputSchema, *args, **kwargs):
    logger.info(f"Running module with inputs {inputs}")
    return f"Hello {inputs.param1} + {inputs.param2}"

if __name__ == "__main__":
    inputs = InputSchema(
        param1="world",
        param2="naptha",
    )
    print(run(inputs))
