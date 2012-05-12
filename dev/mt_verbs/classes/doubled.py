#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## doubled
## ----------------------------------------------------------------------------##


def doubled_consonant_forms (form_sg, form_sg_suff, r, ek): #{

	if ek == 'ok' :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__xrobt/ni', r),
			 (form_sg_suff, 'S__xrobt/nix', r),
			 (form_sg_suff, 'S__xrobt/ilha', r),
			 (form_sg_suff, 'S__xrobt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];
	else :
		forms = [(form_sg, '-', r),
			 (form_sg_suff, 'S__qtalt/x', r),
			 (form_sg_suff, 'S__qtalt/ni', r),
			 (form_sg_suff, 'S__qtalt/nix', r),
			 (form_sg_suff, 'S__qtalt/ilha', r),
			 (form_sg_suff, 'S__qtalt/ilhiex', r),
			 (form_sg_suff, 'S__qtaltu/hielha', r),
			 (form_sg_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


def doubled_vowel_forms (form_pl, form_pl_suff, r): #{

	forms = [(form_pl, '-', r),
		 (form_pl_suff, 'S__qtalt/x', r),
		 (form_pl_suff, 'S__qtaltu/ni', r),
		 (form_pl_suff, 'S__qtaltu/nix', r),
		 (form_pl_suff, 'S__qtaltu/lha', r),
		 (form_pl_suff, 'S__qtaltu/lhiex', r),
		 (form_pl_suff, 'S__qtaltu/hielha', r),
		 (form_pl_suff, 'S__qtaltu/hielhiex', r)];

	return forms;
#}


# no ek/ok?
def doubled_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	ek = 'ek';

	forms['past.p3.m.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2], r[0] + v[0] + r[1] + r[2], '-', ek);
	forms['past.p3.f.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'et', r[0] + v[0] + r[1] + r[2] + 'it', '-', ek);
	forms['past.p2.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek);
	forms['past.p1.sg'] = doubled_consonant_forms (r[0] + v[0] + r[1] + r[2] + 'ejt', r[0] + v[0] + r[1] + r[2] + 'ejt', '-', ek);
	forms['past.p3.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'u', r[0] + v[0] + r[1] + r[2] + 'u', '-');
	forms['past.p3.pl'] += doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ew', r[0] + v[0] + r[1] + r[2] + 'ew', 'LR');
	forms['past.p2.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejtu', r[0] + v[0] + r[1] + r[2] + 'ejtu', '-');
	forms['past.p1.pl'] = doubled_vowel_forms (r[0] + v[0] + r[1] + r[2] + 'ejna', r[0] + v[0] + r[1] + r[2] + 'ejna', '-');

	return forms;
#}


# ek/ok done
def doubled_pres(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';

	forms['pres.p3.m.sg'] = doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# irodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('j' + r[0] + v[1] + r[1] + r[2], 'j' + r[0] + v[1] + r[1] + r[2], 'LR', ek); 		# jrodd
	forms['pres.p3.m.sg'] += doubled_consonant_forms ('i' + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + v[1] + r[1] + r[2], 'RL', ek);		# ~irodd

	forms['pres.p3.f.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek);		# trodd

	forms['pres.p2.sg'] = doubled_consonant_forms ('t' + r[0] + v[1] + r[1] + r[2], 't' + r[0] + v[1] + r[1] + r[2], '-', ek);			# trodd

	forms['pres.p1.sg'] = doubled_consonant_forms ('in' + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# inrodd
	forms['pres.p1.sg'] += doubled_consonant_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2], 'i' + r[0] + r[0] + v[1] + r[1] + r[2], 'LR', ek);		# irrodd
	forms['pres.p1.sg'] += doubled_consonant_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2], 'in' + r[0] + r[0] + v[1] + r[1] + r[2], 'RL', ek);	# irrodd

	forms['pres.p3.pl'] = doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');		# iroddu
	forms['pres.p3.pl'] += doubled_vowel_forms ('j' + r[0] + v[1] + r[1] + r[2] + 'u', 'j' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR'); 	# jroddu
	forms['pres.p3.pl'] += doubled_vowel_forms ('i' + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + v[1] + r[1] + r[2] + 'u', 'RL');	# ~iroddu

	forms['pres.p2.pl'] = doubled_vowel_forms ('t' + r[0] + v[1] + r[1] + r[2] + 'u', 't' + r[0] + v[1] + r[1] + r[2] + 'u', '-');		# troddu

	forms['pres.p1.pl'] = doubled_vowel_forms ('in' + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');		# inroddu
	forms['pres.p1.pl'] += doubled_vowel_forms ('i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'i' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'LR');	# irroddu
	forms['pres.p1.pl'] += doubled_vowel_forms ('in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'in' + r[0] + r[0] + v[1] + r[1] + r[2] + 'u', 'RL');	# irroddu


	return forms;
#}


# ek/ok done
def doubled_imp(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[1] == 'o' :
		ek = 'ok';
	else :
		ek = 'ek';	

	suffix = 'u'

	forms['imp.p2.sg'] = doubled_consonant_forms (r[0] + v[1] + r[1] + r[2], r[0] + v[1] + r[1] + r[2], '-', ek);
	forms['imp.p2.pl'] = doubled_vowel_forms (r[0] + v[1] + r[1] + r[2] + suffix , r[0] + v[1] + r[1] + r[2] + suffix , '-');

	return forms;
#}


def doubled_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'u' + r[2], '-', '-')];
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'a', '-', '-')];
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'u' + r[2] + 'in', '-', '-')];

	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{

		forms = doubled_past(stem['root'], stem['vowel_perf']);
		if stem['vowel_impf'] != '' : 
			forms.update(doubled_pres(stem['root'], stem['vowel_impf']));
			forms.update(doubled_imp(stem['root'], stem['vowel_impf']));
		if stem['pp'] != '' : #{
			forms.update(doubled_pp(stem['root'], stem['vowel_perf'], stem['pp']));

	#}

	return forms;

#}
