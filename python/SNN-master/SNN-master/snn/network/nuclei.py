from .tools import *


class Izhi_Nucleus:
    """
    A set of neurons with (Izhiekievich, 2003) model
        dv/dt = 0.04 * v ^ 2 + 5 * v + 140 - u + I
        du/dt = a * (b * v - u)

        if v >= 30 :
        v <- c
        u <- u + d

    Parameters
    ----------
    n : int
        Number of neurons
    a : float
        Izhiekievich model parameter: time constant of the membrane
    b : float
        Izhiekievich model parameter: sensibility of u wrt to v
    c : float
        Izhiekievich model parameter: v reset value
    d : float
        Izhiekievich model parameter: u incrementation value
    Iext : float, function t -> float
        external input
    label : str
        Label

    Attributes
    ----------
    afference : list
        List of all Nucleus sending projections to self
    historique : dict
        Stock the values of variables over time
    """

    def __init__(self, n, a=0.03, b=0.2, c=-65, d=4,
                 Iext=5, label=None):

        # Stock number of neurons
        self.n = n

        # Stock parameters
        self.a = treat_parameter(a, n, label='a')
        self.b = treat_parameter(b, n, label='b')
        self.c = treat_parameter(c, n, label='c')
        self.d = treat_parameter(d, n, label='d')

        # Stock external input
        self.Iext = treat_callable(Iext, n)

        # Stock label
        self.label = label

        # Initalize external connection list
        self.afference = list()

        # Initialize historic
        self.historique = {'v': np.array([]),
                           'u': np.array([]),
                           'I': np.array([]),
                           'fired': {},
                           't': 0}

    # return the firing rate in Hz
    @property
    def firing_rate(self):
        fired, t = self.historique['fired'], self.historique['t']
        return (1000 / (t * self.n)) * sum([len(list_of_idx)
                                          for list_of_idx in fired.values()])
