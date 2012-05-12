#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## hollow verbs
## ----------------------------------------------------------------------------##

def hollow_pp(root, vowels, pref): #{
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
def hollow_pprs(root, vowel): #{
	r = root.split('-'); # radicals

	forms = {};
	
	forms['pp.m.sg'] = [(r[0] + vowel + 'jje' + r[2], '-', '-')] ;
	forms['pp.f.sg'] = [(r[0] + vowel + 'j' + r[2] + 'a', '-', '-')] ;
	forms['pp.mf.pl'] = [(r[0] + vowel + 'j' + r[2] + 'in', '-', '-')] ;

	return forms;
#}


def hollow_sg_forms (form_sg, form_sg_suff, r, ok): #{
# past & impf sg forms end with consontant(s)
# only past.p3.sg.f have different forms with and without suffixes


	if ok == 'ok' : #{
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


def hollow_pl_forms (form_pl, form_pl_suff, r): #{
# all past forms end with a vowel
# different with/without suffix forms only for past.p1.pl

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


def hollow_past(root, vowels): #{
	r = root.split('-'); # radicals
	v = vowels.split('-'); # vowels

	if r[1] != 'j' and r[1] != 'w': #{
		print >> sys.stderr, 'Hollow verb without second radical as \'w\' or \'j\'';
	#}

	forms = {};

	forms['past.p3.m.sg'] = hollow_sg_forms(r[0] + v[0] + r[2], r[0] + v[0] + r[2], '-', 'ek');
# additional forms for past.p3.m.sg + indirect object suffixes
# TYM p. 211: hollow verbs can insert or omit stressed i before 3rd pers. fem. and pl
# ġabilha, ġabilhom, but also ġablha, ġablhom
# seems that's a pure theory
##	forms['past.p3.m.sg'] += [(r[0] + v[0] + r[2], 'S__fetħ/ilha', r)];


	forms['past.p3.f.sg'] = hollow_sg_forms(r[0] + v[0] + r[2] + 'et', r[0] + v[0] + r[2] + 'it', '-', 'ek');
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

	forms['past.p2.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-', ok);	
	forms['past.p1.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2] + 't', r[0] + link_vowel + r[2] + 't', '-', ok);	

	forms['past.p2.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'tu', r[0] + link_vowel + r[2] + 'tu', '-');
	forms['past.p1.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'na', r[0] + link_vowel + r[2] + 'nie', '-');

# v[0]/'a'
	forms['past.p3.pl'] = hollow_pl_forms(r[0] + v[0] + r[2] + 'u', r[0] + v[0] + r[2] + 'u', '-');


#	# This is not in the grammar, but it seems that 'ie' (mutation of long 'a')
#	# does not have the usual rules applied
#	if v[0] == 'ie': #{
#
#		# I'm not so  sure
#		# usually past.p1.pl share rules with 
#		# past.p2.pl, past.p2.sg, past.p1.sg
#		# and r[0] + 'ie' + r[2] + 'na' can be
#		# past.3.sg.m + prn.p1.pl d.o. 
#
#		# or maybe past.3.sg.m + prn.p1.pl d.o. is
#		# r[0] + 'i/o' + r[2] + 'na' too?
#
#		forms['past.p1.pl'] = [(r[0] + 'ie' + r[2] + 'na', '-', '-')];
#		
#		# that's the usual rule though
#		forms['past.p3.pl'] = [(r[0] + 'ie' + r[2] + 'u', '-', '-')];	
	#}

	return forms;
#}


# no ek/ok
def hollow_imp(root, vowels): #{
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
		
	forms['imp.p2.sg'] = hollow_sg_forms(r[0] + link_vowel + r[2], r[0] + link_vowel + r[2], '-', ok);
	forms['imp.p2.pl'] = hollow_pl_forms(r[0] + link_vowel + r[2] + 'u', r[0] + link_vowel + r[2] + 'u', '-');

	return forms;
#}


# no ek/ok
def hollow_pres(root, vowels): #{
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

	forms['pres.p3.m.sg'] = hollow_sg_forms('i' + form_sg, 'i' + form_sg, 'LR', ok);		# irid		isir		idur
	forms['pres.p3.m.sg'] += hollow_sg_forms('j' + form_sg, 'j' + form_sg, 'LR', ok);		# jrid		jsir		jdur
	forms['pres.p3.m.sg'] += hollow_sg_forms('i' + form_sg, 'i' + form_sg, 'RL', ok);		# ~irid		~isir		~idur

	forms['pres.p3.f.sg'] = hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'LR', ok);		# irrid 	issir		iddur
	forms['pres.p3.f.sg'] += hollow_sg_forms(r[0] + form_sg, r[0] + form_sg, 'LR', ok);		# rrid		ssir		ddur
	forms['pres.p3.f.sg'] += hollow_sg_forms('t' + form_sg, 't' + form_sg, 'LR', ok);		# trid		tsir(!)		tdur(!)
	forms['pres.p3.f.sg'] += hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'RL', ok);	# ~irrid	~issir		~iddur

	forms['pres.p2.sg'] = hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'LR', ok);		# irrid 	issir		iddur
	forms['pres.p2.sg'] += hollow_sg_forms(r[0] + form_sg, r[0] + form_sg, 'LR', ok);			# rrid		ssir		ddur
	forms['pres.p2.sg'] += hollow_sg_forms('t' + form_sg, 't' + form_sg, 'LR', ok);			# trid 		tsir(!)		tdur(!)
	forms['pres.p2.sg'] += hollow_sg_forms('i' + r[0] + form_sg, 'i' + r[0] + form_sg, 'RL', ok);		# ~irrid	~issir		~iddur

	forms['pres.p1.sg'] = hollow_sg_forms('in' + form_sg, 'in' + form_sg, 'LR', ok);			# inrid		insir		indur
	forms['pres.p1.sg'] += hollow_sg_forms('n' + form_sg, 'n' + form_sg, 'LR', ok);			# nrid		nsir		ndur
	forms['pres.p1.sg'] += hollow_sg_forms('in' + form_sg, 'in' + form_sg, 'RL', ok);		# ~inrid	~insir		~indur


	form_pl = r[0] + link_vowel + r[2] + 'u';

	forms['pres.p3.pl'] = hollow_pl_forms('i' + form_pl, 'i' + form_pl, 'LR');		# iridu		isiru		iduru
	forms['pres.p3.pl'] += hollow_pl_forms('j' + form_pl, 'j' + form_pl, 'LR');		# jridu		jsiru		jduru
	forms['pres.p3.pl'] += hollow_pl_forms('i' + form_pl, 'i' + form_pl, 'RL');		# ~iridu	~isiru		~iduru

	forms['pres.p2.pl'] = hollow_pl_forms('i' + r[0] + form_pl, 'i' + r[0] + form_pl, 'LR');	# irridu	issiru		idduru
	forms['pres.p2.pl'] += hollow_pl_forms(r[0] + form_pl, r[0] + form_pl, 'LR');		# rridu		ssiru		dduru
	forms['pres.p2.pl'] += hollow_pl_forms('t' + form_pl, 't' + form_pl, 'LR');		# tridu		tsiru(!)	tduru(!)
	forms['pres.p2.pl'] += hollow_pl_forms('i' + r[0] + form_pl, 'i' + r[0] + form_pl, 'RL');	# ~irridu	~issiru		~idduru

	forms['pres.p1.pl'] = hollow_pl_forms('in' + form_pl, 'in' + form_pl, 'LR');		# inridu	insiru		induru
	forms['pres.p1.pl'] += hollow_pl_forms('n' + form_pl, 'n' + form_pl, 'LR');		# nridu		nsiru		nduru
	forms['pres.p1.pl'] += hollow_pl_forms('in' + form_pl, 'in' + form_pl, 'RL');		# ~inridu	~insiru		~induru
	
	return forms;
#}



def main(stem): #{

	forms = {};

	if stem['theme'] == '1' : #{

		forms = hollow_past(stem['root'], stem['vowel_perf']);

		if stem['pprs'] != '' : 
			forms.update(hollow_pprs(stem['root'], stem['pprs']));
		if stem['pp'] != '' : #{
			forms.update(hollow_pp(stem['root'], stem['vowel_perf'], stem['pp']));

		forms.update(hollow_pres(stem['root'], stem['vowel_perf']));
		forms.update(hollow_imp(stem['root'], stem['vowel_perf']));

	#}

	return forms;

#}


