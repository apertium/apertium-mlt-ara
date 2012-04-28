#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy;

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


def strong_pres_sg_forms (prefix, pres_sg_long, pres_sg_short, r): #{

	forms = [(prefix + pres_sg_long, '-', r),
		 (prefix + pres_sg_long, 'S__qtalt/x', r),
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

	pres_sg_long = v[0] + r[0] + r[1] + v[1] + r[2];
	pres_sg_short = v[0] + r[0] + r[1] + r[2];
	pres_pl = v[0] + r[0] + r[1] + r[2] + 'u';

	forms['pres.p3.m.sg'] = strong_pres_sg_forms('', pres_sg_long, pres_sg_short, 'LR');
	forms['pres.p3.m.sg'] += strong_pres_sg_forms('j', pres_sg_long, pres_sg_short, 'LR');
	forms['pres.p3.m.sg'] += strong_pres_sg_forms('', pres_sg_long, pres_sg_short, 'RL');

	forms['pres.p3.f.sg'] = strong_pres_sg_forms('t', pres_sg_long, pres_sg_short, '-');
	forms['pres.p2.sg'] = strong_pres_sg_forms('t', pres_sg_long, pres_sg_short, '-');
	forms['pres.p1.sg'] = strong_pres_sg_forms('n', pres_sg_long, pres_sg_short, '-');
	
	forms['pres.p3.pl'] = strong_pres_pl_forms('j', pres_pl, '-'); # j-iDĦL-u j-iFTĦ-u
	forms['pres.p2.pl'] = strong_pres_pl_forms('t', pres_pl, '-');
	forms['pres.p1.pl'] = strong_pres_pl_forms('n', pres_pl, '-');

	# When the second radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted
	if r[1] == 'l' or r[1] == 'm' or r[1] == 'n' or r[1] == 'għ': #{
		forms['pres.p3.pl'] = [('j' + v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-', '-')] ; # j-iToLB-u
		forms['pres.p2.pl'] = [('t' + v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-', '-')] ; # t-iToLB-u
		forms['pres.p1.pl'] = [('n' + v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-', '-')] ; # n-iToLB-u
	#}

	return forms;
#}



def strong_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels
	
	forms = {};

	pres_sg_long = v[0] + r[0] + r[1] + v[1] + r[2];
	pres_sg_short = v[0] + r[0] + r[1] + r[2];
	pres_pl = v[0] + r[0] + r[1] + r[2] + 'u';

	forms['imp.p2.sg'] = strong_pres_sg_forms('', pres_sg_long, pres_sg_short, '-');

	# When the second radical of the verb is 'l', 'm', 'n' or 'għ', a euphonic 
	# vowel must be inserted
	if r[1] == 'l' or r[1] == 'm' or r[1] == 'n' or r[1] == 'għ': #{
		forms['imp.p2.pl'] = [(v[0] + r[0] + v[1] + r[1] + r[2] + 'u', '-', '-')];
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
		 (past_sg, 'S__qtalt/x', r),
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
		 (past_sg, 'S__qtalt/x', r),
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
		 (past_pl, 'S__qtalt/x', r),
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

	# add long form with second e->i
	forms['past.p3.m.sg'] = strong_past_p3_sg_m_forms(r[0] + v[0] + r[1] + v[1] + r[2], r[0] + v[0] + r[1] + v[1] + r[2], r[0] + v[0] + r[1] + r[2], '');
	# add -ot suffix for o-o class
	forms['past.p3.f.sg'] = strong_past_sg_forms(r[0] + v[0] + r[1] + r[2] + 'et', r[0] + v[0] + r[1] + r[2] + 'it', '-');	# Omit second vowel of stem word
	forms['past.p2.sg'] = strong_past_sg_forms(r[0] + r[1] + v[1] + r[2] + 't', r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word
	forms['past.p1.sg'] = strong_past_sg_forms(r[0] + r[1] + v[1] + r[2] + 't', r[0] + r[1] + v[1] + r[2] + 't', '-');	# Omit first vowel of stem word

	forms['past.p3.pl'] = strong_past_pl_forms(r[0] + v[0] + r[1] + r[2] + 'u', r[0] + v[0] + r[1] + r[2] + 'u', '-');	# Omit second vowel of stem word
	forms['past.p2.pl'] = strong_past_pl_forms(r[0] + r[1] + v[1] + r[2] + 'tu', r[0] + r[1] + v[1] + r[2] + 'tu', '-');	# Omit first vowel of stem word
	forms['past.p1.pl'] = strong_past_pl_forms(r[0] + r[1] + v[1] + r[2] + 'na', r[0] + r[1] + v[1] + r[2] + 'nie', '-');	# Omit first vowel of stem word

	# == Overrides == 

	if r[0] == 'w' or r[0] == 'għ': #{
		# If the first radical is 'w' or 'għ' then we have a full disyllabic form
		forms['past.p2.sg'] = [(r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-', '-')];	
		forms['past.p1.sg'] = [(r[0] + v[0] + r[1] + v[1] + r[2] + 't', '-', '-')];	
	#}


	return forms;
#}



##-----------------------------------------------------------------------------##

tv_with_pprs = [];

stems = [
	{'stem': 'fetaħ', 'type': 'strong', 'gloss': 'open', 'root': 'f-t-ħ', 'vowel_perf': 'e-a', 'vowel_impf': 'i-a', 'trans': 'tv', 'pp': 'mi'}, # itv

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
#######
#	elif stem['type'] == 'hollow': #{

#		infl[stem['stem']] = hollow_past(stem['root'], stem['vowel_perf']);
#		infl[stem['stem']].update(hollow_pres(stem['root'], stem['vowel_perf']));
#		if 'pp' in stem: #{
#			infl[stem['stem']].update(hollow_pp(stem['root'], stem['vowel_perf'], stem['pp']));
#		infl[stem['stem']].update(hollow_imp(stem['root'], stem['vowel_perf']));

#	elif stem['type'] == 'weak': #{
#
#		infl[stem['stem']] = weak_past(stem['root'], stem['vowel_perf']);
#		infl[stem['stem']].update(weak_pres(stem['root'], stem['vowel_impf']));
#		infl[stem['stem']].update(weak_imp(stem['root'], stem['vowel_impf']));
#		if 'pp' in stem: #{
#			infl[stem['stem']].update(weak_pp(stem['root'], stem['vowel_perf'], stem['pp']));

#	elif stem['type'] == 'doubled': #{

#		infl[stem['stem']] = doubled_past(stem['root'], stem['vowel_perf']);
#		if 'vowel_impf' in stem: 
#			infl[stem['stem']].update(doubled_pres(stem['root'], stem['vowel_impf']));
#			infl[stem['stem']].update(doubled_imp(stem['root'], stem['vowel_impf']));
#		if 'pp' in stem: #{
#			infl[stem['stem']].update(doubled_pp(stem['root'], stem['vowel_perf'], stem['pp']));

#	elif stem['type'] == 'quad': #{

#		infl[stem['stem']] = quad_past(stem['root'], stem['vowel_perf']);
#		infl[stem['stem']].update(quad_pres(stem['root'], stem['vowel_perf']));
#		infl[stem['stem']].update(quad_imp(stem['root'], stem['vowel_perf']));
#		if 'pp' in stem: #{
#			infl[stem['stem']].update(quad_pp(stem['root'], stem['vowel_perf'], stem['pp']));
#	#}
##}

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
