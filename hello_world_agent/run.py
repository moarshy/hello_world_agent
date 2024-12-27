#!/usr/bin/env python

import logging
from hello_world_agent.schemas import InputSchema
from naptha_sdk.schemas import AgentRunInput


logger = logging.getLogger(__name__)


def run(module_run: AgentRunInput, *args, **kwargs):
    logger.info(f"Running module with inputs {module_run}")
    return f"Hello {module_run.inputs.firstname} {module_run.inputs.surname}"

if __name__ == "__main__":
    inputs = InputSchema(
        firstname="sam",
        surname="altman",
    )
    print(run(inputs))
