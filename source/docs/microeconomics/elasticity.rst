Elasticity
----------

In economics, elasticity describes the susceptibility :doc:`supply or demand <./supply-and-demand>` in response to a change in price for a certain good or service. The elasticity of a certain good or service depends on various factors, including the type of good or service, availability, cost, the number of substitute goods, etc. 

Calculating Elasticity
~~~~~~~~~~~~~~~~~~~~~~

To calculate **elasticity**, the following formula is used:

.. math:: 
    \varepsilon = \frac{\% \Delta y}{\% \Delta x}

where:
    - :math:`\varepsilon` is **elasticity**
    - :math:`\% \Delta x` is the **percent change of the independent variable**
    - :math:`\% \Delta y` is the **percent change of the dependent variable**

.. tip::
    
    **Percentage Change**, also known as relative change, is calculated with the following formula:

    .. math::
        C = \frac{v_2 - v_1}{v_1} 

    where:
        - :math:`C` is the **percent change**
        - :math:`v_1` is the **initial value**
        - :math:`v_2` is the **final value**

- When :math:`\left| \varepsilon \right| > 1`, the product is **elastic**
- When :math:`\left| \varepsilon \right| < 1`, the product is **inelastic**
- When :math:`\left| \varepsilon \right| = 1`, the product is **unitary elastic**
- When :math:`\left| \varepsilon \right| = \infty`, the product is **perfectly elastic**
- When :math:`\left| \varepsilon \right| = 0`, the product is **perfectly inelastic**

.. figure:: /_static/assets/graphs/econ-graph_elasticity-comparison.png
    :align: center
    :alt: elasticity-comparison
    
    Diagram which depicts the graphs for each scenario of elasticity.


Price Elasticity of Demand 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Price elasticity of demand (PED) is the measure of the change in demand of a product relative to a change in price. It is used by firms to help determine at what price they should set their product at and how much of it they should produce. It is also used by the government to determine the potential effects that imposed :doc:`price controls <./price-controls>` could have on the demand of the good or service. 

Calculating Price Elasticity of Demand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For discrete changes in **price elasticity of demand**, the following formula is used:

.. math::
    \varepsilon_d = \frac{\% \Delta D}{\% \Delta P} 

where:
    - :math:`\varepsilon_d` is the **price elasticity of demand**
    - :math:`\% \Delta D` is the **percent change in quantity demanded**
    - :math:`\% \Delta P` is the **percent change in price**

.. admonition:: Example
    :class: math-example

    Based on the following graph, calculate the **Price Elasticity of Demand** and state whether it is elastic or inelastic. 

    .. image:: /_static/assets/graphs/econ-graph_PED-graph.png
        :scale: 65%
        :align: center
        :alt: inelastic-graph

    **Solution**:

    .. math::
        \varepsilon_d = \frac{\% \Delta D}{\% \Delta P} &= \frac{(5-4)/4}{(10-20)/20} \\
                                                        &= \frac{1/4}{-1/2} \\ 
                                                        &= \boxed{\frac{-1}{2}}

    Since :math:`\varepsilon_d = \left| \frac{-1}{2} \right| < 1`, the demand is inelastic.


Price Elasticity of Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Price elasticity of supply (PES) is the measure of the responsiveness of the supply of a good or service relative to a change in price. In general, firms are inelastic in the short run and elastic in the long run, as it often takes time to adjust to changes in demand. 

There are many factors which can affect the PES of a market, including:
 - **Flexibility of Production** - If a firm is unable to quickly reallocate resources and ramp up production in times of high demand, this will affect the market's supply elasticity.  
 - **Availability of Resources** - If a product requires scarce materials, the firm may not be able to quickly step up production when demand spikes. It may also affect the stability of supply down the line, as the resource could become increasingly expensive, forcing the firm to increase its prices or decrease its production.
 - **Stock Levels** - If a firm has low stock levels in storage, it may not be able to meet demand when it rises. 
 - **Production Timeframes** - If the product takes a long period of time to produce, it will take time before the supplier will be able to increase its output and meet demand. 
 - **Competition** - If there are more competitors in a market, this means that if one firm struggles to meet demand, another firm could come and fill the gap. 

As such, firms continually aim to improve and refine their production process so that they can rapidly increase or decrease production to meet changes in demand and minimize losses and delays. 

Calculating Price Elasticity of Supply
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For discrete changes in **price elasticity of supply**, the following formula is used:

.. math::
    \varepsilon_s = \frac{\% \Delta S}{\% \Delta P} 

where:
    - :math:`\varepsilon_s` is the **price elasticity of supply**
    - :math:`\% \Delta S` is the **percent change in quantity supplied**
    - :math:`\% \Delta P` is the **percent change in price**

.. admonition:: Example
    :class: math-example

    Based on the following graph, calculate the **Price Elasticity of Supply** and state whether it is elastic or inelastic. 

    .. image:: /_static/assets/graphs/econ-graph_PES-graph.png
        :scale: 60%
        :align: center
        :alt: elastic-graph

    **Solution**:

    .. math::
        \varepsilon_s = \frac{\% \Delta S}{\% \Delta P} &= \frac{(12-3)/3}{(12-9)/9} \\
                                                        &= \frac{9/3}{3/9} \\ 
                                                        &= \frac{81}{9} \\ 
                                                        &= \boxed{9}

    Since :math:`\varepsilon_s = \left| 9 \right| > 1`, the supply is elastic.

.. _yed-section:

Income Elasticity of Demand
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Income elasticity of demand (YED) is the susceptibility of demand to the change in consumer income. In other words, it measures the difference in demand for a product among lower income consumers versus those of higher income. Using income elasticity of demand, one can determine the :doc:`type of a good <./type-of-goods>`.

Calculating Income Elasticity of Demand
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For discrete changes in **income elasticity of demand**, the following formula is used:

.. math::
    \epsilon_d = \frac{\% \Delta D}{\% \Delta I}

where:
 - :math:`\epsilon_d` is the **income elasticity of demand**
 - :math:`\% \Delta D` is the **percent change in quantity demanded**
 - :math:`\% \Delta I` is the **percent change in income**


.. seealso::
    - :doc:`Type of Goods <./type-of-goods>`
    - :doc:`Price Controls <./price-controls>`

