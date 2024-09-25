#!/usr/bin/env python

from hello_world.schemas import InputSchema
from naptha_sdk.utils import get_logger

logger = get_logger(__name__)

def run(inputs: InputSchema, worker_nodes = None, orchestrator_node = None, flow_run = None, cfg: dict = None, **kwargs):
    logger.info(f"Running module with inputs {inputs}")
    logger.info(f"cfg: {cfg}")
    return f"Hello {inputs.param1} + {inputs.param2}"

if __name__ == "__main__":
    inputs = InputSchema(
        param1="world",
        param2="naptha",
    )
    print(run(inputs))
