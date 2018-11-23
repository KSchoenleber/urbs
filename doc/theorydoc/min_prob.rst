.. module:: urbs

A minimal optimization model with urbs
======================================
The minimal model in urbs is a simple expansion and dispatch model with only
processes being able to fulfill the given demands. All spatial information is
neglected in this case. The minimal model is already multiple-input/multiple
output (mimo) and the variable vector is takes the following form:

.. math::

   x^{\text{T}}=(\xi, \underbrace{\rho_{ct}}_{\text{commodity~variables}},
   \underbrace{\kappa_{p}, \widehat{\kappa}_{p}, \tau_{pt},
   \epsilon^{\text{in}}_{cpt},
   \epsilon^{\text{out}}_{cpt}}_{\text{process~variables}})

Here, :math:`\xi` represents the total annualized system cost, :math:`\rho_ct`
the amount of commodities :math:`c` taken from a virtual, infinite stock at
time :math:`t`, :math:`\kappa_{vp}` and :math:`\widehat{\kappa}_{vp}` the total
and the newly installed process capacities of processes :math:`p`,
:math:`\tau_{pt}` the operational state of processes :math:`p` at time
:math:`t` and :math:`\epsilon^{\text{in}}_{cpt}` and
:math:`\epsilon^{\text{out}}_{cpt}` the total inputs and outputs of commodities
:math:`c` to and from process :math:`p` at time :math:`t`, respectively.