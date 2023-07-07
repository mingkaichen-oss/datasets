# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: skip-file

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_datasets/proto/tf_example.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_datasets.proto import tf_feature_generated_pb2 as tensorflow__datasets_dot_proto_dot_tf__feature__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n*tensorflow_datasets/proto/tf_example.proto\x12\x0ftensorflow_copy\x1a*tensorflow_datasets/proto/tf_feature.proto"6\n\x07\x45xample\x12+\n\x08\x66\x65\x61tures\x18\x01'
    b' \x01(\x0b\x32\x19.tensorflow_copy.Features"s\n\x0fSequenceExample\x12*\n\x07\x63ontext\x18\x01'
    b' \x01(\x0b\x32\x19.tensorflow_copy.Features\x12\x34\n\rfeature_lists\x18\x02'
    b' \x01(\x0b\x32\x1d.tensorflow_copy.FeatureListsB\x81\x01\n\x16org.tensorflow.exampleB\rExampleProtosP\x01ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\xf8\x01\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'tensorflow_datasets.proto.tf_example_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026org.tensorflow.exampleB\rExampleProtosP\001ZSgithub.com/tensorflow/tensorflow/tensorflow/go/core/example/example_protos_go_proto\370\001\001'
  _EXAMPLE._serialized_start = 107
  _EXAMPLE._serialized_end = 161
  _SEQUENCEEXAMPLE._serialized_start = 163
  _SEQUENCEEXAMPLE._serialized_end = 278
# @@protoc_insertion_point(module_scope)
