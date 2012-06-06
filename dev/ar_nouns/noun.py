#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy, time;

sys.stdin  = codecs.getreader('utf-8')(sys.stdin);
sys.stdout = codecs.getwriter('utf-8')(sys.stdout);
sys.stderr = codecs.getwriter('utf-8')(sys.stderr);

def sym(syms): #{
	return '<s n="' + syms.replace('.', '"/><s n="') + '"/>';
#}

def header(): #{
	header = '';
	header = header + '<dictionary>\n';
	header = header + '  <alphabet>ABĊDEFĠGGHĦIIJKLMNOPQRSTUVWXZŻabċdefġgħghieiejklmnopqrstuvwxzżycYCáéíóúàèìòùñöëäïüçÿāēīōūăĕĭŏŭãẽĩõũ</alphabet>\n';
	header = header + '  <sdefs>\n';
	header = header + '    <sdef n="n"/>\n';
	header = header + '    <sdef n="np"/>\n';
	header = header + '    <sdef n="nn"/>\n';
	header = header + '    <sdef n="aa"/>\n';
	header = header + '    <sdef n="m"/>\n';
	header = header + '    <sdef n="f"/>\n';
	header = header + '    <sdef n="mf"/>\n';
	header = header + '    <sdef n="GD"/>\n';
	header = header + '    <sdef n="sg"/>\n';
	header = header + '    <sdef n="du"/>\n';
	header = header + '    <sdef n="pl"/>\n';
	header = header + '    <sdef n="sp"/>\n';
	header = header + '    <sdef n="ND"/>\n';
	header = header + '    <sdef n="nom"/>\n';
	header = header + '    <sdef n="gen"/>\n';
	header = header + '    <sdef n="acc"/>\n';
	header = header + '    <sdef n="genacc"/>\n';
	header = header + '    <sdef n="CD"/>\n';
	header = header + '    <sdef n="px3sg_m"/>\n';
	header = header + '    <sdef n="px3sg_f"/>\n';
	header = header + '    <sdef n="px2sg_m"/>\n';
	header = header + '    <sdef n="px2sg_f"/>\n';
	header = header + '    <sdef n="px1sg"/>\n';
	header = header + '    <sdef n="px3du"/>\n';
	header = header + '    <sdef n="px2du"/>\n';
	header = header + '    <sdef n="px3pl_m"/>\n';
	header = header + '    <sdef n="px3pl_f"/>\n';
	header = header + '    <sdef n="px2pl_m"/>\n';
	header = header + '    <sdef n="px2pl_f"/>\n';
	header = header + '    <sdef n="px1pl"/>\n';
	header = header + '    <sdef n="cstr"/>\n';
	header = header + '  </sdefs>\n';
	header = header + '  <pardefs>\n';


# possessive suffixes
	header = header + '    <pardef n="S__مدرس/ه">\n';
        header = header + '      <e><p><l>ه</l><r><s n="px3sg_m"/></r></p></e>\n';
        header = header + '      <e><p><l>ها</l><r><s n="px3sg_f"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><s n="px2sg_m"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><s n="px2sg_f"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="px1sg"/></r></p></e>\n';
        header = header + '      <e><p><l>هما</l><r><s n="px3du"/></r></p></e>\n';
        header = header + '      <e><p><l>كما</l><r><s n="px2du"/></r></p></e>\n';
        header = header + '      <e><p><l>هم</l><r><s n="px3pl_m"/></r></p></e>\n';
        header = header + '      <e><p><l>هن</l><r><s n="px3pl_f"/></r></p></e>\n';
        header = header + '      <e><p><l>كم</l><r><s n="px2pl_m"/></r></p></e>\n';
        header = header + '      <e><p><l>كن</l><r><s n="px2pl_f"/></r></p></e>\n';
        header = header + '      <e><p><l>نا</l><r><s n="px1pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';


# possessive suffixes - same as above, just split into px1sg and the rest
	header = header + '    <pardef n="S__مدرس/ي">\n';
        header = header + '      <e><p><l>ي</l><r><s n="px1sg"/></r></p></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__مدرس/ك">\n';
        header = header + '      <e><p><l>ه</l><r><s n="px3sg_m"/></r></p></e>\n';
        header = header + '      <e><p><l>ها</l><r><s n="px3sg_f"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><s n="px2sg_m"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><s n="px2sg_f"/></r></p></e>\n';
        header = header + '      <e><p><l>هما</l><r><s n="px3du"/></r></p></e>\n';
        header = header + '      <e><p><l>كما</l><r><s n="px2du"/></r></p></e>\n';
        header = header + '      <e><p><l>هم</l><r><s n="px3pl_m"/></r></p></e>\n';
        header = header + '      <e><p><l>هن</l><r><s n="px3pl_f"/></r></p></e>\n';
        header = header + '      <e><p><l>كم</l><r><s n="px2pl_m"/></r></p></e>\n';
        header = header + '      <e><p><l>كن</l><r><s n="px2pl_f"/></r></p></e>\n';
        header = header + '      <e><p><l>نا</l><r><s n="px1pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# no special ending
	header = header + '    <pardef n="S__بيت/">\n';
# absolute
        header = header + '      <e><p><l/><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ا</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l/><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l/><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l/><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# no special ending, with article
	header = header + '    <pardef n="S__البيت/">\n';
        header = header + '      <e><p><l/><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';


# with preposition ب, ك or ل
	header = header + '    <pardef n="S__ببيت/">\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالبيت/">\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final ة
	header = header + '    <pardef n="S__مدرس/ة">\n';
# absolute
        header = header + '      <e><p><l>ة</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ة</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ت</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ت</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ت</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__المدرس/ة">\n';
        header = header + '      <e><p><l>ة</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition ب, ك or ل
	header = header + '    <pardef n="S__بمدرس/ة">\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ت</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';

# with preposition and article
	header = header + '    <pardef n="S__بالمدرس/ة">\n';
        header = header + '      <e><p><l>ة</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final أ
	header = header + '    <pardef n="S__/أ">\n';
# absolute
        header = header + '      <e><p><l>أ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>أ</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p><par n="S__مدرس/ك"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/></r></p><par n="S__مدرس/ك"/></e>\n';
	header = header + '    </pardef>\n';
	

# with article
	header = header + '    <pardef n="S__ال/أ">\n';
        header = header + '      <e><p><l>أ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';


# with preposition ب, ك or ل
	header = header + '    <pardef n="S__ب/أ">\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بال/أ">\n';
        header = header + '      <e><p><l>أ</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final ئ
	header = header + '    <pardef n="S__قار/ئ">\n';
# absolute
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئا</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';

# with article
	header = header + '    <pardef n="S__القار/ئ">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بقار/ئ">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';

# with preposition and article
	header = header + '    <pardef n="S__بالقار/ئ">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final ؤ
	header = header + '    <pardef n="S__لؤل/ؤ">\n';
# absolute
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤا</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p><par n="S__مدرس/ك"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="acc"/></r></p><par n="S__مدرس/ك"/></e>\n';
	header = header + '    </pardef>\n';

# with article
	header = header + '    <pardef n="S__اللؤل/ؤ">\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';


# with preposition
	header = header + '    <pardef n="S__بلؤل/ؤ">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__باللؤل/ؤ">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final ء, no additional ا in acc
	header = header + '    <pardef n="S__جزء/">\n';
# absolute
        header = header + '      <e><p><l>ء</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ء</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p><par n="S__مدرس/ك"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/></r></p><par n="S__مدرس/ك"/></e>\n';
	header = header + '    </pardef>\n';


	header = header + '    <pardef n="S__الجزء/">\n';
        header = header + '      <e><p><l>ء</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';


	header = header + '    <pardef n="S__بجزء/">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


	header = header + '    <pardef n="S__بالجزء/">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';



## -------------------------------------------------------------------------##


# final ء، ا in acc
	header = header + '    <pardef n="S__شي/ء">\n';
# absolute
        header = header + '      <e><p><l>ء</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r>><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ءا</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ء</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ئ</l><r><s n="nom"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>ؤ</l><r><s n="nom"/></r></p><par n="S__مدرس/ك"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="acc"/></r></p><par n="S__مدرس/ي"/></e>\n';
        header = header + '      <e><p><l>أ</l><r><s n="acc"/></r></p><par n="S__مدرس/ك"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__شي/ء">\n';
        header = header + '      <e><p><l>ء</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ء</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition ب, ك or ل 
	header = header + '    <pardef n="S__شي/ء">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';

# with preposition and article
	header = header + '    <pardef n="S__شي/ء">\n';
        header = header + '      <e><p><l>ئ</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';

## -------------------------------------------------------------------------##


# final tanwin kasra
	header = header + '    <pardef n="S__قاض/">\n';
# absolute
        header = header + '      <e><p><l/><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>يا</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ي</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ي</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__القاض/">\n';
        header = header + '      <e><p><l>ي</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بقاض/">\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالقاض/">\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';



## -------------------------------------------------------------------------##


# false final tanwin kasra
	header = header + '    <pardef n="S__صحار/">\n';
# absolute
        header = header + '      <e><p><l/><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ي</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ي</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__الصحار/">\n';
        header = header + '      <e><p><l>ي</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بصحار/">\n';
        header = header + '      <e><p><l/><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l/><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالصحار/">\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


# final tanwin fatha
	header = header + '    <pardef n="S__مستشفى/">\n';
# absolute
        header = header + '      <e><p><l>ى</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ى</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ا</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ا</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ا</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__المستشفى/">\n';
        header = header + '      <e><p><l>ى</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بمستشفى/">\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ا</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالمستشفى/">\n';
        header = header + '      <e><p><l>ى</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##

# dual
	header = header + '    <pardef n="S__بيت/ان">\n';
# absolute
        header = header + '      <e><p><l>ان</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ا</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ا</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__البيت/ان">\n';
        header = header + '      <e><p><l>ان</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__ببيت/ان">\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالبيت/ان">\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##

# sound plural m
	header = header + '    <pardef n="S__مدرس/ون">\n';
# absolute
        header = header + '      <e><p><l>ون</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>و</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>و</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__المدرس/ون">\n';
        header = header + '      <e><p><l>ون</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ين</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بمدرس/ون">\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ي</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالمدرس/ون">\n';
        header = header + '      <e><p><l>ين</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##

# sound plural f
	header = header + '    <pardef n="S__مدرس/ات">\n';
# absolute
        header = header + '      <e><p><l>ات</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="acc"/></r></p></e>\n';
# construct state
        header = header + '      <e><p><l>ات</l><r><s n="nom"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="acc"/><s n="cstr"/></r></p></e>\n';
# with possessive suffixes
        header = header + '      <e><p><l>ات</l><r><s n="nom"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="acc"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with article
	header = header + '    <pardef n="S__المدرس/ات">\n';
        header = header + '      <e><p><l>ات</l><r><s n="nom"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="acc"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# with preposition
	header = header + '    <pardef n="S__بمدرس/ات">\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/><s n="cstr"/></r></p></e>\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p><par n="S__مدرس/ه"/></e>\n';
	header = header + '    </pardef>\n';


# with preposition and article
	header = header + '    <pardef n="S__بالمدرس/ات">\n';
        header = header + '      <e><p><l>ات</l><r><s n="gen"/></r></p></e>\n';
	header = header + '    </pardef>\n';


## -------------------------------------------------------------------------##


	header = header + '  </pardefs>\n\n';
	header = header + '  <section id="main" type="standard">\n';
    	header = header + '  <!-- Generated on: ' + time.strftime('%Y-%m-%d %H:%M %Z') + ' -->\n\n';
	

	return header;
	
#}



##-----------------------------------------------------------------------------##


 
def footer(): #{
	footer = '';
	footer = footer + '  </section>\n';
	footer = footer + '</dictionary>\n';
	
	return footer;
#}


##-----------------------------------------------------------------------------##

if len(sys.argv)>1:
    if '--help' in sys.argv:
        print "Usage: nouns.py nouns_file";
        sys.exit(1);


#if len(sys.argv) == 2 :
#	nounsfile = sys.argv[1];
#else :
#	nounsfile = sys.path[0] + '/nouns.wiki';

#try:
#	lines = file(stemsfile);
#except IOError as e:
#        sys.stderr.write("Error reading file: {0}\n".format(nounsfile));
#        sys.exit(1);


#nouns = [];

#for line in lines: #{

#	line = line.strip(); 
#
#	# '|-', '|}', headings, '{|'
#	if len(line) < 3 or line[0] == '!' or line[0] == '{':
#	        continue;
    
#	line = line.lstrip('|');
#	row = line.split('||'); 


#	noun = {'stem': row[0].strip(), 'cat': row[1].strip(), 'type': row[2].strip(), 'theme': row[3].strip(), 'subtype': row[4].strip(), 'gloss': row[5].strip(), 'root': row[6].strip(), 'vowels_perf': row[7].strip(), 'vowels_impf': row[8].strip(), 'trans': row[9].strip()};
#	nouns = nouns + [noun];


#}



##-----------------------------------------------------------------------------##


#for noun in nouns: #{

#}


print header().decode('utf-8');

#for stem in infl: #{
#
#	s = stem.split('.');
#	stem_stem = s[0];
#	stem_trans = s[1];

#	for flex in infl[stem]: #{
#		for subflex in infl[stem][flex]: #{
#			# restriction attribute, lm attribute, postgenerator tag:
#			r, lm, a = '', '', ''	 
#			if flex == 'past.p3.m.sg' and subflex[1] == '-':  
#				lm = ' lm="%s"' % (stem,)
#			if subflex[2] == 'LR':
#				r = ' r="%s"' % (subflex[2],)
#				a = ''
#			elif subflex[2] == 'RL':
#				r = ' r="%s"' % (subflex[2],)
#				a = '<a/>'
#
#			left = subflex[0];
#			right = '%s<s n="%s"/><s n="%s"/>%s' % (stem_stem, verb_cat[stem], stem_trans, sym(flex));
#			paradigm = subflex[1];
#
#			if paradigm == "-": # no suffix
#				entry  = '<e%s%s><p><l>%s%s</l><r>%s</r></p></e>' % (r, lm, a, left,right);
#			else :  # suffix, in this case subflex[1] tells us which paradigm should be used
#				entry = '<e%s><p><l>%s%s</l><r>%s</r></p><par n="%s"/></e>' % (r, a, left, right, paradigm);
#
#			print entry.decode('utf-8')
#			#}
#		#}
#	#}
#}

print footer();
