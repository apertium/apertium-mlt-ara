#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## doubled verbs
## ----------------------------------------------------------------------------##


## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def doubled_patt1_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [(r[0] + 'ا' + r[1], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + 'ا' + r[1] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [(r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [(r[0] + 'ا' + r[1] + 'ات', '-', '-')] ;

	return forms;
#}


def doubled_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'و' + r[1], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'و' + r[1] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'و' + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'و' + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


def doubled_patt1_pres(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	if r[1] == 'ن' :
		base_long = r[0] + r[1];
	else :
		base_long = r[0] + r[1] + r[1];

	if tv == 'iv' : #{
		forms['pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['pres.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
		forms['pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
		forms['pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

		forms['pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['pres.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
		forms['pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['pres.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
		forms['pres.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['pres.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['pres.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['pres.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];
	#}

	forms['pres.pasv.p3.m.sg'] = [('ي' + base, '-', '-')];
	forms['pres.pasv.p3.f.sg'] = [('ت' + base, '-', '-')];
	forms['pres.pasv.p2.m.sg'] = [('ت' + base, '-', '-')];
	forms['pres.pasv.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
	forms['pres.pasv.p1.mf.sg'] = [('أ' + base, '-', '-')];

	forms['pres.pasv.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
	forms['pres.pasv.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
	forms['pres.pasv.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

	forms['pres.pasv.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
	forms['pres.pasv.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
	forms['pres.pasv.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
	forms['pres.pasv.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
	forms['pres.pasv.p1.mf.pl'] = [('ن' + base, '-', '-')];

	return forms;
#}


def doubled_patt1_subjun(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	if r[1] == 'ن' :
		base_long = r[0] + r[1];
	else :
		base_long = r[0] + r[1] + r[1];


	if tv == 'iv' : #{
		forms['subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['subjun.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
		forms['subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['subjun.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
		forms['subjun.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['subjun.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['subjun.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['subjun.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];
	#}

	forms['subjun.pasv.p3.m.sg'] = [('ي' + base, '-', '-')];
	forms['subjun.pasv.p3.f.sg'] = [('ت' + base, '-', '-')];
	forms['subjun.pasv.p2.m.sg'] = [('ت' + base, '-', '-')];
	forms['subjun.pasv.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['subjun.pasv.p1.mf.sg'] = [('أ' + base, '-', '-')];

	forms['subjun.pasv.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
	forms['subjun.pasv.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
	forms['subjun.pasv.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

	forms['subjun.pasv.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['subjun.pasv.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
	forms['subjun.pasv.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['subjun.pasv.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
	forms['subjun.pasv.p1.mf.pl'] = [('ن' + base, '-', '-')];

	return forms;
#}


def doubled_patt1_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	base_long = r[0] + r[1] + r[1];
	if r[1] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];


	if tv == 'iv' : #{
		forms['apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base_long, '-', 'LR')];
		forms['apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
		forms['apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
		forms['apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base_long, '-', 'LR')];

		forms['apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base_long, '-', 'LR')];
	#}
	else : #{
		forms['apocop.p3.m.sg'] = [('ي' + base, '-', '-'),
					   ('ي' + base_long, '-', 'LR'),
					   ('ي' + base, 'S__فتح/ه', '-'),
					   ('ي' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p3.f.sg'] = [('ت' + base, '-', '-'), 
					   ('ت' + base_long, '-', 'LR'),
					   ('ي' + base, 'S__فتح/ه', '-'),
					   ('ي' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p2.m.sg'] = [('ت' + base, '-', '-'),
					   ('ت' + base_long, '-', 'LR'),
					   ('ت' + base, 'S__فتح/ه', '-'),
					   ('ت' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'),
					   ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['apocop.p1.mf.sg'] = [('أ' + base, '-', '-'),
					    ('أ' + base_long, '-', 'LR'),
					    ('أ' + base, 'S__فتح/ه', '-'),
					    ('أ' + base_long, 'S__فتح/ه', 'LR')];
	
		forms['apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['apocop.p1.mf.pl'] = [('ن' + base, '-', '-'),
					    ('ن' + base_long, '-', 'LR'),
					    ('ن' + base, 'S__فتح/ه', '-'),
					    ('ن' + base_long, 'S__فتح/ه', 'LR')];
	#}

	forms['apocop.pasv.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base_long, '-', 'LR')];
	forms['apocop.pasv.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
	forms['apocop.pasv.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
	forms['apocop.pasv.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['apocop.pasv.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base_long, '-', 'LR')];

	forms['apocop.pasv.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
	forms['apocop.pasv.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
	forms['apocop.pasv.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

	forms['apocop.pasv.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['apocop.pasv.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
	forms['apocop.pasv.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['apocop.pasv.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
	forms['apocop.pasv.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base_long, '-', 'LR')];

	return forms;
#}


def doubled_patt1_imp(root, tv): #{
	r = root.split('-'); # radicals

	# passive voice?

	base = r[0] + r[1];
	base_long = r[0] + r[1] + r[1];
	if r[1] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];


	forms = {};

	if tv == 'iv' : #{
		forms['imp.p2.m.sg'] = [(base, '-', '-'), ('ا' + base_long, '-', 'LR')];
		forms['imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['imp.p2.mf.du'] = [(base + 'ا', '-', '-')];
		forms['imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['imp.p2.f.pl'] = [('ا' + base_n + 'ن', '-', '-')];
	#}
	else : #{
		forms['imp.p2.m.sg'] = [(base, '-', '-'),
					('ا' + base_long, '-', 'LR'),
					(base, 'S__فتح/ه', '-'),
					('ا' + base_long, 'S__فتح/ه', 'LR')];
		forms['imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', 'S__فتح/ه', '-')];
		forms['imp.p2.mf.du'] = [(base + 'ا', '-', '-'), (base + 'ا', 'S__فتح/ه', '-')];
		forms['imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', 'S__فتح/ه', '-')];
		forms['imp.p2.f.pl'] = [('ا' + base_n + 'ن', '-', '-'), ('ا' + base_n + 'ن', 'S__فتح/ه', '-')];
	#}

	return forms ; 
#}


def doubled_patt1_past(root, tv): #{
	r = root.split('-'); # radicals

	# add forms like مديت ?

	base = r[0] + r[1];

	if r[2] == 'ت' :
		base_t = r[0] + r[1];
	else :
		base_t = r[0] + r[1] + r[1];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];

	forms = {};

	if tv == 'iv' : #{
		forms['past.p3.m.sg'] = [(base, '-', '-')];
		forms['past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['past.p2.m.sg'] = [(base_t + 'ت', '-', '-')];
		forms['past.p2.f.sg'] = [(base_t + 'ت', '-', '-')];
		forms['past.p1.mf.sg'] = [(base_t + 'ت', '-', '-')];

		forms['past.p3.m.du'] = [(base + 'ا', '-', '-')];
		forms['past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['past.p2.mf.du'] = [(base_t + 'تما', '-', '-')];

		forms['past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['past.p3.f.pl'] = [(base_n + 'ن', '-', '-')];
		forms['past.p2.m.pl'] = [(base_t + 'تم', '-', '-')];
		forms['past.p2.f.pl'] = [(base_t + 'تن', '-', '-')];
		forms['past.p1.mf.pl'] = [(base_n + 'نا', '-', '-')];
	#}
	else : #{
		forms['past.p3.m.sg'] = [(base, '-', '-'), (base, 'S__فتح/ه', '-')];
		forms['past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', 'S__فتح/ه', '-')];
		forms['past.p2.m.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];
		forms['past.p2.f.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];
		forms['past.p1.mf.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];

		forms['past.p3.m.du'] = [(base + 'ا', '-', '-'), (base + 'ا', 'S__فتح/ه', '-')];
		forms['past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', 'S__فتح/ه', '-')];
		forms['past.p2.mf.du'] = [(base_t + 'تما', '-', '-'), (base_t + 'تما', 'S__فتح/ه', '-')];

		forms['past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', 'S__فتح/ه', '-')];
		forms['past.p3.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', 'S__فتح/ه', '-')];
		forms['past.p2.m.pl'] = [(base_t + 'تم', '-', '-'), (base_t + 'تمو', 'S__فتح/ه', '-')];
		forms['past.p2.f.pl'] = [(base_t + 'تن', '-', '-'), (base_t + 'تن', 'S__فتح/ه', '-')];
		forms['past.p1.mf.pl'] = [(base_n + 'نا', '-', '-'), (base_n + 'نا', 'S__فتح/ه', '-')];
	#}

	forms['past.pasv.p3.m.sg'] = [(base, '-', '-')];
	forms['past.pasv.p3.f.sg'] = [(base + 'ت', '-', '-')];
	forms['past.pasv.p2.m.sg'] = [(base_t + 'ت', '-', '-')];
	forms['past.pasv.p2.f.sg'] = [(base_t + 'ت', '-', '-')];
	forms['past.pasv.p1.mf.sg'] = [(base_t + 'ت', '-', '-')];

	forms['past.pasv.p3.m.du'] = [(base + 'ا', '-', '-')];
	forms['past.pasv.p3.f.du'] = [(base + 'تا', '-', '-')];
	forms['past.pasv.p2.mf.du'] = [(base_t + 'تما', '-', '-')];

	forms['past.pasv.p3.m.pl'] = [(base + 'وا', '-', '-')];
	forms['past.pasv.p3.f.pl'] = [(base_n + 'ن', '-', '-')];
	forms['past.pasv.p2.m.pl'] = [(base_t + 'تم', '-', '-')];
	forms['past.pasv.p2.f.pl'] = [(base_t + 'تن', '-', '-')];
	forms['past.pasv.p1.mf.pl'] = [(base_n + 'نا', '-', '-')];

	return forms;
#}



## ----------------------------------------------------------------------------##
## pattern 4
## ----------------------------------------------------------------------------##


def doubled_patt4_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'ات', '-', '-')] ;

	return forms;
#}


def doubled_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


def doubled_patt4_pres(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	if r[1] == 'ن' :
		base_long = r[0] + r[1];
	else :
		base_long = r[0] + r[1] + r[1];

	if tv == 'iv' : #{
		forms['pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['pres.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
		forms['pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
		forms['pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

		forms['pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['pres.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
		forms['pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['pres.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
		forms['pres.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['pres.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['pres.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['pres.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];
	#}

	forms['pres.pasv.p3.m.sg'] = [('ي' + base, '-', '-')];
	forms['pres.pasv.p3.f.sg'] = [('ت' + base, '-', '-')];
	forms['pres.pasv.p2.m.sg'] = [('ت' + base, '-', '-')];
	forms['pres.pasv.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
	forms['pres.pasv.p1.mf.sg'] = [('أ' + base, '-', '-')];

	forms['pres.pasv.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
	forms['pres.pasv.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
	forms['pres.pasv.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

	forms['pres.pasv.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
	forms['pres.pasv.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
	forms['pres.pasv.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
	forms['pres.pasv.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
	forms['pres.pasv.p1.mf.pl'] = [('ن' + base, '-', '-')];

	return forms;
#}


def doubled_patt4_subjun(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	if r[1] == 'ن' :
		base_long = r[0] + r[1];
	else :
		base_long = r[0] + r[1] + r[1];


	if tv == 'iv' : #{
		forms['subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['subjun.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
		forms['subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['subjun.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
		forms['subjun.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['subjun.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['subjun.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['subjun.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];
	#}

	forms['subjun.pasv.p3.m.sg'] = [('ي' + base, '-', '-')];
	forms['subjun.pasv.p3.f.sg'] = [('ت' + base, '-', '-')];
	forms['subjun.pasv.p2.m.sg'] = [('ت' + base, '-', '-')];
	forms['subjun.pasv.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['subjun.pasv.p1.mf.sg'] = [('أ' + base, '-', '-')];

	forms['subjun.pasv.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
	forms['subjun.pasv.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
	forms['subjun.pasv.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

	forms['subjun.pasv.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['subjun.pasv.p3.f.pl'] = [('ي' + base_long + 'ن', '-', '-')];
	forms['subjun.pasv.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['subjun.pasv.p2.f.pl'] = [('ت' + base_long + 'ن', '-', '-')];
	forms['subjun.pasv.p1.mf.pl'] = [('ن' + base, '-', '-')];

	return forms;
#}


def doubled_patt4_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1];
	base_long = r[0] + r[1] + r[1];
	if r[1] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];


	if tv == 'iv' : #{
		forms['apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base_long, '-', 'LR')];
		forms['apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
		forms['apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
		forms['apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base_long, '-', 'LR')];

		forms['apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base_long, '-', 'LR')];
	#}
	else : #{
		forms['apocop.p3.m.sg'] = [('ي' + base, '-', '-'),
					   ('ي' + base_long, '-', 'LR'),
					   ('ي' + base, 'S__فتح/ه', '-'),
					   ('ي' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p3.f.sg'] = [('ت' + base, '-', '-'), 
					   ('ت' + base_long, '-', 'LR'),
					   ('ي' + base, 'S__فتح/ه', '-'),
					   ('ي' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p2.m.sg'] = [('ت' + base, '-', '-'),
					   ('ت' + base_long, '-', 'LR'),
					   ('ت' + base, 'S__فتح/ه', '-'),
					   ('ت' + base_long, 'S__فتح/ه', 'LR')];
		forms['apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'),
					   ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['apocop.p1.mf.sg'] = [('أ' + base, '-', '-'),
					    ('أ' + base_long, '-', 'LR'),
					    ('أ' + base, 'S__فتح/ه', '-'),
					    ('أ' + base_long, 'S__فتح/ه', 'LR')];
	
		forms['apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_long + 'ن', 'S__فتح/ه', '-')];
		forms['apocop.p1.mf.pl'] = [('ن' + base, '-', '-'),
					    ('ن' + base_long, '-', 'LR'),
					    ('ن' + base, 'S__فتح/ه', '-'),
					    ('ن' + base_long, 'S__فتح/ه', 'LR')];
	#}

	forms['apocop.pasv.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base_long, '-', 'LR')];
	forms['apocop.pasv.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
	forms['apocop.pasv.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base_long, '-', 'LR')];
	forms['apocop.pasv.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['apocop.pasv.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base_long, '-', 'LR')];

	forms['apocop.pasv.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
	forms['apocop.pasv.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
	forms['apocop.pasv.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

	forms['apocop.pasv.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['apocop.pasv.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
	forms['apocop.pasv.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['apocop.pasv.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
	forms['apocop.pasv.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base_long, '-', 'LR')];

	return forms;
#}


def doubled_patt4_imp(root, tv): #{
	r = root.split('-'); # radicals

	# passive voice?

	base = r[0] + r[1];
	base_long = r[0] + r[1] + r[1];
	if r[1] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];


	forms = {};

	if tv == 'iv' : #{
		forms['imp.p2.m.sg'] = [('أ' + base, '-', '-'), ('أ' + base_long, '-', 'LR')];
		forms['imp.p2.f.sg'] = [('أ' + base_long + 'ي', '-', '-')];
		forms['imp.p2.mf.du'] = [('أ' + base + 'ا', '-', '-')];
		forms['imp.p2.m.pl'] = [('أ' + base + 'وا', '-', '-')];
		forms['imp.p2.f.pl'] = [('أ' + base_n + 'ن', '-', '-')];
	#}
	else : #{
		forms['imp.p2.m.sg'] = [('أ' + base, '-', '-'),
					('أ' +  base_long, '-', 'LR'),
					('أ' + base, 'S__فتح/ه', '-'),
					('أ' + base_long, 'S__فتح/ه', 'LR')];
		forms['imp.p2.f.sg'] = [('أ' + base_long + 'ي', '-', '-'), ('أ' + base_long + 'ي', 'S__فتح/ه', '-')];
		forms['imp.p2.mf.du'] = [('أ' + base + 'ا', '-', '-'), ('أ' + base + 'ا', 'S__فتح/ه', '-')];
		forms['imp.p2.m.pl'] = [('أ' + base + 'وا', '-', '-'), ('أ' + base + 'و', 'S__فتح/ه', '-')];
		forms['imp.p2.f.pl'] = [('أ' + base_n + 'ن', '-', '-'), ('أ' + base_n + 'ن', 'S__فتح/ه', '-')];
	#}

	return forms ; 
#}


def doubled_patt4_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	if r[2] == 'ت' :
		base_t = r[0] + r[1];
	else :
		base_t = r[0] + r[1] + r[1];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[1];

	forms = {};

	if tv == 'iv' : #{
		forms['past.p3.m.sg'] = [('أ' + base, '-', '-')];
		forms['past.p3.f.sg'] = [('أ' + base + 'ت', '-', '-')];
		forms['past.p2.m.sg'] = [('أ' + base_t + 'ت', '-', '-')];
		forms['past.p2.f.sg'] = [('أ' + base_t + 'ت', '-', '-')];
		forms['past.p1.mf.sg'] = [('أ' + base_t + 'ت', '-', '-')];

		forms['past.p3.m.du'] = [('أ' + base + 'ا', '-', '-')];
		forms['past.p3.f.du'] = [('أ' + base + 'تا', '-', '-')];
		forms['past.p2.mf.du'] = [('أ' + base_t + 'تما', '-', '-')];

		forms['past.p3.m.pl'] = [('أ' + base + 'وا', '-', '-')];
		forms['past.p3.f.pl'] = [('أ' + base_n + 'ن', '-', '-')];
		forms['past.p2.m.pl'] = [('أ' + base_t + 'تم', '-', '-')];
		forms['past.p2.f.pl'] = [('أ' + base_t + 'تن', '-', '-')];
		forms['past.p1.mf.pl'] = [('أ' + base_n + 'نا', '-', '-')];
	#}
	else : #{
		forms['past.p3.m.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
		forms['past.p3.f.sg'] = [('أ' + base + 'ت', '-', '-'), ('أ' + base + 'ت', 'S__فتح/ه', '-')];
		forms['past.p2.m.sg'] = [('أ' + base_t + 'ت', '-', '-'), ('أ' + base_t + 'ت', 'S__فتح/ه', '-')];
		forms['past.p2.f.sg'] = [('أ' + base_t + 'ت', '-', '-'), ('أ' + base_t + 'ت', 'S__فتح/ه', '-')];
		forms['past.p1.mf.sg'] = [('أ' + base_t + 'ت', '-', '-'), ('أ' + base_t + 'ت', 'S__فتح/ه', '-')];

		forms['past.p3.m.du'] = [('أ' + base + 'ا', '-', '-'), ('أ' + base + 'ا', 'S__فتح/ه', '-')];
		forms['past.p3.f.du'] = [('أ' + base + 'تا', '-', '-'), ('أ' + base + 'تا', 'S__فتح/ه', '-')];
		forms['past.p2.mf.du'] = [('أ' + base_t + 'تما', '-', '-'), ('أ' + base_t + 'تما', 'S__فتح/ه', '-')];

		forms['past.p3.m.pl'] = [('أ' + base + 'وا', '-', '-'), ('أ' + base + 'و', 'S__فتح/ه', '-')];
		forms['past.p3.f.pl'] = [('أ' + base_n + 'ن', '-', '-'), ('أ' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['past.p2.m.pl'] = [('أ' + base_t + 'تم', '-', '-'), ('أ' + base_t + 'تمو', 'S__فتح/ه', '-')];
		forms['past.p2.f.pl'] = [('أ' + base_t + 'تن', '-', '-'), ('أ' + base_t + 'تن', 'S__فتح/ه', '-')];
		forms['past.p1.mf.pl'] = [('أ' + base_n + 'نا', '-', '-'), ('أ' + base_n + 'نا', 'S__فتح/ه', '-')];
	#}

	forms['past.pasv.p3.m.sg'] = [('أ' + base, '-', '-')];
	forms['past.pasv.p3.f.sg'] = [('أ' + base + 'ت', '-', '-')];
	forms['past.pasv.p2.m.sg'] = [('أ' + base_t + 'ت', '-', '-')];
	forms['past.pasv.p2.f.sg'] = [('أ' + base_t + 'ت', '-', '-')];
	forms['past.pasv.p1.mf.sg'] = [('أ' + base_t + 'ت', '-', '-')];

	forms['past.pasv.p3.m.du'] = [('أ' + base + 'ا', '-', '-')];
	forms['past.pasv.p3.f.du'] = [('أ' + base + 'تا', '-', '-')];
	forms['past.pasv.p2.mf.du'] = [('أ' + base_t + 'تما', '-', '-')];

	forms['past.pasv.p3.m.pl'] = [('أ' + base + 'وا', '-', '-')];
	forms['past.pasv.p3.f.pl'] = [('أ' + base_n + 'ن', '-', '-')];
	forms['past.pasv.p2.m.pl'] = [('أ' + base_t + 'تم', '-', '-')];
	forms['past.pasv.p2.f.pl'] = [('أ' + base_t + 'تن', '-', '-')];
	forms['past.pasv.p1.mf.pl'] = [('أ' + base_n + 'نا', '-', '-')];

	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(doubled_patt1_pres(stem['root'], stem['trans']));
		forms.update(doubled_patt1_subjun(stem['root'], stem['trans']));
		forms.update(doubled_patt1_apocop(stem['root'], stem['trans']));
		forms.update(doubled_patt1_imp(stem['root'], stem['trans']));
		forms.update(doubled_patt1_past(stem['root'], stem['trans']));
		forms.update(doubled_patt1_pprs(stem['root']));
		forms.update(doubled_patt1_pp(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(doubled_patt4_pres(stem['root'], stem['trans']));
		forms.update(doubled_patt4_subjun(stem['root'], stem['trans']));
		forms.update(doubled_patt4_apocop(stem['root'], stem['trans']));
		forms.update(doubled_patt4_imp(stem['root'], stem['trans']));
		forms.update(doubled_patt4_past(stem['root'], stem['trans']));
		forms.update(doubled_patt4_pprs(stem['root']));
		forms.update(doubled_patt4_pp(stem['root']));
	#}

	return forms;

#}

