# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: avod/protos/kitti_dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from avod.protos import kitti_utils_pb2 as avod_dot_protos_dot_kitti__utils__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='avod/protos/kitti_dataset.proto',
  package='avod.protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x61vod/protos/kitti_dataset.proto\x12\x0b\x61vod.protos\x1a\x1d\x61vod/protos/kitti_utils.proto\"\xd7\x02\n\x12KittiDatasetConfig\x12\x13\n\x04name\x18\x01 \x01(\t:\x05kitti\x12/\n\x0b\x64\x61taset_dir\x18\x02 \x01(\t:\x1a../avod_data/Kitti/object/\x12\x19\n\ndata_split\x18\x03 \x01(\t:\x05train\x12 \n\x0e\x64\x61ta_split_dir\x18\x04 \x01(\t:\x08training\x12\x18\n\nhas_labels\x18\x05 \x01(\x08:\x04true\x12\x1c\n\rcluster_split\x18\x06 \x01(\t:\x05train\x12\x0f\n\x07\x63lasses\x18\x07 \x03(\t\x12\x14\n\x0cnum_clusters\x18\x08 \x03(\x05\x12\x12\n\nbev_source\x18\t \x02(\t\x12\x10\n\x08\x61ug_list\x18\n \x03(\t\x12\x39\n\x12kitti_utils_config\x18\x14 \x01(\x0b\x32\x1d.avod.protos.KittiUtilsConfig'
  ,
  dependencies=[avod_dot_protos_dot_kitti__utils__pb2.DESCRIPTOR,])




_KITTIDATASETCONFIG = _descriptor.Descriptor(
  name='KittiDatasetConfig',
  full_name='avod.protos.KittiDatasetConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='avod.protos.KittiDatasetConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"kitti".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_dir', full_name='avod.protos.KittiDatasetConfig.dataset_dir', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"../avod_data/Kitti/object/".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_split', full_name='avod.protos.KittiDatasetConfig.data_split', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"train".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_split_dir', full_name='avod.protos.KittiDatasetConfig.data_split_dir', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"training".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_labels', full_name='avod.protos.KittiDatasetConfig.has_labels', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_split', full_name='avod.protos.KittiDatasetConfig.cluster_split', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"train".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classes', full_name='avod.protos.KittiDatasetConfig.classes', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_clusters', full_name='avod.protos.KittiDatasetConfig.num_clusters', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bev_source', full_name='avod.protos.KittiDatasetConfig.bev_source', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aug_list', full_name='avod.protos.KittiDatasetConfig.aug_list', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kitti_utils_config', full_name='avod.protos.KittiDatasetConfig.kitti_utils_config', index=10,
      number=20, type=11, cpp_type=10, label=1,
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
  serialized_start=80,
  serialized_end=423,
)

_KITTIDATASETCONFIG.fields_by_name['kitti_utils_config'].message_type = avod_dot_protos_dot_kitti__utils__pb2._KITTIUTILSCONFIG
DESCRIPTOR.message_types_by_name['KittiDatasetConfig'] = _KITTIDATASETCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KittiDatasetConfig = _reflection.GeneratedProtocolMessageType('KittiDatasetConfig', (_message.Message,), {
  'DESCRIPTOR' : _KITTIDATASETCONFIG,
  '__module__' : 'avod.protos.kitti_dataset_pb2'
  # @@protoc_insertion_point(class_scope:avod.protos.KittiDatasetConfig)
  })
_sym_db.RegisterMessage(KittiDatasetConfig)


# @@protoc_insertion_point(module_scope)
