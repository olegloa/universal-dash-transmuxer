# Tools, tests, and utilities for DashToHls.
#
# Do not OpenSource.  The OpenSource packager will run this to generate
# Xcode projects and Makefiles.

{
  'target_defaults': {
    'xcode_settings': {
      'CLANG_ENABLE_OBJC_ARC': [ 'YES' ],
    },
    'conditions': [
      ['OS=="mac"', {
        'xcode_settings': {
          'GCC_PREFIX_HEADER': 'DashToHls_osx.pch',
        },
      }],
      ['OS=="ios"', {
        'xcode_settings': {
          'GCC_PREFIX_HEADER': 'DashToHls_ios.pch',
        },
      }],
    ],
  },
  'conditions': [
    ['OS=="mac"', {
      'target_defaults': {
        'xcode_settings': {
          'ARCHS[sdk=macosx*]': 'x86_64',
        },
      },
      'targets': [{
          'target_name': 'DashToHlsTools',
          'type': 'executable',
            'xcode_settings': {
              'INFOPLIST_FILE': 'tools/OSX/tools-Info.plist',
            },
            'mac_bundle': 1,
            'mac_bundle_resources': [
              'tools/OSX/Base.lproj/MainMenu.xib',
              'tools/OSX/tools-Info.plist',
              'tools/OSX/en.lproj/InfoPlist.strings',
            ],
            'sources': [
              'tools/OSX/ToolsAppDelegate.h',
              'tools/OSX/ToolsAppDelegate.mm',
              'tools/OSX/ToolsMpdParser.h',
              'tools/OSX/ToolsMpdParser.mm',
              'tools/OSX/main.m',
            ],
            'include_dirs': [
              '..',
            ],
            'dependencies': [
              'DashToHls.gyp:DashToHlsLibrary',
            ],
          }],
        },
      ]],
  'targets': [
    {
      'target_name': 'gtestlib',
      'type': 'static_library',
      'include_dirs': [
        '<(DEPTH)/',
        '<(DEPTH)/third_party/gtest/include',
        '<(DEPTH)/third_party/gmock/include',
      ],
      'all_dependent_settings': {
        'include_dirs': [
          '<(DEPTH)/',
          '<(DEPTH)/third_party/gtest/include',
          '<(DEPTH)/third_party/gmock/include',
        ],
        'xcode_settings': {
          'OTHER_CFLAGS': [
          '-DGTEST_USE_OWN_TR1_TUPLE=1',
          ],
        },
      },
      'xcode_settings': {
        'OTHER_CFLAGS': [
        '-DGTEST_USE_OWN_TR1_TUPLE=1',
        ],
      },
      'sources': [
        '<(DEPTH)/third_party/gtest/src/gtest-all.cc',
        '<(DEPTH)/third_party/gmock/src/gmock-all.cc',
      ]
    },
  ],
}
