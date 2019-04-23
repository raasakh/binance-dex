# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stdSignature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stdSignature.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12stdSignature.proto\"f\n\x0cStdSignature\x12\x0f\n\x07pub_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x03 \x01(\x03\x12\x10\n\x08sequence\x18\x04 \x01(\x03\x1a\x08\n\x06PubKeyb\x06proto3')
)




_STDSIGNATURE_PUBKEY = _descriptor.Descriptor(
  name='PubKey',
  full_name='StdSignature.PubKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=124,
)

_STDSIGNATURE = _descriptor.Descriptor(
  name='StdSignature',
  full_name='StdSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='StdSignature.pub_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='StdSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_number', full_name='StdSignature.account_number', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='StdSignature.sequence', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STDSIGNATURE_PUBKEY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=124,
)

_STDSIGNATURE_PUBKEY.containing_type = _STDSIGNATURE
DESCRIPTOR.message_types_by_name['StdSignature'] = _STDSIGNATURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StdSignature = _reflection.GeneratedProtocolMessageType('StdSignature', (_message.Message,), dict(

  PubKey = _reflection.GeneratedProtocolMessageType('PubKey', (_message.Message,), dict(
    DESCRIPTOR = _STDSIGNATURE_PUBKEY,
    __module__ = 'stdSignature_pb2'
    # @@protoc_insertion_point(class_scope:StdSignature.PubKey)
    ))
  ,
  DESCRIPTOR = _STDSIGNATURE,
  __module__ = 'stdSignature_pb2'
  # @@protoc_insertion_point(class_scope:StdSignature)
  ))
_sym_db.RegisterMessage(StdSignature)
_sym_db.RegisterMessage(StdSignature.PubKey)


# @@protoc_insertion_point(module_scope)
