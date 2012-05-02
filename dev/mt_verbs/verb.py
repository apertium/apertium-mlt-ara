#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;
#import classes;

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
	header = header + '    <sdef n="vblex"/>\n';
	header = header + '    <sdef n="prn"/>\n';
	header = header + '    <sdef n="past"/>\n';
	header = header + '    <sdef n="neg"/>\n';
	header = header + '    <sdef n="pres"/>\n';
	header = header + '    <sdef n="imp"/>\n';
	header = header + '    <sdef n="pprs"/>\n';
	header = header + '    <sdef n="pp"/>\n';
	header = header + '    <sdef n="p1"/>\n';
	header = header + '    <sdef n="p2"/>\n';
	header = header + '    <sdef n="p3"/>\n';
	header = header + '    <sdef n="sg"/>\n';
	header = header + '    <sdef n="pl"/>\n';
	header = header + '    <sdef n="m"/>\n';
	header = header + '    <sdef n="f"/>\n';
	header = header + '    <sdef n="mf"/>\n';
	header = header + '  </sdefs>\n';
	header = header + '  <pardefs>\n';



	header = header + '    <pardef n="S__qatlu/lhiex">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lekx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__qatlu/lha">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lek</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__qatlu/nix">\n';
        header = header + '      <e><p><l>ux</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>hiex</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ekx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>nix</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>homx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>komx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>niex</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__qatlu/ni">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ha</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ek</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>na</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__qatlu/hielhiex">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>hie</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>ek</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
        header = header + '      <e><p><l>nie</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lhiex"/></e>\n';
	header = header + '    </pardef>\n';

	header = header + '    <pardef n="S__qatlu/hielha">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>hie</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>ek</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lha"/></e>\n';
        header = header + '      <e><p><l>nie</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p><par n="S__qatlu/lha"/></e>\n';
	header = header + '    </pardef>\n';


# negation
	header = header + '    <pardef n="S__qtalt/x">\n';
        header = header + '      <e><p><l>x</l><r><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# direct object
	# after consonant, -ek version
	header = header + '    <pardef n="S__qtalt/ni">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ha</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ek</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>na</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	#after consonant, -ok version
	header = header + '    <pardef n="S__xrobt/ni">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ha</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ok</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>na</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	#after vowel
	header = header + '    <pardef n="S__qtaltu/ni">\n';
        header = header + '      <e><p><l>h</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ha</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>k</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>na</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# consonant endings: fetaħ-ni, fetaħ-ha, fetaħ-kom/hom
	header = header + '    <pardef n="S__fetaħ/ni">\n';
        header = header + '      <e><p><l>ha</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ni</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>kom</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>na</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# vowel endings: fetħ-ek, fetħ-u
	header = header + '    <pardef n="S__fetħ/ek">\n';
        header = header + '      <e><p><l>u</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ek</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
	header = header + '    </pardef>\n';


# direct object + negation
	# after consonant, -ek version
	header = header + '    <pardef n="S__qtalt/nix">\n';
        header = header + '      <e><p><l>ux</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>hiex</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ekx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>nix</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>homx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>komx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>niex</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after consonant, -ok version
	header = header + '    <pardef n="S__xrobt/nix">\n';
        header = header + '      <e><p><l>ux</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>hiex</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ekx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>nix</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>homx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>komx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>niex</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after vowel
	header = header + '    <pardef n="S__qtaltu/nix">\n';
        header = header + '      <e><p><l>hx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>hiex</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>kx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>nix</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>homx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>komx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>niex</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# consonant endings: ma fetaħ-nix etc.
	header = header + '    <pardef n="S__fetaħ/nix">\n';
        header = header + '      <e><p><l>hiex</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>nix</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>homx</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>komx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>niex</l><r><j/>u<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# vowel endings: ma fetħ-ekx, ma fetħ-ux
	header = header + '    <pardef n="S__fetħ/ekx">\n';
        header = header + '      <e><p><l>ux</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ekx</l><r><j/>u<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';



# indirect object
	# after vowel, -lek version
	header = header + '    <pardef n="S__qtaltu/lha">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lek</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after vowel, -lok version
	header = header + '    <pardef n="S__xrobtu/lha">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lok</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>lna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after consonant, -lek version
	header = header + '    <pardef n="S__qtalt/ilha">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lek</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after consonant, -lok version
	header = header + '    <pardef n="S__xrobt/ilha">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lok</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# fetaħli, fetaħlek, fetaħlu
	header = header + '    <pardef n="S__fetaħ/li">\n';
        header = header + '      <e><p><l>lu</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>lek</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>li</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# fetħilha, fetħilna, fetħilkom, fetħilhom
	header = header + '    <pardef n="S__fetħ/ilha">\n';
        header = header + '      <e><p><l>ilha</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhom</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkom</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>ilna</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# indirect object + negation
	# after vowel, -lek version
	header = header + '    <pardef n="S__qtaltu/lhiex">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lekx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after vowel, -lok version
	header = header + '    <pardef n="S__xrobtu/lhiex">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lokx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after consonant, -lek version
	header = header + '    <pardef n="S__qtalt/ilhiex">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lekx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# after consonant, -lok version
	header = header + '    <pardef n="S__xrobt/ilhiex">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lokx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# fetaħlix, fetaħlekx, fetaħlux
	header = header + '    <pardef n="S__fetaħ/lix">\n';
        header = header + '      <e><p><l>lux</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lekx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>lix</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';
	# fetħilhiex etc.
	header = header + '    <pardef n="S__fetħ/ilhiex">\n';
        header = header + '      <e><p><l>ilhiex</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilhomx</l><r><j/>lu<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilkomx</l><r><j/>lu<s n="prn"/><s n="p2"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
        header = header + '      <e><p><l>ilniex</l><r><j/>lu<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/><j/>x<s n="neg"/></r></p></e>\n';
	header = header + '    </pardef>\n';

# direct object + indirect object
	header = header + '    <pardef n="S__qtaltu/hielha">\n';
        header = header + '      <e><p><l>hu</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p><par n="S__qtaltu/lha"/></e>\n';
        header = header + '      <e><p><l>hie</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p><par n="S__qtaltu/lha"/></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p><par n="S__xrobtu/lha"/></e>\n';  # homlkom, not homilkom; and homlok 
	header = header + '    </pardef>\n';


# direct object + indirect object + negation
	header = header + '    <pardef n="S__qtaltu/hielhiex">\n';
        header = header + '      <e><p><l>hu</l><r><j/>u<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p><par n="S__qtaltu/lhiex"/></e>\n';
        header = header + '      <e><p><l>hie</l><r><j/>u<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p><par n="S__qtaltu/lhiex"/></e>\n';
        header = header + '      <e><p><l>hom</l><r><j/>u<s n="prn"/><s n="p3"/><s n="mf"/><s n="pl"/></r></p><par n="S__xrobtu/lhiex"/></e>\n';
	header = header + '    </pardef>\n';



	header = header + '  </pardefs>\n';
	header = header + '  <section id="main" type="standard">\n';
	
	return header;
	
#}
 
def footer(): #{
	footer = '';
	footer = footer + '  </section>\n';
	footer = footer + '</dictionary>\n';
	
	return footer;
#}

##-----------------------------------------------------------------------------##

# KaTaB		qasam, waqaf, qara(j), ġara(j), 
# KaTeB		qabeż, ħareġ
# KeTeB		xegħel, fehem, qered
# KeTaB		seraq, wera(j), ġema', ġama'
# KiTeB		kiser, wiżen
# KoToB		qorob, għolob
# KoTaB		għola(j), għoxa(j), ħola(j)


## ----------------------------------------------------------------------------##
## strong verbs
## ----------------------------------------------------------------------------##


def strong_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'u' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


def strong_pprs(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pprs.m.sg'] = [(r[0] + 'ie' + r[1] + 'e' + r[2] , '-', '-')] ;
	forms['pprs.f.sg'] = [(r[0] + 'ie' + r[1] + r[2] + 'a' , '-', '-')] ;
	forms['pprs.mf.pl'] = [(r[0] + 'ie' + r[1] + r[2] + 'in' , '-', '-')] ;

	return forms;
#}


def strong_pres_sg_forms (prefix, pres_sg, pres_sg_long, pres_sg_short, r): #{

	forms = [(prefix + pres_sg, '-', r),
		 (prefix + pres_sg, 'S__qtalt/x', r),
		 (prefix + pres_sg_long, 'S__fetaħ/ni', r),
# check: euphonic vowel here when r1 is l, m, n, għ?
		 (prefix + pres_sg_short, 'S__fetħ/ek', r),
		 (prefix + pres_sg_long, 'S__fetaħ/nix', r),
# and here
		 (prefix + pres_sg_short, 'S__fetħ/ekx', r),
		 (prefix + pres_sg_long, 'S__fetaħ/li', r),
# and here
		 (prefix + pres_sg_short, 'S__fetħ/ilha', r),
		 (prefix + pres_sg_long, 'S__fetaħ/lix', r),
# and here
		 (prefix + pres_sg_short, 'S__fetħ/ilhiex', r),
		 (prefix + pres_sg_long, 'S__qtaltu/hielha', r),
		 (prefix + pres_sg_long, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def strong_pres_pl_forms (prefix, pres_pl, r): #{

	forms = [(prefix + pres_pl, '-', r),
		 (prefix + pres_pl, 'S__qtalt/x', r),
		 (prefix + pres_pl, 'S__qtaltu/ni', r),
		 (prefix + pres_pl, 'S__qtaltu/nix', r),
		 (prefix + pres_pl, 'S__qtaltu/lha', r),
		 (prefix + pres_pl, 'S__qtaltu/lhiex', r),
		 (prefix + pres_pl, 'S__qtaltu/hielha', r),
		 (prefix + pres_pl, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def strong_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	pres_sg = v[0] + r[0] + r[1] + v[1] + r[2];
	pres_sg_long = v[0] + r[0] + r[1] + v[1] + r[2];
	if v[1] == 'e':
		pres_sg_long = v[0] + r[0] + r[1] + 'i' + r[2];
	pres_sg_short = v[0] + r[0] + r[1] + r[2];
	# When the second radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted
	if r[1] == 'l' or r[1] == 'm' or r[1] == 'n' or r[1] == 'għ': 
		pres_sg_short = v[0] + r[0] + r[1] + v[1] + r[2];
	pres_pl = v[0] + r[0] + r[1] + r[2] + 'u';

	forms['pres.p3.m.sg'] = strong_pres_sg_forms('', pres_sg, pres_sg_long, pres_sg_short, 'LR');
	forms['pres.p3.m.sg'] += strong_pres_sg_forms('j', pres_sg, pres_sg_long, pres_sg_short, 'LR');
	forms['pres.p3.m.sg'] += strong_pres_sg_forms('', pres_sg, pres_sg_long, pres_sg_short, 'RL');

	forms['pres.p3.f.sg'] = strong_pres_sg_forms('t', pres_sg, pres_sg_long, pres_sg_short, '-');
	forms['pres.p2.sg'] = strong_pres_sg_forms('t', pres_sg, pres_sg_long, pres_sg_short, '-');
	forms['pres.p1.sg'] = strong_pres_sg_forms('n', pres_sg, pres_sg_long, pres_sg_short, '-');

	# When the second radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted
# miri what if v[1] == 'e', e->i?
# yes!
	if r[1] == 'l' or r[1] == 'm' or r[1] == 'n' or r[1] == 'għ': #{
		forms['pres.p3.pl'] = strong_pres_pl_forms('j', v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-'); # j-iDĦL-u j-iFTĦ-u
		forms['pres.p2.pl'] = strong_pres_pl_forms('t', v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-');
		forms['pres.p1.pl'] = strong_pres_pl_forms('n', v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-');
	#}
	else : #{
		forms['pres.p3.pl'] = strong_pres_pl_forms('j', pres_pl, '-'); # j-iDĦL-u j-iFTĦ-u
		forms['pres.p2.pl'] = strong_pres_pl_forms('t', pres_pl, '-');
		forms['pres.p1.pl'] = strong_pres_pl_forms('n', pres_pl, '-');
	#}

	return forms;
#}



def strong_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels
	
	forms = {};

	pres_sg = v[0] + r[0] + r[1] + v[1] + r[2];
	pres_sg_long = v[0] + r[0] + r[1] + v[1] + r[2];
	if v[1] == 'e':
		pres_sg_long = v[0] + r[0] + r[1] + 'i' + r[2];
	pres_sg_short = v[0] + r[0] + r[1] + r[2];
	pres_pl = v[0] + r[0] + r[1] + r[2] + 'u';

	forms['imp.p2.sg'] = strong_pres_sg_forms('', pres_sg, pres_sg_long, pres_sg_short, '-');

	# When the second radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted
# miri what if v[1]=='e' - e->i?
	if r[1] == 'l' or r[1] == 'm' or r[1] == 'n' or r[1] == 'għ': #{
		forms['imp.p2.pl'] = strong_pres_pl_forms('', v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-');
	#}
	else :
		forms['imp.p2.pl'] = strong_pres_pl_forms('', pres_pl, '-');

	return forms ; 
#}


# all past sg forms end with a consonant
def strong_past_p3_sg_m_forms (past_sg, past_sg_long, past_sg_short, r): #{
# past.p3.sg.m
# sometimes 3 different forms of past.p3.sg.m are used: kiteb, kitib, kitb
# sometimes only 2: fetaħ, fetaħ, fetħ

	forms = [(past_sg, '-', r),
# seems it's 'ma kitibx', not 'ma kitebx'
# add (past_sg, 'S__qtalt/x', 'LR')? (not correct)
		 (past_sg_long, 'S__qtalt/x', r),
		 (past_sg_long, 'S__fetaħ/ni', r),
		 (past_sg_short, 'S__fetħ/ek', r),
		 (past_sg_long, 'S__fetaħ/nix', r),
		 (past_sg_short, 'S__fetħ/ekx', r),
		 (past_sg_long, 'S__fetaħ/li', r),
		 (past_sg_short, 'S__fetħ/ilha', r),
		 (past_sg_long, 'S__fetaħ/lix', r),
		 (past_sg_short, 'S__fetħ/ilhiex', r),
		 (past_sg_long, 'S__qtaltu/hielha', r),
		 (past_sg_long, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def strong_past_sg_forms (past_sg, past_sg_suff, r): #{
# past.p3.f.sg, past.2.sg, past.1.sg
# for past.p3.sg.f different forms with and without suffixes: kitbet, kitbit
# for past.p2.sg and past.p1.sg only one form: ktibt

	forms = [(past_sg, '-', r),
# add (past_sg_suff, 'S__qtalt/x', 'LR')? (not correct)
		 (past_sg_suff, 'S__qtalt/x', r),
		 (past_sg_suff, 'S__qtalt/ni', r),
		 (past_sg_suff, 'S__qtalt/nix', r),
		 (past_sg_suff, 'S__qtalt/ilha', r),
		 (past_sg_suff, 'S__qtalt/ilhiex', r),
		 (past_sg_suff, 'S__qtaltu/hielha', r),
		 (past_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


# all past pl forms end with a vowel
def strong_past_pl_forms (past_pl, past_pl_suff, r): #{

	forms = [(past_pl, '-', r),
		 (past_pl_suff, 'S__qtalt/x', r),
		 (past_pl_suff, 'S__qtaltu/ni', r),
		 (past_pl_suff, 'S__qtaltu/nix', r),
		 (past_pl_suff, 'S__qtaltu/lha', r),
		 (past_pl_suff, 'S__qtaltu/lhiex', r),
		 (past_pl_suff, 'S__qtaltu/hielha', r),
		 (past_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def strong_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

# maybe there should be another class for this kind of verbs
	if r[2] == 'j' or r[2] == 'għ': #{
		r[2] = '';
	#}

	forms = {};

	if v[1] == 'e' :
		forms['past.p3.m.sg'] = strong_past_p3_sg_m_forms(r[0] + v[0] + r[1] + v[1] + r[2], r[0] + v[0] + r[1] + 'i' + r[2], r[0] + v[0] + r[1] + r[2], '');
	else :
		forms['past.p3.m.sg'] = strong_past_p3_sg_m_forms(r[0] + v[0] + r[1] + v[1] + r[2], r[0] + v[0] + r[1] + v[1] + r[2], r[0] + v[0] + r[1] + r[2], '');

	# add -ot suffix for o-o class (għoġbot vs. għoġbitni, għoġbitek, għoġbitu,...)
	# -et after għ remains -et before suffixes? (semgħetu, qatgħetli qalbi)
	forms['past.p3.f.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + r[2] + 'et', r[0] + v[0] + r[1] + r[2] + 'it', '-');	# Omit second vowel of stem word

	if v[1] == 'e' :
		forms['past.p2.sg'] = strong_past_sg_forms(r[0] + r[1] + 'i' + r[2] + 't', r[0] + r[1] + 'i' + r[2] + 't', '-');	# Omit first vowel of stem word
		forms['past.p1.sg'] = strong_past_sg_forms(r[0] + r[1] + 'i' + r[2] + 't', r[0] + r[1] + 'i' + r[2] + 't', '-');	# Omit first vowel of stem word
	else :
		forms['past.p2.sg'] = strong_past_sg_forms(r[0] + r[1] + v[1] + r[2] + 't', r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word
		forms['past.p1.sg'] = strong_past_sg_forms(r[0] + r[1] + v[1] + r[2] + 't', r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word

	forms['past.p3.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + r[2] + 'u', r[0] + v[0] + r[1] + r[2] + 'u', '-');	# Omit second vowel of stem word

	if v[1] == 'e' :
		forms['past.p2.pl'] = strong_past_pl_forms(r[0] + r[1] + 'i' + r[2] + 'tu', r[0] + r[1] + 'i' + r[2] + 'tu', '-');	# Omit first vowel of stem word
		forms['past.p1.pl'] = strong_past_pl_forms(r[0] + r[1] + 'i' + r[2] + 'na', r[0] + r[1] + 'i' + r[2] + 'nie', '-');	# Omit first vowel of stem word
	else :
		forms['past.p2.pl'] = strong_past_pl_forms(r[0] + r[1] + v[1] + r[2] + 'tu', r[0] + r[1] + v[1] + r[2] + 'tu', '-');	# Omit first vowel of stem word
		forms['past.p1.pl'] = strong_past_pl_forms(r[0] + r[1] + v[1] + r[2] + 'na', r[0] + r[1] + v[1] + r[2] + 'nie', '-');	# Omit first vowel of stem word

	# == Overrides == 

	if r[0] == 'w' or r[0] == 'għ': #{
		# If the first radical is 'w' or 'għ' then we have a full disyllabic form
		if v[1] == 'e' : #{
			forms['past.p2.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + 'i' + r[2] + 't', r[0] + v[0] + r[1] + 'i' + r[2] + 't', '-');	
			forms['past.p1.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + 'i' + r[2] + 't', r[0] + v[0] + r[1] + 'i' + r[2] + 't', '-');
			forms['past.p2.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + 'i' + r[2] + 'tu', r[0] + v[0] + r[1] + 'i' + r[2] + 'tu', '-');
			forms['past.p1.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + 'i' + r[2] + 'na', r[0] + v[0] + r[1] + 'i' + r[2] + 'nie', '-');
		#}
		else : #{
			forms['past.p2.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + v[1] + r[2] + 't', r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-');
			forms['past.p1.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + v[1] + r[2] + 't', r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-');
			forms['past.p2.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + v[1] + r[2] + 'tu', r[0] + v[0] + r[1] + v[1] + r[2] + 'tu', '-');
			forms['past.p1.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + v[1] + r[2] + 'na', r[0] + v[0] + r[1] + v[1] + r[2] + 'nie', '-');
		#}

	#}

	return forms;
#}


## ----------------------------------------------------------------------------##
## hollow verbs
## ----------------------------------------------------------------------------##

def hollow_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + 'ju' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(pref + r[0] + 'ju' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(pref + r[0] + 'ju' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


# Not all intransitive hollow verbs have pprs
# pattern: KeJJeB, KeJBa, KeJBin (but sajjem, sajma, sajmin)
def hollow_pprs(root, vowel): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pp.m.sg'] = [(r[0] + vowel + 'jje' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + vowel + 'j' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(r[0] + vowel + 'j' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


def hollow_sg_forms (prefix, form_sg, form_sg_suff, r): #{
# past & impf sg forms end with consontant(s)
# only past.p3.sg.f have different forms with and without suffixes

	forms = [(prefix + form_sg, '-', r),
		 (prefix + form_sg_suff, 'S__qtalt/x', r),
		 (prefix + form_sg_suff, 'S__qtalt/ni', r),
		 (prefix + form_sg_suff, 'S__qtalt/nix', r),
		 (prefix + form_sg_suff, 'S__qtalt/ilha', r),
		 (prefix + form_sg_suff, 'S__qtalt/ilhiex', r),
		 (prefix + form_sg_suff, 'S__qtaltu/hielha', r),
		 (prefix + form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def hollow_pl_forms (prefix, form_pl, form_pl_suff, r): #{
# all past forms end with a vowel
# different with/without suffix forms only for past.p1.pl

	forms = [(prefix + form_pl, '-', r),
		 (prefix + form_pl_suff, 'S__qtalt/x', r),
		 (prefix + form_pl_suff, 'S__qtaltu/ni', r),
		 (prefix + form_pl_suff, 'S__qtaltu/nix', r),
		 (prefix + form_pl_suff, 'S__qtaltu/lha', r),
		 (prefix + form_pl_suff, 'S__qtaltu/lhiex', r),
		 (prefix + form_pl_suff, 'S__qtaltu/hielha', r),
		 (prefix + form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def hollow_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	forms['past.p3.m.sg'] = hollow_sg_forms('', r[0] + v[0] + r[2], r[0] + v[0] + r[2], '-');
# additional forms for past.p3.m.sg + indirect object suffixes
# TYM p. 211: hollow verbs can insert or omit stressed i before 3rd pers. fem. and pl
# ġabilha, ġabilhom, but also ġablha, ġablhom
# seems that's a pure theory
##	forms['past.p3.m.sg'] += [(r[0] + v[0] + r[2], 'S__fetħ/ilha', r)];


	forms['past.p3.f.sg'] = hollow_sg_forms('', r[0] + v[0] + r[2] + 'et', r[0] + v[0] + r[2] + 'it', '-');
# daritlha? daritilha? both?

	# This form is obtained by the insertion of 'o' for second radical 'w' and
	# 'i' for second radical 'j'
	if r[1] == 'w': #{
		link_vowel = 'o';
	elif r[1] == 'j': #{
		link_vowel = 'i';
	#}

	forms['past.p2.sg'] = hollow_sg_forms('', r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-');	
	forms['past.p1.sg'] = hollow_sg_forms('', r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-');	

	forms['past.p2.pl'] = hollow_pl_forms('', r[0] + link_vowel + r[2] + 'tu', r[0] + link_vowel + r[2] + 'tu', '-');
	forms['past.p1.pl'] = hollow_pl_forms('', r[0] + link_vowel + r[2] + 'na', r[0] + link_vowel + r[2] + 'nie', '-');

# v[0]/'a'
	forms['past.p3.pl'] = hollow_pl_forms('', r[0] + v[0] + r[2] + 'u', r[0] + v[0] + r[2] + 'u', '-');


#	# This is not in the grammar, but it seems that 'ie' (mutation of long 'a')
#	# does not have the usual rules applied
#	if v[0] == 'ie': #{
#
#		# I'm not so  sure
#		# usually past.p1.pl share rules with 
#		# past.p2.pl, past.p2.sg, past.p1.sg
#		# and r[0] + 'ie' + r[2] + 'na' can be
#		# past.3.sg.m + prn.p1.pl d.o. 
#
#		# or maybe past.3.sg.m + prn.p1.pl d.o. is
#		# r[0] + 'i/o' + r[2] + 'na' too?
#
#		forms['past.p1.pl'] = [(r[0] + 'ie' + r[2] + 'na', '-', '-')];
#		
#		# that's the usual rule though
#		forms['past.p3.pl'] = [(r[0] + 'ie' + r[2] + 'u', '-', '-')];	
	#}

	return forms;
#}



def hollow_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	link_vowel = '';
	if r[1] == 'w': #{
		link_vowel = 'u';
	elif r[1] == 'j': #{
		link_vowel = 'i';
	#}
		
	forms['imp.p2.sg'] = hollow_sg_forms('', r[0] + link_vowel + r[2], r[0] + link_vowel + r[2], '-');
	forms['imp.p2.pl'] = hollow_pl_forms('', r[0] + link_vowel + r[2] + 'u', r[0] + link_vowel + r[2] + 'u', '-');

	return forms;
#}



def hollow_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	# The imperfect is obtained by the addition of the usual prefixes (j,t,n) 
	# to the first radical of the verb with the stressed long vowel 'u' or 'i'
	# between the first and third radicals. And 'u' for the plural.

	#	- This is all well and good, but there is some ambiguity because we find
	#	- e.g. iddur/ddur in the corpus, but not jddur. On the other hand,
	#	- we find 'trid' and 'jrid' in the corpus

	link_vowel = '';
	if r[1] == 'w': #{
		link_vowel = 'u';
	elif r[1] == 'j': #{
		link_vowel = 'i';
	#}
											# (!) form not attested

	form_sg = r[0] + link_vowel + r[2];

	forms['pres.p3.m.sg'] = hollow_sg_forms('i', form_sg, form_sg, 'LR');		# irid		isir		idur
	forms['pres.p3.m.sg'] += hollow_sg_forms('j', form_sg, form_sg, 'LR');		# jrid		jsir		jdur
	forms['pres.p3.m.sg'] += hollow_sg_forms('i', form_sg, form_sg, 'RL');		# ~irid		~isir		~idur

	forms['pres.p3.f.sg'] = hollow_sg_forms('i' + r[0], form_sg, form_sg, 'LR');		# irrid 	issir		iddur
	forms['pres.p3.f.sg'] += hollow_sg_forms(r[0], form_sg, form_sg, 'LR');		# rrid		ssir		ddur
	forms['pres.p3.f.sg'] += hollow_sg_forms('t', form_sg, form_sg, 'LR');		# trid		tsir(!)		tdur(!)
	forms['pres.p3.f.sg'] += hollow_sg_forms('i' + r[0], form_sg, form_sg, 'RL');	# ~irrid	~issir		~iddur

	forms['pres.p2.sg'] = hollow_sg_forms('i' + r[0], form_sg, form_sg, 'LR');		# irrid 	issir		iddur
	forms['pres.p2.sg'] += hollow_sg_forms(r[0], form_sg, form_sg, 'LR');			# rrid		ssir		ddur
	forms['pres.p2.sg'] += hollow_sg_forms('t', form_sg, form_sg, 'LR');			# trid 		tsir(!)		tdur(!)
	forms['pres.p2.sg'] += hollow_sg_forms('i' + r[0], form_sg, form_sg, 'RL');		# ~irrid	~issir		~iddur

	forms['pres.p1.sg'] = hollow_sg_forms('in', form_sg, form_sg, 'LR');			# inrid		insir		indur
	forms['pres.p1.sg'] += hollow_sg_forms('n', form_sg, form_sg, 'LR');			# nrid		nsir		ndur
	forms['pres.p1.sg'] += hollow_sg_forms('in', form_sg, form_sg, 'RL');		# ~inrid	~insir		~indur


	form_pl = r[0] + link_vowel + r[2] + 'u';

	forms['pres.p3.pl'] = hollow_pl_forms('i', form_pl, form_pl, 'LR');		# iridu		isiru		iduru
	forms['pres.p3.pl'] += hollow_pl_forms('j', form_pl, form_pl, 'LR');		# jridu		jsiru		jduru
	forms['pres.p3.pl'] += hollow_pl_forms('i', form_pl, form_pl, 'RL');		# ~iridu	~isiru		~iduru

	forms['pres.p2.pl'] = hollow_pl_forms('i' + r[0], form_pl, form_pl, 'LR');	# irridu	issiru		idduru
	forms['pres.p2.pl'] += hollow_pl_forms(r[0], form_pl, form_pl, 'LR');		# rridu		ssiru		dduru
	forms['pres.p2.pl'] += hollow_pl_forms('t', form_pl, form_pl, 'LR');		# tridu		tsiru(!)	tduru(!)
	forms['pres.p2.pl'] += hollow_pl_forms('i' + r[0], form_pl, form_pl, 'RL');	# ~irridu	~issiru		~idduru

	forms['pres.p1.pl'] = hollow_pl_forms('in', form_pl, form_pl, 'LR');		# inridu	insiru		induru
	forms['pres.p1.pl'] += hollow_pl_forms('n', form_pl, form_pl, 'LR');		# nridu		nsiru		nduru
	forms['pres.p1.pl'] += hollow_pl_forms('in', form_pl, form_pl, 'RL');		# ~inridu	~insiru		~induru
	
	return forms;
#}


## ----------------------------------------------------------------------------##
## weak
## ----------------------------------------------------------------------------##


def weak_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pprs.m.sg'] = [(r[0] + 'ie' + r[1] + 'i', '-', '-')] ;
	forms['pprs.f.sg'] = [(r[0] + 'ie' + r[1] + 'ja', '-', '-')] ;
	forms['pprs.mf.pl'] = [(r[0] + 'e' + r[1] + 'jin', '-', '-')] ;

	return forms;
#}


def weak_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'i', '-', '-')] ;
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'ija', '-', '-')] ;
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'ijin', '-', '-')] ;

	return forms;
#}


def weak_consonant_forms (form_sg, form_sg_suff, r): #{
# only past.p3.sg.f have different forms with and without suffixes

	forms = [(form_sg, '-', r),
		 (form_sg_suff, 'S__qtalt/x', r),
		 (form_sg_suff, 'S__qtalt/ni', r),
		 (form_sg_suff, 'S__qtalt/nix', r),
		 (form_sg_suff, 'S__qtalt/ilha', r),
		 (form_sg_suff, 'S__qtalt/ilhiex', r),
		 (form_sg_suff, 'S__qtaltu/hielha', r),
		 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def weak_vowel_forms (form_pl, form_pl_suff, r): #{
# different with/without suffix forms only for past.p1.pl

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def weak_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[0] == 'e' and v[1] == 'a': #{

		forms['past.p3.m.sg'] = weak_vowel_forms(r[0] + v[0] + r[1] + v[1], r[0] + r[1] + 'ie', '-');

		# This form is obtained by the elision of the first vowel of the 
		# stem and the change of the second vowel to 'ie' (for e-a) and
		# 'a' for (a-a)
		# rmiet - ma rmitx? or ma rmietx?
		forms['past.p3.f.sg'] = weak_consonant_forms(r[0] + r[1] + 'iet', r[0] + r[1] + 'it', '-');
	#}
	else : #{
		forms['past.p3.m.sg'] = weak_vowel_forms(r[0] + v[0] + r[1] + v[1], r[0] + r[1] + 'a', '-');
		# qratu? or qritu?
		forms['past.p3.f.sg'] = weak_consonant_forms(r[0] + r[1] + 'at', r[0] + r[1] + 'at', '-');
	#}

	# This form is obtained by the omission of the two vowels in the stem
	# and the addition of the dipthong 'ej' (for e-a) and 'aj' (for a-a)
	forms['past.p2.sg'] = weak_consonant_forms(r[0] + r[1] + v[0] + 'jt', r[0] + r[1] + v[0] + 'jt', '-');	
	forms['past.p1.sg'] = weak_consonant_forms(r[0] + r[1] + v[0] + 'jt', r[0] + r[1] + v[0] + 'jt', '-');	

	# This form is obtained by the omission of the two vowels in the vocalic
	# sequence + dipthong 'ew' or 'aw'
	# In the context of the attached pronouns 'ew' and 'aw'
	# are also treated like vowels
	forms['past.p3.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'w', r[0] + r[1] + v[0] + 'w', '-');
	forms['past.p2.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'jtu', r[0] + r[1] + v[0] + 'jtu', '-');
	forms['past.p1.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'jna', r[0] + r[1] + v[0] + 'jnie', '-');

	return forms;
#}


def weak_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	presuff_vowel = v[1];
	# That's only my guess
	if v[0] == 'e' and v[1] == 'a': 
		presuff_vowel = 'ie';

	# no first vowel elision in forms with suffixes? 
	forms['pres.p3.m.sg'] = weak_vowel_forms('j' + v[0] + r[0] + r[1] + v[1] , 'j' + v[0] + r[0] + r[1] + presuff_vowel , '-');
	forms['pres.p3.f.sg'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + v[1] , 't' + v[0] + r[0] + r[1] + presuff_vowel , '-');
	forms['pres.p2.sg'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + v[1] , 't' + v[0] + r[0] + r[1] + presuff_vowel , '-');
	forms['pres.p1.sg'] = weak_vowel_forms('n' + v[0] + r[0] + r[1] + v[1] , 'n' + v[0] + r[0] + r[1] + presuff_vowel , '-');
	
	if vowels == 'a-a': #{
		suffix =  'aw';
	elif vowels == 'i-a': #{
		suffix =  'ew';
	else: #{
		suffix = 'u'
	#}
										# QaRaJ		BeDaJ		MeXaJ	ReMaJ
										# a-a		i-a		i-i	a-i
	forms['pres.p3.pl'] = weak_vowel_forms('j' + v[0] + r[0] + r[1] + suffix, 'j' + v[0] + r[0] + r[1] + suffix, '-');	# j-aQRa-w	j-iBDe-w	j-iMXu	j-aRMu
	forms['pres.p2.pl'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + suffix, 't' + v[0] + r[0] + r[1] + suffix, '-');	# t-aQRa-w
	forms['pres.p1.pl'] = weak_vowel_forms('n' + v[0] + r[0] + r[1] + suffix, 'n' + v[0] + r[0] + r[1] + suffix, '-');	# n-aQRa-w

	return forms;
#}

def weak_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	presuff_sg_vowel = v[1];
	# That's only my guess
	if v[0] == 'e' and v[1] == 'a': 
		presuff_sg_vowel = 'ie';
	
	if vowels == 'a-a': #{
		pl_suffix =  'aw';
	elif vowels == 'i-a': #{
		pl_suffix =  'ew';
	else: #{
		pl_suffix = 'u'
	#}

	forms['imp.p2.sg'] = weak_vowel_forms(v[0] + r[0] + r[1] + v[1] , v[0] + r[0] + r[1] + presuff_sg_vowel , '-');
	forms['imp.p2.pl'] = weak_vowel_forms(v[0] + r[0] + r[1] + pl_suffix , v[0] + r[0] + r[1] + pl_suffix , '-');

	return forms;
#}


## ----------------------------------------------------------------------------##
## doubled
## ----------------------------------------------------------------------------##


def doubled_consonant_forms (form_sg, form_sg_suff, r, ek): #{

	if ek == 'ok' :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__xrobt/ni', r),
			 (form_sg_suff, 'S__xrobt/nix', r),
			 (form_sg_suff, 'S__xrobt/ilha', r),
			 (form_sg_suff, 'S__xrobt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];
	else :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__qtalt/ni', r),
			 (form_sg_suff, 'S__qtalt/nix', r),
			 (form_sg_suff, 'S__qtalt/ilha', r),
			 (form_sg_suff, 'S__qtalt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def doubled_vowel_forms (form_pl, form_pl_suff, r): #{

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}



def doubled_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	ek = 'ek';

	forms['past.p3.m.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2], r[0] + v[0] + r[1] + r[2], '-', ek);
	forms['past.p3.f.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'et', r[0] + v[0] + r[1] + r[2] + 'it', '-', ek);
	forms['past.p2.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek);
	forms['past.p1.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek);
	forms['past.p3.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'u', r[0] + v[0] + r[1] + r[2] + 'u', '-');
	forms['past.p3.pl'] += doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ew', r[0] + v[0] + r[1] + r[2] + 'ew', 'LR');
	forms['past.p2.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejtu', r[0] + v[0] + r[1] + r[2] + 'ejtu', '-');
	forms['past.p1.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejna', r[0] + v[0] + r[1] + r[2] + 'ejna', '-');

	return forms;
#}

def doubled_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';

	forms['pres.p3.m.sg'] = doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# irodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('j' + r[0] + v[1] + r[1] + r[2], 'j' + r[0] + v[1] + r[1] + r[2], 'LR', ek); 		# jrodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'RL', ek);		# ~irodd

	forms['pres.p3.f.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek);		# trodd

	forms['pres.p2.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek);			# trodd

	forms['pres.p1.sg'] = doubled_consonant_forms ('in' + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# inrodd
	forms['pres.p1.sg'] += doubled_consonant_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# irrodd
	forms['pres.p1.sg'] += doubled_consonant_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + r[0] + v[1] + r[1] + r[2], 'RL', ek);	# irrodd

	forms['pres.p3.pl'] = doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');		# iroddu
	forms['pres.p3.pl'] += doubled_vowel_forms ('j' + r[0] + v[1] + r[1] + r[2] + 'u', 'j' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR'); 	# jroddu
	forms['pres.p3.pl'] += doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'RL');	# ~iroddu

	forms['pres.p2.pl'] = doubled_vowel_forms ('t' + r[0] + v[1] + r[1] + r[2] + 'u', 't' + r[0] + v[1] + r[1] + r[2] + 'u', '-');		# troddu

	forms['pres.p1.pl'] = doubled_vowel_forms ('in' + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');		# inroddu
	forms['pres.p1.pl'] += doubled_vowel_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');	# irroddu
	forms['pres.p1.pl'] += doubled_vowel_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'RL');	# irroddu


	return forms;
#}


def doubled_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';	

	suffix = 'u'

	forms['imp.p2.sg'] = doubled_consonant_forms (r[0] + v[1] + r[1] + r[2], r[0] + v[1] + r[1] + r[2], '-', ek);
	forms['imp.p2.pl'] = doubled_vowel_forms (r[0] + v[1] + r[1] + r[2] + suffix , r[0] + v[1] + r[1] + r[2] + suffix , '-');

	return forms;
#}


def doubled_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'u' + r[2], '-', '-')];
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'a', '-', '-')];
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'in', '-', '-')];

	return forms;
#}


## ----------------------------------------------------------------------------##
## quadriliteral
## ----------------------------------------------------------------------------##


def quad_consonant_forms (form_sg, form_sg_suff, r): #{
# no ek/ok problems

	forms = [(form_sg, '-', r),
		 (form_sg_suff, 'S__qtalt/x', r),
		 (form_sg_suff, 'S__qtalt/ni', r),
		 (form_sg_suff, 'S__qtalt/nix', r),
		 (form_sg_suff, 'S__qtalt/ilha', r),
		 (form_sg_suff, 'S__qtalt/ilhiex', r),
		 (form_sg_suff, 'S__qtaltu/hielha', r),
		 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def quad_e_consonant_forms (pres_sg, pres_sg_long, pres_sg_short, r): #{
# a-e, e-e, i-e verbs: forms ending with e + cons (past.p3.sg.m, pers.sg)

	forms = [(pres_sg, '-', r),
		 (pres_sg_long, 'S__qtalt/x', r),
		 (pres_sg_long, 'S__fetaħ/ni', r),
		 (pres_sg_short, 'S__fetħ/ek', r),
		 (pres_sg_long, 'S__fetaħ/nix', r),
		 (pres_sg_short, 'S__fetħ/ekx', r),
		 (pres_sg_long, 'S__fetaħ/li', r),
		 (pres_sg_short, 'S__fetħ/ilha', r),
		 (pres_sg_long, 'S__fetaħ/lix', r),
		 (pres_sg_short, 'S__fetħ/ilhiex', r),
		 (pres_sg_long, 'S__qtaltu/hielha', r),
		 (pres_sg_long, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def quad_vowel_forms (form_pl, form_pl_suff, r): #{

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def quad_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};


	# no suffix
	past = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; # dardar, kexkex (past.p3.sg.m)

	# with suffix(es)
	if v[1] == 'e' : #{
		past_long = r[0] + v[0] + r[1] + r[2] + 'i' + r[3]; # kexkixni (past.p3.sg.m + prn.p1.sg)
	else :
		past_long = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; # dardarni (past.p3.sg.m + prn.p1.sg)

	past_short = r[0] + v[0] + r[1] + r[2] + r[3]; # dardrek, kexkxek (past.p3.sg.m + prn.p2.sg)


	forms['past.p3.m.sg'] = quad_e_consonant_forms (past, past_long, past_short, '-');
	forms['past.p3.f.sg'] = quad_consonant_forms (r[0] + v[0] + r[1] + r[2] + r[3] + 'et', r[0] + v[0] + r[1] + r[2] + r[3] + 'it', '-');
	forms['past.p2.sg'] = quad_consonant_forms (past_long + 't', past_long + 't', '-');
	forms['past.p1.sg'] = quad_consonant_forms (past_long + 't', past_long + 't', '-');

	forms['past.p3.pl'] = quad_vowel_forms (past_short + 'u', past_short + 'u', '-');
	forms['past.p2.pl'] = quad_vowel_forms (past_long + 'tu', past_long + 'tu', '-');
	forms['past.p1.pl'] = quad_vowel_forms (past_long + 'na', past_long + 'nie', '-');


	return forms;
#}

	
def quad_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};


	# no suffix
	pres = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; # idardar, ikexkex

	# with suffix(es)
	if v[1] == 'e' : #{
		pres_long = r[0] + v[0] + r[1] + r[2] + 'i' + r[3]; #ikexkixni
	else :
		pres_long = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; #idardarni

	pres_short = r[0] + v[0] + r[1] + r[2] + r[3]; # ikexkxek, idardrek


	forms['pres.p3.m.sg'] = quad_e_consonant_forms ('i' + pres, 'i' + pres_long, 'i' + pres_short, 'LR');		# idardar
	forms['pres.p3.m.sg'] += quad_e_consonant_forms ('j' + pres, 'j' + pres_long, 'j' + pres_short, 'LR'); 	# jdardar
	forms['pres.p3.m.sg'] += quad_e_consonant_forms ('i' + pres, 'i' + pres_long, 'i' + pres_short, 'RL');	# ~idardar

	# Oh no. Only some verbs have assimilation  here:
	# iddardar, but itkexkex
	# let me guess what should be assimilated
	# ċ, d, ġ, s, x, ż ?
	forms['pres.p3.f.sg'] = quad_e_consonant_forms ('i' + r[0] + pres, 'i' + r[0] + pres_long, 'i' + r[0] + pres_short, 'LR');	# iddardar
	forms['pres.p3.f.sg'] += quad_e_consonant_forms (r[0] + pres, r[0] + pres_long, r[0] + pres_short, 'LR');	# ddardar
	forms['pres.p3.f.sg'] += quad_e_consonant_forms ('i' + r[0] + pres, 'i' + r[0] + pres_long, 'i' + r[0] + pres_short, 'RL');	# ~iddardar

	forms['pres.p2.sg'] = quad_e_consonant_forms ('i' + r[0] + pres, 'i' + r[0] + pres_long, 'i' + r[0] + pres_short, 'LR');	# iddardar
	forms['pres.p2.sg'] += quad_e_consonant_forms (r[0] + pres, r[0] + pres_long, r[0] + pres_short, 'LR');	# ddardar
	forms['pres.p2.sg'] += quad_e_consonant_forms ('i' + r[0] + pres, 'i' + r[0] + pres_long, 'i' + r[0] + pres_short, 'RL');	# ~iddardar

	forms['pres.p1.sg'] = quad_e_consonant_forms ('in' + pres, 'in' + pres_long, 'in' + pres_short, 'LR');		# indardar
	forms['pres.p1.sg'] += quad_e_consonant_forms ('n' + pres, 'n' + pres_long, 'n' + pres_short, 'LR');		# ndardar
	forms['pres.p1.sg'] += quad_e_consonant_forms ('in' + pres, 'in' + pres_long, 'in' + pres_short, 'RL');	# indardar



	forms['pres.p3.pl'] = quad_vowel_forms ('i' + pres_short + 'u', 'i' + pres_short + 'u', 'LR');		# idardru
	forms['pres.p3.pl'] += quad_vowel_forms ('j' + pres_short + 'u', 'j' + pres_short + 'u', 'LR'); 		# jdardru
	forms['pres.p3.pl'] += quad_vowel_forms ('i' + pres_short + 'u', 'i' + pres_short + 'u', 'RL');		# ~idardru

	forms['pres.p2.pl'] = quad_vowel_forms ('i' + r[0] + pres_short + 'u', 'i' + r[0] + pres_short + 'u', 'LR');	# iddardru
	forms['pres.p2.pl'] += quad_vowel_forms (r[0] + pres_short + 'u', r[0] + pres_short + 'u', 'LR');		# ddardru
	forms['pres.p2.pl'] += quad_vowel_forms ('i' + r[0] + pres_short + 'u', 'i' + r[0] + pres_short + 'u', 'RL');	# ~iddardru

	forms['pres.p1.pl'] = quad_vowel_forms ('in' + pres_short + 'u', 'in' + pres_short + 'u', 'LR');		# indardru
	forms['pres.p1.pl'] += quad_vowel_forms ('n' + pres_short + 'u', 'in' + pres_short + 'u', 'LR');		# indardru
	forms['pres.p1.pl'] += quad_vowel_forms ('in' + pres_short + 'u', 'in' + pres_short + 'u', 'RL');		# indardru

	return forms;
#}


def quad_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	# no suffix
	pres = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; # idardar, ikexkex

	# with suffix(es)
	if v[1] == 'e' : #{
		pres_long = r[0] + v[0] + r[1] + r[2] + 'i' + r[3]; #ikexkixni
	else :
		pres_long = r[0] + v[0] + r[1] + r[2] + v[1] + r[3]; #idardarni

	pres_short = r[0] + v[0] + r[1] + r[2] + r[3]; # ikexkxek, idardrek

	
	suffix = 'u';

	forms['imp.p2.sg'] = quad_e_consonant_forms (pres, pres_long, pres_short, '-');
	forms['imp.p2.pl'] = quad_vowel_forms (pres_short + 'u', pres_short + 'u', '-');

	return forms;
#}


def quad_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	# also mdardar after vowels??

	forms = {};

	forms['pp.m.sg'] = [(pref + r[0] + v[0] + r[1] + r[2] + v[1] + r[3], '-', '-')];	# imdardar
	forms['pp.f.sg'] = [(pref + r[0] + v[0] + r[1] + r[2] + r[3] + 'a', '-', '-')];	# imdardra
	forms['pp.mf.pl'] = [(pref + r[0] + v[0] + r[1] + r[2] + r[3] + 'in', '-', '-')];	# imdardrin

	return forms;
#}



## ----------------------------------------------------------------------------##
## loan
## ----------------------------------------------------------------------------##


# ???
#def loan_pprs(root): #{
#}


def loan_pp(pp): #{

	forms = {};
	
	forms['pp.m.sg'] = [(pp, '-', '-')] ;
	forms['pp.f.sg'] = [(pp + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(pp + 'i', '-', '-')] ;

	return forms;
#}


def loan_consonant_forms (form_sg, form_sg_suff, r): #{
# only past.p3.sg.f have different forms with and without suffixes

	forms = [(form_sg, '-', r),
		 (form_sg_suff, 'S__qtalt/x', r),
		 (form_sg_suff, 'S__qtalt/ni', r),
		 (form_sg_suff, 'S__qtalt/nix', r),
		 (form_sg_suff, 'S__qtalt/ilha', r),
		 (form_sg_suff, 'S__qtalt/ilhiex', r),
		 (form_sg_suff, 'S__qtaltu/hielha', r),
		 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def loan_vowel_forms (form_pl, form_pl_suff, r): #{
# different with/without suffix forms only for past.p1.pl

# jittradíxxi: both ma jittradíx or ma jittradixxíx!!!
# but there is only one form ending with -ixxix or -ixxax in the corpus:
# tissostitwixxix

# oh, but there are also forms like
#      1 ^ttrasferixxiet/*ttrasferixxiet$
#      1 ^stabbilixxiet/*stabbilixxiet$
#      1 ^rreaġixxiet/*rreaġixxiet$
#      1 ^ipprojbixxiet/*ipprojbixxiet$
#      1 ^esegwixxiet/*esegwixxiet$
#      1 ^esebixxiet/*esebixxiet$
#      1 ^aġixxiet/*aġixxiet$
# also with pron. suffixes - only 2:
#      1 ^jissostitwixxihom/*jissostitwixxihom$
#      1 ^issostwixxihom/*issostwixxihom$

# so what? LR for ixx + suffixes ?

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}



def loan_past_forms(forms, stem, ixx, vowel_pres, r): #{

	if vowel_pres == 'i': #{
		# stabilixxa, but stabilieni, stabiliek
		forms['past.p3.m.sg'] += loan_vowel_forms(stem + ixx + 'a', stem + 'ie', r);
		# falliet - ma fallitx? or ma fallietx?
		forms['past.p3.f.sg'] += loan_consonant_forms(stem + 'iet', stem + 'it', r);
		forms['past.p2.sg'] += loan_consonant_forms(stem + 'ejt', stem + 'ejt', r);	
		forms['past.p1.sg'] += loan_consonant_forms(stem + 'ejt', stem + 'ejt', r);
		forms['past.p3.pl'] += loan_vowel_forms(stem + 'ew', stem + 'ew', r);
		forms['past.p2.pl'] += loan_vowel_forms(stem + 'ejtu', stem + 'ejtu', r);
		forms['past.p1.pl'] += loan_vowel_forms(stem + 'ejna', stem + 'ejnie', r);
	#}
	else : #{   vowel_pres == a
		forms['past.p3.m.sg'] += loan_vowel_forms(stem + ixx + 'a', stem + 'a', r);
		forms['past.p3.f.sg'] += loan_consonant_forms(stem + 'at', stem + 'at', r);
		forms['past.p2.sg'] += loan_consonant_forms(stem + 'ajt', stem + 'ajt', r);	
		forms['past.p1.sg'] += loan_consonant_forms(stem + 'ajt', stem + 'ajt', r);
		forms['past.p3.pl'] += loan_vowel_forms(stem + 'aw', stem + 'aw', r);
		forms['past.p2.pl'] += loan_vowel_forms(stem + 'ajtu', stem + 'ajtu', r);
		forms['past.p1.pl'] += loan_vowel_forms(stem + 'ajna', stem + 'ajnie', r);
	#}

	return forms;
#}



def loan_past_double_cons(base, ixx, vowel_pres): #{

	forms = {};

	forms['past.p3.m.sg'] = [];
	forms['past.p3.f.sg'] = [];
	forms['past.p2.sg'] = [];
	forms['past.p1.sg'] = [];
	forms['past.p3.pl'] = [];
	forms['past.p2.pl'] = []; 
	forms['past.p1.pl'] = []; 

	loan_past_forms(forms, base, ixx, vowel_pres, 'LR');
	loan_past_forms(forms, 'i' + base, ixx, vowel_pres, 'LR');
#	loan_past_forms(forms, first_cons + base, ixx, vowel_pres, 'LR');
#	loan_past_forms(forms, 'i' + first_cons + base, ixx, vowel_pres, 'LR');
	loan_past_forms(forms, 'i' + base, ixx, vowel_pres, 'RL');

	return forms;
#}



def loan_past(base, ixx, vowel_pres): #{

	forms = {};

	forms['past.p3.m.sg'] = [];
	forms['past.p3.f.sg'] = [];
	forms['past.p2.sg'] = [];
	forms['past.p1.sg'] = [];
	forms['past.p3.pl'] = [];
	forms['past.p2.pl'] = []; 
	forms['past.p1.pl'] = []; 

	loan_past_forms(forms, base, ixx, vowel_pres, '-');

	return forms;
#}



def loan_pres_first_vowel(first_vowel, stem, ixx, vowel_pres): #{

	forms = {};

	if vowel_pres == 'i' : #{
		sg_suffix = 'i';
		pl_suffix = 'u';
	#}
	else : #{ # vowel_pres == 'a'
		sg_suffix = 'a';
		pl_suffix = "aw";
	#}

	if first_vowel == 'i' : #{
	# jistabilixxa, but jistabilini
		forms['pres.p3.m.sg'] = loan_vowel_forms(stem + ixx + sg_suffix, stem + sg_suffix, 'LR');
		forms['pres.p3.m.sg'] += loan_vowel_forms('j' + stem + ixx + sg_suffix, 'j' + stem + sg_suffix, 'LR');
		forms['pres.p3.m.sg'] += loan_vowel_forms(stem + ixx + sg_suffix, stem + sg_suffix, 'RL');

		forms['pres.p3.pl'] = loan_vowel_forms(stem + ixx + pl_suffix, stem + pl_suffix, 'LR');
		forms['pres.p3.pl'] += loan_vowel_forms('j' + stem + ixx + pl_suffix, 'j' + stem + pl_suffix, 'LR');
		forms['pres.p3.pl'] += loan_vowel_forms(stem + ixx + pl_suffix, stem + pl_suffix, 'RL');
	#}
	else : #{
		forms['pres.p3.m.sg'] = loan_vowel_forms('j' + stem + ixx + sg_suffix, 'j' + stem + sg_suffix, '-');
		forms['pres.p3.pl'] = loan_vowel_forms('j' + stem + ixx + pl_suffix, 'j' + stem + pl_suffix, '-');
	#}

	forms['pres.p3.f.sg'] = loan_vowel_forms('t' + stem + ixx + sg_suffix, 't' + stem + sg_suffix, '-');
	forms['pres.p2.sg'] = loan_vowel_forms('t' + stem + ixx + sg_suffix, 't' + stem + sg_suffix, '-')
	forms['pres.p1.sg'] = loan_vowel_forms('n' + stem + ixx + sg_suffix, 'n' + stem + sg_suffix, '-');

	forms['pres.p2.pl'] = loan_vowel_forms('t' + stem + ixx + pl_suffix, 't' + stem + pl_suffix, '-');
	forms['pres.p1.pl'] = loan_vowel_forms('n' + stem + ixx  + pl_suffix, 'n' + stem + pl_suffix, '-');

	return forms;

#}



def loan_pres_first_cons(first_cons, stem, ixx, vowel_pres): #{

	forms = {};

	if vowel_pres == 'i' : #{
		sg_suffix = 'i';
		pl_suffix = 'u';
	#}
	else : #{ # vowel_pres == 'a'
		sg_suffix = 'a';
		pl_suffix = "aw";
	#}

	forms['pres.p3.m.sg'] = loan_vowel_forms('i' + stem + ixx + sg_suffix, 'i' + stem + sg_suffix, 'LR');
	forms['pres.p3.m.sg'] += loan_vowel_forms('j' + stem + ixx + sg_suffix, 'j' + stem + sg_suffix, 'LR');
	forms['pres.p3.m.sg'] += loan_vowel_forms('i' + stem + ixx + sg_suffix, 'i' + stem + sg_suffix, 'RL');

	forms['pres.p3.f.sg'] = loan_vowel_forms('t' + stem + ixx + sg_suffix, 't' + stem + sg_suffix, 'LR');
	forms['pres.p3.f.sg'] += loan_vowel_forms(first_cons + stem + ixx + sg_suffix, first_cons + stem + sg_suffix, 'LR');
	forms['pres.p3.f.sg'] += loan_vowel_forms('it' + stem + ixx + sg_suffix, 'it' + stem + sg_suffix, 'LR');
	forms['pres.p3.f.sg'] += loan_vowel_forms('i' + first_cons + stem + ixx + sg_suffix, 'i' + first_cons + stem + sg_suffix, 'LR');
	forms['pres.p3.f.sg'] += loan_vowel_forms('it' + stem + ixx + sg_suffix, 'it' + stem + sg_suffix, 'RL');

	forms['pres.p2.sg'] = loan_vowel_forms('t' + stem + ixx + sg_suffix, 't' + stem + sg_suffix, 'LR');
	forms['pres.p2.sg'] += loan_vowel_forms(first_cons + stem + ixx + sg_suffix, first_cons + stem + sg_suffix, 'LR');
	forms['pres.p2.sg'] += loan_vowel_forms('it' + stem + ixx + sg_suffix, 'it' + stem + sg_suffix, 'LR');
	forms['pres.p2.sg'] += loan_vowel_forms('i' + first_cons + stem + ixx + sg_suffix, 'i' + first_cons + stem + sg_suffix, 'LR');
	forms['pres.p2.sg'] += loan_vowel_forms('it' + stem + ixx + sg_suffix, 'it' + stem + sg_suffix, 'RL');

	forms['pres.p1.sg'] = loan_vowel_forms('n' + stem + ixx + sg_suffix, 'n' + stem + sg_suffix, 'LR');
	forms['pres.p1.sg'] += loan_vowel_forms('in' + stem + ixx + sg_suffix, 'in' + stem + sg_suffix, 'LR');
	forms['pres.p1.sg'] += loan_vowel_forms('in' + stem + ixx + sg_suffix, 'in' + stem + sg_suffix, 'RL');

	forms['pres.p3.pl'] = loan_vowel_forms('i' + stem + ixx + pl_suffix, 'i' + stem + pl_suffix, 'LR');
	forms['pres.p3.pl'] += loan_vowel_forms('j' + stem + ixx + pl_suffix, 'j' + stem + pl_suffix, 'LR');
	forms['pres.p3.pl'] += loan_vowel_forms('i' + stem + ixx + pl_suffix, 'i' + stem + pl_suffix, 'RL');

	forms['pres.p2.pl'] = loan_vowel_forms('t' + stem + ixx + pl_suffix, 't' + stem + pl_suffix, 'LR');
	forms['pres.p2.pl'] += loan_vowel_forms(first_cons + stem + ixx + pl_suffix, first_cons + stem + pl_suffix, 'LR');
	forms['pres.p2.pl'] += loan_vowel_forms('it' + stem + ixx + pl_suffix, 'it' + stem + pl_suffix, 'LR');
	forms['pres.p2.pl'] += loan_vowel_forms('i' + first_cons + stem + ixx + pl_suffix, 'i' + first_cons + stem + pl_suffix, 'LR');
	forms['pres.p2.pl'] += loan_vowel_forms('it' + stem + ixx + pl_suffix, 'it' + stem + pl_suffix, 'RL');

	forms['pres.p1.pl'] = loan_vowel_forms('n' + stem + ixx  + pl_suffix, 'n' + stem + pl_suffix, 'LR');
	forms['pres.p1.pl'] += loan_vowel_forms('in' + stem + ixx  + pl_suffix, 'in' + stem + pl_suffix, 'LR');
	forms['pres.p1.pl'] += loan_vowel_forms('in' + stem + ixx  + pl_suffix, 'in' + stem + pl_suffix, 'RL');

	return forms;

#}



def loan_pres_two_cons(stem, ixx, vowel_pres): #{
# two or double

	forms = {};

	if vowel_pres == 'i' : #{
		sg_suffix = 'i';
		pl_suffix = 'u';
	#}
	else : #{ # vowel_pres == 'a'
		sg_suffix = 'a';
		pl_suffix = "aw";
	#}

	# only 1 form? that may be too optimistic 
	forms['pres.p3.m.sg'] = loan_vowel_forms('ji' + stem + ixx + sg_suffix, 'ji' + stem + sg_suffix, '-');
	forms['pres.p3.f.sg'] = loan_vowel_forms('ti' + stem + ixx + sg_suffix, 'ti' + stem + sg_suffix, '-');
	forms['pres.p2.sg'] = loan_vowel_forms('ti' + stem + ixx + sg_suffix, 'ti' + stem + sg_suffix, '-');
	forms['pres.p1.sg'] = loan_vowel_forms('ni' + stem + ixx + sg_suffix, 'ni' + stem + sg_suffix, '-');

	forms['pres.p3.pl'] = loan_vowel_forms('ji' + stem + ixx + pl_suffix, 'ji' + stem + pl_suffix, '-');
	forms['pres.p2.pl'] = loan_vowel_forms('ti' + stem + ixx + pl_suffix, 'ti' + stem + pl_suffix, '-');
	forms['pres.p1.pl'] = loan_vowel_forms('ni' + stem + ixx  + pl_suffix, 'ni' + stem + pl_suffix, '-');

	return forms;

#}


def loan_imp(stem, ixx, vowel_pres): #{

	forms = {};

	if vowel_pres == 'i': #{
		# jistabilixxa, but jistabilini
		forms['imp.p2.sg'] = loan_vowel_forms(stem + ixx + 'i', stem + 'i', '-');
		forms['imp.p2.pl'] = loan_vowel_forms(stem + ixx + 'u', stem + 'u', '-');
	#}
	else : #{   vowel_pres == a
		forms['imp.p2.sg'] = loan_vowel_forms(stem + ixx + 'a', stem + 'a', '-');
		forms['imp.p2.pl'] = loan_vowel_forms(stem + ixx + 'aw', stem + 'aw', '-');
	#}

	return forms;

#}


## ----------------------------------------------------------------------------##
## irregular
## ----------------------------------------------------------------------------##



def irreg_consonant_forms (form_sg, form_sg_suff, r, ek): #{

	if ek == 'ok' :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__xrobt/ni', r),
			 (form_sg_suff, 'S__xrobt/nix', r),
			 (form_sg_suff, 'S__xrobt/ilha', r),
			 (form_sg_suff, 'S__xrobt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];
	else :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__qtalt/ni', r),
			 (form_sg_suff, 'S__qtalt/nix', r),
			 (form_sg_suff, 'S__qtalt/ilha', r),
			 (form_sg_suff, 'S__qtalt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def irreg_vowel_forms (form_pl, form_pl_suff, r): #{

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def irregular_forms (stem): #{

	forms = {};

	if stem == 'ta' : #{
		forms['past.p3.m.sg'] = irreg_vowel_forms('ta', 'ta', '-');
		forms['past.p3.f.sg'] = irreg_consonant_forms('tat', 'tat', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('tajt', 'tajt', '-', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('tajt', 'tajt', '-', 'ek');
		forms['past.p3.pl'] = irreg_vowel_forms('taw', 'taw', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('tajtu', 'tajtu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('tajna', 'tajnie', '-');

		forms['pres.p3.m.sg'] = irreg_vowel_forms('jagħti', 'jagħti', '-');
		forms['pres.p3.f.sg'] = irreg_vowel_forms('tagħti', 'tagħti', '-');
		forms['pres.p2.sg'] = irreg_vowel_forms('tagħti', 'tagħti', '-');
		forms['pres.p1.sg'] = irreg_vowel_forms('nagħti', 'nagħti', '-');
		forms['pres.p3.pl'] = irreg_vowel_forms('jagħtu', 'jagħtu', '-');
		forms['pres.p2.pl'] = irreg_vowel_forms('tagħtu', 'tagħtu', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('nagħtu', 'nagħtu', '-');

		forms['imp.p2.sg'] = irreg_vowel_forms('agħti', 'agħti', '-');
		forms['imp.p2.pl'] = irreg_vowel_forms('agħtu', 'agħtu', '-');

		forms['pp.m.sg'] = [('mogħti', '-', '-')] ;
		forms['pp.f.sg'] = [('mogħtija', '-', '-')] ;
		forms['pp.mf.pl'] = [('mogħtijin', '-', '-')] ;
	#}

	elif stem == 'ħa' : #{
		# ħa, but ħad-ha
		# what with negation suffix? 
		# only ma ħadx or both ma ħadx and ma hax? 
		forms['past.p3.m.sg'] = irreg_consonant_forms('ħa', 'ħad', '-', 'ek');
		forms['past.p3.f.sg'] = irreg_consonant_forms('ħadet', 'ħadit', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('ħadt', 'ħadt', '-', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('ħadt', 'ħadt', '-', 'ek');
		forms['past.p3.pl'] = irreg_vowel_forms('ħadu', 'ħadu', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('ħadtu', 'ħadtu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('ħadna', 'ħadnie', '-');

		# hm. jieħu with suff: jiħdu-? jieħdu-? jiħu-? jieħu-?
		# oh. jeħu-! TYM 201
		# min jagħti jieħu, min ma jagħtix ma jeħux
		forms['pres.p3.m.sg'] = irreg_vowel_forms('jieħu', 'jeħu', '-');
		forms['pres.p3.f.sg'] = irreg_vowel_forms('tieħu', 'teħu', '-');
		forms['pres.p2.sg'] = irreg_vowel_forms('tieħu', 'teħu', '-');
		forms['pres.p1.sg'] = irreg_vowel_forms('nieħu', 'neħu', '-');
		# so here: jieħdu with suffixes - jeħdu-?
		# we have
		# 2 ^jeħduh/*jeħduh$, 1 ^jeħduli/*jeħduli$, 1 ^jeħduhulhom/*jeħduhulhom$
		# but we also have
		# 1 ^nieħduh/*nieħduh$, 1 ^jieħdux/*jieħdux$, 1 ^jieħduh/*jieħduh$
		# so probably there should also be LR-only form jieħdu-
		forms['pres.p3.pl'] = irreg_vowel_forms('jieħdu', 'jeħdu', '-');
		forms['pres.p3.pl'] += irreg_vowel_forms('jieħdu', 'jieħdu', 'LR');
		forms['pres.p2.pl'] = irreg_vowel_forms('tieħdu', 'teħdu', '-');
		forms['pres.p2.pl'] = irreg_vowel_forms('tieħdu', 'tieħdu', 'LR');
		forms['pres.p1.pl'] = irreg_vowel_forms('nieħdu', 'neħdu', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('nieħdu', 'nieħdu', '-');

		forms['imp.p2.sg'] = irreg_consonant_forms('ħu', 'ħud', '-', 'ek');
		forms['imp.p2.pl'] = irreg_vowel_forms('ħudu', 'ħudu', '-');

		forms['pp.m.sg'] = [('meħud', '-', '-')] ;
		forms['pp.f.sg'] = [('meħuda', '-', '-')] ;
		forms['pp.mf.pl'] = [('meħudin', '-', '-')] ;
	#}

	elif stem == 'ra' : #{
		forms['past.p3.m.sg'] = irreg_vowel_forms('ra', 'ra', '-');
		forms['past.p3.f.sg'] = irreg_consonant_forms('rat', 'rat', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('rajt', 'rajt', '-', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('rajt', 'rajt', '-', 'ek');
		forms['past.p3.pl'] = irreg_vowel_forms('raw', 'raw', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('rajtu', 'rajtu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('rajna', 'rajnie', '-');

		forms['pres.p3.m.sg'] = irreg_vowel_forms('jara', 'jara', '-');
		forms['pres.p3.f.sg'] = irreg_vowel_forms('tara', 'tara', '-');
		forms['pres.p2.sg'] = irreg_vowel_forms('tara', 'tara', '-');
		forms['pres.p1.sg'] = irreg_vowel_forms('nara', 'nara', '-');
		forms['pres.p3.pl'] = irreg_vowel_forms('jaraw', 'jaraw', '-');
		forms['pres.p2.pl'] = irreg_vowel_forms('taraw', 'taraw', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('naraw', 'naraw', '-');

		forms['imp.p2.sg'] = irreg_vowel_forms('ara', 'ara', '-');
		forms['imp.p2.pl'] = irreg_vowel_forms('araw', 'araw', '-');

		forms['pp.m.sg'] = [('muri', '-', '-')] ;
		forms['pp.f.sg'] = [('murija', '-', '-')] ;
		forms['pp.mf.pl'] = [('murijin', '-', '-')] ;
	#}

	elif stem == 'qal' : #{
		# qal-hu-li or qal-u-li? 
		forms['past.p3.m.sg'] = irreg_consonant_forms('qal', 'qal', '-', 'ek');
		forms['past.p3.f.sg'] = irreg_consonant_forms('qalet', 'qalit', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('għedt', 'għedt', '-', 'ek');
		forms['past.p2.sg'] += irreg_consonant_forms('għidt', 'għidt', 'LR', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('għedt', 'għedt', '-', 'ek');
		forms['past.p1.sg'] += irreg_consonant_forms('għidt', 'għidt', 'LR', 'ek');

		forms['past.p3.pl'] = irreg_vowel_forms('qalu', 'qalu', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('għedtu', 'għedtu', '-');
		forms['past.p2.pl'] += irreg_vowel_forms('għidtu', 'għidtu', 'LR');
		forms['past.p1.pl'] = irreg_vowel_forms('għedna', 'għednie', '-');
		forms['past.p1.pl'] += irreg_vowel_forms('għidna', 'għidnie', 'LR');

		forms['pres.p3.m.sg'] = irreg_consonant_forms('igħid', 'igħid', 'LR', 'ek');
		forms['pres.p3.m.sg'] += irreg_consonant_forms('jgħid', 'jgħid', 'LR', 'ek');
		forms['pres.p3.m.sg'] += irreg_consonant_forms('igħid', 'igħid', 'RL', 'ek');

		forms['pres.p3.f.sg'] = irreg_consonant_forms('tgħid', 'tgħid', '-', 'ek');
		forms['pres.p2.sg'] = irreg_consonant_forms('tgħid', 'tgħid', '-', 'ek');
		forms['pres.p1.sg'] = irreg_consonant_forms('ngħid', 'ngħid', '-', 'ek');

		forms['pres.p3.pl'] = irreg_vowel_forms('igħidu', 'igħidu', 'LR');
		forms['pres.p3.pl'] += irreg_vowel_forms('jgħidu', 'jgħidu', 'LR');
		forms['pres.p3.pl'] += irreg_vowel_forms('igħidu', 'igħidu', 'RL');

		forms['pres.p2.pl'] = irreg_vowel_forms('tgħidu', 'tgħidu', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('ngħidu', 'ngħidu', '-');

		forms['imp.p2.sg'] = irreg_consonant_forms('għed', 'għed', '-', 'ek');
		forms['imp.p2.sg'] += irreg_consonant_forms('għid', 'għid', '-', 'ek');
		forms['imp.p2.pl'] = irreg_consonant_forms('għedu', 'għedu', '-', 'ek');
		forms['imp.p2.pl'] += irreg_consonant_forms('għidu', 'għidu', '-', 'ek');

#		forms['pp.m.sg'] = [('mogħti', '-', '-')] ;
#		forms['pp.f.sg'] = [('mogħtija', '-', '-')] ;
#		forms['pp.mf.pl'] = [('mogħtijin', '-', '-')] ;
	#}

	elif stem == 'ġie' : #{
		# with suffixes: hemm ġiethom darba waħda li raw
		# meta tiġik, ħudha - hm - 
		# 'do not miss a good opportunity when it comes your way'
		# also 2 ^ġietni/*ġietni$, 1 ^ġietu/*ġietu$, 1 ^ġiethom/*ġiethom$

		# what about i.o. andd d.o. + i.o.?
		forms['past.p3.m.sg'] = irreg_vowel_forms('ġie', 'ġie', '-');
		forms['past.p3.f.sg'] = irreg_consonant_forms('ġiet', 'ġiet', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('ġejt', 'ġejt', '-', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('ġejt', 'ġejt', '-', 'ek');
		forms['past.p3.pl'] = irreg_vowel_forms('ġew', 'ġew', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('ġejtu', 'ġejtu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('ġejna', 'ġejnie', '-');

		forms['pres.p3.m.sg'] = irreg_vowel_forms('jiġi', 'jiġi', '-');
		forms['pres.p3.f.sg'] = irreg_vowel_forms('tiġi', 'tiġi', '-');
		forms['pres.p2.sg'] = irreg_vowel_forms('tiġi', 'tiġi', '-');
		forms['pres.p1.sg'] = irreg_vowel_forms('niġi', 'niġi', '-');
		forms['pres.p3.pl'] = irreg_vowel_forms('jiġu', 'jiġu', '-');
		forms['pres.p2.pl'] = irreg_vowel_forms('tiġu', 'tiġu', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('niġu', 'niġu', '-');

		forms['imp.p2.sg'] = irreg_vowel_forms('ejja', 'ejja', '-');
		forms['imp.p2.pl'] = irreg_vowel_forms('ejjew', 'ejjew', '-');

		forms['pprs.m.sg'] = [('ġej', '-', '-')] ;
		forms['pprs.f.sg'] = [('ġejja', '-', '-')] ;
		forms['pprs.mf.pl'] = [('ġejjin', '-', '-')] ;
	#}

	elif stem == 'mar' : #{
		# it's possible to use mar + d.o.
		# but no sign of mar + d.o. suffix

		forms['past.p3.m.sg'] = irreg_consonant_forms('mar', 'mar', '-', 'ek');
		forms['past.p3.f.sg'] = irreg_consonant_forms('marret', 'marrit', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('mort', 'mort', '-', 'ok');	
		forms['past.p1.sg'] = irreg_consonant_forms('mort', 'mort', '-', 'ok');
		forms['past.p3.pl'] = irreg_vowel_forms('marru', 'marru', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('mortu', 'mortu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('morna', 'mornie', '-');

		forms['pres.p3.m.sg'] = irreg_consonant_forms('imur', 'imur', 'LR', 'ek');
		forms['pres.p3.m.sg'] = irreg_consonant_forms('jmur', 'jmur', 'LR', 'ek');
		forms['pres.p3.m.sg'] = irreg_consonant_forms('imur', 'imur', 'RL', 'ek');

		forms['pres.p3.f.sg'] = irreg_consonant_forms('tmur', 'tmur', '-', 'ek');
		forms['pres.p2.sg'] = irreg_consonant_forms('tmur', 'tmur', '-', 'ek');

		# there is also 1 ^inmorru/*inmorru$
		forms['pres.p1.sg'] = irreg_consonant_forms('immur', 'immur', 'LR', 'ek');
		forms['pres.p1.sg'] = irreg_consonant_forms('mmur', 'mmur', 'LR', 'ek');
		forms['pres.p1.sg'] = irreg_consonant_forms('immur', 'immur', 'RL', 'ek');

		forms['pres.p3.pl'] = irreg_vowel_forms('imorru', 'imorru', 'LR');
		forms['pres.p3.pl'] = irreg_vowel_forms('jmorru', 'jmorru', 'LR');
		forms['pres.p3.pl'] = irreg_vowel_forms('imorru', 'imorru', 'RL');

		forms['pres.p2.pl'] = irreg_vowel_forms('tmorru', 'tmorru', '-');

		forms['pres.p1.pl'] = irreg_vowel_forms('immorru', 'immorru', 'LR');
		forms['pres.p1.pl'] = irreg_vowel_forms('mmorru', 'mmorru', 'LR');
		forms['pres.p1.pl'] = irreg_vowel_forms('immorru', 'immorru', 'RL');

		forms['imp.p2.sg'] = irreg_consonant_forms('mur', 'mur', '-', 'ek');
		forms['imp.p2.pl'] = loan_vowel_forms('morru', 'morru', '-');

	#}

# isn't it a special -ie type of hollow verbs (in Arabic primae hamza though)
	elif stem == 'kiel' : #{

		# kiel-u, kiel-x? not kilu, kilx? or maybe kielu, but kilha?
		forms['past.p3.m.sg'] = irreg_consonant_forms('kiel', 'kiel', '-', 'ek');
		forms['past.p3.f.sg'] = irreg_consonant_forms('kielet', 'kielit', '-', 'ek');
		forms['past.p2.sg'] = irreg_consonant_forms('kilt', 'kilt', '-', 'ek');	
		forms['past.p1.sg'] = irreg_consonant_forms('kilt', 'kilt', '-', 'ek');
		forms['past.p3.pl'] = irreg_vowel_forms('kielu', 'kielu', '-');
		forms['past.p2.pl'] = irreg_vowel_forms('kiltu', 'kiltu', '-');
		forms['past.p1.pl'] = irreg_vowel_forms('kilna', 'kilnie', '-');

		# 1 ^jiekolhom/*jiekolhom$  1 ^jiekolhielu/*jiekolhielu$
		forms['pres.p3.m.sg'] = irreg_consonant_forms('jiekol', 'jiekol', '-', 'ok');
		forms['pres.p3.f.sg'] = irreg_consonant_forms('tiekol', 'tiekol', '-', 'ok');
		forms['pres.p2.sg'] = irreg_consonant_forms('tiekol', 'tiekol', '-', 'ok');
		forms['pres.p1.sg'] = irreg_consonant_forms('niekol', 'niekol', '-', 'ok');

		forms['pres.p3.pl'] = irreg_vowel_forms('jieklu', 'jieklu', '-');
		forms['pres.p2.pl'] = irreg_vowel_forms('tieklu', 'tieklu', '-');
		forms['pres.p1.pl'] = irreg_vowel_forms('nieklu', 'nieklu', '-');

		forms['imp.p2.sg'] = irreg_consonant_forms('kul', 'kul', '-', 'ek');
		forms['imp.p2.pl'] = irreg_vowel_forms('kulu', 'kulu', '-');

	#}

	return forms;

#}


## ----------------------------------------------------------------------------##
## defective
## ----------------------------------------------------------------------------##


def auxiliary_forms (stem): #{

	forms = {};

	if stem == 'kien' : #{
		forms['past.p3.m.sg'] = [('kien', '-', '-'),
					 ('kien', 'S__qtalt/x', '-')];
		forms['past.p3.f.sg'] = [('kienet', '-', '-'),
					 ('kienit', 'S__qtalt/x', '-')];
		forms['past.p2.sg'] =  [('kont', '-', '-'),
					('kont', 'S__qtalt/x', '-')];	
		forms['past.p1.sg'] =  [('kont', '-', '-'),
					('kont', 'S__qtalt/x', '-')];
		forms['past.p3.pl'] =  [('kienu', '-', '-'),
					('kienu', 'S__qtalt/x', '-')];
		forms['past.p2.pl'] =  [('kontu', '-', '-'),
					('kontu', 'S__qtalt/x', '-')];
		forms['past.p1.pl'] =  [('konna', '-', '-'),
					('konnie', 'S__qtalt/x', '-')];

		forms['pres.p3.m.sg'] = [('ikun', '-', 'LR'),
					 ('jkun', '-', 'LR'),
					 ('ikun', '-', 'RL'),
					 ('ikun', 'S__qtalt/x', 'LR'), 
					 ('jkun', 'S__qtalt/x', 'LR'),
					 ('ikun', 'S__qtalt/x', 'RL')];
		forms['pres.p3.f.sg'] = [('tkun', '-', '-'),
					 ('tkun', 'S__qtalt/x', '-')];
		forms['pres.p2.sg'] =  [('tkun', '-', '-'),
					('tkun', 'S__qtalt/x', '-')];
		forms['pres.p1.sg'] =  [('inkun', '-', 'LR'),
					('nkun', '-', 'LR'),
					('inkun', '-', 'RL'),
					('inkun', 'S__qtalt/x', 'LR'), 
					('nkun', 'S__qtalt/x', 'LR'),
					('inkun', 'S__qtalt/x', 'RL')];
		forms['pres.p3.pl'] =  [('ikunu', '-', 'LR'),
					('jkunu', '-', 'LR'),
					('ikunu', '-', 'RL'),
					('ikunu', 'S__qtalt/x', 'LR'), 
					('jkunu', 'S__qtalt/x', 'LR'),
					('ikunu', 'S__qtalt/x', 'RL')];
		forms['pres.p2.pl'] =  [('tkunu', '-', '-'),
					('tkunu', 'S__qtalt/x', '-')];
		forms['pres.p1.pl'] =  [('inkunu', '-', 'LR'),
					('nkunu', '-', 'LR'),
					('inkunu', '-', 'RL'),
					('inkunu', 'S__qtalt/x', 'LR'), 
					('nkunu', 'S__qtalt/x', 'LR'),
					('inkunu', 'S__qtalt/x', 'RL')];

		# I'm guessing here
		forms['imp.p2.sg'] = [('kun', '-', '-'),
				      ('kun', 'S__qtalt/x', '-')];
		forms['imp.p2.pl'] = [('kunu', '-', '-'),
				      ('kunu', 'S__qtalt/x', '-')];

	#}

	elif stem == 'kellu' : #{
		forms['past.p3.m.sg'] = [('kellu', '-', '-'),
					 ('kellu', 'S__qtalt/x', '-')];
		forms['past.p3.f.sg'] = [('kellha', '-', '-'),
					 ('kellhie', 'S__qtalt/x', '-')];
		forms['past.p2.sg'] =  [('kellek', '-', '-'),
					('kellek', 'S__qtalt/x', '-')];	
		forms['past.p1.sg'] =  [('kelli', '-', '-'),
					('kelli', 'S__qtalt/x', '-')];
		forms['past.p3.pl'] =  [('kellhom', '-', '-'),
					('kellhom', 'S__qtalt/x', '-')];
		forms['past.p2.pl'] =  [('kellkom', '-', '-'),
					('kellkom', 'S__qtalt/x', '-')];
		forms['past.p1.pl'] =  [('kellna', '-', '-'),
					('kellnie', 'S__qtalt/x', '-')];

		forms['pres.p3.m.sg'] = [('ikollu', '-', 'LR'),
					 ('jkollu', '-', 'LR'),
					 ('ikollu', '-', 'RL'),
					 ('ikollu', 'S__qtalt/x', 'LR'), 
					 ('jkollu', 'S__qtalt/x', 'LR'),
					 ('ikollu', 'S__qtalt/x', 'RL')];
		forms['pres.p3.f.sg'] = [('ikollha', '-', 'LR'),
					 ('jkollha', '-', 'LR'),
					 ('ikollha', '-', 'RL'),
					 ('ikollhie', 'S__qtalt/x', 'LR'), 
					 ('jkollhie', 'S__qtalt/x', 'LR'),
					 ('ikollhie', 'S__qtalt/x', 'RL')];
		forms['pres.p2.sg'] =  [('ikollok', '-', 'LR'),
					('jkollok', '-', 'LR'),
					('ikollok', '-', 'RL'),
					('ikollok', 'S__qtalt/x', 'LR'), 
					('jkollok', 'S__qtalt/x', 'LR'),
					('ikollok', 'S__qtalt/x', 'RL')];
		forms['pres.p1.sg'] =  [('ikolli', '-', 'LR'),
					('jkolli', '-', 'LR'),
					('ikolli', '-', 'RL'),
					('ikolli', 'S__qtalt/x', 'LR'), 
					('jkolli', 'S__qtalt/x', 'LR'),
					('ikolli', 'S__qtalt/x', 'RL')];
		forms['pres.p3.pl'] =  [('ikollhom', '-', 'LR'),
					('jkollhom', '-', 'LR'),
					('ikollhom', '-', 'RL'),
					('ikollhom', 'S__qtalt/x', 'LR'), 
					('jkollhom', 'S__qtalt/x', 'LR'),
					('ikollhom', 'S__qtalt/x', 'RL')];
		forms['pres.p2.pl'] =  [('ikollkom', '-', 'LR'),
					('jkollkom', '-', 'LR'),
					('ikollkom', '-', 'RL'),
					('ikollkom', 'S__qtalt/x', 'LR'), 
					('jkollkom', 'S__qtalt/x', 'LR'),
					('ikollkom', 'S__qtalt/x', 'RL')];
		forms['pres.p1.pl'] =  [('ikollna', '-', 'LR'),
					('jkollna', '-', 'LR'),
					('ikollna', '-', 'RL'),
					('ikollnie', 'S__qtalt/x', 'LR'), 
					('jkollnie', 'S__qtalt/x', 'LR'),
					('ikollnie', 'S__qtalt/x', 'RL')];

	#}

	return forms;

#}


##-----------------------------------------------------------------------------##

tv_with_pprs = [];

stems = [
	{'stem': 'fetaħ', 'type': 'strong', 'gloss': 'open', 'root': 'f-t-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mi'}, # itv
	{'stem': 'qasam', 'type': 'strong', 'gloss': 'break', 'root': 'q-s-m', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'kiteb', 'type': 'strong', 'gloss': 'write', 'root': 'k-t-b', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'ħabat', 'type': 'strong', 'gloss': 'strike', 'root': 'ħ-b-t', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'}, #itv
	{'stem': 'ħaqar', 'type': 'strong', 'gloss': 'oppress', 'root': 'ħ-q-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'ħalaq', 'type': 'strong', 'gloss': 'create', 'root': 'ħ-l-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'}, #itv, o-o be created
	{'stem': 'ħaraq', 'type': 'strong', 'gloss': 'burn', 'root': 'ħ-r-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'}, #itv
	{'stem': 'ħataf', 'type': 'strong', 'gloss': 'snatch', 'root': 'ħ-t-f', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'}, #itv
	{'stem': 'għalaq', 'type': 'strong', 'gloss': 'shut', 'root': 'għ-l-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'}, #itv
	{'stem': 'għasar', 'type': 'strong', 'gloss': 'squeeze', 'root': 'għ-s-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'għażaq', 'type': 'strong', 'gloss': 'dig', 'root': 'għ-ż-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'bagħat', 'type': 'strong', 'gloss': 'send', 'root': 'b-għ-t', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'ċaħad', 'type': 'strong', 'gloss': 'deny', 'root': 'ċ-ħ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mi'}, #itv
## ------ checked above this line ------
	{'stem': 'daħak', 'type': 'strong', 'gloss': 'laugh', 'root': 'd-ħ-k', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'dalam', 'type': 'strong', 'gloss': 'grow·dark', 'root': 'd-l-m', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'fadal', 'type': 'strong', 'gloss': 'be·left·over', 'root': 'f-d-l', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'fasad', 'type': 'strong', 'gloss': 'bleed', 'root': 'f-s-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'laħaq', 'type': 'strong', 'gloss': 'reach', 'root': 'l-ħ-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'iv'},
	{'stem': 'lagħab', 'type': 'strong', 'gloss': 'play', 'root': 'l-għ-b', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'bagħad', 'type': 'strong', 'gloss': 'hate', 'root': 'b-għ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'lagħaq', 'type': 'strong', 'gloss': 'lick', 'root': 'l-għ-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'marad', 'type': 'strong', 'gloss': 'fall·sick', 'root': 'm-r-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'sahar', 'type': 'strong', 'gloss': 'work·overtime', 'root': 's-h-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'taħan', 'type': 'strong', 'gloss': 'grind', 'root': 't-ħ-n', 'vowel_perf': 'a-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'wasal', 'type': 'strong', 'gloss': 'arrive', 'root': 'w-s-l', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'daħal', 'type': 'strong', 'gloss': 'enter', 'root': 'd-ħ-l', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'ġabar', 'type': 'strong', 'gloss': 'collect', 'root': 'ġ-b-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'saħan', 'type': 'strong', 'gloss': 'become·warm', 'root': 's-ħ-n', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'talab', 'type': 'strong', 'gloss': 'pray, ask', 'root': 't-l-b', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'maxat', 'type': 'strong', 'gloss': 'comb', 'root': 'm-x-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'qagħad', 'type': 'strong', 'gloss': 'stand', 'root': 'q-għ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'bagħad', 'type': 'strong', 'gloss': 'hate', 'root': 'b-għ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'baram', 'type': 'strong', 'gloss': 'twist', 'root': 'b-r-m', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħanaq', 'type': 'strong', 'gloss': 'make', 'root': 'ħ-n-q', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'laqat', 'type': 'strong', 'gloss': 'hit', 'root': 'l-q-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'qaras', 'type': 'strong', 'gloss': 'pinch', 'root': 'q-r-s', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'rabat', 'type': 'strong', 'gloss': 'tie, bind', 'root': 'r-b-t', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'raqad', 'type': 'strong', 'gloss': 'sleep', 'root': 'r-q-d', 'vowel_perf': 'a-a', 'vowel_impf': 'o-o', 'trans': 'iv'}, # with pprs ??
	{'stem': 'qara', 'type': 'strong', 'gloss': 'read', 'root': 'q-r-j', 'vowel_perf': 'a-a', 'trans': 'TD'},
	{'stem': 'ġara', 'type': 'strong', 'gloss': 'happen', 'root': 'ġ-r-j', 'vowel_perf': 'a-a', 'trans': 'TD'},
	{'stem': 'ħareġ', 'type': 'strong', 'gloss': 'go·out', 'root': 'ħ-r-ġ', 'vowel_perf': 'a-e', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħadem', 'type': 'strong', 'gloss': 'work', 'root': 'ħ-d-m', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħafer', 'type': 'strong', 'gloss': 'forgive', 'root': 'ħ-f-r', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħaleb', 'type': 'strong', 'gloss': 'milk', 'root': 'ħ-l-b', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħalef', 'type': 'strong', 'gloss': 'swear', 'root': 'ħ-l-f', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'għalef', 'type': 'strong', 'gloss': 'feed·animals', 'root': 'għ-l-f', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'ħasel', 'type': 'strong', 'gloss': 'wash', 'root': 'ħ-s-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'għamel', 'type': 'strong', 'gloss': 'make', 'root': 'għ-m-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qabel', 'type': 'strong', 'gloss': 'agree', 'root': 'q-b-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qabeż', 'type': 'strong', 'gloss': 'jump', 'root': 'q-b-ż', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'għażel', 'type': 'strong', 'gloss': 'choose', 'root': 'għ-ż-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'TD'},
	{'stem': 'qatel', 'type': 'strong', 'gloss': 'kill', 'root': 'q-t-l', 'vowel_perf': 'a-e', 'vowel_impf': 'o-o', 'trans': 'TD', 'pp': 'ma'},
	{'stem': 'ħeles', 'type': 'strong', 'gloss': 'deliver', 'root': 'ħ-l-s', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'me'}, # also iv ?
	{'stem': 'għereq', 'type': 'strong', 'gloss': 'stink', 'root': 'għ-r-q', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'hemeż', 'type': 'strong', 'gloss': 'fasten·with·pin', 'root': 'h-m-ż', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'heġem', 'type': 'strong', 'gloss': 'devour', 'root': 'h-ġ-m', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'hebeż', 'type': 'strong', 'gloss': 'recede', 'root': 'h-b-ż', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'heres', 'type': 'strong', 'gloss': 'pestle', 'root': 'h-r-s', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħebel', 'type': 'strong', 'gloss': 'rave', 'root': 'ħ-b-l', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħemer', 'type': 'strong', 'gloss': 'ferment', 'root': 'ħ-m-r', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'ħerek', 'type': 'strong', 'gloss': 'rise·early', 'root': 'ħ-r-k', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'TD'},
	{'stem': 'deher', 'type': 'strong', 'gloss': 'appear', 'root': 'd-h-r', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'fehem', 'type': 'strong', 'gloss': 'understand', 'root': 'f-h-m', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'xeher', 'type': 'strong', 'gloss': 'wail', 'root': 'x-h-r', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'xegħel', 'type': 'strong', 'gloss': 'light', 'root': 'x-għ-l', 'vowel_perf': 'e-e', 'trans': 'iv'},
	{'stem': 'resaq', 'type': 'strong', 'gloss': 'approach', 'root': 'r-s-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'TD'},
	{'stem': 'feraħ', 'type': 'strong', 'gloss': 'rejoice', 'root': 'f-r-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'refa', 'type': 'strong', 'gloss': 'raise', 'root': 'r-f-għ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD', 'pp': 'me'},# check impf_v
#	{'stem': 'fetaħ', 'type': 'strong', 'gloss': 'open', 'root': 'f-t-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'felaħ', 'type': 'strong', 'gloss': 'be·strong', 'root': 'f-l-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'kesaħ', 'type': 'strong', 'gloss': 'be·cold', 'root': 'k-s-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'mesaħ', 'type': 'strong', 'gloss': 'wipe', 'root': 'm-s-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'lemaħ', 'type': 'strong', 'gloss': 'perceive', 'root': 'l-m-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'rebaħ', 'type': 'strong', 'gloss': 'win', 'root': 'r-b-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'reżaħ', 'type': 'strong', 'gloss': 'shiver', 'root': 'r-ż-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'sebaħ', 'type': 'strong', 'gloss': 'dawn', 'root': 's-b-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'seraq', 'type': 'strong', 'gloss': 'steal', 'root': 's-r-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'telaq', 'type': 'strong', 'gloss': 'depart', 'root': 't-l-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'TD'},
	{'stem': 'selaħ', 'type': 'strong', 'gloss': 'skin', 'root': 's-l-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'żebagħ', 'type': 'strong', 'gloss': 'paint', 'root': 'ż-b-għ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'żelaq', 'type': 'strong', 'gloss': 'slip', 'root': 'ż-l-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sebaq', 'type': 'strong', 'gloss': 'outstrip', 'root': 's-b-q', 'vowel_perf': 'e-a', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'nefaħ', 'type': 'strong', 'gloss': 'blow', 'root': 'n-f-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'iv'},
	{'stem': 'nefaq', 'type': 'strong', 'gloss': 'spend', 'root': 'n-f-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'beżaq', 'type': 'strong', 'gloss': 'spit', 'root': 'b-ż-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'fetaq', 'type': 'strong', 'gloss': 'unstitch', 'root': 'f-t-q', 'vowel_perf': 'e-a', 'vowel_impf': 'o-o', 'trans': 'TD'},
#	{'stem': 'wera', 'type': 'strong', 'gloss': 'show', 'root': 'w-r-j', 'vowel_perf': 'e-a', 'trans': 'TD'},
	{'stem': 'ġema', 'type': 'strong', 'gloss': 'gather', 'root': 'ġ-m-għ', 'vowel_perf': 'e-a', 'trans': 'TD'},
	{'stem': 'kiser', 'type': 'strong', 'gloss': 'break', 'root': 'k-s-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'niżel', 'type': 'strong', 'gloss': 'descend', 'root': 'n-ż-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'bidel', 'type': 'strong', 'gloss': 'change', 'root': 'b-d-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'difen', 'type': 'strong', 'gloss': 'bury', 'root': 'd-f-n', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'dilek', 'type': 'strong', 'gloss': 'smear', 'root': 'd-l-k', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'fired', 'type': 'strong', 'gloss': 'separate', 'root': 'f-r-d', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'firex', 'type': 'strong', 'gloss': 'spread', 'root': 'f-r-x', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'ġibed', 'type': 'strong', 'gloss': 'pull', 'root': 'ġ-b-d', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'gideb', 'type': 'strong', 'gloss': 'lie', 'root': 'g-d-b', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'gidem', 'type': 'strong', 'gloss': 'bite', 'root': 'g-d-m', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kiber', 'type': 'strong', 'gloss': 'grow', 'root': 'k-b-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kines', 'type': 'strong', 'gloss': 'sweep', 'root': 'k-n-s', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'giref', 'type': 'strong', 'gloss': 'scratch', 'root': 'g-r-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'nidem', 'type': 'strong', 'gloss': 'repent', 'root': 'n-d-m', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'kixef', 'type': 'strong', 'gloss': 'unveil', 'root': 'k-x-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD', 'pp': 'mi'},
	{'stem': 'siker', 'type': 'strong', 'gloss': 'get·drunk', 'root': 's-k-r', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'silef', 'type': 'strong', 'gloss': 'lend', 'root': 's-l-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'tilef', 'type': 'strong', 'gloss': 'lose', 'root': 't-l-f', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'żifen', 'type': 'strong', 'gloss': 'dance', 'root': 'ż-f-n', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'TD'},
	{'stem': 'wiżen', 'type': 'strong', 'gloss': 'weigh', 'root': 'w-ż-n', 'vowel_perf': 'i-e', 'trans': 'TD'},
	{'stem': 'siket', 'type': 'strong', 'gloss': 'be·silent', 'root': 's-k-t', 'vowel_perf': 'i-e', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sogħol', 'type': 'strong', 'gloss': 'cough', 'root': 's-għ-l', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'sogħob', 'type': 'strong', 'gloss': 'be·sorry', 'root': 's-għ-b', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'xorob', 'type': 'strong', 'gloss': 'drink', 'root': 'x-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'i-o', 'trans': 'TD'},
	{'stem': 'ħolom', 'type': 'strong', 'gloss': 'dream', 'root': 'ħ-l-m', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'korob', 'type': 'strong', 'gloss': 'groan', 'root': 'k-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'ħoloq', 'type': 'strong', 'gloss': 'create', 'root': 'ħ-l-q', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'forogħ', 'type': 'strong', 'gloss': 'ebb', 'root': 'f-r-għ', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'kotor', 'type': 'strong', 'gloss': 'abound', 'root': 'k-t-r', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għodos', 'type': 'strong', 'gloss': 'dive', 'root': 'għ-d-s', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għokos', 'type': 'strong', 'gloss': 'decay', 'root': 'għ-k-s', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għorok', 'type': 'strong', 'gloss': 'rub', 'root': 'għ-r-k', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'TD'},
	{'stem': 'għolob', 'type': 'strong', 'gloss': 'grow·thin', 'root': 'għ-l-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'iv'},
	{'stem': 'qorob', 'type': 'strong', 'gloss': 'get·near', 'root': 'q-r-b', 'vowel_perf': 'o-o', 'vowel_impf': 'o-o', 'trans': 'iv'},
	# - Whether the middle radical of a hollow verb is 'j' or 'w' can be known by the second vowel of the 
	#   vocalic sequence of the imperfect. If this vowel is long 'u', the middle radical is 'w' if it is 
	#   long 'i' then the middle radical is 'j'. 
	# - Of all the hollow verbs, only a few have past participles
	{'stem': 'dar', 'type': 'hollow', 'gloss': 'turn', 'root': 'd-w-r', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'sar', 'type': 'hollow', 'gloss': 'become', 'root': 's-j-r', 'vowel_perf': 'a-a', 'trans': 'iv', 'pp': 'mi'}, # 'pprs': 'e' - that's sar2
### hollow verbs - checked above this line
	{'stem': 'miet', 'type': 'hollow', 'gloss': 'die', 'root': 'm-w-t', 'vowel_perf': 'ie-a', 'trans': 'iv'},
	{'stem': 'dieq', 'type': 'hollow', 'gloss': 'taste', 'root': 'd-w-q', 'vowel_perf': 'ie-a', 'trans': 'iv'},
	{'stem': 'daq', 'type': 'hollow', 'gloss': 'taste', 'root': 'd-w-q', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'dam', 'type': 'hollow', 'gloss': 'take.time', 'root': 'd-w-m', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'sam', 'type': 'hollow', 'gloss': 'fast', 'root': 's-w-m', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'far', 'type': 'hollow', 'gloss': 'boil', 'root': 'f-w-r', 'vowel_perf': 'a-a', 'trans': 'iv'},
#	{'stem': 'mar', 'type': 'hollow', 'gloss': 'go', 'root': 'm-w-r', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'sab', 'type': 'hollow', 'gloss': 'find', 'root': 's-j-b', 'vowel_perf': 'a-a', 'trans': 'iv', 'pp': 'mi'},
	{'stem': 'għam', 'type': 'hollow', 'gloss': 'swim', 'root': 'għ-w-m', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'qam', 'type': 'hollow', 'gloss': 'rise', 'root': 'q-w-m', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'żar', 'type': 'hollow', 'gloss': 'visit', 'root': 'ż-w-r', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'ġab', 'type': 'hollow', 'gloss': 'bring', 'root': 'ġ-j-b', 'vowel_perf': 'a-a', 'trans': 'iv', 'pp': 'me'},
	{'stem': 'ġieb', 'type': 'hollow', 'gloss': 'bring', 'root': 'ġ-j-b', 'vowel_perf': 'ie-a', 'trans': 'iv', 'pp': 'me'},
	{'stem': 'biegħ', 'type': 'hollow', 'gloss': 'sell', 'root': 'b-j-għ', 'vowel_perf': 'ie-a', 'trans': 'iv', 'pp': 'mi'},
	{'stem': 'fieq', 'type': 'hollow', 'gloss': 'recuperate', 'root': 'f-j-q', 'vowel_perf': 'ie-a', 'trans': 'iv'},
	{'stem': 'għab', 'type': 'hollow', 'gloss': 'disappear', 'root': 'għ-j-b', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'għan', 'type': 'hollow', 'gloss': 'help', 'root': 'għ-j-n', 'vowel_perf': 'a-a', 'trans': 'iv', 'pp': 'me'},
	{'stem': 'għar', 'type': 'hollow', 'gloss': 'envy', 'root': 'għ-j-r', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'għax', 'type': 'hollow', 'gloss': 'live', 'root': 'għ-j-x', 'vowel_perf': 'a-a', 'trans': 'iv'},
	{'stem': 'qies', 'type': 'hollow', 'gloss': 'measure', 'root': 'q-j-s', 'vowel_perf': 'ie-a', 'trans': 'iv', 'pp': 'mi'},
	{'stem': 'ried', 'type': 'hollow', 'gloss': 'want', 'root': 'r-j-d', 'vowel_perf': 'ie-a', 'trans': 'tv'},
	{'stem': 'tar', 'type': 'hollow', 'gloss': 'fly', 'root': 't-j-r', 'vowel_perf': 'a-a', 'trans': 'tv'},
	{'stem': 'żied', 'type': 'hollow', 'gloss': 'increase', 'root': 'ż-j-d', 'vowel_perf': 'ie-a', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'qiem', 'type': 'hollow', 'gloss': 'venerate', 'root': 'q-w-m', 'vowel_perf': 'ie-a', 'trans': 'tv', 'pp': 'me'},

# weak verbs
	{'stem': 'qara', 'type': 'weak', 'gloss': 'read', 'root': 'q-r-j', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'p_stem': 'qra', 'pp': 'mo'},
	{'stem': 'mexa', 'type': 'weak', 'gloss': 'walk', 'root': 'm-x-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-i', 'trans': 'iv', 'p_stem': 'mxie'},
#
	{'stem': 'beda', 'type': 'weak', 'gloss': 'start', 'root': 'b-d-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'p_stem': 'bdie', 'pp': 'mi'},
	{'stem': 'mela', 'type': 'weak', 'gloss': 'fill', 'root': 'm-l-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'reħa', 'type': 'weak', 'gloss': 'let·go', 'root': 'r-ħ-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'me'},
	{'stem': 'ħela', 'type': 'weak', 'gloss': 'waste', 'root': 'ħ-l-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mo'},
	{'stem': 'ħeba', 'type': 'weak', 'gloss': 'hide', 'root': 'ħ-b-j', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mo'},
	{'stem': 'rema', 'type': 'weak', 'gloss': 'throw·away', 'root': 'r-m-j', 'vowel_perf': 'e-a', 'vowel_impf': 'a-i', 'trans': 'tv', 'p_stem': 'rmie', 'pp': 'mo'},

# doubled
	{'stem': 'radd', 'type': 'doubled', 'gloss': 'restore', 'root': 'r-d-d', 'vowel_perf': 'a-a', 'vowel_impf': 'a-o', 'trans': 'tv', 'pp': 'mi'}, # + pp ma?
	{'stem': 'mess', 'type': 'doubled', 'gloss': 'touch', 'root': 'm-s-s', 'vowel_perf': 'e-e', 'vowel_impf': 'e-i', 'trans': 'tv', 'pp': 'mi'},
#
	{'stem': 'qarr', 'type': 'doubled', 'gloss': 'go·to·confession', 'root': 'q-r-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-e', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'raqq', 'type': 'doubled', 'gloss': 'become·thin', 'root': 'r-q-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-e', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'saħħ', 'type': 'doubled', 'gloss': 'materialise', 'root': 's-ħ-ħ', 'vowel_perf': 'a-a', 'vowel_impf': 'i-e', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'xaħħ', 'type': 'doubled', 'gloss': 'be·stingy', 'root': 'x-ħ-ħ', 'vowel_perf': 'a-a', 'vowel_impf': 'i-e', 'trans': 'iv', 'pp': 'ma'},
	{'stem': 'damm', 'type': 'doubled', 'gloss': 'string·together', 'root': 'd-m-m', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'iv', 'pp': 'mi'},
	{'stem': 'daqq', 'type': 'doubled', 'gloss': 'play', 'root': 'd-q-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'iv', 'pp': 'mi'},
	{'stem': 'ġarr', 'type': 'doubled', 'gloss': 'carry', 'root': 'ġ-r-r', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'ħakk', 'type': 'doubled', 'gloss': 'scratch', 'root': 'ħ-k-k', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'ħall', 'type': 'doubled', 'gloss': 'loosen', 'root': 'ħ-l-l', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'ħass', 'type': 'doubled', 'gloss': 'feel', 'root': 'ħ-s-s', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'ħatt', 'type': 'doubled', 'gloss': 'unload', 'root': 'ħ-t-t', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'għażż', 'type': 'doubled', 'gloss': 'cherish', 'root': 'għ-ż-ż', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'rass', 'type': 'doubled', 'gloss': 'press', 'root': 'r-s-s', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'ma'},
	{'stem': 'sadd', 'type': 'doubled', 'gloss': 'plug', 'root': 's-d-d', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'xaqq', 'type': 'doubled', 'gloss': 'crack', 'root': 'x-q-q', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'żamm', 'type': 'doubled', 'gloss': 'hold', 'root': 'ż-m-m', 'vowel_perf': 'a-a', 'vowel_impf': 'i-o', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'leqq', 'type': 'doubled', 'gloss': 'glitter', 'root': 'l-q-q', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'iv'},
	{'stem': 'temm', 'type': 'doubled', 'gloss': 'finish', 'root': 't-m-m', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'bell', 'type': 'doubled', 'gloss': 'wet', 'root': 'b-l-l', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'bexx', 'type': 'doubled', 'gloss': 'sprinkle', 'root': 'b-x-x', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'ġeżż', 'type': 'doubled', 'gloss': 'shear', 'root': 'ġ-ż-ż', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},
	{'stem': 'kedd', 'type': 'doubled', 'gloss': 'vex', 'root': 'k-d-d', 'vowel_perf': 'e-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'mi'},

# quadriliteral
	{'stem': 'qaħqaħ', 'type': 'quad', 'gloss': 'hack', 'root': 'q-ħ-q-ħ', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'dardar', 'type': 'quad', 'gloss': 'make·turbid', 'root': 'd-r-d-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'farfar', 'type': 'quad', 'gloss': 'shake·off·dust', 'root': 'f-r-f-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ħarbat', 'type': 'quad', 'gloss': 'rout', 'root': 'ħ-r-b-t', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'każbar', 'type': 'quad', 'gloss': 'revile', 'root': 'k-ż-b-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'bandal', 'type': 'quad', 'gloss': 'swing', 'root': 'b-n-d-l', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ċaflas', 'type': 'quad', 'gloss': 'splash', 'root': 'ċ-f-l-s', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ċaħħad', 'type': 'quad', 'gloss': 'deprive', 'root': 'ċ-ħ-ħ-d', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'}, # strong pattern 2
	{'stem': 'ċanfar', 'type': 'quad', 'gloss': 'reproach', 'root': 'ċ-n-f-r', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ċapċap', 'type': 'quad', 'gloss': 'clap', 'root': 'ċ-p-ċ-p', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ċappas', 'type': 'quad', 'gloss': 'smear', 'root': 'ċ-p-p-s', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'}, # strong pattern 2
	{'stem': 'ċaqlaq', 'type': 'quad', 'gloss': 'shake', 'root': 'ċ-q-l-q', 'vowel_perf': 'a-a', 'vowel_impf': 'a-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'qarmeċ', 'type': 'quad', 'gloss': 'crunch', 'root': 'q-r-m-ċ', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ħawtel', 'type': 'quad', 'gloss': 'be·diligent', 'root': 'ħ-w-t-l', 'vowel_perf': 'a-e', 'vowel_impf': 'a-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'kexkex', 'type': 'quad', 'gloss': 'shock', 'root': 'k-x-k-x', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'petpet', 'type': 'quad', 'gloss': 'blink', 'root': 'p-t-p-t', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'temtem', 'type': 'quad', 'gloss': 'stutter', 'root': 't-m-t-m', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'xengel', 'type': 'quad', 'gloss': 'swing', 'root': 'x-n-g-l', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'ċempel', 'type': 'quad', 'gloss': 'ring', 'root': 'ċ-m-p-l', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'dendel', 'type': 'quad', 'gloss': 'hang', 'root': 'd-n-d-l', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'gerbeb', 'type': 'quad', 'gloss': 'roll', 'root': 'g-r-b-b', 'vowel_perf': 'e-e', 'vowel_impf': 'e-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'fesdaq', 'type': 'quad', 'gloss': 'shell·peas', 'root': 'f-s-d-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'tertaq', 'type': 'quad', 'gloss': 'shatter', 'root': 't-r-t-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'werżaq', 'type': 'quad', 'gloss': 'scream', 'root': 'w-r-ż-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'fixkel', 'type': 'quad', 'gloss': 'obstruct', 'root': 'f-x-k-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'im'},
	{'stem': 'bixkel', 'type': 'quad', 'gloss': 'cheat', 'root': 'b-x-k-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'iv', 'pp': 'im'},
	{'stem': 'biddel', 'type': 'quad', 'gloss': 'alter', 'root': 'b-d-d-l', 'vowel_perf': 'i-e', 'vowel_impf': 'i-e', 'trans': 'tv', 'pp': 'im'}, # strong pattern 2
	{'stem': 'berbaq', 'type': 'quad', 'gloss': 'squander', 'root': 'b-r-b-q', 'vowel_perf': 'e-a', 'vowel_impf': 'e-a', 'trans': 'tv', 'pp': 'im'},

# loan
	{'stem': 'kanta', 'type': 'loan', 'gloss': 'sing', 'subtype': 'first_cons', 'first_cons': 'k', 'base': 'kant', 'vowel_impf': 'a', 'pp': 'kantat'},
	{'stem': 'ammira', 'type': 'loan', 'gloss': 'admire', 'subtype': 'first_vowel', 'first_vowel': 'a', 'base': 'ammir', 'vowel_impf': 'a', 'pp': 'ammirat'},
	{'stem': 'stimula', 'type': 'loan', 'gloss': 'stimulate', 'subtype': 'two_cons', 'base': 'stimul', 'vowel_impf': 'a', 'pp': 'stimulat'},
	{'stem': 'ipparteċipa', 'type': 'loan', 'gloss': 'participate', 'subtype': 'double_cons', 'base': 'pparteċip', 'imp_base': 'ipparteċip', 'vowel_impf': 'a', 'pp': 'parteċipat'},
#irrappreżenta, loan, represent, r-r-p-r-ż-n-t-a, a-a, romance, unchecked
#ippenetra, loan, penetrate, p-p-n-t-r, a-a, romance, checked
#ivvjola, loan, violate, v-v-j-l, a-a, romance, checked
#indika, loan, indicate, i-n-d-k, a-a, romance, checked
#eżerċita, loan, exercise, e-ż-r-ċ-t, a-a, romance, checked
#ipprova, loan, try, i-p-p-r-v, a-a, romance, checked
#esperjenza, loan, experience, s-p-r-j-n-z, a-a, romance, checked
#iddeċide, loan, decide, d-e-ċ-d, a-a, romance, checked
#ordna, loan, order, o-r-d-n, a-a, romance, unchecked
#
	{'stem': 'falla', 'type': 'loan', 'gloss': 'be·absent', 'subtype': 'first_cons', 'first_cons': 'f', 'base': 'fall', 'vowel_impf': 'i', 'pp': 'fallut'}, # also pp mfalli?
#iddeskriva, loan, describe, d-s-k-r-v, a-i, romance, checked
#aggredixxa, loan, agress, a-g-g-r-s, a-i, romance, checked
#irrisponda, loan, respond, r-s-p-n-d, a-i, romance, checked
#ittraduċa, loan, translate, t-r-a-c-d-c, a-i, romance, checked
	{'stem': 'irreaġixxa', 'type': 'loan', 'gloss': 'react', 'subtype': 'double_cons', 'base': 'rreaġ', 'ixx': 'ixx', 'vowel_impf': 'i'},
#ipprojbixxa, loan, prohibit, p-r-j-b-x, a-i, romance, checked
#ippromwova, loan, promote, p-r-m-w-v, a-i, romance, checked
#inkluda, loan, include, i-n-k-l-u-d, a-i, romance, unchecked
#ikkonsista, loan, consist, k-k-n-s-s-t, a-i, romance, unchecked
#iżviluppa, loan, develop, ż-v-l-p-p, a-i, romance, unchecked
#
#espressa, loan, express, e-s-p-r-s-s, e-e, romance # that's pp of esprima
#
#aġġastja, loan, adjust, ġ-s-t-j, a-a, english, checked
#iddawnlowdja, loan, download, d-w-n-l-w-d, a-a, english, checked
#infurza, loan, enforce, i-n-f-u-r-z, a-a, english, unchecked
#vjola, loan, violate, v-j-o-l, a-a, english, unchecked
#vvjola, loan, breach, v-v-j-o-l, a-a, english, unchecked
#ikklassifika, loan, classify, k-l-s-f-k, a-i, english, unchecked
#ikkonsidra, loan, consider, k-k-n-s-d-r, a-i, english, unchecked
#

# irregular
	{'stem': 'ta', 'type': 'irregular', 'gloss': 'give', 'root': 'għ-t-j'}, # Arabic 4th form أعطى
	{'stem': 'ħa', 'type': 'irregular', 'gloss': 'take', 'root': 'hamza-ħ-d'}, # Arabic أخذ
	{'stem': 'ra', 'type': 'irregular', 'gloss': 'see', 'root': 'hamza-ħ-d'}, # Arabic أخذ
	{'stem': 'qal', 'type': 'irregular', 'gloss': 'say', 'root': 'q-w-l'}, # Arabic قال
	{'stem': 'ġie', 'type': 'irregular', 'gloss': 'come', 'root': 'ġ-j-hamza'}, # Arabic جاء
	{'stem': 'mar', 'type': 'irregular', 'gloss': 'go'},
	{'stem': 'kiel', 'type': 'irregular', 'gloss': 'eat'}, # أكل

# auxiliary
	{'stem': 'kien', 'type': 'auxiliary', 'gloss': 'be'},
	{'stem': 'kellu', 'type': 'auxiliary', 'gloss': 'have'},

];

##-----------------------------------------------------------------------------##

infl = {};

for stem in stems: #{

	if stem['type'] == 'strong': #{
		infl[stem['stem']] = {};
		infl[stem['stem']].update(strong_past(stem['root'], stem['vowel_perf']));

		if stem['trans'] == 'iv' or stem['stem'] in tv_with_pprs:
			infl[stem['stem']].update(strong_pprs(stem['root'], stem['vowel_perf']));

		if 'pp' in stem: 
			infl[stem['stem']].update(strong_pp(stem['root'], stem['vowel_perf'], stem['pp']));

		if 'vowel_impf' in stem: 
			infl[stem['stem']].update(strong_pres(stem['root'], stem['vowel_impf']));
			infl[stem['stem']].update(strong_imp(stem['root'], stem['vowel_impf']));

	elif stem['type'] == 'hollow': #{

		infl[stem['stem']] = {};
		infl[stem['stem']] = hollow_past(stem['root'], stem['vowel_perf']);

		if 'pprs' in stem: 
			infl[stem['stem']].update(hollow_pprs(stem['root'], stem['pprs']));
		if 'pp' in stem: #{
			infl[stem['stem']].update(hollow_pp(stem['root'], stem['vowel_perf'], stem['pp']));

		infl[stem['stem']].update(hollow_pres(stem['root'], stem['vowel_perf']));
		infl[stem['stem']].update(hollow_imp(stem['root'], stem['vowel_perf']));

	elif stem['type'] == 'weak': #{

		infl[stem['stem']] = weak_past(stem['root'], stem['vowel_perf']);
		infl[stem['stem']].update(weak_pres(stem['root'], stem['vowel_impf']));
		infl[stem['stem']].update(weak_imp(stem['root'], stem['vowel_impf']));
		if 'pp' in stem: #{
			infl[stem['stem']].update(weak_pp(stem['root'], stem['vowel_perf'], stem['pp']));
# pprs

	elif stem['type'] == 'doubled': #{

		infl[stem['stem']] = doubled_past(stem['root'], stem['vowel_perf']);
		if 'vowel_impf' in stem: 
			infl[stem['stem']].update(doubled_pres(stem['root'], stem['vowel_impf']));
			infl[stem['stem']].update(doubled_imp(stem['root'], stem['vowel_impf']));
		if 'pp' in stem: #{
			infl[stem['stem']].update(doubled_pp(stem['root'], stem['vowel_perf'], stem['pp']));

	elif stem['type'] == 'quad': #{

		infl[stem['stem']] = quad_past(stem['root'], stem['vowel_perf']);
		infl[stem['stem']].update(quad_pres(stem['root'], stem['vowel_perf']));
		infl[stem['stem']].update(quad_imp(stem['root'], stem['vowel_perf']));
		if 'pp' in stem: #{
			infl[stem['stem']].update(quad_pp(stem['root'], stem['vowel_perf'], stem['pp']));
	#}

	elif stem['type'] == 'loan': #{

		infl[stem['stem']] = {};

		ixx = '';
		if 'ixx' in stem:
			ixx = stem['ixx'];   # ixx = 'ixx';

		if stem['subtype'] == 'first_vowel': #{
			infl[stem['stem']] = loan_past(stem['base'], ixx, stem['vowel_impf']);
			infl[stem['stem']].update(loan_pres_first_vowel(stem['first_vowel'], stem['base'], ixx, stem['vowel_impf']));
			infl[stem['stem']].update(loan_imp(stem['base'], ixx, stem['vowel_impf']));
		#}

		elif stem['subtype'] == 'first_cons': #{
			infl[stem['stem']] = loan_past(stem['base'], ixx, stem['vowel_impf']);
			infl[stem['stem']].update(loan_pres_first_cons(stem['first_cons'], stem['base'], ixx, stem['vowel_impf']));
			infl[stem['stem']].update(loan_imp(stem['base'], ixx, stem['vowel_impf']));
		#}

		elif stem['subtype'] == 'two_cons' : #{
			infl[stem['stem']] = loan_past(stem['base'], ixx, stem['vowel_impf']);
			infl[stem['stem']].update(loan_pres_two_cons(stem['base'], ixx, stem['vowel_impf']));
			infl[stem['stem']].update(loan_imp(stem['base'], ixx, stem['vowel_impf']));
		#}

		elif stem['subtype'] == 'double_cons' : #{
			infl[stem['stem']] = loan_past_double_cons(stem['base'], ixx, stem['vowel_impf']);
			infl[stem['stem']].update(loan_pres_two_cons(stem['base'], ixx, stem['vowel_impf']));
			infl[stem['stem']].update(loan_imp('i' + stem['base'], ixx, stem['vowel_impf']));
		#}

		if 'pp' in stem: #{
			infl[stem['stem']].update(loan_pp(stem['pp']));
# pprs
	#}

	elif stem['type'] == 'irregular' : #{
		infl[stem['stem']] = irregular_forms(stem['stem']);

	elif stem['type'] == 'auxiliary' : #{
		infl[stem['stem']] = auxiliary_forms(stem['stem']);

#}

print header().decode('utf-8');

for stem in infl: #{

	for flex in infl[stem]: #{
		for subflex in infl[stem][flex]: #{
			# restriction attribute, lm attribute, postgenerator tag:
			r, lm, a = '', '', ''	 
			if flex == 'past.p3.m.sg' and subflex[1] == '-':  
				lm = ' lm="%s"' % (stem,)
			if subflex[2] == 'LR':
				r = ' r="%s"' % (subflex[2],)
				a = ''
			elif subflex[2] == 'RL':
				r = ' r="%s"' % (subflex[2],)
				a = '<a/>'

			left = subflex[0];
			right = stem + '<s n="vblex"/>' + sym(flex);
			paradigm = subflex[1];

			if paradigm == "-": # no suffix
				entry  = '<e%s%s><p><l>%s%s</l><r>%s</r></p></e>' % (r, lm, a, left,right);
			else :  # suffix, in this case subflex[1] tells us which paradigm should be used
				entry = '<e%s><p><l>%s%s</l><r>%s</r></p><par n="%s"/></e>' % (r, a, left, right, paradigm);

			print entry.decode('utf-8')
			#}
		#}
	#}
#}

print footer();
