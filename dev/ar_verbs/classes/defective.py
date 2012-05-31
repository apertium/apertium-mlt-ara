#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## defective verbs
## ----------------------------------------------------------------------------##


# دعا type
def defective_past_wa_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ا', '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'وت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'وت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'وت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'وتما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ون', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'وتم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'وتن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ونا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ا', '-', '-'), (base + 'ا', paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'وا', '-', '-'), (base + 'وا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'وتما', '-', '-'), (base + 'وتما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ون', '-', '-'), (base + 'ون', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'وتم', '-', '-'), (base + 'وتمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'وتن', '-', '-'), (base + 'وتن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ونا', '-', '-'), (base + 'ونا', paradigm, '-')];
	#}

	return forms;
#}



# سرو type
def defective_past_ww_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base + 'و', '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'وت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'وت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'وت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'وت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'وتا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'وتما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ون', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'وتم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'وتن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ونا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base + 'و', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'وت', '-', '-'), (base + 'وت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'وا', '-', '-'), (base + 'وا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'وتا', '-', '-'), (base + 'وتا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'وتما', '-', '-'), (base + 'وتما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ون', '-', '-'), (base + 'ون', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'وتم', '-', '-'), (base + 'وتمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'وتن', '-', '-'), (base + 'وتن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ونا', '-', '-'), (base + 'ونا', paradigm, '-')];
	#}

	return forms;
#}



# رمى type
def defective_past_ya_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ى', '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'يت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'يت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'يت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'يا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'يتما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ين', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'يتم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'يتن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ينا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ى', '-', '-'), (base + 'ى', paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'ت', '-', '-'), (base + 'ت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'يا', '-', '-'), (base + 'يا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'تا', '-', '-'), (base + 'تا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'يتما', '-', '-'), (base + 'يتما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ين', '-', '-'), (base + 'ين', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'يتم', '-', '-'), (base + 'يتمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'يتن', '-', '-'), (base + 'يتن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ينا', '-', '-'), (base + 'ينا', paradigm, '-')];
	#}

	return forms;
#}



# لقي type
def defective_past_yy_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'يت', '-', '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'يت', '-', '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'يت', '-', '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'يت', '-', '-')];

		forms['actv.past.p3.m.du'] = [(base + 'يا', '-', '-')];
		forms['actv.past.p3.f.du'] = [(base + 'يتا', '-', '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'يتما', '-', '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ين', '-', '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'يتم', '-', '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'يتن', '-', '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ينا', '-', '-')];
	#}
	else : #{
		forms['actv.past.p3.m.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', paradigm, '-')];
		forms['actv.past.p3.f.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];
		forms['actv.past.p2.m.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];
		forms['actv.past.p2.f.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];
		forms['actv.past.p1.mf.sg'] = [(base + 'يت', '-', '-'), (base + 'يت', paradigm, '-')];

		forms['actv.past.p3.m.du'] = [(base + 'يا', '-', '-'), (base + 'يا', paradigm, '-')];
		forms['actv.past.p3.f.du'] = [(base + 'يتا', '-', '-'), (base + 'يتا', paradigm, '-')];
		forms['actv.past.p2.mf.du'] = [(base + 'يتما', '-', '-'), (base + 'يتما', paradigm, '-')];

		forms['actv.past.p3.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.past.p3.f.pl'] = [(base + 'ين', '-', '-'), (base + 'ين', paradigm, '-')];
		forms['actv.past.p2.m.pl'] = [(base + 'يتم', '-', '-'), (base + 'يتمو', paradigm, '-')];
		forms['actv.past.p2.f.pl'] = [(base + 'يتن', '-', '-'), (base + 'يتن', paradigm, '-')];
		forms['actv.past.p1.mf.pl'] = [(base + 'ينا', '-', '-'), (base + 'ينا', paradigm, '-')];
	#}

	return forms;
#}


# always the same type - like لقي active voice
def defective_past_pasv(base): #{

	forms = {};

	forms['pasv.past.p3.m.sg'] = [(base + 'ي', '-', '-')];
	forms['pasv.past.p3.f.sg'] = [(base + 'يت', '-', '-')];
	forms['pasv.past.p2.m.sg'] = [(base + 'يت', '-', '-')];
	forms['pasv.past.p2.f.sg'] = [(base + 'يت', '-', '-')];
	forms['pasv.past.p1.mf.sg'] = [(base + 'يت', '-', '-')];
	forms['pasv.past.p3.m.du'] = [(base + 'يا', '-', '-')];
	forms['pasv.past.p3.f.du'] = [(base + 'يتا', '-', '-')];
	forms['pasv.past.p2.mf.du'] = [(base + 'يتما', '-', '-')];

	forms['pasv.past.p3.m.pl'] = [(base + 'وا', '-', '-')];
	forms['pasv.past.p3.f.pl'] = [(base + 'ين', '-', '-')];
	forms['pasv.past.p2.m.pl'] = [(base + 'يتم', '-', '-')];
	forms['pasv.past.p2.f.pl'] = [(base + 'يتن', '-', '-')];
	forms['pasv.past.p1.mf.pl'] = [(base + 'ينا', '-', '-')];

	return forms;
#}


# يدعو type
def defective_pres_w_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'و', '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'و', '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'و', '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'و', '-', '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'وان', '-', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'وان', '-', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'وان', '-', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'و', '-', '-')];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'و', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'و', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'و', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'و', '-', '-'), ('أ' + base + 'و', paradigm, '-')];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'وان', '-', '-'), ('ي' + base + 'وا', paradigm, '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'وان', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'وان', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'ون', paradigm, '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'ون', paradigm, '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'و', '-', '-'), ('ن' + base + 'و', paradigm, '-')];

	#}

	return forms;
#}


# يرمي type, ى in past
def defective_pres_ya_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'ي', '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'ي', '-', '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'يان', '-', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'يان', '-', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'يان', '-', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'ي', '-', '-')];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'ي', '-', '-'), ('ي' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'ي', '-', '-'), ('أ' + base + 'ي', paradigm, '-')];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'يان', '-', '-'), ('ي' + base + 'يا', paradigm, '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'يان', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'يان', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ين', '-', '-'), ('ي' + base + 'ين', paradigm, '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ين', paradigm, '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'ي', '-', '-'), ('ن' + base + 'ي', paradigm, '-')];

	#}

	return forms;
#}



# يلقى type, ي in past
def defective_pres_yy_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'ى', '-', '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'ى', '-', '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'ى', '-', '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-')];

		forms['actv.pres.p3.m.du'] = [('ي' + base + 'يان', '-', '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'يان', '-', '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'يان', '-', '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-')];
	#}
	else : #{
		forms['actv.pres.p3.m.sg'] = [('ي' + base + 'ى', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p3.f.sg'] = [('ت' + base + 'ى', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p2.m.sg'] = [('ت' + base + 'ى', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.pres.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-'), ('أ' + base + 'ا', paradigm, '-')];
	
		forms['actv.pres.p3.m.du'] = [('ي' + base + 'يان', '-', '-'), ('ي' + base + 'يا', paradigm, '-')];
		forms['actv.pres.p3.f.du'] = [('ت' + base + 'يان', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];
		forms['actv.pres.p2.mf.du'] = [('ت' + base + 'يان', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];

		forms['actv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.pres.p3.f.pl'] = [('ي' + base + 'ين', '-', '-'), ('ي' + base + 'ين', paradigm, '-')];
		forms['actv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.pres.p2.f.pl'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ين', paradigm, '-')];
		forms['actv.pres.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-'), ('ن' + base + 'ا', paradigm, '-')];

	#}

	return forms;
#}



# one type only - like يلقى active
def defective_pres_pasv(base): #{

	forms = {};
	forms['pasv.pres.p3.m.sg'] = [('ي' + base + 'ى', '-', '-')];
	forms['pasv.pres.p3.f.sg'] = [('ت' + base + 'ى', '-', '-')];
	forms['pasv.pres.p2.m.sg'] = [('ت' + base + 'ى', '-', '-')];
	forms['pasv.pres.p2.f.sg'] = [('ت' + base + 'ين', '-', '-')];
	forms['pasv.pres.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-')];

	forms['pasv.pres.p3.m.du'] = [('ي' + base + 'يان', '-', '-')];
	forms['pasv.pres.p3.f.du'] = [('ت' + base + 'يان', '-', '-')];
	forms['pasv.pres.p2.mf.du'] = [('ت' + base + 'يان', '-', '-')];

	forms['pasv.pres.p3.m.pl'] = [('ي' + base + 'ون', '-', '-')];
	forms['pasv.pres.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
	forms['pasv.pres.p2.m.pl'] = [('ت' + base + 'ون', '-', '-')];
	forms['pasv.pres.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
	forms['pasv.pres.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-')];

	return forms;
#}



# يدعو type
def defective_subjun_w_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'و', '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'و', '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'و', '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'و', '-', '-')];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'وا', '-', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'و', '-', '-')];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'و', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'و', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'و', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'و', '-', '-'), ('أ' + base + 'و', paradigm, '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'وا', paradigm, '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'ون', paradigm, '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'ون', paradigm, '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'و', '-', '-'), ('ن' + base + 'و', paradigm, '-')];

	#}

	return forms;
#}


# يرمي type, ى in past
def defective_subjun_ya_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'ي', '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'ي', '-', '-')];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'يا', '-', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'يا', '-', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'يا', '-', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'ي', '-', '-')];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'ي', '-', '-'), ('ي' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'ي', '-', '-'), ('أ' + base + 'ي', paradigm, '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'يا', '-', '-'), ('ي' + base + 'يا', paradigm, '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ين', '-', '-'), ('ي' + base + 'ين', paradigm, '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ين', paradigm, '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'ي', '-', '-'), ('ن' + base + 'ي', paradigm, '-')];

	#}

	return forms;
#}



# يلقى type, ي in past
def defective_subjun_yy_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'ى', '-', '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'ى', '-', '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'ى', '-', '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-')];

		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'يا', '-', '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'يا', '-', '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'يا', '-', '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-')];
	#}
	else : #{
		forms['actv.subjun.p3.m.sg'] = [('ي' + base + 'ى', '-', '-'), ('ي' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p3.f.sg'] = [('ت' + base + 'ى', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p2.m.sg'] = [('ت' + base + 'ى', '-', '-'), ('ت' + base + 'ا', paradigm, '-')];
		forms['actv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.subjun.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-'), ('أ' + base + 'ا', paradigm, '-')];
	
		forms['actv.subjun.p3.m.du'] = [('ي' + base + 'يا', '-', '-'), ('ي' + base + 'يا', paradigm, '-')];
		forms['actv.subjun.p3.f.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];
		forms['actv.subjun.p2.mf.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];

		forms['actv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p3.f.pl'] = [('ي' + base + 'ين', '-', '-'), ('ي' + base + 'ين', paradigm, '-')];
		forms['actv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.subjun.p2.f.pl'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ين', paradigm, '-')];
		forms['actv.subjun.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-'), ('ن' + base + 'ا', paradigm, '-')];

	#}

	return forms;
#}



# one type only - like يلقى active
def defective_subjun_pasv(base): #{

	forms = {};
	forms['pasv.subjun.p3.m.sg'] = [('ي' + base + 'ى', '-', '-')];
	forms['pasv.subjun.p3.f.sg'] = [('ت' + base + 'ى', '-', '-')];
	forms['pasv.subjun.p2.m.sg'] = [('ت' + base + 'ى', '-', '-')];
	forms['pasv.subjun.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['pasv.subjun.p1.mf.sg'] = [('أ' + base + 'ى', '-', '-')];

	forms['pasv.subjun.p3.m.du'] = [('ي' + base + 'يا', '-', '-')];
	forms['pasv.subjun.p3.f.du'] = [('ت' + base + 'يا', '-', '-')];
	forms['pasv.subjun.p2.mf.du'] = [('ت' + base + 'يا', '-', '-')];

	forms['pasv.subjun.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['pasv.subjun.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
	forms['pasv.subjun.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['pasv.subjun.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
	forms['pasv.subjun.p1.mf.pl'] = [('ن' + base + 'ى', '-', '-')];

	return forms;
#}



# يدعو type
def defective_apocop_w_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'وا', '-', '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base + 'ون', '-', '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base + 'ون', '-', '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'وا', paradigm, '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'وا', paradigm, '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base + 'ون', '-', '-'), ('ي' + base + 'ون', paradigm, '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base + 'ون', '-', '-'), ('ت' + base + 'ون', paradigm, '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];

	#}

	return forms;
#}


# both يرم and يلق type
def defective_apocop_y_actv(base, tv): #{

	forms = {};
	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'يا', '-', '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'يا', '-', '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'يا', '-', '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];
	#}
	else : #{
		forms['actv.apocop.p3.m.sg'] = [('ي' + base, '-', '-'), ('ي' + base, paradigm, '-')];
		forms['actv.apocop.p3.f.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.m.sg'] = [('ت' + base, '-', '-'), ('ت' + base, paradigm, '-')];
		forms['actv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-'), ('ت' + base + 'ي', paradigm, '-')];
		forms['actv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-'), ('أ' + base, paradigm, '-')];
	
		forms['actv.apocop.p3.m.du'] = [('ي' + base + 'يا', '-', '-'), ('ي' + base + 'يا', paradigm, '-')];
		forms['actv.apocop.p3.f.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];
		forms['actv.apocop.p2.mf.du'] = [('ت' + base + 'يا', '-', '-'), ('ت' + base + 'يا', paradigm, '-')];

		forms['actv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-'), ('ي' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p3.f.pl'] = [('ي' + base + 'ين', '-', '-'), ('ي' + base + 'ين', paradigm, '-')];
		forms['actv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-'), ('ت' + base + 'و', paradigm, '-')];
		forms['actv.apocop.p2.f.pl'] = [('ت' + base + 'ين', '-', '-'), ('ت' + base + 'ين', paradigm, '-')];
		forms['actv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-'), ('ن' + base, paradigm, '-')];

	#}

	return forms;
#}


# one type only - like يلقى active
def defective_apocop_pasv(base): #{

	forms = {};
	forms['pasv.apocop.p3.m.sg'] = [('ي' + base, '-', '-')];
	forms['pasv.apocop.p3.f.sg'] = [('ت' + base, '-', '-')];
	forms['pasv.apocop.p2.m.sg'] = [('ت' + base, '-', '-')];
	forms['pasv.apocop.p2.f.sg'] = [('ت' + base + 'ي', '-', '-')];
	forms['pasv.apocop.p1.mf.sg'] = [('أ' + base, '-', '-')];

	forms['pasv.apocop.p3.m.du'] = [('ي' + base + 'يا', '-', '-')];
	forms['pasv.apocop.p3.f.du'] = [('ت' + base + 'يا', '-', '-')];
	forms['pasv.apocop.p2.mf.du'] = [('ت' + base + 'يا', '-', '-')];

	forms['pasv.apocop.p3.m.pl'] = [('ي' + base + 'وا', '-', '-')];
	forms['pasv.apocop.p3.f.pl'] = [('ي' + base + 'ين', '-', '-')];
	forms['pasv.apocop.p2.m.pl'] = [('ت' + base + 'وا', '-', '-')];
	forms['pasv.apocop.p2.f.pl'] = [('ت' + base + 'ين', '-', '-')];
	forms['pasv.apocop.p1.mf.pl'] = [('ن' + base, '-', '-')];

	return forms;
#}


def defective_imp_w(base, tv): #{

	# passive voice?

	forms = {};

	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.f.pl'] = [(base + 'ون', '-', '-')];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-'), (base, paradigm, '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', paradigm, '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'وا', '-', '-'), (base + 'وا', paradigm, '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.imp.p2.f.pl'] = [(base + 'ون', '-', '-'), (base + 'ون', paradigm, '-')];
	#}

	return forms ; 
#}


def defective_imp_y(base, tv): #{

	# passive voice?

	forms = {};

	paradigm = 'S__فتح/ه';

	if tv == 'iv' : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'يا', '-', '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-')];
		forms['actv.imp.p2.f.pl'] = [(base + 'ين', '-', '-')];
	#}
	else : #{
		forms['actv.imp.p2.m.sg'] = [(base, '-', '-'), (base, paradigm, '-')];
		forms['actv.imp.p2.f.sg'] = [(base + 'ي', '-', '-'), (base + 'ي', paradigm, '-')];
		forms['actv.imp.p2.mf.du'] = [(base + 'يا', '-', '-'), (base + 'يا', paradigm, '-')];
		forms['actv.imp.p2.m.pl'] = [(base + 'وا', '-', '-'), (base + 'و', paradigm, '-')];
		forms['actv.imp.p2.f.pl'] = [(base + 'ين', '-', '-'), (base + 'ين', paradigm, '-')];
	#}

	return forms ; 
#}


## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


def defective_patt1_past(root, subtype, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	if subtype == 'ا' :
		forms = defective_past_wa_actv(base, tv);
	elif subtype == 'و' :
		forms = defective_past_ww_actv(base, tv);
	elif subtype == 'ى' :
		forms = defective_past_ya_actv(base, tv);
	else : # subtype == 'ي'
		forms = defective_past_yy_actv(base, tv);

	if (tv == 'tv') :
		forms.update(defective_past_pasv(base));

	return forms;
#}


def defective_patt1_impf(root, subtype, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	if (subtype == 'ا') or (subtype == 'و') : #{
		forms = defective_pres_w_actv(base, tv);
		forms.update(defective_subjun_w_actv(base, tv));
		forms.update(defective_apocop_w_actv(base, tv));
  		forms.update(defective_imp_w('ا' + base, tv));
	#}
	elif subtype == 'ى' : #{
		forms = defective_pres_ya_actv(base, tv);
		forms.update(defective_subjun_ya_actv(base, tv));
		forms.update(defective_apocop_y_actv(base, tv));
		forms.update(defective_imp_y('ا' + base, tv));
	#}
	else : # subtype == 'ي' #{
		forms = defective_pres_yy_actv(base, tv);
		forms.update(defective_subjun_yy_actv(base, tv));
		forms.update(defective_apocop_y_actv(base, tv));
		forms.update(defective_imp_y('ا' + base, tv));
	#}

	if (tv == 'tv') :
		forms.update(defective_pres_pasv(base));

	return forms;
#}



def defective_patt1_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [(r[0] + 'ا' + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [(r[0] + 'ا' + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [(r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [(r[0] + 'ا' + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt1_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'ي', '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'ية', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'يون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'يات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 2
## ----------------------------------------------------------------------------##


def defective_patt2_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	forms = defective_past_ya_actv(base);
	if (tv == 'tv') :
		forms.update(defective_past_pasv(base));

	return forms;
#}


def defective_patt2_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y(base, tv));


	if (tv == 'tv') :
		forms.update(defective_pres_pasv(base));

	return forms;
#}


def defective_patt2_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + r[1]  + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + r[1]  + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt2_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1]  + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1]  + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1]  + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 3
## ----------------------------------------------------------------------------##


def defective_patt3_past(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1];

	forms = defective_past_ya_actv(base, tv);
	if (tv == 'tv') : #{
		base = r[0] + 'و' + r[1];
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt3_imp(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + 'ا' + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y(base, tv));

	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}


def defective_patt3_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + 'ا' + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + 'ا' + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + 'ا' + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt3_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + 'ا' + r[1] + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + 'ا' + r[1] + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + 'ا' + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 4
## ----------------------------------------------------------------------------##


def defective_patt4_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'أ' + r[0] + r[1];

	forms = defective_past_ya_actv(base, tv);
	if (tv == 'tv') : #{
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt4_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = r[0] + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y(base, tv));

	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}


def defective_patt4_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('م' + r[0] + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('م' + r[0] + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + r[0] + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt4_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('م' + r[0] + r[1] + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('م' + r[0] + r[1] + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + r[0] + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 5
## ----------------------------------------------------------------------------##


def defective_patt5_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1];

	forms = defective_past_ya_actv(base, tv);
	if (tv == 'tv') : #{
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt5_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y(base, tv));

	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}


def defective_patt5_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مت' + r[0] + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('مت' + r[0] + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('مت' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مت' + r[0] + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


# rare
def defective_patt5_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + r[1] + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + r[1] + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 6
## ----------------------------------------------------------------------------##


def defective_patt6_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1];

	forms = defective_past_actv(base, tv);
	if (tv == 'tv') : #{
		base = 'ت' + r[0] + 'و' + r[1];
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt6_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ت' + r[0] + 'ا' + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y(base, tv));

	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}


def defective_patt6_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('مت' + r[0] + 'ا' + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('مت' + r[0] + 'ا' + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('مت' + r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('مت' + r[0] + 'ا' + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt6_pp(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pp.m.sg'] = [('مت' + r[0] + 'ا' + r[1] + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('مت' + r[0] + 'ا' + r[1] + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('مت' + r[0] + 'ا' + r[1] + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('مت' + r[0] + 'ا' + r[1] + 'ات', '-', '-')] ;

	return forms;

#}


## ----------------------------------------------------------------------------##
## pattern 7
## ----------------------------------------------------------------------------##


def defective_patt7_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ان' + r[0] + r[1];

	return defective_past_ya_actv(base, tv);
#}


def defective_patt7_pres(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ن' + r[0] + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y('ا' + base, tv));

	return forms;
#}


def defective_patt7_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};

	forms['pprs.m.sg'] = [('من' + r[0] + r[1], '-', '-')] ;
	forms['pprs.f.sg'] = [('من' + r[0] + r[1] + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('من' + r[0] + r[1] + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('من' + r[0] + r[1] + 'يات', '-', '-')] ;

	return forms;
#}


## ----------------------------------------------------------------------------##
## pattern 8
## ----------------------------------------------------------------------------##


def defective_patt8_past(root, tv): #{
	r = root.split('-'); # radicals

	base_start = 'ا' + r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = 'ا' + r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = 'ا' + r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = 'ا' + r[0] + 'د';
	
	base = base_start + r[1];

	forms = defective_past_ya_actv(base, tv);
	if (tv == 'tv') : #{
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt8_impf(root, tv): #{
	r = root.split('-'); # radicals

	base_start = r[0] + 'ت';
	# with ذ assimilation may be partial (د)
	if (r[0] == 'ط') or (r[0] == 'د') or (r[0] == 'ذ') or (r[0] == 'ظ') :
		base_start = r[0];
	elif (r[0] == 'ص') or (r[0] == 'ض') :
		base_start = r[0] + 'ط';
	elif (r[0] == 'ز') :
		base_start = r[0] + 'د';
	
	base = base_start + r[1];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y('ا' + base, tv));

	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}



def defective_patt8_pprs(root): #{
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
	forms['pprs.f.sg'] = [('م' + base + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [('م' + base + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt8_pp(root): #{
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

	forms['pp.m.sg'] = [('م' + base + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [('م' + base + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [('م' + base + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [('م' + base + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## pattern 10
## ----------------------------------------------------------------------------##


def defective_patt10_past(root, tv): #{
	r = root.split('-'); # radicals

	base = 'است' + r[0] + r[1];

	forms = defective_past_ya_actv(base, tv);
	if (tv == 'tv') : #{
		forms.update(defective_past_pasv(base));
	#}

	return forms;
#}


def defective_patt10_impf(root, tv): #{
	r = root.split('-'); # radicals

	base = 'ست' + r[0] + r[1] + r[2];

	forms = defective_pres_ya_actv(base, tv);
	forms.update(defective_subjun_ya_actv(base, tv));
	forms.update(defective_apocop_y_actv(base, tv));
	forms.update(defective_imp_y('ا' + base, tv));


	if (tv == 'tv') : #{
		forms.update(defective_pres_pasv(base));
	#}

	return forms;
#}


def defective_patt10_pprs(root): #{
	r = root.split('-'); # radicals
	
	base = 'مست' + r[0] + r[1];

	forms = {};

	forms['pprs.m.sg'] = [(base, '-', '-')] ;
	forms['pprs.f.sg'] = [(base + 'ية', '-', '-')] ;
	forms['pprs.m.pl'] = [(base + 'ون', '-', '-')] ;
	forms['pprs.f.pl'] = [(base + 'يات', '-', '-')] ;

	return forms;
#}


def defective_patt10_pp(root): #{
	r = root.split('-'); # radicals

	base = 'مست' + r[0] + r[1];

	forms = {};

	forms['pp.m.sg'] = [(base + 'ى', '-', '-')] ;
	forms['pp.f.sg'] = [(base + 'اة', '-', '-')] ;
	forms['pp.m.pl'] = [(base + 'ون', '-', '-')] ;
	forms['pp.f.pl'] = [(base + 'ات', '-', '-')] ;

	return forms;

#}



## ----------------------------------------------------------------------------##
## main
## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{
		forms.update(defective_patt1_past(stem['root'], stem['subtype'], stem['trans']));
		forms.update(defective_patt1_impf(stem['root'], stem['subtype'], stem['trans']));
		forms.update(defective_patt1_pp(stem['root']));
		forms.update(defective_patt1_pprs(stem['root']));
	#}
	elif stem['theme'] == '2' : #{
		forms.update(defective_patt2_past(stem['root'], stem['trans']));
		forms.update(defective_patt2_impf(stem['root'], stem['trans']));
		forms.update(defective_patt2_pp(stem['root']));
		forms.update(defective_patt2_pprs(stem['root']));
	#}
	elif stem['theme'] == '3' : #{
		forms.update(defective_patt3_past(stem['root'], stem['trans']));
		forms.update(defective_patt3_impf(stem['root'], stem['trans']));
		forms.update(defective_patt3_pp(stem['root']));
		forms.update(defective_patt3_pprs(stem['root']));
	#}
	elif stem['theme'] == '4' : #{
		forms.update(defective_patt4_past(stem['root'], stem['trans']));
		forms.update(defective_patt4_impf(stem['root'], stem['trans']));
		forms.update(defective_patt4_pp(stem['root']));
		forms.update(defective_patt4_pprs(stem['root']));
	#}
	elif stem['theme'] == '5' : #{
		forms.update(defective_patt5_past(stem['root'], stem['trans']));
		forms.update(defective_patt5_impf(stem['root'], stem['trans']));
		forms.update(defective_patt5_pp(stem['root']));
		forms.update(defective_patt5_pprs(stem['root']));
	#}
	elif stem['theme'] == '6' : #{
		forms.update(defective_patt6_past(stem['root'], stem['trans']));
		forms.update(defective_patt6_impf(stem['root'], stem['trans']));
		forms.update(defective_patt6_pp(stem['root']));
		forms.update(defective_patt6_pprs(stem['root']));
	#}
	elif stem['theme'] == '7' : #{
		forms.update(defective_patt7_past(stem['root'], stem['trans']));
		forms.update(defective_patt7_impf(stem['root'], stem['trans']));
		forms.update(defective_patt7_pprs(stem['root']));
	#}
	elif stem['theme'] == '8' : #{
		forms.update(defective_patt8_past(stem['root'], stem['trans']));
		forms.update(defective_patt8_impf(stem['root'], stem['trans']));
		forms.update(defective_patt8_pp(stem['root']));
		forms.update(defective_patt8_pprs(stem['root']));
	#}
	elif stem['theme'] == '10' : #{
		forms.update(defective_patt10_past(stem['root'], stem['trans']));
		forms.update(defective_patt10_impf(stem['root'], stem['trans']));
		forms.update(defective_patt10_pp(stem['root']));
		forms.update(defective_patt10_pprs(stem['root']));
	#}

	return forms;

#}

