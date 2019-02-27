import pytest

from fairing.preprocessors.function import FunctionPreProcessor
from fairing.builders.append.append import AppendBuilder
from fairing.deployers.gcp.gcp import GCPJob

def run(fn):
  preprocessor = FunctionPreProcessor(function_obj=fn)
  builder = AppendBuilder(preprocessor=preprocessor)
  deployer = GCPJob()

  builder.build()
  pod_spec = builder.generate_pod_spec()
  deployer.deploy(pod_spec)

def hello_world():
  import time
  time.sleep(120)
  print('Hello world')

def test_end_to_end():
  run(hello_world)
  assert True

