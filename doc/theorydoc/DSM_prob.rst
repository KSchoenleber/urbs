.. module:: urbs

Demand side management
======================
Demand side management allows for the shifting of demands in time. It thus
gives the model the possibility to divert from the strict restriction that all
demands have to be fulfilled at all timesteps. Demand side management adds two
variables to an urbs problem and the variable vector then reads:

.. math::

   x^{\text{T}}=(\zeta, \underbrace{\rho_{yvct}}_{\text{commodity variables}},
   \underbrace{\kappa_{yvp}, \widehat{\kappa}_{yvp}, \tau_{yvpt},
   \epsilon^{\text{in}}_{yvcpt},
   \epsilon^{\text{out}}_{yvcpt}}_{\text{process variables}},
   \underbrace{\kappa_{yaf}, \widehat{\kappa}_{yaf}, \pi^{\text{in}}_{yaft},
   \pi^{\text{out}}_{yaft}}_{\text{transmission variables}},\underbrace{
   \delta^{\text{up}}_{yvct}, \delta^{\text{down}}_{yvct(tt)}}_
   {\text{DSM variables}}).

The new variable :math:`\delta^{\text{up}}_{yvct}` represent the upshift of the
momentary demand at time :math:`t` and :math:`\delta^{\text{down}}_{yvct(tt)}`
the corresponding downshifts. The downshifts need two time indices as they are
referencing to the corresponding upshift with the first index :math:`t` and the
timesteps they actually occur via the second time index :math:`tt`. The latter
is then restricted to an intervall arouns the reference upshift since loads
cannot in general be shifted indefinitely. As it is modeled in urbs, DSM does
not introduce any costs.

Commodity dispatch constraints
------------------------------
Demand side management changes the vertex rule. Every upshift
:math:`\delta^{\text{up}}_{yvct}` leads to an additional demand, i.e., to an
additional required output of the system, and vice versa for the downshifts. 
Effectively this changes the vertex rule (Kirchhoff's current law) for demand
commodities with DSM to:

.. math::
   &\forall y\in Y,~v\in V,~c \in C_{\text{dem}},~ t \in T_m:\\\\
   &-d_{yvct}-\delta^{\text{up}}_{yvct} \geq \text{CB}(y,v,c,t)\\
   &-d_{yvct}+\sum_{tt\in [t - y_{yvc},t + y_{yvc}]}
   \delta^{\text{down}}_{yvc(tt)t} \geq \text{CB}(y,v,c,t).

The downshift equation requires a little elaboration. Here, the total downshift
occuring at a timestep :math:`t` can be caused by downshifts linked to
different upshifts, which in the notation above occur at times :math:`tt`. All
downshift contributions within the delay time :math:`y_{yvc}` of their
respective upshifts are then summed up.   

DSM variables rule
~~~~~~~~~~~~~~~~~~
This central constraint rule for DSM in urbs links the up- and down shifts of
DSM events. An upshift (multiplied with the DSM efficiency) at time :math:`t`
must be compensated with multiple downshifts during a certain time interval.
The lower and upper bounds of this time interval are given by
:math:`t - y_{yvc}` and :math:`t + y_{yvc}`, where :math:`y_{yvc}` is the delay
time parameter specifying the allowed duration of a DSM event. Inside this time
interval, another time index :math:`tt` is required. It is used to index the
downshift processes that are always linked to one upshift. Of course, the
intervals of several upshifts can overlap. Mathematically, this rule can be
noted like this:

.. math::
   &\forall y\in Y,~v\in V,~c\in C^{\text{DSM}}_{dem},~t\in T_m:\\\\
   &e_{yvc}\delta^{\text{up}}_{yvct}=\sum_{tt\in [t - y_{yvc},t + y_{yvc}]}
   \delta^{\text{down}}_{yvct(tt)},

where :math:`e_{yvc}` is the DSM efficiency. Note here, that the summation is
over the timesteps where the downshifts are occuring as opposed to the vertex
rule above, where the summation is over the timesteps of the corresponding
upshifts.

DSM shift limitations
~~~~~~~~~~~~~~~~~~~~~
DSM shifts are limited in size in both directions. This is modeled by

.. math::
   &\forall y\in Y,~v\in V,~c\in C^{\text{DSM}}_{\text{dem}}, t\in T_m:\\\\
   &\delta^{\text{up}}_{yvct}\leq \overline{K}^{\text{up}}_{yvc}\\\\
   &\sum_{tt\in [t - y_{yvc},t + y_{yvc}]}\delta^{\text{down}}_{yvc(tt)t}\leq
   \overline{K}^{\text{down}}_{yvc},

where again the downshifts are summed over the corresponding upshifts, making
sure that at no time there is a total downshift sum larger than the set maximum
value.

In addition to these limitations on the single shift directions, the total sum
of shifts is also limited in an urbs model via:

.. math::
   &\forall y\in Y,~v\in V,~c\in C^{\text{DSM}}_{\text{dem}}, t\in T_m:\\\\
   &\delta^{\text{up}}_{yvct}+
   \sum_{tt\in [t - y_{yvc},t + y_{yvc}]}\delta^{\text{down}}_{yvc(tt)t} \leq
   \text{max}
   \{\overline{K}^{\text{up}}_{yvc},\overline{K}^{\text{down}}_{yvc}\}.

DSM recovery
~~~~~~~~~~~~
Assuming that DSm is linked to some real physical devices, it is necessary to
allow these devices to have some minimal time between DSM events, where, e.g.,
the ability to perform DSM is recovered. This is modeled in the follwoing way:

.. math::
   &\forall y\in Y,~v\in V,~c\in C^{\text{DSM}}_{\text{dem}}, t\in T_m:\\\\
   & \sum_{tt=t}^{o_{yvc}/\Delta t-1}\delta^{\text{up}}_{yvc(tt)}\leq
   \overline{K}^{\text{up}}_{yvc}\cdot y_{yvc},

where :math:`o_{yvc}` is the recovery time in hours. This constraint limits the
total amount of upshifted energy within the recovery period (lhs) to the
maximum allowed energy shift retained for the maximum amount of allowed
shifting time for one shifting event. This means that only one full shifting
event can occur within the recovery period.

This concludes the demand side management constraints. 
   