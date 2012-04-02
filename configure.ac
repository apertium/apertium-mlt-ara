#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.52)

m4_define([required_apertium_version], [3.2.0])
m4_define([required_lttolbox_version], [3.1.2])

AC_INIT([apertium-mt-he], [0.1.0], [sagie@maoz.info])
AM_INIT_AUTOMAKE([apertium-mt-he], [0.1.0], no-define)
AC_PROG_LN_S
AC_PROG_AWK
# todo: only needed if we use a config.in file--should we?
# AC_CONFIG_HEADER([config])

AC_DEFUN([PKG_CHECK_APERTIUM], [
  APERTIUM_VER=0
  PKG_CHECK_MODULES(APERTIUM, apertium-3.0 >= 3.0.0,
  [
    APERTIUM_VER=30
  ],
  [
    PKG_CHECK_MODULES(APERTIUM, apertium-3.1 >= 3.1.0,
    [
      APERTIUM_VER=31
    ],
    [
      PKG_CHECK_MODULES(APERTIUM, apertium-3.2 >= 3.2.0)
      APERTIUM_VER=32
    ])
  ])
  AC_SUBST(APERTIUM_VER)
])

AC_DEFUN([PKG_CHECK_LTTOOLBOX], [
  LTTOOLBOX_VER=0
  PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox-3.0 >= 3.0.0,
  [
    LTTOOLBOX_VER=30
  ],
  [
    PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox-3.1 >= 3.1.0,
    [
      LTTOOLBOX_VER=31
    ],
    [
      PKG_CHECK_MODULES(LTTOOLBOX, lttoolbox-3.2 >= 3.2.0)
      LTTOOLBOX_VER=32
    ])
  ])
  AC_SUBST(LTTOOLBOX_VER)
])

PKG_CHECK_APERTIUM
PKG_CHECK_LTTOOLBOX


AC_OUTPUT([Makefile])
