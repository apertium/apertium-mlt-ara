#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## sound verbs
## ----------------------------------------------------------------------------##


def sound_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [(r[0] + 'ا' + r[1] + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + 'ا' + r[1] + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [(r[0] + 'ا' + r[1] + r[2] + 'ات', '-', '-')] ;

	return forms;
#}


def sound_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'و' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'و' + r[2] + 'ات', '-', '-')] ;

	return forms;

#}


def sound_pres_tv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pres.p3.m.sg'] = [('ي' + r[0] + r[1] + r[2], '-', '-'), ('ي' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];
	forms['pres.p3.f.sg'] = [('ت' + r[0] + r[1] + r[2], '-', '-'), ('ت' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];
	forms['pres.p2.m.sg'] = [('ت' + r[0] + r[1] + r[2], '-', '-'), ('ت' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];
	forms['pres.p2.f.sg'] = [('ت' + r[0] + r[1] + r[2] + 'ين', '-', '-'), ('ت' + r[0] + r[1] + r[2] + 'ي', 'S__فتح/ه', '-')];
	forms['pres.p1.mf.sg'] = [('أ' + r[0] + r[1] + r[2], '-', '-'), ('أ' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];

	forms['pres.p3.m.du'] = [('ي' + r[0] + r[1] + r[2] + 'ان', '-', '-'), ('ي' + r[0] + r[1] + r[2] + 'ا', 'S__فتح/ه', '-')];
	forms['pres.p3.f.du'] = [('ت' + r[0] + r[1] + r[2] + 'ان', '-', '-'), ('ت' + r[0] + r[1] + r[2] + 'ا', 'S__فتح/ه', '-')];
	forms['pres.p2.mf.du'] = [('ت' + r[0] + r[1] + r[2] + 'ان', '-', '-'), ('ت' + r[0] + r[1] + r[2] + 'ا', 'S__فتح/ه', '-')];

	forms['pres.p3.m.pl'] = [('ي' + r[0] + r[1] + r[2] + 'ون', '-', '-'), ('ي' + r[0] + r[1] + r[2] + 'و', 'S__فتح/ه', '-')];
	forms['pres.p3.f.pl'] = [('ي' + r[0] + r[1] + r[2] + 'ن', '-', '-'), ('ي' + r[0] + r[1] + r[2] + 'ن', 'S__فتح/ه', '-')];
	forms['pres.p2.m.pl'] = [('ت' + r[0] + r[1] + r[2] + 'ون', '-', '-'), ('ت' + r[0] + r[1] + r[2] + 'و', 'S__فتح/ه', '-')];
	forms['pres.p2.f.pl'] = [('ت' + r[0] + r[1] + r[2] + 'ن', '-', '-'), ('ت' + r[0] + r[1] + r[2] + 'ن', 'S__فتح/ه', '-')];
	forms['pres.p1.mf.pl'] = [('ن' + r[0] + r[1] + r[2], '-', '-'), ('ن' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];

	return forms;
#}



def sound_pres_iv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pres.p3.m.sg'] = [('ي' + r[0] + r[1] + r[2], '-', '-')];
	forms['pres.p3.f.sg'] = [('ت' + r[0] + r[1] + r[2], '-', '-')];
	forms['pres.p2.m.sg'] = [('ت' + r[0] + r[1] + r[2], '-', '-')];
	forms['pres.p2.f.sg'] = [('ت' + r[0] + r[1] + r[2] + 'ين', '-', '-')];
	forms['pres.p1.mf.sg'] = [('أ' + r[0] + r[1] + r[2], '-', '-')];

	forms['pres.p3.m.du'] = [('ي' + r[0] + r[1] + r[2] + 'ان', '-', '-')];
	forms['pres.p3.f.du'] = [('ت' + r[0] + r[1] + r[2] + 'ان', '-', '-')];
	forms['pres.p2.mf.du'] = [('ت' + r[0] + r[1] + r[2] + 'ان', '-', '-')];

	forms['pres.p3.m.pl'] = [('ي' + r[0] + r[1] + r[2] + 'ون', '-', '-')];
	forms['pres.p3.f.pl'] = [('ي' + r[0] + r[1] + r[2] + 'ن', '-', '-')];
	forms['pres.p2.m.pl'] = [('ت' + r[0] + r[1] + r[2] + 'ون', '-', '-')];
	forms['pres.p2.f.pl'] = [('ت' + r[0] + r[1] + r[2] + 'ن', '-', '-')];
	forms['pres.p1.mf.pl'] = [('ن' + r[0] + r[1] + r[2], '-', '-')];

	return forms;
#}



def sound_imp_tv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['imp.p2.m.sg'] = [('ا' + r[0] + r[1] + r[2], '-', '-'), ('ا' + r[0] + r[1] + r[2], 'S__فتح/ه', '-')];
	forms['imp.p2.f.sg'] = [('ا' + r[0] + r[1] + r[2] + 'ي', '-', '-'), ('ا' + r[0] + r[1] + r[2] + 'ي', 'S__فتح/ه', '-')];
	forms['imp.p2.mf.du'] = [('ا' + r[0] + r[1] + r[2] + 'ا', '-', '-'), ('ا' + r[0] + r[1] + r[2] + 'ا', 'S__فتح/ه', '-')];
	forms['imp.p2.m.pl'] = [('ا' + r[0] + r[1] + r[2] + 'وا', '-', '-'), ('ا' + r[0] + r[1] + r[2] + 'و', 'S__فتح/ه', '-')];
	forms['imp.p2.f.pl'] = [('ا' + r[0] + r[1] + r[2] + 'ن', '-', '-'), ('ا' + r[0] + r[1] + r[2] + 'ن', 'S__فتح/ه', '-')];

	return forms ; 
#}


def sound_imp_iv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['imp.p2.m.sg'] = [('ا' + r[0] + r[1] + r[2], '-', '-')];
	forms['imp.p2.f.sg'] = [('ا' + r[0] + r[1] + r[2] + 'ي', '-', '-')];
	forms['imp.p2.mf.du'] = [('ا' + r[0] + r[1] + r[2] + 'ا', '-', '-')];
	forms['imp.p2.m.pl'] = [('ا' + r[0] + r[1] + r[2] + 'وا', '-', '-')];
	forms['imp.p2.f.pl'] = [('ا' + r[0] + r[1] + r[2] + 'ن', '-', '-')];

	return forms ; 
#}


def sound_past_tv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['past.p3.m.sg'] = [(r[0] + r[1] + r[2], '-', '-'), (r[0] + r[1] + r[2], 'S__فتح/ه', '-')];
	forms['past.p3.f.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-'), (r[0] + r[1] + r[2] + 'ت', 'S__فتح/ه', '-')];
	forms['past.p2.m.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-'), (r[0] + r[1] + r[2] + 'ت', 'S__فتح/ه', '-')];
	forms['past.p2.f.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-'), (r[0] + r[1] + r[2] + 'ت', 'S__فتح/ه', '-')];
	forms['past.p1.mf.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-'), (r[0] + r[1] + r[2] + 'ت', 'S__فتح/ه', '-')];

	forms['past.p3.m.du'] = [(r[0] + r[1] + r[2] + 'ا', '-', '-'), (r[0] + r[1] + r[2] + 'ا', 'S__فتح/ه', '-')];
	forms['past.p3.f.du'] = [(r[0] + r[1] + r[2] + 'تا', '-', '-'), (r[0] + r[1] + r[2] + 'تا', 'S__فتح/ه', '-')];
	forms['past.p2.mf.du'] = [(r[0] + r[1] + r[2] + 'تما', '-', '-'), (r[0] + r[1] + r[2] + 'تما', 'S__فتح/ه', '-')];

	forms['past.p3.m.pl'] = [(r[0] + r[1] + r[2] + 'وا', '-', '-'), (r[0] + r[1] + r[2] + 'و', 'S__فتح/ه', '-')];
	forms['past.p3.f.pl'] = [(r[0] + r[1] + r[2] + 'ن', '-', '-'), (r[0] + r[1] + r[2] + 'ن', 'S__فتح/ه', '-')];
	forms['past.p2.m.pl'] = [(r[0] + r[1] + r[2] + 'تم', '-', '-'), (r[0] + r[1] + r[2] + 'تمو', 'S__فتح/ه', '-')];
	forms['past.p2.f.pl'] = [(r[0] + r[1] + r[2] + 'تن', '-', '-'), (r[0] + r[1] + r[2] + 'تن', 'S__فتح/ه', '-')];
	forms['past.p1.mf.pl'] = [(r[0] + r[1] + r[2] + 'نا', '-', '-'), (r[0] + r[1] + r[2] + 'نا', 'S__فتح/ه', '-')];

	return forms;
#}


def sound_past_iv(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['past.p3.m.sg'] = [(r[0] + r[1] + r[2], '-', '-')];
	forms['past.p3.f.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-')];
	forms['past.p2.m.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-')];
	forms['past.p2.f.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-')];
	forms['past.p1.mf.sg'] = [(r[0] + r[1] + r[2] + 'ت', '-', '-')];

	forms['past.p3.m.du'] = [(r[0] + r[1] + r[2] + 'ا', '-', '-')];
	forms['past.p3.f.du'] = [(r[0] + r[1] + r[2] + 'تا', '-', '-')];
	forms['past.p2.mf.du'] = [(r[0] + r[1] + r[2] + 'تما', '-', '-')];

	forms['past.p3.m.pl'] = [(r[0] + r[1] + r[2] + 'وا', '-', '-')];
	forms['past.p3.f.pl'] = [(r[0] + r[1] + r[2] + 'ن', '-', '-')];
	forms['past.p2.m.pl'] = [(r[0] + r[1] + r[2] + 'تم', '-', '-')];
	forms['past.p2.f.pl'] = [(r[0] + r[1] + r[2] + 'تن', '-', '-')];
	forms['past.p1.mf.pl'] = [(r[0] + r[1] + r[2] + 'نا', '-', '-')];

	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		
		if stem['trans'] == 'tv' : #{
			forms.update(sound_past_tv(stem['root']));
			forms.update(sound_pres_tv(stem['root']));
			forms.update(sound_imp_tv(stem['root']));
		#}
		else : #{
			forms.update(sound_past_iv(stem['root']));
			forms.update(sound_pres_iv(stem['root']));
			forms.update(sound_imp_iv(stem['root']));
		#}
 
		forms.update(sound_pprs(stem['root']));
		forms.update(sound_pp(stem['root']));

	#}

	return forms;

#}

