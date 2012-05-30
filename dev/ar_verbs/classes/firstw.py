#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## first و verbs
## ----------------------------------------------------------------------------##


def firstw_past_actv(base, base_t, base_n, tv): #{

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


def firstw_past_pasv(base, base_t, base_n): #{

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


def firstw_pres_actv(base, base_n, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

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
		forms['actv.pres.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
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



def firstw_pres_pasv(base, base_n): #{

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



def firstw_subjun_actv(base, base_n, subtype, tv): #{

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
		forms['actv.subjun.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm_cons, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm_cons, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm_cons, '-')];
	
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


def firstw_subjun_pasv(base, base_n): #{

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


def firstw_apocop_actv(base, base_n, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

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
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
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


def firstw_apocop_pasv(base, base_n): #{

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


def firstw_imp(base, base_n, subtype, tv): #{

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


def firstw_patt1_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') :
		forms.update(firstw_past_pasv(base, base_t, base_n));

	return forms;
#}


def firstw_patt1_pres(root, subtype, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); #vowels

	suftype = '-';
	if r[2] == 'ن' :
		suftype = 'n';
	elif r[2] == 'ك' :
		suftype = 'k';
	if r[2] == 'ه' : 
		suftype = 'h';

	if subtype == 'و' : #{
		base = r[0] + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + r[1];
		else :
			base_n = r[0] + r[1] + r[2];
	#}
	else : #{
		base = r[1] + r[2];

		if r[2] == 'ن' :
			base_n = r[1];
		else :
			base_n = r[1] + r[2];
	#}

	forms = firstw_pres_actv(base, base_n, tv);
	forms.update(firstw_subjun_actv(base, base_n, suftype, tv));
	forms.update(firstw_apocop_actv(base, base_n, tv));

	if subtype == 'و' : #{

		if (v[1] == 'a') or (v[1] == 'i') :
			imp_pref = 'اي';
		else : 
			imp_pref = 'او';

		base = imp_pref + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = imp_pref + r[1];
		else :
			base_n = imp_pref + r[1] + r[2];
	#}
	else : #{
		base = r[1] + r[2];

		if r[2] == 'ن' :
			base_n = r[1];
		else :
			base_n = r[1] + r[2];
	#}

	forms.update(firstw_imp(base, base_n, suftype, tv)); 


	if (tv == 'tv') :
		forms.update(firstw_pres_pasv(base, base_n));
		forms.update(firstw_subjun_pasv(base, base_n));
		forms.update(firstw_apocop_pasv(base, base_n));

	return forms;
#}


def firstw_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [(r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [(r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt1_pp(root): #{
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


def firstw_patt2_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') :
		forms.update(firstw_past_pasv(base, base_t, base_n));

	return forms;
#}


def firstw_patt2_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') :
		forms.update(firstw_pres_pasv(base, base_n));

	return forms;
#}


def firstw_patt2_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') :
		forms.update(firstw_subjun_pasv(base, base_n));

	return forms;
#}


def firstw_patt2_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') :
		forms.update(firstw_apocop_pasv(base, base_n));

	return forms;
#}


def firstw_patt2_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt2_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt2_pp(root): #{
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


def firstw_patt3_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = r[0] + 'و' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = r[0] + 'و' + r[1];
		else :
			base_t = r[0] + 'و' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = r[0] + 'و' + r[1];
		else :
			base_n = r[0] + 'و' + r[1] + r[2];

		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt3_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt3_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt3_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt3_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + 'ا' + r[1];
	else :
		base_n = r[0] + 'ا' + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt3_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt3_pp(root): #{
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


def firstw_patt4_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt4_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt4_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt4_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = r[0] + r[1];
	else :
		base_n = r[0] + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt4_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'أ' + r[0] + r[1];
	else :
		base_n = 'أ' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt4_pp(root): #{
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


def firstw_patt5_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt5_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt5_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt5_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt5_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + r[1];
	else :
		base_n = 'ت' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt5_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مت' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مت' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مت' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


# rare
def firstw_patt5_pp(root): #{
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


def firstw_patt6_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		base = 'ت' + r[0] + 'و' + r[1] + r[2];

		if r[2] == 'ت' :
			base_t = 'ت' + r[0] + 'و' + r[1];
		else :
			base_t = 'ت' + r[0] + 'و' + r[1] + r[2];

		if r[2] == 'ن' :
			base_n = 'ت' + r[0] + 'و' + r[1];
		else :
			base_n = 'ت' + r[0] + 'و' + r[1] + r[2];

		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt6_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt6_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt6_apocop(root, tv): #{
	r = root.split('-'); # radicals

	forms = {};

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt6_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ت' + r[0] + 'ا' + r[1];
	else :
		base_n = 'ت' + r[0] + 'ا' + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt6_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مت' + r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt6_pp(root): #{
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


def firstw_patt7_past(root, tv): #{
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

	return firstw_past_actv(base, base_t, base_n, tv);

	return forms;
#}


def firstw_patt7_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];


	return firstw_pres_actv(base, base_n, tv);
#}


def firstw_patt7_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_subjun_actv(base, base_n, subtype, tv);
#}


def firstw_patt7_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ن' + r[0] + r[1];
	else :
		base_n = 'ن' + r[0] + r[1] + r[2];

	return firstw_apocop_actv(base, base_n, tv);
#}


def firstw_patt7_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ان' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ان' + r[0] + r[1];
	else :
		base_n = 'ان' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt7_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('من' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('من' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('من' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('من' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


## ----------------------------------------------------------------------------##
## pattern 8
## ----------------------------------------------------------------------------##


def firstw_patt8_past(root, tv): #{
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


	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt8_pres(root, tv): #{
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

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt8_subjun(root, tv): #{
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

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt8_apocop(root, tv): #{
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


	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt8_imp(root, tv): #{
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

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt8_pprs(root): #{
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

	forms['pprs.m.sg'] = [('م' + base, '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + base + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + base + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt8_pp(root): #{
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


def firstw_patt10_past(root, tv): #{
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

	forms = firstw_past_actv(base, base_t, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_past_pasv(base, base_t, base_n));
	#}

	return forms;
#}


def firstw_patt10_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	forms = firstw_pres_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_pres_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt10_subjun(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	forms = firstw_subjun_actv(base, base_n, subtype, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_subjun_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt10_apocop(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'ست' + r[0] + r[1];
	else :
		base_n = 'ست' + r[0] + r[1] + r[2];

	forms = firstw_apocop_actv(base, base_n, tv);
	if (tv == 'tv') : #{
		forms.update(firstw_apocop_pasv(base, base_n));
	#}

	return forms;
#}


def firstw_patt10_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = 'است' + r[0] + r[1] + r[2];

	if r[2] == 'ن' :
		base_n = 'است' + r[0] + r[1];
	else :
		base_n = 'است' + r[0] + r[1] + r[2];

	subtype = '-';
	if r[2] == 'ن' :
		subtype = 'n';
	elif r[2] == 'ك' :
		subtype = 'k';
	if r[2] == 'ه' : 
		subtype = 'h';

	return firstw_imp(base, base_n, subtype, tv); 
#}


def firstw_patt10_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مست' + r[0] + r[1] + r[2], '-', '-')] ;
	forms['pprs.f.sg'] = [('مست' + r[0] + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pprs.m.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مست' + r[0] + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def firstw_patt10_pp(root): #{
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
		forms.update(firstw_patt1_past(stem['root'], stem['trans']));
		forms.update(firstw_patt1_pres(stem['root'], stem['subtype'], stem['vowels_impf'], stem['trans']));
		forms.update(firstw_patt1_pp(stem['root']));
		forms.update(firstw_patt1_pprs(stem['root']));
	#}
	elif stem['theme'] == '2' : #{
		forms.update(firstw_patt2_past(stem['root'], stem['trans']));
		forms.update(firstw_patt2_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt2_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt2_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt2_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt2_pp(stem['root']));
		forms.update(firstw_patt2_pprs(stem['root']));
	#}
	elif stem['theme'] == '3' : #{
		forms.update(firstw_patt3_past(stem['root'], stem['trans']));
		forms.update(firstw_patt3_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt3_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt3_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt3_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt3_pp(stem['root']));
		forms.update(firstw_patt3_pprs(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(firstw_patt4_past(stem['root'], stem['trans']));
		forms.update(firstw_patt4_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt4_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt4_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt4_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt4_pp(stem['root']));
		forms.update(firstw_patt4_pprs(stem['root']));
	#}
	elif stem['theme'] == '5' : #{
		forms.update(firstw_patt5_past(stem['root'], stem['trans']));
		forms.update(firstw_patt5_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt5_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt5_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt5_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt5_pp(stem['root']));
		forms.update(firstw_patt5_pprs(stem['root']));
	#}
	elif stem['theme'] == '6' : #{
		forms.update(firstw_patt6_past(stem['root'], stem['trans']));
		forms.update(firstw_patt6_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt6_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt6_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt6_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt6_pp(stem['root']));
		forms.update(firstw_patt6_pprs(stem['root']));
	#}
	elif stem['theme'] == '7' : #{
		forms.update(firstw_patt7_past(stem['root'], stem['trans']));
		forms.update(firstw_patt7_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt7_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt7_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt7_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt7_pprs(stem['root']));
	#}
	elif stem['theme'] == '8' : #{
		forms.update(firstw_patt8_past(stem['root'], stem['trans']));
		forms.update(firstw_patt8_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt8_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt8_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt8_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt8_pp(stem['root']));
		forms.update(firstw_patt8_pprs(stem['root']));
	#}
	elif stem['theme'] == '10' : #{
		forms.update(firstw_patt10_past(stem['root'], stem['trans']));
		forms.update(firstw_patt10_pres(stem['root'], stem['trans']));
		forms.update(firstw_patt10_subjun(stem['root'], stem['trans']));
		forms.update(firstw_patt10_apocop(stem['root'], stem['trans']));
		forms.update(firstw_patt10_imp(stem['root'], stem['trans']));
		forms.update(firstw_patt10_pp(stem['root']));
		forms.update(firstw_patt10_pprs(stem['root']));
	#}

	return forms;

#}

