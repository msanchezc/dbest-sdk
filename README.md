# DBEST SDK

A Python package for remote control of DBEST (drone battery exchanger system)

## Generate protos
python -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. bidirectional.proto