#!/usr/bin/env python
import os
import logging
from typing import Dict
from hello_world_agent.schemas import InputSchema
from naptha_sdk.schemas import AgentRunInput
from naptha_sdk.user import sign_consumer_id

logger = logging.getLogger(__name__)


def run(module_run: Dict, *args, **kwargs):
    logger.info(f"SERPER_API_KEY: {os.getenv('SERPER_API_KEY')}")
    module_run = AgentRunInput(**module_run)
    module_run.inputs = InputSchema(**module_run.inputs)
    return f"Hello {module_run.inputs.firstname} {module_run.inputs.surname} from v0.1"

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
        "signature": sign_consumer_id(naptha.user.id, os.getenv("PRIVATE_KEY"))
    }

    response = run(module_run)

    print("Response: ", response)