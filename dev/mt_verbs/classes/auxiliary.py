#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-


## ----------------------------------------------------------------------------##
## auxiliary
## ----------------------------------------------------------------------------##

def auxiliary_forms (stem): #{

	forms = {};

	if stem == 'kien' : #{
		forms['past.p3.m.sg'] = [('kien', '-', '-'),
					 ('kien', 'S__qtalt/x', '-')];
		forms['past.p3.f.sg'] = [('kienet', '-', '-'),
					 ('kienit', 'S__qtalt/x', '-')];
		forms['past.p2.sg'] =  [('kont', '-', '-'),
					('kont', 'S__qtalt/x', '-')];	
		forms['past.p1.sg'] =  [('kont', '-', '-'),
					('kont', 'S__qtalt/x', '-')];
		forms['past.p3.pl'] =  [('kienu', '-', '-'),
					('kienu', 'S__qtalt/x', '-')];
		forms['past.p2.pl'] =  [('kontu', '-', '-'),
					('kontu', 'S__qtalt/x', '-')];
		forms['past.p1.pl'] =  [('konna', '-', '-'),
					('konnie', 'S__qtalt/x', '-')];

		forms['pres.p3.m.sg'] = [('ikun', '-', 'LR'),
					 ('jkun', '-', 'LR'),
					 ('ikun', '-', 'RL'),
					 ('ikun', 'S__qtalt/x', 'LR'), 
					 ('jkun', 'S__qtalt/x', 'LR'),
					 ('ikun', 'S__qtalt/x', 'RL')];
		forms['pres.p3.f.sg'] = [('tkun', '-', '-'),
					 ('tkun', 'S__qtalt/x', '-')];
		forms['pres.p2.sg'] =  [('tkun', '-', '-'),
					('tkun', 'S__qtalt/x', '-')];
		forms['pres.p1.sg'] =  [('inkun', '-', 'LR'),
					('nkun', '-', 'LR'),
					('inkun', '-', 'RL'),
					('inkun', 'S__qtalt/x', 'LR'), 
					('nkun', 'S__qtalt/x', 'LR'),
					('inkun', 'S__qtalt/x', 'RL')];
		forms['pres.p3.pl'] =  [('ikunu', '-', 'LR'),
					('jkunu', '-', 'LR'),
					('ikunu', '-', 'RL'),
					('ikunu', 'S__qtalt/x', 'LR'), 
					('jkunu', 'S__qtalt/x', 'LR'),
					('ikunu', 'S__qtalt/x', 'RL')];
		forms['pres.p2.pl'] =  [('tkunu', '-', '-'),
					('tkunu', 'S__qtalt/x', '-')];
		forms['pres.p1.pl'] =  [('inkunu', '-', 'LR'),
					('nkunu', '-', 'LR'),
					('inkunu', '-', 'RL'),
					('inkunu', 'S__qtalt/x', 'LR'), 
					('nkunu', 'S__qtalt/x', 'LR'),
					('inkunu', 'S__qtalt/x', 'RL')];

		# I'm guessing here
		forms['imp.p2.sg'] = [('kun', '-', '-'),
				      ('kun', 'S__qtalt/x', '-')];
		forms['imp.p2.pl'] = [('kunu', '-', '-'),
				      ('kunu', 'S__qtalt/x', '-')];

	#}

	elif stem == 'kellu' : #{
		forms['past.p3.m.sg'] = [('kellu', '-', '-'),
					 ('kellu', 'S__qtalt/x', '-')];
		forms['past.p3.f.sg'] = [('kellha', '-', '-'),
					 ('kellhie', 'S__qtalt/x', '-')];
		forms['past.p2.sg'] =  [('kellek', '-', '-'),
					('kellek', 'S__qtalt/x', '-')];	
		forms['past.p1.sg'] =  [('kelli', '-', '-'),
					('kelli', 'S__qtalt/x', '-')];
		forms['past.p3.pl'] =  [('kellhom', '-', '-'),
					('kellhom', 'S__qtalt/x', '-')];
		forms['past.p2.pl'] =  [('kellkom', '-', '-'),
					('kellkom', 'S__qtalt/x', '-')];
		forms['past.p1.pl'] =  [('kellna', '-', '-'),
					('kellnie', 'S__qtalt/x', '-')];

		forms['pres.p3.m.sg'] = [('ikollu', '-', 'LR'),
					 ('jkollu', '-', 'LR'),
					 ('ikollu', '-', 'RL'),
					 ('ikollu', 'S__qtalt/x', 'LR'), 
					 ('jkollu', 'S__qtalt/x', 'LR'),
					 ('ikollu', 'S__qtalt/x', 'RL')];
		forms['pres.p3.f.sg'] = [('ikollha', '-', 'LR'),
					 ('jkollha', '-', 'LR'),
					 ('ikollha', '-', 'RL'),
					 ('ikollhie', 'S__qtalt/x', 'LR'), 
					 ('jkollhie', 'S__qtalt/x', 'LR'),
					 ('ikollhie', 'S__qtalt/x', 'RL')];
		forms['pres.p2.sg'] =  [('ikollok', '-', 'LR'),
					('jkollok', '-', 'LR'),
					('ikollok', '-', 'RL'),
					('ikollok', 'S__qtalt/x', 'LR'), 
					('jkollok', 'S__qtalt/x', 'LR'),
					('ikollok', 'S__qtalt/x', 'RL')];
		forms['pres.p1.sg'] =  [('ikolli', '-', 'LR'),
					('jkolli', '-', 'LR'),
					('ikolli', '-', 'RL'),
					('ikolli', 'S__qtalt/x', 'LR'), 
					('jkolli', 'S__qtalt/x', 'LR'),
					('ikolli', 'S__qtalt/x', 'RL')];
		forms['pres.p3.pl'] =  [('ikollhom', '-', 'LR'),
					('jkollhom', '-', 'LR'),
					('ikollhom', '-', 'RL'),
					('ikollhom', 'S__qtalt/x', 'LR'), 
					('jkollhom', 'S__qtalt/x', 'LR'),
					('ikollhom', 'S__qtalt/x', 'RL')];
		forms['pres.p2.pl'] =  [('ikollkom', '-', 'LR'),
					('jkollkom', '-', 'LR'),
					('ikollkom', '-', 'RL'),
					('ikollkom', 'S__qtalt/x', 'LR'), 
					('jkollkom', 'S__qtalt/x', 'LR'),
					('ikollkom', 'S__qtalt/x', 'RL')];
		forms['pres.p1.pl'] =  [('ikollna', '-', 'LR'),
					('jkollna', '-', 'LR'),
					('ikollna', '-', 'RL'),
					('ikollnie', 'S__qtalt/x', 'LR'), 
					('jkollnie', 'S__qtalt/x', 'LR'),
					('ikollnie', 'S__qtalt/x', 'RL')];

	#}

	return forms;

#}


def main(stem): #{

		return auxiliary_forms(stem['stem']);

#}

