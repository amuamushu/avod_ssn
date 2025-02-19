# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: avod/protos/kitti_utils.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from avod.protos import mini_batch_pb2 as avod_dot_protos_dot_mini__batch__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='avod/protos/kitti_utils.proto',
  package='avod.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x61vod/protos/kitti_utils.proto\x12\x0b\x61vod.protos\x1a\x1c\x61vod/protos/mini_batch.proto\"\xdd\x01\n\x10KittiUtilsConfig\x12\x14\n\x0c\x61rea_extents\x18\x01 \x03(\x02\x12\x12\n\nvoxel_size\x18\x02 \x02(\x02\x12\x16\n\x0e\x61nchor_strides\x18\x03 \x03(\x02\x12\x1c\n\x11\x64\x65nsity_threshold\x18\x04 \x01(\x05:\x01\x31\x12\x30\n\rbev_generator\x18\x14 \x02(\x0b\x32\x19.avod.protos.BevGenerator\x12\x37\n\x11mini_batch_config\x18\x15 \x02(\x0b\x32\x1c.avod.protos.MiniBatchConfig\"\x97\x01\n\x0c\x42\x65vGenerator\x12\x32\n\x06slices\x18\x01 \x01(\x0b\x32 .avod.protos.BevGenerator.SlicesH\x00\x1a\x42\n\x06Slices\x12\x11\n\theight_lo\x18\x01 \x02(\x02\x12\x11\n\theight_hi\x18\x02 \x02(\x02\x12\x12\n\nnum_slices\x18\x03 \x02(\x05\x42\x0f\n\rbev_maps_type'
  ,
  dependencies=[avod_dot_protos_dot_mini__batch__pb2.DESCRIPTOR,])




_KITTIUTILSCONFIG = _descriptor.Descriptor(
  name='KittiUtilsConfig',
  full_name='avod.protos.KittiUtilsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_extents', full_name='avod.protos.KittiUtilsConfig.area_extents', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voxel_size', full_name='avod.protos.KittiUtilsConfig.voxel_size', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='anchor_strides', full_name='avod.protos.KittiUtilsConfig.anchor_strides', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='density_threshold', full_name='avod.protos.KittiUtilsConfig.density_threshold', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bev_generator', full_name='avod.protos.KittiUtilsConfig.bev_generator', index=4,
      number=20, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mini_batch_config', full_name='avod.protos.KittiUtilsConfig.mini_batch_config', index=5,
      number=21, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=298,
)


_BEVGENERATOR_SLICES = _descriptor.Descriptor(
  name='Slices',
  full_name='avod.protos.BevGenerator.Slices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height_lo', full_name='avod.protos.BevGenerator.Slices.height_lo', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height_hi', full_name='avod.protos.BevGenerator.Slices.height_hi', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_slices', full_name='avod.protos.BevGenerator.Slices.num_slices', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=435,
)

_BEVGENERATOR = _descriptor.Descriptor(
  name='BevGenerator',
  full_name='avod.protos.BevGenerator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='slices', full_name='avod.protos.BevGenerator.slices', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BEVGENERATOR_SLICES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='bev_maps_type', full_name='avod.protos.BevGenerator.bev_maps_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=301,
  serialized_end=452,
)

_KITTIUTILSCONFIG.fields_by_name['bev_generator'].message_type = _BEVGENERATOR
_KITTIUTILSCONFIG.fields_by_name['mini_batch_config'].message_type = avod_dot_protos_dot_mini__batch__pb2._MINIBATCHCONFIG
_BEVGENERATOR_SLICES.containing_type = _BEVGENERATOR
_BEVGENERATOR.fields_by_name['slices'].message_type = _BEVGENERATOR_SLICES
_BEVGENERATOR.oneofs_by_name['bev_maps_type'].fields.append(
  _BEVGENERATOR.fields_by_name['slices'])
_BEVGENERATOR.fields_by_name['slices'].containing_oneof = _BEVGENERATOR.oneofs_by_name['bev_maps_type']
DESCRIPTOR.message_types_by_name['KittiUtilsConfig'] = _KITTIUTILSCONFIG
DESCRIPTOR.message_types_by_name['BevGenerator'] = _BEVGENERATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KittiUtilsConfig = _reflection.GeneratedProtocolMessageType('KittiUtilsConfig', (_message.Message,), {
  'DESCRIPTOR' : _KITTIUTILSCONFIG,
  '__module__' : 'avod.protos.kitti_utils_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.KittiUtilsConfig)
  })
_sym_db.RegisterMessage(KittiUtilsConfig)

BevGenerator = _reflection.GeneratedProtocolMessageType('BevGenerator', (_message.Message,), {

  'Slices' : _reflection.GeneratedProtocolMessageType('Slices', (_message.Message,), {
    'DESCRIPTOR' : _BEVGENERATOR_SLICES,
    '__module__' : 'avod.protos.kitti_utils_pb2'
    # @@protoc_insertion_point(class_scope:avod.protos.BevGenerator.Slices)
    })
  ,
  'DESCRIPTOR' : _BEVGENERATOR,
  '__module__' : 'avod.protos.kitti_utils_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.BevGenerator)
  })
_sym_db.RegisterMessage(BevGenerator)
_sym_db.RegisterMessage(BevGenerator.Slices)


# @@protoc_insertion_point(module_scope)
