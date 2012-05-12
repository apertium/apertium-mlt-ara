#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys, codecs, copy, time;
import classes;

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
	header = header + '    <sdef n="du"/>\n';
	header = header + '    <sdef n="pl"/>\n';
	header = header + '    <sdef n="m"/>\n';
	header = header + '    <sdef n="f"/>\n';
	header = header + '    <sdef n="mf"/>\n';
	header = header + '  </sdefs>\n';
	header = header + '  <pardefs>\n';


# direct object
	header = header + '    <pardef n="S__فتح/ه">\n';
        header = header + '      <e><p><l>ه</l><r><j/>ه<s n="prn"/><s n="p3"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ها</l><r><j/>ه<s n="prn"/><s n="p3"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><j/>ه<s n="prn"/><s n="p2"/><s n="m"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ك</l><r><j/>ه<s n="prn"/><s n="p2"/><s n="f"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>ني</l><r><j/>ه<s n="prn"/><s n="p1"/><s n="mf"/><s n="sg"/></r></p></e>\n';
        header = header + '      <e><p><l>هما</l><r><j/>ه<s n="prn"/><s n="p3"/><s n="mf"/><s n="du"/></r></p></e>\n';
        header = header + '      <e><p><l>كما</l><r><j/>ه<s n="prn"/><s n="p2"/><s n="mf"/><s n="du"/></r></p></e>\n';
        header = header + '      <e><p><l>هم</l><r><j/>ه<s n="prn"/><s n="p3"/><s n="m"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>هن</l><r><j/>ه<s n="prn"/><s n="p3"/><s n="f"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>كم</l><r><j/>ه<s n="prn"/><s n="p2"/><s n="m"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>كن</l><r><j/>ه<s n="prn"/><s n="p2"/><s n="f"/><s n="pl"/></r></p></e>\n';
        header = header + '      <e><p><l>نا</l><r><j/>ه<s n="prn"/><s n="p1"/><s n="mf"/><s n="pl"/></r></p></e>\n';
	header = header + '    </pardef>\n';


	header = header + '  </pardefs>\n\n';
	header = header + '  <section id="main" type="standard">\n';
    	header = header + '  <!-- Generated on: ' + time.strftime('%Y-%m-%d %H:%M %Z') + ' -->\n\n';
	

	return header;
	
#}
 
def footer(): #{
	footer = '';
	footer = footer + '  </section>\n';
	footer = footer + '</dictionary>\n';
	
	return footer;
#}


##-----------------------------------------------------------------------------##

#tv_with_pprs = [];

if len(sys.argv)>1:
    if '--help' in sys.argv:
        print "Usage: verbs.py stems_file";
        sys.exit(1);


if len(sys.argv) == 2 :
	stemsfile = sys.argv[1];
else :
	stemsfile = sys.path[0] + '/stems.wiki';

try:
	lines = file(stemsfile);
except IOError as e:
        sys.stderr.write("Error reading file: {0}\n".format(stemsfile));
        sys.exit(1);


stems = [];
aux_verbs = [];

for line in lines: #{

	line = line.strip(); 

	# '|-', '|}', headings, '{|'
	if len(line) < 3 or line[0] == '!' or line[0] == '{':
	        continue;
    
	line = line.lstrip('|');
	row = line.split('||'); 


	stem = {'stem': row[0].strip(), 'type': row[1].strip(), 'theme': row[2].strip(), 'gloss': row[3].strip(), 'root': row[4].strip(), 'trans': row[5].strip(), 'cat': row[6].strip()};
	stems = stems + [stem];
        if stem['cat'] == 'vaux' :
                aux_verbs = aux_verbs + [stem['stem']];


#}



##-----------------------------------------------------------------------------##

infl = {};

for stem in stems: #{

    	try:
    	    stem_class = getattr(classes, stem['type']);
    	except AttributeError:
    	    sys.stderr.write("Error: Missing class '{0}'\n".format(stem['type']));
    	    sys.exit(1);

    	infl[stem['stem']] = stem_class.main(stem);
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
			if stem in aux_verbs :
				right = stem + '<s n="vaux"/>' + sym(flex);
			else :
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
