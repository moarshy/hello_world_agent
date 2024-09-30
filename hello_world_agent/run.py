#!/usr/bin/env python

from hello_world_agent.schemas import InputSchema
from naptha_sdk.utils import get_logger

logger = get_logger(__name__)

def run(inputs: InputSchema, *args, **kwargs):
    logger.info(f"Running module with inputs {inputs}")
    return f"Hello {inputs.firstname} {inputs.surname}"

if __name__ == "__main__":
    inputs = InputSchema(
        firstname="sam",
        surname="altman",
    )
    print(run(inputs))
