.. module:: urbs

Structure of an urbs model
==========================
urbs is an abstract generator for linear optimization problems. Such
problems can in general be written in the following standard form:

.. math::

	\text{min}~c^{\text{T}}x\\
	\text{s.t.}~Ax=b\\
	Bx\leq d.

where :math:`x` is the variable vector, :math:`c` the coefficient vector for
the objective function and :math:`A` and :math:`B` the matrices for the
equality and inequality constraints, respectively. The equality constraints
could also be represented by inequality constraints, which is not done here for
simplicity reasons. The structure of the following parts will be first a
description of :math:`x` and :math:`c` and subsequently a general formulation
of the constraint functions that make up the matrices :math:`A` and :math:`B`
as well as the vectors :math:`b` and :math:`d`. All variables and equations
will be first presented for a minimally complex problem and the optional
additional variables and equations are presented in extra parts. For a detailed
description of the index sets, variables, parameters please refer to:

.. toctree::
   ../implementdoc/sets
   ../implementdoc/variables
   ../implementdoc/parameters