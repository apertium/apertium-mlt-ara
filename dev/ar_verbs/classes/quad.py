#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## quad verbs
## ----------------------------------------------------------------------------##


# TODO : add past LR forms like أحبيت
def quad_past_actv(base, base_t, base_n, tv, r): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', r)];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', r)];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', r)];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', r)];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', r)];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', r)];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', r)];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', r)];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', r)];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', r)];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', r)];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', r)];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', r)];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base, '-', r), (base, paradigm, r)];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', r), (base + 'ت', paradigm, r)];
		forms['actv.past.p2.m.sg'] = [(base_t + 'ت', '-', r), (base_t + 'ت', paradigm, r)];
		forms['actv.past.p2.f.sg'] = [(base_t + 'ت', '-', r), (base_t + 'ت', paradigm, r)];
		forms['actv.past.p1.mf.sg'] = [(base_t + 'ت', '-', r), (base_t + 'ت', paradigm, r)];

		forms['actv.past.p3.m.du'] = [(base + 'ا', '-', r), (base + 'ا', paradigm, r)];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', r), (base + 'تا', paradigm, r)];
		forms['actv.past.p2.mf.du'] = [(base_t + 'تما', '-', r), (base_t + 'تما', paradigm, r)];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', r), (base + 'و', paradigm, r)];
		forms['actv.past.p3.f.pl'] = [(base_n + 'ن', '-', r), (base_n + 'ن', paradigm, r)];
		forms['actv.past.p2.m.pl'] = [(base_t + 'تم', '-', r), (base_t + 'تمو', paradigm, r)];
		forms['actv.past.p2.f.pl'] = [(base_t + 'تن', '-', r), (base_t + 'تن', paradigm, r)];
		forms['actv.past.p1.mf.pl'] = [(base_n + 'نا', '-', r), (base_n + 'نا', paradigm, r)];
	#}

	return forms;
#}


def quad_past_pasv(base, base_t, base_n, r): #{

	forms = {};

	forms['pasv.past.p3.m.sg'] = [(base, '-', r)];
	forms['pasv.past.p3.f.sg'] = [(base + 'ت', '-', r)];
	forms['pasv.past.p2.m.sg'] = [(base_t + 'ت', '-', r)];
	forms['pasv.past.p2.f.sg'] = [(base_t + 'ت', '-', r)];
	forms['pasv.past.p1.mf.sg'] = [(base_t + 'ت', '-', r)];
	forms['pasv.past.p3.m.du'] = [(base + 'ا', '-', r)];
	forms['pasv.past.p3.f.du'] = [(base + 'تا', '-', r)];
	forms['pasv.past.p2.mf.du'] = [(base_t + 'تما', '-', r)];

	forms['pasv.past.p3.m.pl'] = [(base + 'وا', '-', r)];
	forms['pasv.past.p3.f.pl'] = [(base_n + 'ن', '-', r)];
	forms['pasv.past.p2.m.pl'] = [(base_t + 'تم', '-', r)];
	forms['pasv.past.p2.f.pl'] = [(base_t + 'تن', '-', r)];
	forms['pasv.past.p1.mf.pl'] = [(base_n + 'نا', '-', r)];

	return forms;
#}


def quad_pres_actv(base, base_n, tv, r): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', r)];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', r)];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', r)];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', r)];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', r)];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', r)];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', r)];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', r)];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', r)];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', r)];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', r)];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', r), ('ي' + base, paradigm, r)];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm, r)];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm, r)];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', r), ('ت' + base + 'ي', paradigm, r)];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', r), ('أ' + base, paradigm, r)];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', r), ('ي' + base + 'ا', paradigm, r)];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', r), ('ت' + base + 'ا', paradigm, r)];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', r), ('ت' + base + 'ا', paradigm, r)];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', r), ('ي' + base + 'و', paradigm, r)];
		forms['actv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r), ('ي' + base_n + 'ن', paradigm, r)];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', r), ('ت' + base + 'و', paradigm, r)];
		forms['actv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r), ('ت' + base_n + 'ن', paradigm, r)];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base, '-', r), ('ن' + base, paradigm, r)];

	#}

	return forms;
#}


def quad_pres_pasv(base, base_n, r): #{

	forms = {};

	forms['pasv.pres.p3.m.sg'] = [('ي' + base, '-', r)];
	forms['pasv.pres.p3.f.sg'] = [('ت' + base, '-', r)];
	forms['pasv.pres.p2.m.sg'] = [('ت' + base, '-', r)];
	forms['pasv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', r)];
	forms['pasv.pres.p1.mf.sg'] = [('أ' + base, '-', r)];

	forms['pasv.pres.p3.m.du'] = [('ي' + base + 'ان', '-', r)];
	forms['pasv.pres.p3.f.du'] = [('ت' + base + 'ان', '-', r)];
	forms['pasv.pres.p2.mf.du'] = [('ت' + base + 'ان', '-', r)];

	forms['pasv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', r)];
	forms['pasv.pres.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
	forms['pasv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', r)];
	forms['pasv.pres.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
	forms['pasv.pres.p1.mf.pl'] = [('ن' + base, '-', r)];

	return forms;
#}



def quad_subjun_actv(base, base_n, tv, r): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', r)];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', r)];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', r)];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', r)];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', r)];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', r)];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', r)];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', r)];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', r)];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', r)];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', r)];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', r), ('ي' + base, paradigm, r)];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm, r)];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm, r)];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', r), ('ت' + base + 'ي', paradigm, r)];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', r), ('أ' + base, paradigm, r)];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', r), ('ي' + base + 'ا', paradigm, r)];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', r), ('ت' + base + 'ا', paradigm, r)];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', r), ('ت' + base + 'ا', paradigm, r)];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', r), ('ي' + base + 'و', paradigm, r)];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r), ('ي' + base_n + 'ن', paradigm, r)];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', r), ('ت' + base + 'و', paradigm, r)];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r), ('ت' + base_n + 'ن', paradigm, r)];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base, '-', r), ('ن' + base, paradigm, r)];
	#}

	return forms;
#}


def quad_subjun_pasv(base, base_n, r): #{

	forms = {};

	forms['pasv.subjun.p3.m.sg'] = [('ي' + base, '-', r)];
	forms['pasv.subjun.p3.f.sg'] = [('ت' + base, '-', r)];
	forms['pasv.subjun.p2.m.sg'] = [('ت' + base, '-', r)];
	forms['pasv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', r)];
	forms['pasv.subjun.p1.mf.sg'] = [('أ' + base, '-', r)];

	forms['pasv.subjun.p3.m.du'] = [('ي' + base + 'ا', '-', r)];
	forms['pasv.subjun.p3.f.du'] = [('ت' + base + 'ا', '-', r)];
	forms['pasv.subjun.p2.mf.du'] = [('ت' + base + 'ا', '-', r)];

	forms['pasv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', r)];
	forms['pasv.subjun.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
	forms['pasv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', r)];
	forms['pasv.subjun.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
	forms['pasv.subjun.p1.mf.pl'] = [('ن' + base, '-', r)];

	return forms;
#}



# TODO: add LR long forms
def quad_apocop_actv(base, base_n, suftype, tv, r): #{

	forms = {};

	paradigm = 'S__فتح/ه';
	paradigm_cons = 'S__فتح/ه';

	if suftype == 'n' :
		paradigm_cons = 'S__يلون/ه';
	elif suftype == 'k' :
		paradigm_cons = 'S__يترك/ه';
	elif suftype == 'h' :
		paradigm_cons = 'S__يشبه/ه';

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', r)];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', r)];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', r)];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', r)];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', r)];

		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', r)];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', r)];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', r)];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', r)];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', r)];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', r)];
	#}
	else : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', r), ('ي' + base, paradigm_cons, r)];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm_cons, r)];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', r), ('ت' + base, paradigm_cons, r)];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', r), ('ت' + base + 'ي', paradigm, r)];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', r), ('أ' + base, paradigm_cons, r)];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', r), ('ي' + base + 'ا', paradigm, r)];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', r), ('ت' + base + 'ا', paradigm, r)];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', r), ('ت' + base + 'ا', paradigm, r)];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', r), ('ي' + base + 'و', paradigm, r)];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r), ('ي' + base_n + 'ن', paradigm, r)];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', r), ('ت' + base + 'و', paradigm, r)];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r), ('ت' + base_n + 'ن', paradigm, r)];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', r), ('ن' + base, paradigm_cons, r)];
	#}

	return forms;
#}


def quad_apocop_pasv(base, base_n, r): #{

	forms = {};

	forms['pasv.apocop.p3.m.sg'] = [('ي' + base, '-', r)];
	forms['pasv.apocop.p3.f.sg'] = [('ت' + base, '-', r)];
	forms['pasv.apocop.p2.m.sg'] = [('ت' + base, '-', r)];
	forms['pasv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', r)];
	forms['pasv.apocop.p1.mf.sg'] = [('أ' + base, '-', r)];

	forms['pasv.apocop.p3.m.du'] = [('ي' + base + 'ا', '-', r)];
	forms['pasv.apocop.p3.f.du'] = [('ت' + base + 'ا', '-', r)];
	forms['pasv.apocop.p2.mf.du'] = [('ت' + base + 'ا', '-', r)];

	forms['pasv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', r)];
	forms['pasv.apocop.p3.f.pl'] = [('ي' + base_n + 'ن', '-', r)];
	forms['pasv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', r)];
	forms['pasv.apocop.p2.f.pl'] = [('ت' + base_n + 'ن', '-', r)];
	forms['pasv.apocop.p1.mf.pl'] = [('ن' + base, '-', r)];

	return forms;
#}



# TODO : add LR long forms
def quad_imp(base, base_n, suftype, tv, r): #{

	# passive voice?

	forms = {};

	paradigm = 'S__فتح/ه';
	paradigm_cons = 'S__فتح/ه';

	if suftype == 'n' :
		paradigm_cons = 'S__يلون/ه';
	elif suftype == 'k' :
		paradigm_cons = 'S__يترك/ه';
	elif suftype == 'h' :
		paradigm_cons = 'S__يشبه/ه';


	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', r)];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', r)];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', r)];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', r)];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', r)];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', r), (base, paradigm_cons, r)];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', r), (base + 'ي', paradigm, r)];
		forms['actv.imp.p2.mf.du'] = [(base + 'ا', '-', r), (base + 'ا', paradigm, r)];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', r), (base + 'و', paradigm, r)];
		forms['actv.imp.p2.f.pl'] = [(base_n + 'ن', '-', r), (base_n + 'ن', paradigm, r)];
	#}

	return forms ; 
#}



def quad_pprs(base, r): #{


	forms = {};

        forms['pprs.m.sg.nom'] = [(base, '-', r)] ;
        forms['pprs.m.sg.gen'] = [(base, '-', r)] ;
        forms['pprs.m.sg.acc'] = [(base + 'ا', '-', r)] ;
        forms['pprs.m.du.nom'] = [(base + 'ان', '-', r)] ;
        forms['pprs.m.du.gen'] = [(base + 'ين', '-', r)] ;
        forms['pprs.m.du.acc'] = [(base + 'ين', '-', r)] ;
        forms['pprs.m.pl.nom'] = [(base + 'ين', '-', r)] ;
        forms['pprs.m.pl.gen'] = [(base + 'ين', '-', r)] ;
        forms['pprs.m.pl.acc'] = [(base + 'ين', '-', r)] ;

        forms['pprs.f.sg.nom'] = [(base + 'ة', '-', r)] ;
        forms['pprs.f.sg.gen'] = [(base + 'ة', '-', r)] ;
        forms['pprs.f.sg.acc'] = [(base + 'ة', '-', r)] ;
        forms['pprs.f.du.nom'] = [(base + 'تان', '-', r)] ;
        forms['pprs.f.du.gen'] = [(base + 'تين', '-', r)] ;
        forms['pprs.f.du.acc'] = [(base + 'تين', '-', r)] ;
        forms['pprs.f.pl.nom'] = [(base + 'ات', '-', r)] ;
        forms['pprs.f.pl.gen'] = [(base + 'ات', '-', r)] ;
        forms['pprs.f.pl.acc'] = [(base + 'ات', '-', r)] ;

	return forms ; 
#}



def quad_pp(base, r): #{


	forms = {};

        forms['pp.m.sg.nom'] = [(base, '-', r)] ;
        forms['pp.m.sg.gen'] = [(base, '-', r)] ;
        forms['pp.m.sg.acc'] = [(base + 'ا', '-', r)] ;
        forms['pp.m.du.nom'] = [(base + 'ان', '-', r)] ;
        forms['pp.m.du.gen'] = [(base + 'ين', '-', r)] ;
        forms['pp.m.du.acc'] = [(base + 'ين', '-', r)] ;
        forms['pp.m.pl.nom'] = [(base + 'ين', '-', r)] ;
        forms['pp.m.pl.gen'] = [(base + 'ين', '-', r)] ;
        forms['pp.m.pl.acc'] = [(base + 'ين', '-', r)] ;

        forms['pp.f.sg.nom'] = [(base + 'ة', '-', r)] ;
        forms['pp.f.sg.gen'] = [(base + 'ة', '-', r)] ;
        forms['pp.f.sg.acc'] = [(base + 'ة', '-', r)] ;
        forms['pp.f.du.nom'] = [(base + 'تان', '-', r)] ;
        forms['pp.f.du.gen'] = [(base + 'تين', '-', r)] ;
        forms['pp.f.du.acc'] = [(base + 'تين', '-', r)] ;
        forms['pp.f.pl.nom'] = [(base + 'ات', '-', r)] ;
        forms['pp.f.pl.gen'] = [(base + 'ات', '-', r)] ;
        forms['pp.f.pl.acc'] = [(base + 'ات', '-', r)] ;

	return forms ; 
#}


## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def quad_patt1_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2] + r[3];

	if r[3] == 'ت' :
		base_t = r[0] + r[1] + r[2];
	else :
		base_t = r[0] + r[1] + r[2] + r[3];

	if r[3] == 'ن' :
		base_n = r[0] + r[1] + r[2];
	else :
		base_n = r[0] + r[1] + r[2] + r[3];

	forms = quad_past_actv(base, base_t, base_n, tv, '-');
	if (tv == 'tv') :
		forms.update(quad_past_pasv(base, base_t, base_n, '-'));

	return forms;
#}



def quad_patt1_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2] + r[3];

	if r[3] == 'ن' :
		base_n = r[0] + r[1] + r[2];
	else :
		base_n = r[0] + r[1] + r[2] + r[3];


        suftype = '-';
        if r[3] == 'ن' :
                suftype = 'n';
        elif r[3] == 'ك' :
                suftype = 'k';
        elif r[3] == 'ه' : 
                suftype = 'h'

	forms = quad_pres_actv(base, base_n, tv, '-');
	forms.update(quad_subjun_actv(base, base_n, tv, '-'));
	forms.update(quad_apocop_actv(base, base_n, suftype, tv, '-'));
	forms.update(quad_imp(base, base_n, suftype, tv, '-')); 
	if (tv == 'tv') : #{
		forms.update(quad_pres_pasv(base, base_n, '-'));
		forms.update(quad_subjun_pasv(base, base_n, '-'));
		forms.update(quad_apocop_pasv(base, base_n, '-'));
	#}
	
	return forms;
#}


def quad_patt1_part(root, tv): #{
	r = root.split('-'); # radicals

	base = 'م' + r[0] + r[1] + r[2] + r[3];

	forms = quad_pprs(base, '-');
	if tv == 'tv' :
		forms.update(quad_pp(base, '-'));

	return forms;
#}


## ----------------------------------------------------------------------------##
## main
## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(quad_patt1_past(stem['root'], stem['trans']));
		forms.update(quad_patt1_impf(stem['root'], stem['trans']));
		forms.update(quad_patt1_part(stem['root'], stem['trans']));
	#}

	return forms;

#}

