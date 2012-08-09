#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## hollow verbs
## ----------------------------------------------------------------------------##


def hollow_sg_forms (form_sg, form_sg_suff, r, ok, tv): #{
# past & impf sg forms end with consontant(s)
# only past.p3.sg.f have different forms with and without suffixes


	if ok == 'ok' : #{
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


def hollow_pl_forms (form_pl, form_pl_suff, r, tv): #{
# all past forms end with a vowel
# different with/without suffix forms only for past.p1.mf.pl

	if tv == 'iv' : #{
	 	forms = [(form_pl, '-', r),
	 		 (form_pl_suff, 'S__qtalt/x', r)];
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


def hollow_patt1_pp(root, vowels, pref): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	forms = {};
	
	forms['pp.m.sg'] = [(pref + r[0] + 'ju' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(pref + r[0] + 'ju' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(pref + r[0] + 'ju' + r[2] + 'in', '-', '-')] ;

	return forms;

#}


# Not all intransitive hollow verbs have pprs
# pattern: KeJJeB, KeJBa, KeJBin (but sajjem, sajma, sajmin)
def hollow_patt1_pprs(root, vowel): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pp.m.sg'] = [(r[0] + vowel + 'jje' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + vowel + 'j' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(r[0] + vowel + 'j' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


def hollow_patt1_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	forms['past.p3.m.sg'] = hollow_sg_forms(r[0] + v[0] + r[2], r[0] + v[0] + r[2], '-', 'ek', tv);
# additional forms for past.p3.m.sg + indirect object suffixes
# TYM p. 211: hollow verbs can insert or omit stressed i before 3rd pers. fem. and pl
# ġabilha, ġabilhom, but also ġablha, ġablhom
# seems that's a pure theory
##	forms['past.p3.m.sg'] += [(r[0] + v[0] + r[2], 'S__fetħ/ilha', r)];


	forms['past.p3.f.sg'] = hollow_sg_forms(r[0] + v[0] + r[2] + 'et', r[0] + v[0] + r[2] + 'it', '-', 'ek', tv);
# daritlha? daritilha? both?

	# This form is obtained by the insertion of 'o' for second radical 'w' and
	# 'i' for second radical 'j'
	if r[1] == 'w': #{
		link_vowel = 'o';
		ok = 'ok';
	elif r[1] == 'j': #{
		link_vowel = 'i';
		ok = 'ek';
	#}

	forms['past.p2.mf.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-', ok, tv);	
	forms['past.p1.mf.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-', ok, tv);	

	forms['past.p2.mf.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'tu', r[0] + link_vowel + r[2] + 'tu', '-', tv);
	forms['past.p1.mf.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'na', r[0] + link_vowel + r[2] + 'nie', '-', tv);

# v[0]/'a'
	forms['past.p3.mf.pl'] = hollow_pl_forms(r[0] + v[0] + r[2] + 'u', r[0] + v[0] + r[2] + 'u', '-', tv);


#	# This is not in the grammar, but it seems that 'ie' (mutation of long 'a')
#	# does not have the usual rules applied
#	if v[0] == 'ie': #{
#
#		# I'm not so  sure
#		# usually past.p1.mf.pl share rules with 
#		# past.p2.mf.pl, past.p2.mf.sg, past.p1.mf.sg
#		# and r[0] + 'ie' + r[2] + 'na' can be
#		# past.3.sg.m + prn.p1.mf.pl d.o. 
#
#		# or maybe past.3.sg.m + prn.p1.mf.pl d.o. is
#		# r[0] + 'i/o' + r[2] + 'na' too?
#
#		forms['past.p1.mf.pl'] = [(r[0] + 'ie' + r[2] + 'na', '-', '-')];
#		
#		# that's the usual rule though
#		forms['past.p3.mf.pl'] = [(r[0] + 'ie' + r[2] + 'u', '-', '-')];	
	#}

	return forms;
#}


# no ek/ok
def hollow_patt1_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	link_vowel = '';
	if r[1] == 'w': #{
		link_vowel = 'u';
	elif r[1] == 'j': #{
		link_vowel = 'i';
	#}
	ok = 'ek';
		
	forms['imp.p2.mf.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2], r[0] + link_vowel + r[2], '-', ok, tv);
	forms['imp.p2.mf.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'u', r[0] + link_vowel + r[2] + 'u', '-', tv);

	return forms;
#}


# no ek/ok
def hollow_patt1_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}
	ok = 'ek';

	forms = {};

	# The imperfect is obtained by the addition of the usual prefixes (j,t,n) 
	# to the first radical of the verb with the stressed long vowel 'u' or 'i'
	# between the first and third radicals. And 'u' for the plural.

	#	- This is all well and good, but there is some ambiguity because we find
	#	- e.g. iddur/ddur in the corpus, but not jddur. On the other hand,
	#	- we find 'trid' and 'jrid' in the corpus

	link_vowel = '';
	if r[1] == 'w': #{
		link_vowel = 'u';
	elif r[1] == 'j': #{
		link_vowel = 'i';
	#}
											# (!) form not attested

	form_sg = r[0] + link_vowel + r[2];

	forms['pres.p3.m.sg'] = hollow_sg_forms('i' + form_sg, 'i' + form_sg, 'LR', ok, tv);		# irid		isir		idur
	forms['pres.p3.m.sg'] += hollow_sg_forms('j' + form_sg, 'j' + form_sg, 'LR', ok, tv);		# jrid		jsir		jdur
	forms['pres.p3.m.sg'] += hollow_sg_forms('i' + form_sg, 'i' + form_sg, 'RL', ok, tv);		# ~irid		~isir		~idur

	forms['pres.p3.f.sg'] = hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'LR', ok, tv);		# irrid 	issir		iddur
	forms['pres.p3.f.sg'] += hollow_sg_forms(r[0] + form_sg, r[0] + form_sg, 'LR', ok, tv);		# rrid		ssir		ddur
	forms['pres.p3.f.sg'] += hollow_sg_forms('t' + form_sg, 't' + form_sg, 'LR', ok, tv);		# trid		tsir(!)		tdur(!)
	forms['pres.p3.f.sg'] += hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'RL', ok, tv);	# ~irrid	~issir		~iddur

	forms['pres.p2.mf.sg'] = hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'LR', ok, tv);		# irrid 	issir		iddur
	forms['pres.p2.mf.sg'] += hollow_sg_forms(r[0] + form_sg, r[0] + form_sg, 'LR', ok, tv);			# rrid		ssir		ddur
	forms['pres.p2.mf.sg'] += hollow_sg_forms('t' + form_sg, 't' + form_sg, 'LR', ok, tv);			# trid 		tsir(!)		tdur(!)
	forms['pres.p2.mf.sg'] += hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'RL', ok, tv);		# ~irrid	~issir		~iddur

	forms['pres.p1.mf.sg'] = hollow_sg_forms('in' + form_sg, 'in' + form_sg, 'LR', ok, tv);			# inrid		insir		indur
	forms['pres.p1.mf.sg'] += hollow_sg_forms('n' + form_sg, 'n' + form_sg, 'LR', ok, tv);			# nrid		nsir		ndur
	forms['pres.p1.mf.sg'] += hollow_sg_forms('in' + form_sg, 'in' + form_sg, 'RL', ok, tv);		# ~inrid	~insir		~indur


	form_pl = r[0] + link_vowel + r[2] + 'u';

	forms['pres.p3.mf.pl'] = hollow_pl_forms('i' + form_pl, 'i' + form_pl, 'LR', tv);		# iridu		isiru		iduru
	forms['pres.p3.mf.pl'] += hollow_pl_forms('j' + form_pl, 'j' + form_pl, 'LR', tv);		# jridu		jsiru		jduru
	forms['pres.p3.mf.pl'] += hollow_pl_forms('i' + form_pl, 'i' + form_pl, 'RL', tv);		# ~iridu	~isiru		~iduru

	forms['pres.p2.mf.pl'] = hollow_pl_forms('i' + r[0] + form_pl, 'i' + r[0] + form_pl, 'LR', tv);	# irridu	issiru		idduru
	forms['pres.p2.mf.pl'] += hollow_pl_forms(r[0] + form_pl, r[0] + form_pl, 'LR', tv);		# rridu		ssiru		dduru
	forms['pres.p2.mf.pl'] += hollow_pl_forms('t' + form_pl, 't' + form_pl, 'LR', tv);		# tridu		tsiru(!)	tduru(!)
	forms['pres.p2.mf.pl'] += hollow_pl_forms('i' + r[0] + form_pl, 'i' + r[0] + form_pl, 'RL', tv);	# ~irridu	~issiru		~idduru

	forms['pres.p1.mf.pl'] = hollow_pl_forms('in' + form_pl, 'in' + form_pl, 'LR', tv);		# inridu	insiru		induru
	forms['pres.p1.mf.pl'] += hollow_pl_forms('n' + form_pl, 'n' + form_pl, 'LR', tv);		# nridu		nsiru		nduru
	forms['pres.p1.mf.pl'] += hollow_pl_forms('in' + form_pl, 'in' + form_pl, 'RL', tv);		# ~inridu	~insiru		~induru
	
	return forms;
#}



## ----------------------------------------------------------------------------##
## pattern 7
## ----------------------------------------------------------------------------##


# Borg p. 375 


def hollow_patt7_pprs(root, vowel): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pp.m.sg'] = [('mi' + r[0] + 'ju' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [('mi' + r[0] + 'ju' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [('mi' + r[0] + 'ju' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


def hollow_patt7_past(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	forms['past.p3.m.sg'] = hollow_sg_forms('n' + r[0] + v[0] + r[2], 'n' + r[0] + v[0] + r[2], '-', 'ek', tv);
	forms['past.p3.m.sg'] += hollow_sg_forms('in' + r[0] + v[0] + r[2], 'in' + r[0] + v[0] + r[2], 'LR', 'ek', tv);

	forms['past.p3.f.sg'] = hollow_sg_forms('n' + r[0] + v[0] + r[2] + 'et', 'n' + r[0] + v[0] + r[2] + 'it', '-', 'ek', tv);
	forms['past.p3.f.sg'] += hollow_sg_forms('in' + r[0] + v[0] + r[2] + 'et', 'in' + r[0] + v[0] + r[2] + 'it', 'LR', 'ek', tv);

	ok = 'ek';
	if v[0] == 'ie': #{
		link_vowel = 'i';
	elif v[0] == 'a': #{
		link_vowel = 'a';
	#}

	forms['past.p2.mf.sg'] = hollow_sg_forms('n' + r[0] + link_vowel + r[2] + 't', 'n' + r[0] + link_vowel + r[2] + 't', '-', ok, tv);	
	forms['past.p2.mf.sg'] += hollow_sg_forms('in' + r[0] + link_vowel + r[2] + 't', 'in' + r[0] + link_vowel + r[2] + 't', 'LR', ok, tv);	
	forms['past.p1.mf.sg'] = hollow_sg_forms('n' + r[0] + link_vowel + r[2] + 't', 'n' + r[0] + link_vowel + r[2] + 't', '-', ok, tv);	
	forms['past.p1.mf.sg'] += hollow_sg_forms('in' + r[0] + link_vowel + r[2] + 't', 'in' + r[0] + link_vowel + r[2] + 't', 'LR', ok, tv);	

	forms['past.p2.mf.pl'] = hollow_pl_forms('n' + r[0] + link_vowel + r[2] + 'tu', 'n' + r[0] + link_vowel + r[2] + 'tu', '-', tv);
	forms['past.p2.mf.pl'] += hollow_pl_forms('in' + r[0] + link_vowel + r[2] + 'tu', 'in' + r[0] + link_vowel + r[2] + 'tu', 'LR', tv);
	forms['past.p1.mf.pl'] = hollow_pl_forms('n' + r[0] + link_vowel + r[2] + 'na', 'n' + r[0] + link_vowel + r[2] + 'nie', '-', tv);
	forms['past.p1.mf.pl'] += hollow_pl_forms('in' + r[0] + link_vowel + r[2] + 'na', 'in' + r[0] + link_vowel + r[2] + 'nie', 'LR', tv);

	forms['past.p3.mf.pl'] = hollow_pl_forms('n' + r[0] + v[0] + r[2] + 'u', 'n' + r[0] + v[0] + r[2] + 'u', '-', tv);
	forms['past.p3.mf.pl'] += hollow_pl_forms('in' + r[0] + v[0] + r[2] + 'u', 'in' + r[0] + v[0] + r[2] + 'u', 'LR', tv);

	#}

	return forms;
#}


# no ek/ok
def hollow_patt7_imp(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};
	ok = 'ek';
		
	forms['imp.p2.mf.sg'] = hollow_sg_forms('in' + r[0] + v[0] + r[2], 'in' + r[0] + v[0] + r[2], '-', ok, tv);
	forms['imp.p2.mf.pl'] = hollow_pl_forms('in' + r[0] + v[0] + r[2] + 'u', 'in' + r[0] + v[0] + r[2] + 'u', '-', tv);

	return forms;
#}


# no ek/ok
def hollow_patt7_pres(root, vowels, tv): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}
	ok = 'ek';

	forms = {};
	link_vowel = v[0];

	form_sg = r[0] + link_vowel + r[2];

	forms['pres.p3.m.sg'] = hollow_sg_forms('jin' + form_sg, 'jin' + form_sg, 'LR', ok, tv);	
	forms['pres.p3.f.sg'] = hollow_sg_forms('tin' + form_sg, 'tin' + form_sg, 'LR', ok, tv);
	forms['pres.p2.mf.sg'] = hollow_sg_forms('tin' + form_sg, 'tin' + form_sg, 'LR', ok, tv);
	forms['pres.p1.mf.sg'] = hollow_sg_forms('nin' + form_sg, 'nin' + form_sg, 'LR', ok, tv);

	form_pl = r[0] + link_vowel + r[2] + 'u';

	forms['pres.p3.mf.pl'] = hollow_pl_forms('jin' + form_pl, 'jin' + form_pl, 'LR', tv);
	forms['pres.p2.mf.pl'] = hollow_pl_forms('tin' + form_pl, 'tin' + form_pl, 'LR', tv);
	forms['pres.p1.mf.pl'] = hollow_pl_forms('nin' + form_pl, 'nin' + form_pl, 'LR', tv);
	
	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{

		forms = hollow_patt1_past(stem['root'], stem['vowel_perf'], stem['trans']);

		if stem['pprs'] != '' : 
			forms.update(hollow_patt1_pprs(stem['root'], stem['pprs']));
		if stem['pp'] != '' : #{
			forms.update(hollow_patt1_pp(stem['root'], stem['vowel_perf'], stem['pp']));

		forms.update(hollow_patt1_pres(stem['root'], stem['vowel_perf'], stem['trans']));
	#	if stem['trans'] == 'tv':
		forms.update(hollow_patt1_imp(stem['root'], stem['vowel_perf'], stem['trans']));

	#}

	if stem['theme'] == '7' : #{

		forms = hollow_patt7_past(stem['root'], stem['vowel_perf'], stem['trans']);
		forms.update(hollow_patt7_pprs(stem['root'], stem['pprs']));
		forms.update(hollow_patt7_pres(stem['root'], stem['vowel_perf'], stem['trans']));
	#	if stem['trans'] == 'tv':
		forms.update(hollow_patt7_imp(stem['root'], stem['vowel_perf'], stem['trans']));

	#}

	return forms;

#}


