# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lang.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lang.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nlang.proto\"Q\n\x0bRegionProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\npopulation\x18\x03 \x01(\x05\x12\x14\n\x0cregion_group\x18\x04 \x03(\t\"\'\n\x0bScriptProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xec\x01\n\rLanguageProto\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x16\n\x0epreferred_name\x18\x05 \x01(\t\x12\x0f\n\x07\x61utonym\x18\x06 \x01(\t\x12\x12\n\npopulation\x18\x07 \x01(\x05\x12\x0e\n\x06region\x18\x08 \x03(\t\x12+\n\x0e\x65xemplar_chars\x18\t \x01(\x0b\x32\x13.ExemplarCharsProto\x12%\n\x0bsample_text\x18\n \x01(\x0b\x32\x10.SampleTextProto\"z\n\x12\x45xemplarCharsProto\x12\x0c\n\x04\x62\x61se\x18\x01 \x01(\t\x12\x11\n\tauxiliary\x18\x02 \x01(\t\x12\r\n\x05marks\x18\x03 \x01(\t\x12\x10\n\x08numerals\x18\x04 \x01(\t\x12\x13\n\x0bpunctuation\x18\x05 \x01(\t\x12\r\n\x05index\x18\x06 \x01(\t\"\xfc\x02\n\x0fSampleTextProto\x12\x19\n\x11\x66\x61llback_language\x18\x02 \x01(\t\x12\x15\n\rmasthead_full\x18\x03 \x01(\t\x12\x18\n\x10masthead_partial\x18\x04 \x01(\t\x12\x0e\n\x06styles\x18\x05 \x01(\t\x12\x0e\n\x06tester\x18\x06 \x01(\t\x12\x11\n\tposter_sm\x18\x07 \x01(\t\x12\x11\n\tposter_md\x18\x08 \x01(\t\x12\x11\n\tposter_lg\x18\t \x01(\t\x12\x13\n\x0bspecimen_48\x18\n \x01(\t\x12\x13\n\x0bspecimen_36\x18\x0b \x01(\t\x12\x13\n\x0bspecimen_32\x18\x0c \x01(\t\x12\x13\n\x0bspecimen_21\x18\r \x01(\t\x12\x13\n\x0bspecimen_16\x18\x0e \x01(\t\x12,\n\x06glyphs\x18\x0f \x03(\x0b\x32\x1c.SampleTextProto.GlyphsEntry\x1a-\n\x0bGlyphsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01'
)




_REGIONPROTO = _descriptor.Descriptor(
  name='RegionProto',
  full_name='RegionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='RegionProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='RegionProto.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='population', full_name='RegionProto.population', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region_group', full_name='RegionProto.region_group', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=14,
  serialized_end=95,
)


_SCRIPTPROTO = _descriptor.Descriptor(
  name='ScriptProto',
  full_name='ScriptProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScriptProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ScriptProto.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=97,
  serialized_end=136,
)


_LANGUAGEPROTO = _descriptor.Descriptor(
  name='LanguageProto',
  full_name='LanguageProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LanguageProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='LanguageProto.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='script', full_name='LanguageProto.script', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='LanguageProto.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preferred_name', full_name='LanguageProto.preferred_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='autonym', full_name='LanguageProto.autonym', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='population', full_name='LanguageProto.population', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='LanguageProto.region', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exemplar_chars', full_name='LanguageProto.exemplar_chars', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_text', full_name='LanguageProto.sample_text', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=139,
  serialized_end=375,
)


_EXEMPLARCHARSPROTO = _descriptor.Descriptor(
  name='ExemplarCharsProto',
  full_name='ExemplarCharsProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='ExemplarCharsProto.base', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auxiliary', full_name='ExemplarCharsProto.auxiliary', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='marks', full_name='ExemplarCharsProto.marks', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numerals', full_name='ExemplarCharsProto.numerals', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='punctuation', full_name='ExemplarCharsProto.punctuation', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='ExemplarCharsProto.index', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=377,
  serialized_end=499,
)


_SAMPLETEXTPROTO_GLYPHSENTRY = _descriptor.Descriptor(
  name='GlyphsEntry',
  full_name='SampleTextProto.GlyphsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='SampleTextProto.GlyphsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='SampleTextProto.GlyphsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=882,
)

_SAMPLETEXTPROTO = _descriptor.Descriptor(
  name='SampleTextProto',
  full_name='SampleTextProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fallback_language', full_name='SampleTextProto.fallback_language', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='masthead_full', full_name='SampleTextProto.masthead_full', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='masthead_partial', full_name='SampleTextProto.masthead_partial', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='styles', full_name='SampleTextProto.styles', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tester', full_name='SampleTextProto.tester', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poster_sm', full_name='SampleTextProto.poster_sm', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poster_md', full_name='SampleTextProto.poster_md', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poster_lg', full_name='SampleTextProto.poster_lg', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specimen_48', full_name='SampleTextProto.specimen_48', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specimen_36', full_name='SampleTextProto.specimen_36', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specimen_32', full_name='SampleTextProto.specimen_32', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specimen_21', full_name='SampleTextProto.specimen_21', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specimen_16', full_name='SampleTextProto.specimen_16', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='glyphs', full_name='SampleTextProto.glyphs', index=13,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SAMPLETEXTPROTO_GLYPHSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=882,
)

_LANGUAGEPROTO.fields_by_name['exemplar_chars'].message_type = _EXEMPLARCHARSPROTO
_LANGUAGEPROTO.fields_by_name['sample_text'].message_type = _SAMPLETEXTPROTO
_SAMPLETEXTPROTO_GLYPHSENTRY.containing_type = _SAMPLETEXTPROTO
_SAMPLETEXTPROTO.fields_by_name['glyphs'].message_type = _SAMPLETEXTPROTO_GLYPHSENTRY
DESCRIPTOR.message_types_by_name['RegionProto'] = _REGIONPROTO
DESCRIPTOR.message_types_by_name['ScriptProto'] = _SCRIPTPROTO
DESCRIPTOR.message_types_by_name['LanguageProto'] = _LANGUAGEPROTO
DESCRIPTOR.message_types_by_name['ExemplarCharsProto'] = _EXEMPLARCHARSPROTO
DESCRIPTOR.message_types_by_name['SampleTextProto'] = _SAMPLETEXTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegionProto = _reflection.GeneratedProtocolMessageType('RegionProto', (_message.Message,), {
  'DESCRIPTOR' : _REGIONPROTO,
  '__module__' : 'lang_pb2'
  # @@protoc_insertion_point(class_scope:RegionProto)
  })
_sym_db.RegisterMessage(RegionProto)

ScriptProto = _reflection.GeneratedProtocolMessageType('ScriptProto', (_message.Message,), {
  'DESCRIPTOR' : _SCRIPTPROTO,
  '__module__' : 'lang_pb2'
  # @@protoc_insertion_point(class_scope:ScriptProto)
  })
_sym_db.RegisterMessage(ScriptProto)

LanguageProto = _reflection.GeneratedProtocolMessageType('LanguageProto', (_message.Message,), {
  'DESCRIPTOR' : _LANGUAGEPROTO,
  '__module__' : 'lang_pb2'
  # @@protoc_insertion_point(class_scope:LanguageProto)
  })
_sym_db.RegisterMessage(LanguageProto)

ExemplarCharsProto = _reflection.GeneratedProtocolMessageType('ExemplarCharsProto', (_message.Message,), {
  'DESCRIPTOR' : _EXEMPLARCHARSPROTO,
  '__module__' : 'lang_pb2'
  # @@protoc_insertion_point(class_scope:ExemplarCharsProto)
  })
_sym_db.RegisterMessage(ExemplarCharsProto)

SampleTextProto = _reflection.GeneratedProtocolMessageType('SampleTextProto', (_message.Message,), {

  'GlyphsEntry' : _reflection.GeneratedProtocolMessageType('GlyphsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLETEXTPROTO_GLYPHSENTRY,
    '__module__' : 'lang_pb2'
    # @@protoc_insertion_point(class_scope:SampleTextProto.GlyphsEntry)
    })
  ,
  'DESCRIPTOR' : _SAMPLETEXTPROTO,
  '__module__' : 'lang_pb2'
  # @@protoc_insertion_point(class_scope:SampleTextProto)
  })
_sym_db.RegisterMessage(SampleTextProto)
_sym_db.RegisterMessage(SampleTextProto.GlyphsEntry)


_SAMPLETEXTPROTO_GLYPHSENTRY._options = None
# @@protoc_insertion_point(module_scope)
