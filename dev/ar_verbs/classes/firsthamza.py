#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## first hamza verbs
## ----------------------------------------------------------------------------##


def firsthamza_past_actv(base, base_t, base_n, tv): #{

	forms = {};
        paradigm = 'S__فتح/ه';

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
		forms['actv.past.p3.m.sg'] = [(base, '-', '-'), (base, paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', '-'), (base_t + 'ت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', '-'), (base + 'ا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', '-'), (base_t + 'تما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', '-'), (base_t + 'تمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', '-'), (base_t + 'تن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', '-'), (base_n + 'نا', paradigm, '-')];
	#}

	return forms;
#}


def firsthamza_past_pasv(base, base_t, base_n): #{

	forms = {};

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

	return forms;
#}


def firsthamza_pres_actv(base, base_n, base_p1_sg, tv): #{

	forms = {};
        paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		if base_p1_sg == '' :
			forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-')];
		else:
			forms['actv.pres.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-')];


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
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		if base_p1_sg == '' :
			forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
		else :	
			forms['actv.pres.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-'), ('آ' + base_p1_sg, paradigm, '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];

	#}

	return forms;
#}



def firsthamza_pres_pasv(base, base_n): #{

	forms = {};

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

	return forms;
#}



def firsthamza_subjun_actv(base, base_n, base_p1_sg, subtype, tv): #{

	forms = {};

        paradigm = 'S__فتح/ه';
        paradigm_cons = 'S__فتح/ه';

        if subtype == 'n' :
                paradigm_cons = 'S__يلون/ه';
        elif subtype == 'k' :
                paradigm_cons = 'S__يترك/ه';
        elif subtype == 'h' :
                paradigm_cons = 'S__يشبه/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		if base_p1_sg == '' :
			forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-')];
		else:
			forms['actv.subjun.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-')];

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
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm_cons, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		if base_p1_sg == '' :
			forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm_cons, '-')];
		else :	
			forms['actv.subjun.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-'), ('آ' + base_p1_sg, paradigm_cons, '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm_cons, '-')];
	#}

	return forms;
#}


def firsthamza_subjun_pasv(base, base_n): #{

	forms = {};

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

	return forms;
#}


def firsthamza_apocop_actv(base, base_n, base_p1_sg, tv): #{

	forms = {};
        paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		if base_p1_sg == '' :
			forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];
		else :	
			forms['actv.apocop.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-')];

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
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		if base_p1_sg == '1' :
			forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
		else :	
			forms['actv.apocop.p1.mf.sg'] = [('آ' + base_p1_sg, '-', '-'), ('آ' + base_p1_sg, paradigm, '-')];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', '-'), ('ي' + base_n + 'ن', paradigm, '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', '-'), ('ت' + base_n + 'ن', paradigm, '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];
	#}

	return forms;
#}


def firsthamza_apocop_pasv(base, base_n): #{

	forms = {};

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

	return forms;
#}


def firsthamza_imp(base, base_n, subtype, tv): #{

	# passive voice?

	forms = {};

        paradigm = 'S__فتح/ه';
        paradigm_cons = 'S__فتح/ه';

        if subtype == 'n' :
                paradigm_cons = 'S__يلون/ه';
        elif subtype == 'k' :
                paradigm_cons = 'S__يترك/ه';
        elif subtype == 'h' :
                paradigm_cons = 'S__يشبه/ه';

	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-')];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-'), (base, paradigm_cons, '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', paradigm, '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', '-'), (base + 'ا', paradigm, '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', '-'), (base_n + 'ن', paradigm, '-')];
	#}

	return forms ; 
#}


## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def firsthamza_patt1_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'أ' + r[1];
	else :
		base_t = 'أ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') :
		forms.update(firsthamza_past_pasv(base, base_t, base_n));

	return forms;
#}


def firsthamza_patt1_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];
	base_p1_sg = r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];


	forms = firsthamza_pres_actv(base, base_n, base_p1_sg, tv);
	if (tv == 'tv') : #{
		base = 'ؤ' + r[1] + r[2];
		if r[2] == 'ن' :
			base_n = 'ؤ' + r[1];
		else :
			base_n = 'ؤ' + r[1] + r[2];
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt1_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];
	base_p1_sg = r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, base_p1_sg, subtype, tv);
	if (tv == 'tv') : #{
		base = 'ؤ' + r[1] + r[2];
		if r[2] == 'ن' :
			base_n = 'ؤ' + r[1];
		else :
			base_n = 'ؤ' + r[1] + r[2];

		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt1_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];
	base_p1_sg = r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, base_p1_sg, tv);
	if (tv == 'tv') : #{
		base = 'ؤ' + r[1] + r[2];
		if r[2] == 'ن' :
			base_n = 'ؤ' + r[1];
		else :
			base_n = 'ؤ' + r[1] + r[2];

		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt1_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels


	if (v[1] == 'a') or (v[1] == 'i') :
		vowel = '';
	else :
		vowel = '';


	if ((r[1] == 'خ') and (r[2] == 'ذ')) or ((r[1] == 'ك') and (r[2] == 'ل')) : # أخذ، أكل
		base = r[1] + r[2];
		base_n = r[1] + r[2];
	#}
	else : #{
		base = 'ا' + vowel + r[1] + r[2];
		if r[2] == 'ن' :
			base_n = 'ا' + vowel + r[1];
		else :
			base_n = 'ا' + vowel + r[1] + r[2];
	#}

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('آ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('آ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('آ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('آ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt1_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مأ' + r[1] + 'و' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مأ' + r[1] + 'و' + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مأ' + r[1] + 'و' + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مأ' + r[1] + 'و' + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 2
## ----------------------------------------------------------------------------##


def firsthamza_patt2_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'أ' + r[1];
	else :
		base_t = 'أ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') :
		forms.update(firsthamza_past_pasv(base, base_t, base_n));

	return forms;
#}


def firsthamza_patt2_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];
	base_p1_sg = 'أؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') :
		forms.update(firsthamza_pres_pasv(base, base_n));

	return forms;
#}


def firsthamza_patt2_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') :
		forms.update(firsthamza_subjun_pasv(base, base_n));

	return forms;
#}


def firsthamza_patt2_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') :
		forms.update(firsthamza_apocop_pasv(base, base_n));

	return forms;
#}


def firsthamza_patt2_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[1];
	else :
		base_n = 'أ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt2_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مؤ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مؤ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مؤ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مؤ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt2_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مؤ' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مؤ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مؤ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مؤ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 3
## ----------------------------------------------------------------------------##


def firsthamza_patt3_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'آ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'آ' + r[1];
	else :
		base_t = 'آ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'آ' + r[1];
	else :
		base_n = 'آ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'أو' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'أو' + r[1];
		else :
			base_t = 'أو' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'أو' + r[1];
		else :
			base_n = 'أو' + r[1] + r[2];

		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt3_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤا' + r[1];
	else :
		base_n = 'ؤا' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt3_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤا' + r[1];
	else :
		base_n = 'ؤا' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt3_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤا' + r[1];
	else :
		base_n = 'ؤا' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt3_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'آ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'آ' + r[1];
	else :
		base_n = 'آ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt3_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مؤا' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مؤا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مؤا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مؤا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt3_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مؤا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مؤا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مؤا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مؤا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 4
## ----------------------------------------------------------------------------##


def firsthamza_patt4_past(root, tv): #{
# same forms as first hamza patt 3
	r = root.split('-'); # radicals

	base = 'آ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'آ' + r[1];
	else :
		base_t = 'آ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'آ' + r[1];
	else :
		base_n = 'آ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'أو' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'أو' + r[1];
		else :
			base_t = 'أو' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'أو' + r[1];
		else :
			base_n = 'أو' + r[1] + r[2];

		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt4_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt4_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt4_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ؤ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ؤ' + r[1];
	else :
		base_n = 'ؤ' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt4_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'آ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'آ'  + r[1];
	else :
		base_n = 'آ'  + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مؤ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مؤ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مؤ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مؤ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt4_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مؤ' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مؤ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مؤ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مؤ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 5
## ----------------------------------------------------------------------------##


def firsthamza_patt5_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تأ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'تأ' + r[1];
	else :
		base_t = 'تأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تأ' + r[1];
	else :
		base_n = 'تأ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'تؤ' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'تؤ' + r[1];
		else :
			base_t = 'تؤ' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'تؤ' + r[1];
		else :
			base_n = 'تؤ' + r[1] + r[2];

		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt5_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تأ' + r[1];
	else :
		base_n = 'تأ' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt5_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تأ' + r[1];
	else :
		base_n = 'تأ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt5_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تأ' + r[1];
	else :
		base_n = 'تأ' + r[1] + r[2];

	forms = firsthamza_subjun_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt5_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تأ' + r[1];
	else :
		base_n = 'تأ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt5_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('متأ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('متأ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('متأ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('متأ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


# rare
def firsthamza_patt5_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('متأ' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('متأ' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('متأ' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('متأ' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 6
## ----------------------------------------------------------------------------##


def firsthamza_patt6_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تآ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'تآ' + r[1];
	else :
		base_t = 'تآ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تآ' + r[1];
	else :
		base_n = 'تآ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'تؤو' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'تؤو' + r[1];
		else :
			base_t = 'تؤو' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'تؤو' + r[1];
		else :
			base_n = 'تؤو' + r[1] + r[2];

		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt6_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تآ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تآ' + r[1];
	else :
		base_n = 'تآ' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt6_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تآ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تآ' + r[1];
	else :
		base_n = 'تآ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt6_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تآ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تآ' + r[1];
	else :
		base_n = 'تآ' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt6_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'تآ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'تآ' + r[1];
	else :
		base_n = 'تآ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt6_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('متآ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('متآ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('متآ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('متآ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt6_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('متآ' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('متآ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('متآ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('متآ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 7 - does not exist for first hamza verbs
## ----------------------------------------------------------------------------##


## ----------------------------------------------------------------------------##
## pattern 8
## ----------------------------------------------------------------------------##


def firsthamza_patt8_past(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ات';
# if what?	if () :
#		base_start = 'ائ';

	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt8_pres(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ت';
# if what?	if () :
#		base_start = 'أ';

	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt8_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ت';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';


	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt8_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ت';
	
	base = base_start + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = base_start + r[1];
	else :
		base_t = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];


	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt8_imp(root, tv): #{
	r = root.split('-'); # radicals


	base_start = 'ات';
	base = base_start + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = base_start + r[1];
	else :
		base_n = base_start + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt8_pprs(root): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[1] + r[2];

	forms = {};

	forms['pprs.m.sg'] = [('م' + base, '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + base + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + base + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt8_pp(root): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[1] + r[2];

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


def firsthamza_patt10_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'استأ' + r[1] + r[2];

	if r[2] == 'ت' :
		base_t = 'استأ' + r[1];
	else :
		base_t = 'استأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'استأ' + r[1];
	else :
		base_n = 'استأ' + r[1] + r[2];

	forms = firsthamza_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{

		base = 'استؤ' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'استؤ' + r[1];
		else :
			base_t = 'استؤ' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'استؤ' + r[1];
		else :
			base_n = 'استؤ' + r[1] + r[2];

		forms.update(firsthamza_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firsthamza_patt10_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ستأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ستأ' + r[1];
	else :
		base_n = 'ستأ' + r[1] + r[2];

	forms = firsthamza_pres_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt10_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ستأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ستأ' + r[1];
	else :
		base_n = 'ستأ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	forms = firsthamza_subjun_actv(base, base_n, '', subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt10_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ستأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ستأ' + r[1];
	else :
		base_n = 'ستأ' + r[1] + r[2];

	forms = firsthamza_apocop_actv(base, base_n, '', tv);
	if (tv == 'tv') : #{
		forms.update(firsthamza_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firsthamza_patt10_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'استأ' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'استأ' + r[1];
	else :
		base_n = 'استأ' + r[1] + r[2];

        subtype = '-';
        if r[2] == 'ن' :
                subtype = 'n';
        elif r[2] == 'ك' :
                subtype = 'k';
        if r[2] == 'ه' : 
                subtype = 'h';

	return firsthamza_imp(base, base_n, subtype, tv); 
#}


def firsthamza_patt10_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مستأ' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مستأ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مستأ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مستأ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firsthamza_patt10_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مستأ' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('مستأ' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('مستأ' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مستأ' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## main
## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(firsthamza_patt1_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt1_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt1_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt1_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt1_imp(stem['root'], stem['vowels_impf'], stem['trans']));
		forms.update(firsthamza_patt1_pp(stem['root']));
		forms.update(firsthamza_patt1_pprs(stem['root']));
	#}
	elif stem['theme'] == '2' : #{
		forms.update(firsthamza_patt2_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt2_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt2_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt2_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt2_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt2_pp(stem['root']));
		forms.update(firsthamza_patt2_pprs(stem['root']));
	#}
	elif stem['theme'] == '3' : #{
		forms.update(firsthamza_patt3_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt3_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt3_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt3_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt3_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt3_pp(stem['root']));
		forms.update(firsthamza_patt3_pprs(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(firsthamza_patt4_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt4_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt4_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt4_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt4_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt4_pp(stem['root']));
		forms.update(firsthamza_patt4_pprs(stem['root']));
	#}
	elif stem['theme'] == '5' : #{
		forms.update(firsthamza_patt5_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt5_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt5_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt5_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt5_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt5_pp(stem['root']));
		forms.update(firsthamza_patt5_pprs(stem['root']));
	#}
	elif stem['theme'] == '6' : #{
		forms.update(firsthamza_patt6_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt6_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt6_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt6_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt6_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt6_pp(stem['root']));
		forms.update(firsthamza_patt6_pprs(stem['root']));
	#}
	elif stem['theme'] == '8' : #{
		forms.update(firsthamza_patt8_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt8_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt8_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt8_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt8_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt8_pp(stem['root']));
		forms.update(firsthamza_patt8_pprs(stem['root']));
	#}
	elif stem['theme'] == '10' : #{
		forms.update(firsthamza_patt10_past(stem['root'], stem['trans']));
		forms.update(firsthamza_patt10_pres(stem['root'], stem['trans']));
		forms.update(firsthamza_patt10_subjun(stem['root'], stem['trans']));
		forms.update(firsthamza_patt10_apocop(stem['root'], stem['trans']));
		forms.update(firsthamza_patt10_imp(stem['root'], stem['trans']));
		forms.update(firsthamza_patt10_pp(stem['root']));
		forms.update(firsthamza_patt10_pprs(stem['root']));
	#}

	return forms;

#}

