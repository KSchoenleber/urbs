.. module:: urbs

General optimization model
==========================
A general model in urbs is an intertemporal expansion and dispatch model which
fulfills the specified demands with processes, storages and the capacity for
demand side management (DSM) at every modeled site, as well as the possibility
for energy transfer between sites. Furthermore, energy can be traded with an
external market. For such a model the variable vector takes the following form:

.. math::

   x^{\text{T}}=(\zeta, \underbrace{\rho_{ct}}_{\text{commodity~variables}},
   \underbrace{\kappa_{p}, \widehat{\kappa}_{p}, \tau_{pt},
   \epsilon^{\text{in}}_{cpt},
   \epsilon^{\text{out}}_{cpt}}_{\text{process~variables}}).

Here, :math:`\zeta` represents the total annualized system cost, :math:`\rho_ct`
the amount of commodities :math:`c` taken from a virtual, infinite stock at
time :math:`t`, :math:`\kappa_{vp}` and :math:`\widehat{\kappa}_{vp}` the total
and the newly installed process capacities of processes :math:`p`,
:math:`\tau_{pt}` the operational state of processes :math:`p` at time
:math:`t` and :math:`\epsilon^{\text{in}}_{cpt}` and
:math:`\epsilon^{\text{out}}_{cpt}` the total inputs and outputs of commodities
:math:`c` to and from process :math:`p` at time :math:`t`, respectively.

Costs
"""""
In the minimal model the total cost variable can be split into the following
sum:

.. math::

   \zeta = \zeta_{\text{inv}} + \zeta_{\text{fix}} + \zeta_{\text{var}} +
   \zeta_{\text{fuel}} + \zeta_{\text{env}},

where :math:`\zeta_{\text{inv}}` are the annualized invest costs,
:math:`\zeta_{\text{fix}}` the annual fixed costs, :math:`\zeta_{\text{var}}`
the total variable costs accumulating over one year,
:math:`\zeta_{\text{fuel}}` the accumulated fuel costs over one year and
:math:`\zeta_{\text{env}}` the annual penalties for environmental pollution.
These costs are linked then calculated in the following way:

Annualized invest costs:
