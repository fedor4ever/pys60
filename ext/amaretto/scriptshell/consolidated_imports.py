# Copyright (c) 2009 Nokia Corporation
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

import aifc
import anydbm
import array
import asynchat
import asyncore
import atexit
import base64
import BaseHTTPServer
import bdb
import binascii
import binhex
import bisect
import cgi
import chunk
import cmath
import cmd
import code
import codecs
import _codecs_cn
import _codecs_hk
import _codecs_iso2022
import _codecs_jp
import _codecs_kr
import _codecs_tw
import codeop
import collections
import colorsys
import commands
import compiler
import ConfigParser
import contextlib
import Cookie
import cookielib
import copy
import copy_reg
import cPickle
import cProfile
import cStringIO
import csv
import datetime
import decimal
import difflib
import dircache
import dis
import dl
import doctest
import DocXMLRPCServer
import dumbdbm
import dummy_thread
import dummy_threading
import _elementtree
import email
import encodings
import errno
import fcntl
import filecmp
import fileinput
import fnmatch
import formatter
import fpformat
import ftplib
import functools
import getopt
import gettext
import glob
import gzip
import hashlib
import heapq
import hmac
import hotshot
import htmlentitydefs
import htmllib
import HTMLParser
import httplib
import imaplib
import imghdr
import inspect
import interactive_console
import itertools
import keyword
import linecache
import locale
import logging
import _lsprof
import mailbox
import markupbase
import math
import md5
import mhlib
import mimetools
import mimetypes
import MimeWriter
import _multibytecodec
import multifile
import netrc
import new
import ntpath
import nturl2path
import opcode
import operator
import optparse
import os
import parser
import pdb
import pickle
import pickletools
import pkgutil
import platform
import popen2
import posixpath
import pprint
import profile
import pstats
import pty
import pyclbr
import pydoc
import pyexpat
import py_compile
import Queue
import quopri
import random
import re
import repr
import rfc822
import robotparser
import runpy
import select
import sets
import socket
import sgmllib
import sha
import _sha256
import _sha512
import shelve
import shlex
import shutil
import SimpleHTTPServer
import site
import smtplib
import sndhdr
import SocketServer
import sre
import sre_compile
import sre_constants
import sre_parse
import _ssl
import stat
import string
import StringIO
import stringprep
import struct
import subprocess
import symbol
import symtable
import tarfile
import tempfile
import _testcapi
import textwrap
import thread
import threading
import token
import tokenize
import trace
import traceback
import tty
import types
import unicodedata
import unittest
import urllib
import urllib2
import urlparse
import UserDict
import UserList
import UserString
import uu
import uuid
import warnings
import wave
import weakref
import whichdb
import wsgiref
import xdrlib
import xml
import xmllib
import xmlrpclib
import xxsubtype
import zipfile
import _LWPCookieJar
import _MozillaCookieJar
import _strptime
import _threading_local
import __future__

import compiler.ast
import compiler.consts
import compiler.future
import compiler.misc
import compiler.pyassem
import compiler.pycodegen
import compiler.symbols
import compiler.syntax
import compiler.transformer
import compiler.visitor

import email.base64mime
import email.charset
import email.encoders
import email.errors
import email.feedparser
import email.generator
import email.header
import email.iterators
import email.message
import email.mime
import email.parser
import email.quoprimime
import email.utils
import email._parseaddr
import email.mime.application
import email.mime.audio
import email.mime.base
import email.mime.image
import email.mime.message
import email.mime.multipart
import email.mime.nonmultipart
import email.mime.text

import encodings.aliases
import encodings.encodings.ascii
import encodings.encodings.base64_codec
import encodings.big5
import encodings.big5hkscs
import encodings.bz2_codec
import encodings.charmap
import encodings.cp037
import encodings.cp1006
import encodings.cp1026
import encodings.cp1140
import encodings.cp1250
import encodings.cp1251
import encodings.cp1252
import encodings.cp1253
import encodings.cp1254
import encodings.cp1255
import encodings.cp1256
import encodings.cp1257
import encodings.cp1258
import encodings.cp424
import encodings.cp437
import encodings.cp500
import encodings.cp737
import encodings.cp775
import encodings.cp850
import encodings.cp852
import encodings.cp855
import encodings.cp856
import encodings.cp857
import encodings.cp860
import encodings.cp861
import encodings.cp862
import encodings.cp863
import encodings.cp864
import encodings.cp865
import encodings.cp866
import encodings.cp869
import encodings.cp874
import encodings.cp875
import encodings.cp932
import encodings.cp949
import encodings.cp950
import encodings.euc_jisx0213
import encodings.euc_jis_2004
import encodings.euc_jp
import encodings.euc_kr
import encodings.gb18030
import encodings.gb2312
import encodings.gbk
import encodings.hex_codec
import encodings.hp_roman8
import encodings.hz
import encodings.idna
import encodings.iso2022_jp
import encodings.iso2022_jp_1
import encodings.iso2022_jp_2
import encodings.iso2022_jp_2004
import encodings.iso2022_jp_3
import encodings.iso2022_jp_ext
import encodings.iso2022_kr
import encodings.iso8859_1
import encodings.iso8859_10
import encodings.iso8859_11
import encodings.iso8859_13
import encodings.iso8859_14
import encodings.iso8859_15
import encodings.iso8859_16
import encodings.iso8859_2
import encodings.iso8859_3
import encodings.iso8859_4
import encodings.iso8859_5
import encodings.iso8859_6
import encodings.iso8859_7
import encodings.iso8859_8
import encodings.iso8859_9
import encodings.johab
import encodings.koi8_r
import encodings.koi8_u
import encodings.latin_1
import encodings.mac_arabic
import encodings.mac_centeuro
import encodings.mac_croatian
import encodings.mac_cyrillic
import encodings.mac_farsi
import encodings.mac_greek
import encodings.mac_iceland
import encodings.mac_latin2
import encodings.mac_roman
import encodings.mac_romanian
import encodings.mac_turkish
import encodings.mbcs
import encodings.palmos
import encodings.ptcp154
import encodings.punycode
import encodings.quopri_codec
import encodings.raw_unicode_escape
import encodings.rot_13
import encodings.shift_jis
import encodings.shift_jisx0213
import encodings.shift_jis_2004
import encodings.string_escape
import encodings.tis_620
import encodings.undefined
import encodings.unicode_escape
import encodings.unicode_internal
import encodings.utf_16
import encodings.utf_16_be
import encodings.utf_16_le
import encodings.utf_7
import encodings.utf_8
import encodings.utf_8_sig
import encodings.uu_codec
import encodings.zlib_codec

import hotshot
import hotshot.log
import hotshot.stats
import hotshot.stones

import logging.config
import logging.handlers

import wsgiref.handlers
import wsgiref.headers
import wsgiref.simple_server
import wsgiref.util
import wsgiref.validate

import xml.dom
import xml.dom.domreg
import xml.dom.expatbuilder
import xml.dom.minicompat
import xml.dom.minidom
import xml.dom.NodeFilter
import xml.dom.pulldom
import xml.dom.xmlbuilder
import xml.etree.cElementTree
import xml.etree.ElementInclude
import xml.etree.ElementPath
import xml.etree.ElementTree
import xml.etree
import xml.parsers.expat
import xml.parsers
import xml.sax
import xml.sax.expatreader
import xml.sax.handler
import xml.sax.saxutils
import xml.sax.xmlreader
import xml.sax._exceptions

# Adding amaretto modules
import btsocket
import calendar
import camera
import e32
import e32calendar
import e32dbm
import globalui
import gles
import glcanvas
import telephone
import audio
import appuifw
import graphics
import topwindow
import sysinfo
import sensor
import contacts
import e32db
import inbox
import keycapture
import location
import logs
import messaging
import positioning

import scriptext
