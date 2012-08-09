#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## doubled
## ----------------------------------------------------------------------------##


def doubled_consonant_forms (form_sg, form_sg_suff, r, ek, tv): #{

	if ek == 'ok' : #{
		if tv == 'iv' : #{
		 	forms = [(form_sg, '-', r),
		 		 (form_sg_suff, 'S__qtalt/x', r),
				 (form_sg_suff, 'S__xrobt/ilha', r),
				 (form_sg_suff, 'S__xrobt/ilhiex', r)];
		#}
		else : #{
			forms = [(form_sg, '-', r),
				 (form_sg_suff, 'S__qtalt/x', r),
				 (form_sg_suff, 'S__xrobt/ni', r),
				 (form_sg_suff, 'S__xrobt/nix', r),
				 (form_sg_suff, 'S__xrobt/ilha', r),
				 (form_sg_suff, 'S__xrobt/ilhiex', r),
				 (form_sg_suff, 'S__qtaltu/hielha', r),
				 (form_sg_suff, 'S__qtaltu/hielhiex', r)];
		#}
	else : #{
		if tv == 'iv' : #{
		 	forms = [(form_sg, '-', r),
		 		 (form_sg_suff, 'S__qtalt/x', r),
				 (form_sg_suff, 'S__qtalt/ilha', r),
				 (form_sg_suff, 'S__qtalt/ilhiex', r)];
		#}
		else : #{
			forms = [(form_sg, '-', r),
				 (form_sg_suff, 'S__qtalt/x', r),
				 (form_sg_suff, 'S__qtalt/ni', r),
				 (form_sg_suff, 'S__qtalt/nix', r),
				 (form_sg_suff, 'S__qtalt/ilha', r),
				 (form_sg_suff, 'S__qtalt/ilhiex', r),
				 (form_sg_suff, 'S__qtaltu/hielha', r),
				 (form_sg_suff, 'S__qtaltu/hielhiex', r)];
		#}
	#}

	return forms;
#}


def doubled_vowel_forms (form_pl, form_pl_suff, r, tv): #{

	if tv == 'iv' : #{
	 	forms = [(form_pl, '-', r),
	 		 (form_pl_suff, 'S__qtalt/x', r),
			 (form_pl_suff, 'S__qtaltu/lha', r),
			 (form_pl_suff, 'S__qtaltu/lhiex', r)];
	#}
	else : #{
		forms = [(form_pl, '-', r),
			 (form_pl_suff, 'S__qtalt/x', r),
			 (form_pl_suff, 'S__qtaltu/ni', r),
			 (form_pl_suff, 'S__qtaltu/nix', r),
			 (form_pl_suff, 'S__qtaltu/lha', r),
			 (form_pl_suff, 'S__qtaltu/lhiex', r),
			 (form_pl_suff, 'S__qtaltu/hielha', r),
			 (form_pl_suff, 'S__qtaltu/hielhiex', r)];
	#}

	return forms;
#}



## ----------------------------------------------------------------------------##
## pattern 1
## ----------------------------------------------------------------------------##


# no ek/ok?
def doubled_patt1_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	ek = 'ek';

	forms['past.p3.m.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2], r[0] + v[0] + r[1] + r[2], '-', ek, tv);
	forms['past.p3.f.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'et', r[0] + v[0] + r[1] + r[2] + 'it', '-', ek, tv);
	forms['past.p2.mf.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek, tv);
	forms['past.p1.mf.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek, tv);
	forms['past.p3.mf.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'u', r[0] + v[0] + r[1] + r[2] + 'u', '-', tv);
	forms['past.p3.mf.pl'] += doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ew', r[0] + v[0] + r[1] + r[2] + 'ew', 'LR', tv);
	forms['past.p2.mf.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejtu', r[0] + v[0] + r[1] + r[2] + 'ejtu', '-', tv);
	forms['past.p1.mf.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejna', r[0] + v[0] + r[1] + r[2] + 'ejna', '-', tv);

	return forms;
#}


# ek/ok done
def doubled_patt1_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';

	forms['pres.p3.m.sg'] = doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'LR', ek, tv);		# irodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('j' + r[0] + v[1] + r[1] + r[2], 'j' + r[0] + v[1] + r[1] + r[2], 'LR', ek, tv); 		# jrodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'RL', ek, tv);		# ~irodd

	forms['pres.p3.f.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek, tv);		# trodd

	forms['pres.p2.mf.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek, tv);			# trodd

	forms['pres.p1.mf.sg'] = doubled_consonant_forms ('in' + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + v[1] + r[1] + r[2], 'LR', ek, tv);		# inrodd
	forms['pres.p1.mf.sg'] += doubled_consonant_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + r[0] + v[1] + r[1] + r[2], 'LR', ek, tv);		# irrodd
	forms['pres.p1.mf.sg'] += doubled_consonant_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + r[0] + v[1] + r[1] + r[2], 'RL', ek, tv);	# irrodd

	forms['pres.p3.mf.pl'] = doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv);		# iroddu
	forms['pres.p3.mf.pl'] += doubled_vowel_forms ('j' + r[0] + v[1] + r[1] + r[2] + 'u', 'j' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv); 	# jroddu
	forms['pres.p3.mf.pl'] += doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'RL', tv);	# ~iroddu

	forms['pres.p2.mf.pl'] = doubled_vowel_forms ('t' + r[0] + v[1] + r[1] + r[2] + 'u', 't' + r[0] + v[1] + r[1] + r[2] + 'u', '-', tv);		# troddu

	forms['pres.p1.mf.pl'] = doubled_vowel_forms ('in' + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv);		# inroddu
	forms['pres.p1.mf.pl'] += doubled_vowel_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv);	# irroddu
	forms['pres.p1.mf.pl'] += doubled_vowel_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'RL', tv);	# irroddu


	return forms;
#}


# ek/ok done
def doubled_patt1_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';	

	suffix = 'u'

 	forms['imp.p2.mf.sg'] = doubled_consonant_forms (r[0] + v[1] + r[1] + r[2], r[0] + v[1] + r[1] + r[2], '-', ek, tv);
	forms['imp.p2.mf.pl'] = doubled_vowel_forms (r[0] + v[1] + r[1] + r[2] + suffix , r[0] + v[1] + r[1] + r[2] + suffix , '-', tv);

	return forms;
#}


def doubled_patt1_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'u' + r[2], '-', '-')];
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'a', '-', '-')];
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'in', '-', '-')];

	return forms;
#}



## ----------------------------------------------------------------------------##
## pattern 7
## ----------------------------------------------------------------------------##


# no ek/ok?
def doubled_patt7_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	ek = 'ek';

	forms['past.p3.m.sg'] = doubled_consonant_forms ('n' + r[0] + v[0] + r[1] + r[2], 'n' + r[0] + v[0] + r[1] + r[2], '-', ek, tv);
	forms['past.p3.m.sg'] += doubled_consonant_forms ('in' + r[0] + v[0] + r[1] + r[2], 'in' + r[0] + v[0] + r[1] + r[2], 'LR', ek, tv);
	forms['past.p3.f.sg'] = doubled_consonant_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'et', 'n' + r[0] + v[0] + r[1] + r[2] + 'it', '-', ek, tv);
	forms['past.p3.f.sg'] += doubled_consonant_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'et', 'in' + r[0] + v[0] + r[1] + r[2] + 'it', 'LR', ek, tv);
	forms['past.p2.mf.sg'] = doubled_consonant_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'n' + r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek, tv);
	forms['past.p2.mf.sg'] += doubled_consonant_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'in' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'LR', ek, tv);
	forms['past.p1.mf.sg'] = doubled_consonant_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'n' + r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek, tv);
	forms['past.p1.mf.sg'] += doubled_consonant_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'in' + r[0] + v[0] + r[1] + r[2] + 'ejt', 'LR', ek, tv);
	forms['past.p3.mf.pl'] = doubled_vowel_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'u', 'n' + r[0] + v[0] + r[1] + r[2] + 'u', '-', tv);
	forms['past.p3.mf.pl'] += doubled_vowel_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'ew', 'in' + r[0] + v[0] + r[1] + r[2] + 'ew', 'LR', tv);
	forms['past.p2.mf.pl'] = doubled_vowel_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'ejtu', 'n' + r[0] + v[0] + r[1] + r[2] + 'ejtu', '-', tv);
	forms['past.p2.mf.pl'] += doubled_vowel_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'ejtu', 'in' + r[0] + v[0] + r[1] + r[2] + 'ejtu', 'LR', tv);
	forms['past.p1.mf.pl'] = doubled_vowel_forms ('n' + r[0] + v[0] + r[1] + r[2] + 'ejna', 'n' + r[0] + v[0] + r[1] + r[2] + 'ejna', '-', tv);
	forms['past.p1.mf.pl'] += doubled_vowel_forms ('in' + r[0] + v[0] + r[1] + r[2] + 'ejna', 'in' + r[0] + v[0] + r[1] + r[2] + 'ejna', 'LR', tv);

	return forms;
#}


# ek/ok done
def doubled_patt7_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';

	forms['pres.p3.m.sg'] = doubled_consonant_forms ('jin' + r[0] + v[1] + r[1] + r[2], 'jin' + r[0] + v[1] + r[1] + r[2], '-', ek, tv); 
	forms['pres.p3.f.sg'] = doubled_consonant_forms ('tin' + r[0] + v[1] + r[1] + r[2], 'tin' + r[0] + v[1] + r[1] + r[2], '-', ek, tv);	
	forms['pres.p2.mf.sg'] = doubled_consonant_forms ('tin' + r[0] + v[1] + r[1] + r[2], 'tin' + r[0] + v[1] + r[1] + r[2], '-', ek, tv);	
	forms['pres.p1.mf.sg'] = doubled_consonant_forms ('nin' + r[0] + v[1] + r[1] + r[2], 'nin' + r[0] + v[1] + r[1] + r[2], 'LR', ek, tv);	

	forms['pres.p3.mf.pl'] = doubled_vowel_forms ('jin' + r[0] + v[1] + r[1] + r[2] + 'u', 'jin' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv);
	forms['pres.p2.mf.pl'] = doubled_vowel_forms ('tin' + r[0] + v[1] + r[1] + r[2] + 'u', 'tin' + r[0] + v[1] + r[1] + r[2] + 'u', '-', tv);
	forms['pres.p1.mf.pl'] = doubled_vowel_forms ('nin' + r[0] + v[1] + r[1] + r[2] + 'u', 'nin' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR', tv);


	return forms;
#}


# ek/ok done
def doubled_patt7_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';	

	suffix = 'u'

 	forms['imp.p2.mf.sg'] = doubled_consonant_forms ('in' + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + v[1] + r[1] + r[2], '-', ek, tv);
	forms['imp.p2.mf.pl'] = doubled_vowel_forms ('in' + r[0] + v[1] + r[1] + r[2] + suffix , 'in' + r[0] + v[1] + r[1] + r[2] + suffix , '-', tv);

	return forms;
#}



## ----------------------------------------------------------------------------##


def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{

		forms = doubled_patt1_past(stem['root'], stem['vowel_perf'], stem['trans']);
		if stem['vowel_impf'] != '' : #{
			forms.update(doubled_patt1_pres(stem['root'], stem['vowel_impf'], stem['trans']));
		#	if stem['trans'] == 'tv':
			forms.update(doubled_patt1_imp(stem['root'], stem['vowel_impf'], stem['trans']));
		#}
		if stem['pp'] != '' : #{
			forms.update(doubled_patt1_pp(stem['root'], stem['vowel_perf'], stem['pp']));
		#}


	if stem['theme'] == '7' : #{

		forms = doubled_patt7_past(stem['root'], stem['vowel_perf'], stem['trans']);
		if stem['vowel_impf'] != '' : #{
			forms.update(doubled_patt7_pres(stem['root'], stem['vowel_perf'], stem['trans']));
		#	if stem['trans'] == 'tv':
			forms.update(doubled_patt7_imp(stem['root'], stem['vowel_perf'], stem['trans']));
		#}


	#}

	return forms;

#}
