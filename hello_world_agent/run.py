#!/usr/bin/env python

import logging
from hello_world_agent.schemas import InputSchema


logger = logging.getLogger(__name__)


def run(inputs: InputSchema, *args, **kwargs):
    logger.info(f"Running module with inputs {inputs}")
    return f"Hello {inputs.firstname} {inputs.surname}"

if __name__ == "__main__":
    inputs = InputSchema(
        firstname="sam",
        surname="altman",
    )
    print(run(inputs))
