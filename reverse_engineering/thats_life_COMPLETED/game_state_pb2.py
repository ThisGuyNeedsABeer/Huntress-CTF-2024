# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_state.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10game_state.proto\"9\n\x04Grid\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\x12\n\x04rows\x18\x03 \x03(\x0b\x32\x04.Row\"\x1b\n\x03Row\x12\x14\n\x05\x63\x65lls\x18\x01 \x03(\x0b\x32\x05.Cell\"$\n\x04\x43\x65ll\x12\r\n\x05\x61live\x18\x01 \x01(\x08\x12\r\n\x05\x63olor\x18\x02 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_state_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GRID._serialized_start=20
  _GRID._serialized_end=77
  _ROW._serialized_start=79
  _ROW._serialized_end=106
  _CELL._serialized_start=108
  _CELL._serialized_end=144
# @@protoc_insertion_point(module_scope)