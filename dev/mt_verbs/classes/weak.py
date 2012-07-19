#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## weak
## ----------------------------------------------------------------------------##


def weak_pprs(root): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pprs.m.sg'] = [(r[0] + 'ie' + r[1] + 'i', '-', '-')] ;
	forms['pprs.f.sg'] = [(r[0] + 'ie' + r[1] + 'ja', '-', '-')] ;
	forms['pprs.mf.pl'] = [(r[0] + 'e' + r[1] + 'jin', '-', '-')] ;

	return forms;
#}


def weak_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + r[1] + 'i', '-', '-')] ;
	forms['pp.f.sg'] = [(pref + r[0] + r[1] + 'ija', '-', '-')] ;
	forms['pp.mf.pl'] = [(pref + r[0] + r[1] + 'ijin', '-', '-')] ;

	return forms;
#}


# no ek/ok
def weak_consonant_forms (form_sg, form_sg_suff, r, tv): #{
# only past.p3.sg.f have different forms with and without suffixes

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
	return forms;
#}


def weak_vowel_forms (form_pl, form_pl_suff, r, tv): #{
# different with/without suffix forms only for past.p1.mf.pl

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


def weak_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	if v[0] == 'e' and v[1] == 'a': #{

		forms['past.p3.m.sg'] = weak_vowel_forms(r[0] + v[0] + r[1] + v[1], r[0] + r[1] + 'ie', '-', tv);

		# This form is obtained by the elision of the first vowel of the 
		# stem and the change of the second vowel to 'ie' (for e-a) and
		# 'a' for (a-a)
		# rmiet - ma rmitx? or ma rmietx?
		forms['past.p3.f.sg'] = weak_consonant_forms(r[0] + r[1] + 'iet', r[0] + r[1] + 'it', '-', tv);
	#}
	else : #{
		forms['past.p3.m.sg'] = weak_vowel_forms(r[0] + v[0] + r[1] + v[1], r[0] + r[1] + 'a', '-', tv);
		# qratu? or qritu?
		forms['past.p3.f.sg'] = weak_consonant_forms(r[0] + r[1] + 'at', r[0] + r[1] + 'at', '-', tv);
	#}

	# This form is obtained by the omission of the two vowels in the stem
	# and the addition of the dipthong 'ej' (for e-a) and 'aj' (for a-a)
	forms['past.p2.mf.sg'] = weak_consonant_forms(r[0] + r[1] + v[0] + 'jt', r[0] + r[1] + v[0] + 'jt', '-', tv);	
	forms['past.p1.mf.sg'] = weak_consonant_forms(r[0] + r[1] + v[0] + 'jt', r[0] + r[1] + v[0] + 'jt', '-', tv);	

	# This form is obtained by the omission of the two vowels in the vocalic
	# sequence + dipthong 'ew' or 'aw'
	# In the context of the attached pronouns 'ew' and 'aw'
	# are also treated like vowels
	forms['past.p3.mf.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'w', r[0] + r[1] + v[0] + 'w', '-', tv);
	forms['past.p2.mf.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'jtu', r[0] + r[1] + v[0] + 'jtu', '-', tv);
	forms['past.p1.mf.pl'] = weak_vowel_forms(r[0] + r[1] + v[0] + 'jna', r[0] + r[1] + v[0] + 'jnie', '-', tv);

	return forms;
#}


def weak_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	presuff_vowel = v[1];
	# That's only my guess
	if v[0] == 'e' and v[1] == 'a': 
		presuff_vowel = 'ie';

	# no first vowel elision in forms with suffixes? 
	forms['pres.p3.m.sg'] = weak_vowel_forms('j' + v[0] + r[0] + r[1] + v[1] , 'j' + v[0] + r[0] + r[1] + presuff_vowel , '-', tv);
	forms['pres.p3.f.sg'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + v[1] , 't' + v[0] + r[0] + r[1] + presuff_vowel , '-', tv);
	forms['pres.p2.mf.sg'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + v[1] , 't' + v[0] + r[0] + r[1] + presuff_vowel , '-', tv);
	forms['pres.p1.mf.sg'] = weak_vowel_forms('n' + v[0] + r[0] + r[1] + v[1] , 'n' + v[0] + r[0] + r[1] + presuff_vowel , '-', tv);
	
	if vowels == 'a-a': #{
		suffix =  'aw';
	elif vowels == 'i-a': #{
		suffix =  'ew';
	else: #{
		suffix = 'u'
	#}
										# QaRaJ		BeDaJ		MeXaJ	ReMaJ
										# a-a		i-a		i-i	a-i
	forms['pres.p3.mf.pl'] = weak_vowel_forms('j' + v[0] + r[0] + r[1] + suffix, 'j' + v[0] + r[0] + r[1] + suffix, '-', tv);	# j-aQRa-w	j-iBDe-w	j-iMXu	j-aRMu
	forms['pres.p2.mf.pl'] = weak_vowel_forms('t' + v[0] + r[0] + r[1] + suffix, 't' + v[0] + r[0] + r[1] + suffix, '-', tv);	# t-aQRa-w
	forms['pres.p1.mf.pl'] = weak_vowel_forms('n' + v[0] + r[0] + r[1] + suffix, 'n' + v[0] + r[0] + r[1] + suffix, '-', tv);	# n-aQRa-w

	return forms;
#}


def weak_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};

	presuff_sg_vowel = v[1];
	# That's only my guess
	if v[0] == 'e' and v[1] == 'a': 
		presuff_sg_vowel = 'ie';
	
	if vowels == 'a-a': #{
		pl_suffix =  'aw';
	elif vowels == 'i-a': #{
		pl_suffix =  'ew';
	else: #{
		pl_suffix = 'u'
	#}

	forms['imp.p2.mf.sg'] = weak_vowel_forms(v[0] + r[0] + r[1] + v[1] , v[0] + r[0] + r[1] + presuff_sg_vowel , '-', tv);
	forms['imp.p2.mf.pl'] = weak_vowel_forms(v[0] + r[0] + r[1] + pl_suffix , v[0] + r[0] + r[1] + pl_suffix , '-', tv);

	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{

		forms = weak_past(stem['root'], stem['vowel_perf'], stem['trans']);
		forms.update(weak_pres(stem['root'], stem['vowel_impf'], stem['trans']));
		forms.update(weak_imp(stem['root'], stem['vowel_impf'], stem['trans']));
		if stem['pp'] != '' : #{
			forms.update(weak_pp(stem['root'], stem['vowel_perf'], stem['pp']));
# pprs
	#}

	return forms;

#}


