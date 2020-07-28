# Generate pb2.py and pb2_grpc.py files from protos

```bash
python3 -m grpc_tools.protoc -I . –python_out=dbest_sdk/autogen –grpc_python_out=dbest_sdk/autogen –proto_path=protos bidirectional.proto
```

# Fix imports on *_pb2_grpc.py files, example:

```python
import bidirectional_pb2 as bidirectional__pb2
# to
from dbest_sdk.autogen import bidirectional_pb2 as bidirectional__pb2
```
