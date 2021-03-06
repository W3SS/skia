# Copyright 2015 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# GYP file to build experimental directory.
{
  'targets': [
    {
      'target_name': 'experimental',
      'type': 'static_library',
      'include_dirs': [
        '../include/config',
        '../include/core',
      ],
      'sources': [
        '../experimental/SkSetPoly3To3.cpp',
        '../experimental/SkSetPoly3To3_A.cpp',
        '../experimental/SkSetPoly3To3_D.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../experimental',
        ],
      },
    },
  ],
  'conditions': [
    ['skia_os == "mac"',
      {
        'targets': [
          {
            'target_name': 'coreGraphicsPdf2png',
            'type': 'executable',
            'include_dirs': [ '../src/core', ],
            'sources': [ '../experimental/tools/coreGraphicsPdf2png.cpp', ],
            'dependencies': [ 'skia_lib.gyp:skia_lib', ]
          },
        ],
      },
    ],
  ],
}
