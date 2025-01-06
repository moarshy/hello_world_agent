#!/usr/bin/env python

import logging
from hello_world_agent.schemas import InputSchema
from naptha_sdk.schemas import AgentRunInput
from typing import Dict

logger = logging.getLogger(__name__)


def run(module_run: Dict, *args, **kwargs):
    module_run = AgentRunInput(**module_run)
    module_run.inputs = InputSchema(**module_run.inputs)
    return f"Hello {module_run.inputs.firstname} {module_run.inputs.surname}"

if __name__ == "__main__":
    import asyncio
    import os
    from naptha_sdk.configs import setup_module_deployment
    from naptha_sdk.client.naptha import Naptha

    naptha = Naptha()

    deployment = asyncio.run(setup_module_deployment("agent", "hello_world_agent/configs/deployment.json", node_url = os.getenv("NODE_URL")))

    input_params = {
        "firstname": "sam",
        "surname": "altman",
    }
    
    module_run = {
        "inputs": input_params,
        "deployment": deployment,
        "consumer_id": naptha.user.id,
    }

    response = run(module_run)

    print("Response: ", response)