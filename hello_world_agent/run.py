#!/usr/bin/env python

import logging
from hello_world_agent.schemas import InputSchema
from naptha_sdk.schemas import AgentRunInput


logger = logging.getLogger(__name__)


def run(agent_run: AgentRunInput, *args, **kwargs):
    logger.info(f"Running module with inputs {agent_run}")
    return f"Hello {agent_run.inputs.firstname} {agent_run.inputs.surname}"

if __name__ == "__main__":
    inputs = InputSchema(
        firstname="sam",
        surname="altman",
    )
    print(run(inputs))
