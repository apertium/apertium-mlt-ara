#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## sound verbs
## ----------------------------------------------------------------------------##


def sound_past(base, base_t, base_n, tv): #{

	forms = {};

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', '-'), (base, 'S__فتح/ه', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', 'S__فتح/ه', '-')];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', 'S__فتح/ه', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', '-'), (base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', 'S__فتح/ه', '-')];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-'), (base_t + 'تما', 'S__فتح/ه', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', 'S__فتح/ه', '-')];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-'), (base_t + 'تمو', 'S__فتح/ه', '-')];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-'), (base_t + 'تن', 'S__فتح/ه', '-')];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-'), (base_n + 'نا', 'S__فتح/ه', '-')];


		forms['pasv.past.p3.m.sg'] = [(base, '-', '-')];
		forms['pasv.past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['pasv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-')];
		forms['pasv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-')];
		forms['pasv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-')];

		forms['pasv.past.p3.m.du'] = [(base + 'ا', '-', '-')];
		forms['pasv.past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['pasv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-')];

		forms['pasv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['pasv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-')];
		forms['pasv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-')];
		forms['pasv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-')];
		forms['pasv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-')];

	#}

	return forms;
#}


def sound_pres(base, base_n, tv): #{

	forms = {};

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];


		forms['pasv.pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['pasv.pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['pasv.pres.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['pasv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-')];
		forms['pasv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-')];
		forms['pasv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-')];

		forms['pasv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['pasv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['pasv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['pasv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['pasv.pres.p1.mf.pl'] = [('ن' + base, '-', '-')];

	#}

	return forms;
#}


def sound_subjun(base, base_n, tv): #{

	forms = {};

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];


		forms['pasv.subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['pasv.subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['pasv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['pasv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['pasv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['pasv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['pasv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['pasv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['pasv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['pasv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['pasv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-')];

	#}

	return forms;
#}


def sound_apocop(base, base_n, tv): #{

	forms = {};

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, 'S__فتح/ه', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, 'S__فتح/ه', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', 'S__فتح/ه', '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, 'S__فتح/ه', '-')];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', 'S__فتح/ه', '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', 'S__فتح/ه', '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', 'S__فتح/ه', '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, 'S__فتح/ه', '-')];


		forms['pasv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['pasv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['pasv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['pasv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['pasv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-')];
		forms['pasv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-')];
		forms['pasv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-')];

		forms['pasv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['pasv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-')];
		forms['pasv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['pasv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-')];
		forms['pasv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];

	#}

	return forms;
#}


def sound_imp(base, base_n, tv): #{

	# passive voice?

	forms = {};

	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-')];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-'), (base, 'S__فتح/ه', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', 'S__فتح/ه', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-'), (base + 'ا', 'S__فتح/ه', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', 'S__فتح/ه', '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', 'S__فتح/ه', '-')];
	#}

	return forms ; 
#}


## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def sound_patt1_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + r[1];
	else :
		base_t = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt1_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);


def sound_patt1_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt1_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);

#}


def sound_patt1_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ا' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ا' + r[0] + r[1];
	else :
		base_n = 'ا' + r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt1_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [(r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'و' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 2
## ----------------------------------------------------------------------------##


def sound_patt2_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + r[1];
	else :
		base_t = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt2_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);
#}


def sound_patt2_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt2_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);
#}


def sound_patt2_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt2_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt2_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 3
## ----------------------------------------------------------------------------##


def sound_patt3_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = r[0] + 'ا' + r[1];
	else :
		base_t = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt3_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	return sound_pres(base, base_n, tv);


def sound_patt3_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt3_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	return sound_apocop(base, base_n, tv);

#}


def sound_patt3_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt3_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt3_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 4
## ----------------------------------------------------------------------------##


def sound_patt4_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'أ' + r[0] + r[1];
	else :
		base_t = 'أ' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[0] + r[1];
	else :
		base_n = 'أ' + r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt4_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);


def sound_patt4_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt4_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);

#}


def sound_patt4_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[0] + r[1];
	else :
		base_n = 'أ' + r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt4_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 5
## ----------------------------------------------------------------------------##


def sound_patt5_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'ت' + r[0] + r[1];
	else :
		base_t = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt5_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);
#}


def sound_patt5_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt5_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);
#}


def sound_patt5_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt5_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


# rare
def sound_patt5_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 6
## ----------------------------------------------------------------------------##


def sound_patt6_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_t = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt6_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	return sound_pres(base, base_n, tv);


def sound_patt6_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt6_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	return sound_apocop(base, base_n, tv);

#}


def sound_patt6_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt6_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt6_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 7
## ----------------------------------------------------------------------------##


def sound_patt7_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ان' + r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'ان' + r[0] + r[1];
	else :
		base_t = 'ان' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ان' + r[0] + r[1];
	else :
		base_n = 'ان' + r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt7_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);
#}


def sound_patt7_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt7_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);
#}


def sound_patt7_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ان' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ان' + r[0] + r[1];
	else :
		base_n = 'ان' + r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt7_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('من' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('من' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('من' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('من' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


# very rare?
def sound_patt7_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('من' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('من' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('من' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('من' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## pattern 8
## ----------------------------------------------------------------------------##


def sound_patt8_past(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ا' + r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = 'ا' + r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = 'ا' + r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = 'ا' + r[0] + 'د';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt8_pres(root, tv): #{
	r = root.split('-'); # radicals

	base_start = r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = r[0] + 'د';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	return sound_pres(base, base_n, tv);
#}


def sound_patt8_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base_start = r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = r[0] + 'د';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	return sound_subjun(base, base_n, tv);
#}


def sound_patt8_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base_start = r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = r[0] + 'د';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	return sound_apocop(base, base_n, tv);
#}


def sound_patt8_imp(root, tv): #{
	r = root.split('-'); # radicals


	base_start = 'ا' + r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = 'ا' + r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = 'ا' + r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = 'ا' + r[0] + 'د';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	return sound_imp(base, base_n, tv); 
#}


def sound_patt8_pp(root): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ت' + r[1] + r[2];
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base = r[0] + r[1] + r[2];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base = r[0] + 'ط' + r[1] + r[2];
	elif (r[0] == 'ز') :
		base = r[0] + 'د' + r[1] + r[2];

	forms = {};

	forms['pp.m.sg'] = [('م' + base, '-', '-')] ;
	forms['pp.f.sg'] = [('م' + base + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + base + 'ات', '-', '-')] ;

	return forms;
#}


# very rare?
def sound_patt8_pprs(root): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ت' + r[1] + r[2];
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base = r[0] + r[1] + r[2];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base = r[0] + 'ط' + r[1] + r[2];
	elif (r[0] == 'ز') :
		base = r[0] + 'د' + r[1] + r[2];

	forms = {};

	forms['pp.m.sg'] = [('م' + base, '-', '-')] ;
	forms['pp.f.sg'] = [('م' + base + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + base + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## pattern 10
## ----------------------------------------------------------------------------##


def sound_patt10_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'است' + r[0] + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'است' + r[0] + r[1];
	else :
		base_t = 'است' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'است' + r[0] + r[1];
	else :
		base_n = 'است' + r[0] + r[1] + r[2];

	return sound_past(base, base_t, base_n, tv);
#}


def sound_patt10_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	return sound_pres(base, base_n, tv);
#}


def sound_patt10_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	return sound_subjun(base, base_n, tv);
#}


def sound_patt10_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	return sound_apocop(base, base_n, tv);
#}


def sound_patt10_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'است' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'است' + r[0] + r[1];
	else :
		base_n = 'است' + r[0] + r[1] + r[2];

	return sound_imp(base, base_n, tv); 
#}


def sound_patt10_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مست' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مست' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_patt10_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مست' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مست' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## main
## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(sound_patt1_past(stem['root'], stem['trans']));
		forms.update(sound_patt1_pres(stem['root'], stem['trans']));
		forms.update(sound_patt1_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt1_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt1_imp(stem['root'], stem['trans']));
		forms.update(sound_patt1_pp(stem['root']));
		forms.update(sound_patt1_pprs(stem['root']));
	#}
	elif stem['theme'] == '2' : #{
		forms.update(sound_patt2_past(stem['root'], stem['trans']));
		forms.update(sound_patt2_pres(stem['root'], stem['trans']));
		forms.update(sound_patt2_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt2_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt2_imp(stem['root'], stem['trans']));
		forms.update(sound_patt2_pp(stem['root']));
		forms.update(sound_patt2_pprs(stem['root']));
	#}
	elif stem['theme'] == '3' : #{
		forms.update(sound_patt3_past(stem['root'], stem['trans']));
		forms.update(sound_patt3_pres(stem['root'], stem['trans']));
		forms.update(sound_patt3_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt3_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt3_imp(stem['root'], stem['trans']));
		forms.update(sound_patt3_pp(stem['root']));
		forms.update(sound_patt3_pprs(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(sound_patt4_past(stem['root'], stem['trans']));
		forms.update(sound_patt4_pres(stem['root'], stem['trans']));
		forms.update(sound_patt4_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt4_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt4_imp(stem['root'], stem['trans']));
		forms.update(sound_patt4_pp(stem['root']));
		forms.update(sound_patt4_pprs(stem['root']));
	#}
	elif stem['theme'] == '5' : #{
		forms.update(sound_patt5_past(stem['root'], stem['trans']));
		forms.update(sound_patt5_pres(stem['root'], stem['trans']));
		forms.update(sound_patt5_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt5_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt5_imp(stem['root'], stem['trans']));
		forms.update(sound_patt5_pp(stem['root']));
		forms.update(sound_patt5_pprs(stem['root']));
	#}
	elif stem['theme'] == '6' : #{
		forms.update(sound_patt6_past(stem['root'], stem['trans']));
		forms.update(sound_patt6_pres(stem['root'], stem['trans']));
		forms.update(sound_patt6_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt6_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt6_imp(stem['root'], stem['trans']));
		forms.update(sound_patt6_pp(stem['root']));
		forms.update(sound_patt6_pprs(stem['root']));
	#}
	elif stem['theme'] == '7' : #{
		forms.update(sound_patt7_past(stem['root'], stem['trans']));
		forms.update(sound_patt7_pres(stem['root'], stem['trans']));
		forms.update(sound_patt7_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt7_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt7_imp(stem['root'], stem['trans']));
		forms.update(sound_patt7_pp(stem['root']));
		forms.update(sound_patt7_pprs(stem['root']));
	#}
	elif stem['theme'] == '10' : #{
		forms.update(sound_patt10_past(stem['root'], stem['trans']));
		forms.update(sound_patt10_pres(stem['root'], stem['trans']));
		forms.update(sound_patt10_subjun(stem['root'], stem['trans']));
		forms.update(sound_patt10_apocop(stem['root'], stem['trans']));
		forms.update(sound_patt10_imp(stem['root'], stem['trans']));
		forms.update(sound_patt10_pp(stem['root']));
		forms.update(sound_patt10_pprs(stem['root']));
	#}

	return forms;

#}

