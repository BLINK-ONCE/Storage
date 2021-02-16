'''
The unit system.
'''
from .allunits import (
                       # basic units
                       pamp, namp, uamp, mamp, amp,
                       kamp, Mamp, Gamp, Tamp,
                       kelvin,
                       kilogram, # silly to have mkilogram, etc...
                       pmetre, nmetre, umetre, mmetre, metre,
                       kmetre, Mmetre, Gmetre, Tmetre,
                       pmeter, nmeter, umeter, mmeter, meter,
                       kmeter, Mmeter, Gmeter, Tmeter,
                       cmetre, cmeter, # quite commonly used
                       psecond, nsecond, usecond, msecond, second,
                       ksecond, Msecond, Gsecond, Tsecond,
                       pmole, nmole, umole, mmole, mole,
                       kmole, Mmole, Gmole, Tmole,
                       # derived units
                       pcoulomb, ncoulomb, ucoulomb, mcoulomb, coulomb,
                       kcoulomb, Mcoulomb, Gcoulomb, Tcoulomb,
                       pfarad, nfarad, ufarad, mfarad, farad,
                       kfarad, Mfarad, Gfarad, Tfarad,
                       pgram, ngram, ugram, mgram, gram,
                       kgram, Mgram, Ggram, Tgram,
                       pgramme, ngramme, ugramme, mgramme, gramme,
                       kgramme, Mgramme, Ggramme, Tgramme,
                       phertz, nhertz, uhertz, mhertz, hertz,
                       khertz, Mhertz, Ghertz, Thertz,
                       pjoule, njoule, ujoule, mjoule, joule,
                       kjoule, Mjoule, Gjoule, Tjoule,
                       pmolar, nmolar, umolar, mmolar, molar,
                       kmolar, Mmolar, Gmolar, Tmolar,
                       pliter, nliter, uliter, mliter, liter,
                       kliter, Mliter, Gliter, Tliter,
                       plitre, nlitre, ulitre, mlitre, litre,
                       klitre, Mlitre, Glitre, Tlitre,
                       ppascal, npascal, upascal, mpascal, pascal,
                       kpascal, Mpascal, Gpascal, Tpascal,
                       pohm, nohm, uohm, mohm, ohm,
                       kohm, Mohm, Gohm, Tohm,
                       psiemens, nsiemens, usiemens, msiemens, siemens,
                       ksiemens, Msiemens, Gsiemens, Tsiemens,
                       pvolt, nvolt, uvolt, mvolt, volt,
                       kvolt, Mvolt, Gvolt, Tvolt,
                       pwatt, nwatt, uwatt, mwatt, watt,
                       kwatt, Mwatt, Gwatt, Twatt
                       )
from .unitsafefunctions import *
from .unitsafefunctions import __all__ as unitsafefunctions_all

from .fundamentalunits import *
from .fundamentalunits import __all__ as fundamentalunits_all

from .stdunits import *
from .stdunits import __all__ as stdunits_all


__all__ = ['pamp', 'namp', 'uamp', 'mamp', 'amp',
           'kamp', 'Mamp', 'Gamp', 'Tamp',
           'kelvin',
           'kilogram',
           'pmetre', 'nmetre', 'umetre', 'mmetre', 'metre',
           'kmetre', 'Mmetre', 'Gmetre', 'Tmetre',
           'pmeter', 'nmeter', 'umeter', 'mmeter', 'meter',
           'kmeter', 'Mmeter', 'Gmeter', 'Tmeter',
           'cmetre', 'cmeter',
           'psecond', 'nsecond', 'usecond', 'msecond', 'second',
           'ksecond', 'Msecond', 'Gsecond', 'Tsecond',
           'pmole', 'nmole', 'umole', 'mmole', 'mole',
           'kmole', 'Mmole', 'Gmole', 'Tmole',
           # derived units
           'pcoulomb', 'ncoulomb', 'ucoulomb', 'mcoulomb', 'coulomb',
           'kcoulomb', 'Mcoulomb', 'Gcoulomb', 'Tcoulomb',
           'pfarad', 'nfarad', 'ufarad', 'mfarad', 'farad',
           'kfarad', 'Mfarad', 'Gfarad', 'Tfarad',
           'pgram', 'ngram', 'ugram', 'mgram', 'gram',
           'kgram', 'Mgram', 'Ggram', 'Tgram',
           'pgramme', 'ngramme', 'ugramme', 'mgramme', 'gramme',
           'kgramme', 'Mgramme', 'Ggramme', 'Tgramme',
           'phertz', 'nhertz', 'uhertz', 'mhertz', 'hertz',
           'khertz', 'Mhertz', 'Ghertz', 'Thertz',
           'pjoule', 'njoule', 'ujoule', 'mjoule', 'joule',
           'kjoule', 'Mjoule', 'Gjoule', 'Tjoule',
           'pmolar', 'nmolar', 'umolar', 'mmolar', 'molar',
           'kmolar', 'Mmolar', 'Gmolar', 'Tmolar',
           'pliter', 'nliter', 'uliter', 'mliter', 'liter',
           'kliter', 'Mliter', 'Gliter', 'Tliter',
           'plitre', 'nlitre', 'ulitre', 'mlitre', 'litre',
           'klitre', 'Mlitre', 'Glitre', 'Tlitre',
           'ppascal', 'npascal', 'upascal', 'mpascal', 'pascal',
           'kpascal', 'Mpascal', 'Gpascal', 'Tpascal',
           'pohm', 'nohm', 'uohm', 'mohm', 'ohm',
           'kohm', 'Mohm', 'Gohm', 'Tohm',
           'psiemens', 'nsiemens', 'usiemens', 'msiemens', 'siemens',
           'ksiemens', 'Msiemens', 'Gsiemens', 'Tsiemens',
           'pvolt', 'nvolt', 'uvolt', 'mvolt', 'volt',
           'kvolt', 'Mvolt', 'Gvolt', 'Tvolt',
           'pwatt', 'nwatt', 'uwatt', 'mwatt', 'watt',
           'kwatt', 'Mwatt', 'Gwatt', 'Twatt'
           ]
__all__.extend(unitsafefunctions_all)
__all__.extend(fundamentalunits_all)
__all__.extend(stdunits_all)