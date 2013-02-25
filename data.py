STATES = { # translate trac terminology to GH issues
		'new': 'open',
		'assigned': 'open',
		'reopened': 'open',
		'closed': 'closed',
	}

LABELS = {# merge some priority classes and components we only used rarely.
	  # Set target label to '' and it will be removed from the label list for GH.
	  # Default behavior is to keep all priority, component, type labels and lowercase them.
		'demos/pychan_demo':'demo',
		'demos/rio_de_hola':'demo',
		'demos/shooter':'demo',
		'docs':'docs',
		'engine':'engine',
		'engine':'engine',
		'engine':'engine',
		'engine/core':'engine',
		'engine/core/audio':'engine',
		'engine/core/controller':'engine',
		'engine/core/eventchannel':'engine',
		'engine/core/gui':'engine',
		'engine/core/loaders/fallout':'engine',
		'engine/core/loaders/native':'engine',
		'engine/core/model':'engine',
		'engine/core/pathfinder':'engine',
		'engine/core/util':'engine',
		'engine/core/vfs':'engine',
		'engine/core/video':'engine',
		'engine/core/video/movie':'engine',
		'engine/core/video/opengl':'engine',
		'engine/core/video/sdl':'engine',
		'engine/core/view':'engine',
		'engine/extensions':'extensions',
		'engine/extensions/pychan':'pychan',
		'release':'release',
		'swig':'swig',
		'tools/atlascreator':'tools',
		'tools/build':'tools',
		'tools/dev':'tools',
		'tools/editor':'tools',
		'utilities':'utilities',

		'blocker':'blocker',
		'critical':'important',
		'major':'',
		'normal':'',
		'minor':'',
		'trivial':'',

		'defect':'bug',
		'enhancement':'enhancement',
		'task':'task',
		'content':'',
		}

MILESTONES = { # assign temporary, unique ID for each milestone
		'0.3.0':'0',
		'0.3.1':'1',
		'0.3.2':'2',
		'0.3.3':'3',
		'0.3.4':'4',
		'0.3.5':'5',
		'0.3.6':'6',
		'0.3.7':'7',
		'0.4.0':'8',
		'0.4.1':'9',
		'0.5.0':'10',
		'2006.0':'11',
		'2006.1':'12',
		'2006.1-r1':'13',
		'2007.0':'14',
		'2007.1':'15',
		'2007.2':'16',
		'2008.0':'17',
		'2008.1':'18',
		'Deleted':'19',
		'Documentation':'20',
		'Proposal':'21',
		}

# map reporter and comment author names to either GH account {'login': username}
# or email address {'email': email@ddress) (only if GH account exists for that mail)
DEFAULT_USER = {'login' : 'fifengine'}
USERNAMES = {
		'anonymous' : {'login' : 'fifengine'},
                'Beliar' : {'login' : 'Beliaar'}, # yes, two 'a'
                'Beliar@gmx.de' : {'login' : 'Beliaar'}, # yes, two 'a'
                'Beliar <KarstenBock@gmx.net>' : {'login' : 'Beliaar'}, # yes, two 'a'
                'Beliar <karstenbock@gmx.net>' : {'login' : 'Beliaar'}, # yes, two 'a'
                'catpig' : {'login' : 'steffen123'},
                'ChrisOelmueller' : {'login' : 'ChrisOelmueller'},
                'chrisoelmueller' : {'login' : 'ChrisOelmueller'},
                'ChrisOelmueller' : {'login' : 'ChrisOelmueller'},
                'christoph' : {'login' : 'siccegge'},
                'christoph_debian' : {'login' : 'siccegge'},
                'christoph@unknown-horizons.org' : {'login' : 'siccegge'},
                'court-jus' : {'login' : 'court-jus'},
                'desophos' : {'login' : 'desophos'},
                'enno4uh' : {'login' : 'enno4uh'},
                'eoc' : {'login' : 'ChrisOelmueller'},
                'fife' : {'login' : 'fifengine'},
                'FIFE' : {'login' : 'fifengine'},
                'greyghost' : {'login' : 'GreyGhost'},
                'GreyGhost' : {'login' : 'GreyGhost'},
                'Grickit' : {'login' : 'grickit'},
                'gscai' : {'login' : 'otinn'},
                'helios2000' : {'login' : 'helios2000'},
                'H0ff1' : {'login' : 'hoffi'},
                'Jesse <manning.jesse@gmail.com>' : {'login' : 'vtchill'},
                'kaschte' : {'login' : 'kaschte'},
                'ketheriel' : {'login' : 'ketheriel'},
                'kili' : {'login' : 'stubb'},
		'KIlian]' : {'login' : 'stubb'},
		'Kilian]' : {'login' : 'stubb'},
                'kinshuksunil' : {'login' : 'kinshuksunil'},
                'Kiryx' : {'login' : 'kiryx'},
                'knutas' : {'login' : 'kennedyshead'},
                'kozmo' : {'login' : 'k0zmo'},
                'LinuxDonald' : {'login' : 'LinuxDonald'},
		'LinuxDonald <linuxdonald@linuxdonald.de>' : {'login' : 'LinuxDonald'},
		'LinuxDonald (OpenAnno)' : {'login' : 'LinuxDonald'},
                'mage' : {'login' : 'mage666'},
                'manuel' : {'login' : 'manuelm'},
                'manue|' : {'login' : 'manuelm'},
                'MasterofJOKers' : {'login' : 'MasterofJOKers'},
                'mbivol' : {'login' : 'mihaibivol'},
                'mesutcank' : {'login' : 'mesutcank'},
                'mihaibivol' : {'login' : 'mihaibivol'},
                'mssssm' : {'login' : 'mssssm'},
                'MSSSSM' : {'login' : 'mssssm'},
                'mtfk' : {'login' : 'mitfik'},
		'MuteX' : {'login' : 'TankOs'},         
                'mvBarracuda' : {'login' : 'mvbarracuda'},
                'mvbarracuda' : {'login' : 'mvbarracuda'},
                'nightraven' : {'login' : 'tschroefel'},
                'Nightraven' : {'login' : 'tschroefel'},
                'nihathrael' : {'login' : 'nihathrael'},
                'Nihathrael' : {'login' : 'nihathrael'},
                'Nihatrael' : {'login' : 'nihathrael'}, # sic (#273)
                'prock' : {'login' : 'prock-fife'},
                'qubodup' : {'login' : 'qubodup'},
                'RainCT' : {'login' : 'RainCT'},
                'Sharkash' : {'login' : 'Vivek-sagar'},
                'sidi' : {'login' : 'sids-aquarius'},
                'spq' : {'login' : 'spq'},
                'squiddy' : {'login' : 'squiddy'},
                'teraquendya' : {'login' : 'teraquendya'},
                'totycro' : {'login' : 'totycro'},
                'totycro@unknown-horizons.org' : {'login' : 'totycro'},
                'tuempl' : {'login' : 'tuempl'},
                'TunnelWicht' : {'login' : 'TunnelWicht'},
                'UnknownScribe' : {'login' : 'DanielStephens'},
                'vdaras' : {'login' : 'vdaras'},
                'vdaras <vasileiosdaras@gmail.com>' : {'login' : 'vdaras'},
                'vtchill' : {'login' : 'vtchill'},
                'wentam' : {'login' : 'wentam'},
                }

UNKNOWN = {
		'anxs' : {'login' : ''}, #?? anxs@justmail.de
                'CheeseSucker' : {'login' : ''}, #?? cheesesucker@sinnsyk.com
                'Cheesesucker' : {'login' : ''}, #?? cheesesucker@sinnsyk.com
                'chewie' : {'login' : ''}, #?? chewie@gmx.net
                'donbachi' : {'login' : ''}, #?? donbachi@bachmor.de
                'icelus' : {'login' : ''}, #?? icelus2k5@gmail.com
                'ismarc' : {'login' : ''}, #?? ismarc31@gmail.com
                'jasoka' : {'login' : ''}, #?? j.jasoka@gmail.com
		'Moritz Beller <moritzbeller@gmx.de>' : {'login' : ''}, #?? mortizfife@googlemail.com
		'mortiz' : {'login' : ''}, #?? mortizfife@googlemail.com
                'joeh' : {'login', ''}, #?? joe.hegarty@gmail.com
                'joe_hegarty' : {'login', ''}, #?? joe.hegarty@gmail.com
                'Joshdan' : {'login', ''}, #?? joshdan@namba1.com
                'jwt' : {'login', ''}, #?? jthickstun@gmail.com
                'Neurogeek' : {'login' : ''}, #?? jesus.riveroa@gmail.com
                'sja' : {'login' : ''}, #?? sja@mail.org
                'skybound' : {'login' : ''}, #?? under.northern.sky@googlemail.com
                'sleek' : {'login' : ''}, #?? dean98@gmail.com
                'Sleek' : {'login' : ''}, #?? dean98@gmail.com
                'NikN' : {'login' : ''}, #?? nihonnik@gmail.com
                'phoku' : {'login' : ''}, #?? klaus.blindert@web.de
                'plcstpierre' : {'login' : ''}, #?? plcstpierre@gmail.com
                'rwilco' : {'login' : ''}, #?? rogerwilco@nerdshack.com
                'Shadowdancer' : {'login' : ''}, #?? gtdev@spearhead.de
                'shales' : {'login' : ''}, #?? geoff.salmon@gmail.com
                'VovanSim' : {'login' : ''}, #?? vovansim@gmail.com
                'vovansim' : {'login' : ''}, #?? vovansim@gmail.com
                'labrat' : {'login' : ''}, #?? Tom.Hey@mail.com

		'.' : {'login' : ''},
		'abeyer' : {'login' :''},
		'abeyer@alum.rpi.edu' : {'login' : ''},
		'Aeromancer <alex@aeromancer.ca>' : {'login' :''},			
		'aldart' : {'login' :''}, 
		'Artur Komarov <artur.komarov@gmail.com>' : {'login' : ''},
		'artur.komarov@gmail.com' : {'login', ''},
		'aspidites' : {'login', ''},
		'austin' : {'login', ''},
		'c-_-' : {'login', ''},
		'dauerflucher' : {'login' : ''},
		'eefano' : {'login' : ''},
		'ElieDeBrauwer' : {'login' : ''},
		'Elie De Brauwer <elie@de-brauwer.be>' : {'login' : ''},
		'Fabian Streitel <fife@rottenrei.be>' : {'login' : ''},
		'Frenchy' : {'login' : ''},
		'homer' : {'login' : ''},
		'ianout' : {'login' : ''},
		'icefire' : {'login' : ''},
		'Irene' : {'login' : ''},
		'janus' : {'login' : ''},
		'josh_root@users.sourceforge.net' : {'login' : ''},
		'kefrens' : {'login' : ''},
		'kiome' : {'login' : ''},
		'kj@conceptt.com' : {'login' : ''},
		'kj@onceptt.com' : {'login' : ''},
		'krytzz@soylent.eu' : {'login' : ''},
		'leander256' : {'login' : ''},
		'Mahfuz <65mahfuz90@gmail.com>' : {'login' : ''},
		'me@thomaskeller.biz' : {'login' : ''},
		'michel' : {'login' : ''},
		'Mildred' : {'login' : ''},
		'mizipzor@gmail.com' : {'login' : ''},
		'Nelson Marques' : {'login' : ''},
		'November' : {'login' : ''},
		'omurcada@gmail.com' : {'login' : ''},
		'or1andov' : {'login' : ''},
		'or1andov/superfluid' : {'login' : ''},
		'ottar' : {'login' : ''},
		'pH5' : {'login' : ''},
		'Pharmb195' : {'login' : ''},
		'philipp.zabel@gmail.com' : {'login' : ''},
		'qbunia' : {'login' : ''},
		'rvoezman' : {'login' : ''},
		'Seven' : {'login' : ''},
		'SirTwist@web.de' : {'login' : ''},
		'skangas@skangas.se' : {'login' : ''},
		'sp3iel' : {'login' : ''},
		'Stefan Kangas <skangas@skangas.se>' : {'login' : ''},
		'stefhoff@go4more.de' : {'login' : ''},
		'TAbracadabra <lobsterbyter@dejazzd.com>' : {'login' : ''},
		'Technomage' : {'login' : ''},
		'technopolitica@gmail.com' : {'login' : ''},
		'tesseract' : {'login' : ''},
		'Thomas Keller <me@thomaskeller.biz>' : {'login' : ''},
		'Thomas Martin <thomas@thescoundrels.net>' : {'login' : ''},
		'trendy' : {'login' : ''},
		'ulrik@greenarrowgames.com' : {'login' : ''},
		'uzec' : {'login' : ''},
		'varnie <varnie29a@mail.ru>' : {'login' : ''},
		'vja@inbox.ru' : {'login' : ''},
		'wenlin' : {'login' : ''},
		'Wuntvor' : {'login' : ''},
		'zenbitz' : {'login' : ''},
                'neXyon' : {'login' : ''},
                }
