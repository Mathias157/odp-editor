## S1
- Thank you all for coming to hear about my thesis with the.. very catchy title "Soft-linking and ..."
- Hopefully by the end of this thesis the majority in this room will know what that means.

## S2
- The grand challenge motivating today's topic relates to climate change, and how we can keep temperatures within a safe operating space.
- The emissions gap report projects emissions based on current and stated policies,
- and illustrates that there's still a large gap to being on track to reach the emission reduction targets that would lead to a 2 or 1.5 degree warmer world

## S3
- The emissions from the energy consumption is significant, and is here divided into sectors in the stated policies scenario.
- It hints that some sectors might be easier to decarbonise than others,
1. ...and that it is important to also consider other sectors.

## S4
1. The higher decarbonisation rate of the power sector is related to investments in renewable energy and power grids, which hit a 2 B dollar record in 2024 according to Bloomberg 
2. They estimate that this level should more than double immediately to get on track with climate targets,
3. and triple by 2036 and remain at that level until 2050.

## S5
- These are useful numbers, provided by mathematical models
1. the energy system blueprints that models provide can help conceptualise the challenges and solutions of the energy transition
2. They can also support infrastructure companies and producers in making decisions and plans that are robust to a large range of possible futures. 

## S6
- However, it is complex task to make an accurate mathematical depiction of a large-scale energy system and solve it. 
1. This is because such models need to include a lot of temporal data to account for the seasonal and hourly fluctuations of renewable energy, and spatial data to account for the opportunity and costs of evening out the fluctuations of renewable energy through interregional trade.
2. Furthermore, as mentioned previously, if we only look at the power sector we completely neglect the opportunities and costs of inter-sectoral dynamics, such as storing heat and hydrogen instead of electricity, through heat pumps and electrolysers.
3. Finally, the large-scale energy system models that is the topic of today typically follows a linear programming methodology, which simplifies some technical constraints related to economy of scale and the fact that there are costs and constraints to power plants turning repeatedly on and off.  

## S7
4. Those were some of the 'traditional' complexities, but in the future we might not be able to avoid that the list of complexities grows beyond greenhouse gas emissions, which is only one of our ecological crises as shown by the work on planetary boundaries.
5. And behavioural aspects is often quite simplified, which e.g. could be relevant wrt. the roll-out of a certain technology to households.

## S8 
- Hence, modellers apply various methods to reduce the computational complexity of a model while keeping it precise in its description of the problem at hand. 
1. Including temporal-, spatial- and technological aggregation techniques,
2. Heuristic methods that follow a rule-based approach to solving complex problems, e.g. the rolling horizon idea of breaking an optimisation of a full year into weekly problems. 
3. and decomposition of the mathematical formulation of the problem into master- and subproblems

## S9
- I will argue that soft-linking can be seen as another complexity reduction technique
- Soft-linking is the act of combining standalone models that are solved separately through one or several iterations of data exchange,
1. in contrast to hard-linked or integrated models, where the solving process of the coupled models is simultaneous, which increases complexity

## S10
- Some forms of soft-linking could be included in heuristic decomposition techniques, but I would argue that soft-linking of different frameworks could be seen as a less precise complexity reduction technique, with an infinite speed-up potential
- This is due to the fact that optimality is not guaranteed, maybe to even to a lesser extent than heuristic decomposition techniques, but it can shed light on otherwise intractable problems.

## S11
- And when we talk about 'precision' we should also be mindful of the worldview that are assumed by different models: 
1. The economist, Erica Thompson, criticises her colleagues for pursuing 'optimality' - or 'precision' - 
2. and argues that a modeller should expose themselves to several models, or at least multiple scenarios or solutions beyond the optimality gap, in order to deliver more 'accurate' decision support

## S12 
- But of course, increasing precision is still valuable, and this is why the overarching objective of this PhD has been to propose and...
- The work I did touches upon three important sources of complexity related to,
1. weather conditions, 
2. sectoral scope and
3. spatial resolution

## S13 
- As mentioned, these resource adequacy assessments require a lot of weather scenarios to test the to account for extreme events on the long-term.
- Uni-directional studies to evaluate the adequacy of an optimised fleet of capacities is common 
- A bidirectional approach is necessary to explore configurations that are cost-optimal and adequate 
- Pan-European bi-directional studies are more rare 
- No pan-European study have compared bidirectional strategies and included the adequacy of another sector in such a study
- Research gap in a study systematically evaluating different linking methods and their potential impact on results

## S14
- State-of-the-art ESMs often include other sectors explicitly
- Some examples of model couplings across sectorally different models, but no proposed sector agnostic approach
- Demand response has been used to model flexibility from other sectors, but tend to use data from the existing energy system
- A method to aggregate results from a prospective sector coupled model to a demand response model could be a potential soft-linking strategy across sectorally different models
- Research gap in a systematic analysis of a simple soft-linking technique between ESMs and power simulation models

## S15
- Soft-linking techniques have been proposed 
- but this presentation will illustrate they can be complicated 
- meaning model reduction techniques will still be interesting as a ’competing’ approach in many cases
- studies mostly focus on the power system 
- Examples exist where other sectors are optimised, but only for a fixed configuration of the energy carriers. 
- No systematic analysis of how to represent carriers in a sector coupled ESM in addition to altering spatial resolution
- Research gap in a systematic comparison of heat and hydrogen representation in a sector-coupled ESM

## S16
- These research gaps lead to three research questions that all touch on a source of complexity in energy system modelling
- How can...
- How can...
- How can...

## S17
- These questions are covering the following part of the modelling toolchain
- Question III on carrier representation is related to the pre-processing step and investment optimisation 
- Question I concerns the bi-directional evaluation of investment optimisation using results from operational simulations
- and question II addresses a potential soft-linking application between sectorally different models 

## S18
- So, we move on to the methodologies I applied.

## S19
1. Energy system optimisation models and power system simulation models can help answer these questions, so I've used a representative from each discipline: BALMOREL and ANTARES
2. Models assume perfect market conditions in the minimisation of when optimising or simulating supply, transport, storage and conversion of energy
3. BALMOREL requires temporal aggregation, whereas hourly resolution for many scenarios, e.g. weather years, are used for ANTARES
4. Full foresight in BALMOREL, heuristic applied for weekly problems in ANTARES
- BALMOREL could have been used as the simulation model for many scenarios as well, but since one of the challenges in model coupling is the fact that you often need to couple frameworks with different formats, model formulations and data structures, it would be 'cheating' to just do that
- Hence, I applied ANTARES simulator for that part to include this harmonisation challenge in the project. 

## S20
1. Different combinations of optimisations and simulations were used,
2. and i compared methods for each research question
- In the first research question related to the complexity of weather conditions, three bi-directional approaches are tested to update the investment optimisation problem in BALMOREL, based on the adequacy resulting from multi-weather year simulations in ANTARES
- In research question II, BALMOREL simulations with explicit modelling of other sectors are carried out for various scenarios, and compared to the proposed demand response representation in the corresponding ANTARES simulations
- In research question III, various ways to organise heat and hydrogen in the spatial layers of the ESM are compared for various spatial resolutions. 

## S21
- A variety of case studies were used, with various sectoral scopes
- The geographic scopes are mainly European, with the exception of RQIII due to data availability, for example on high-resolution district heating demands
- A net-zero constraint by 2050 is used for RQIII because this stricter approach enhanced spatial effects, whereas the carbon tax allows us to probe how the methods tested in RQI affect the energy trilemma trade-off 
- Finally, 2050 has been the primary focus since these methods are most relevant for prospective studies, but several model years were included in the analysis for RQI 

## S22
- I will now go through each of the research questions, explaining the method variants and main findings

##  S23
- Starting with research question I: "How can..."

## S24
- As mentioned, this research question aims to contribute with methodologies for modellers that want to couple investment optimisation runs to operational simulations, a task that is necessary for TSO's in long-term planning of the system.
- Our hypothesis was that the various approaches in the literature on such bidirectional couplings will lead to different results

## S25
- The first variant is based on capacity credits, inspired by the work of my the work of Heggarty, Alimou and IEA.
- There are different ways to define this metric, but in this thesis, i define the capacity credit as a measure of the technology- or interconnector's ability to contribute to load while accounting for the load time series
- It is based on ANTARES simulations throughout all weather years
- This measure is used for a new equation in BALMOREL where the capacity variable of all technologies and interconnectors, weighted by capacity credit, must be higher than the sum of peak demand and a function that will change based on the loss of load expectancy in a region
- Hence, for a specific region, capacity credits are re-calculated for every iteration, and the right-hand side will increase or decrease, depending if loss of load is either below or above three hours.

## S26
- The second approach is inspired from couplings between macroeconomic models and energy system models, where the annual demand is often decided by the macroeconomic model.
- I call this parameter-based approach the 'fictive demand' method, because it essentially adds demand to the region, for the specific carrier that has a loss of load expectancy higher than 3 hours.
- If the loss of load expectancy drops below 3 hours, this part will decrease again to avoid overinvestments

(could potentially include figure of the function if time allows)

## S27
- Finally, the third variant is what i call the profit signal approach,
1. where a new term is introduced in the BALMOREL objective function comprising the generation variable and the difference in profit of that technology between the two models
2. Since BALMOREL optimise capacities, profits are zero, meaning this reduces to the profit per MWh of ANTARES simulations 
3. this new term essentially decreases the O&M costs of the technology throughout iterations, 
4. but differently so for each technology, which the study that I'm inspired of found effective to harmonise capacities in a coupling of an integrated assessment model to a power system model, and argued this is a more 'endogenous' soft-linking approach compared to a constraint-based approach, as it leaves the solution space unaltered

## S28 
- The main findings of these tests ...

## S29
- Is that we generally see 13-17% more generation capacity at a comparable, 'adequate iteration' compared to the first iteration, where BALMOREL did not receive any incentive
- However, the configuration of the energy system is not the same at this adequate iteration for the various incentive strategies
- The capacity credit approach favours more gas turbine capacity. This can be explained by the definition of the capacity credit i used, which is higher when load is high, where condensing capacities are often in use and renewables will only randomly have potential for generation. 
- This definition didn't succeed in lowering the loss of load expectancy for hydrogen, despite it increasing hydrogen storage capacity. 
- However, if i assume a value of lost load for hydrogen that is similar to electricity, the system is accurate. On the other hand, gas turbine electricity is then used to produce electrolytic hydrogen.
- The fictive demand approach lead to more renewables and transmission capacity, and a larger total generation capacity.
- I explain this by the fact that adding more demand just generally increases capacities as the load profiles are stretched. Of course, this effect is conditional to the potentials of each technology not being fully realised, which means it could be interesting to see what starts to happen when potentials are realised, e.g. by including the heating sector in a follow-up to this study.  
- The profit signal approach was not really promising in my setup, as capacities fluctuated between two inadequate states, 
- This approach was inspired by a study coupling two investment optimisation models, and didn't have a multi-weather year adequacy focus
- I.e.: The models had more similar cost representations than in my case, and the idea that it could be transferred to an adequacy proved wrong.  

## S30
- There are, however, some limitations to the work that I've done ...
- Heat and V2G
- Unit commitment
- Only three methods
- Iteratively adding extreme periods could have been interesting to include in the comparison as it seemed promising in terms costs and emissions

## S31
- Overall, to answer the research question "How can..."
- I conclude that capacity credit method and the fictive demand approach can be effective coupling strategies to find adequate capacities, though with solutions in various corners of the energy trilemma
- I think future research could work on the capacity credit method to account for sector coupling dynamics, for example by including some terms in the constraint for conversion technologies

## S32
- Moving on to the second research question, how can...

## S33
- The motivation for this research question is to develop methods for coupling sectorally different models, e.g. for a TSO that has mainly worked with power system simulations and want to account for sector coupling while keep using the models that their regulators have learned to trust.
- Our hypothesis here was that a demand response model could be used, as it has been historically used in energy system modelling to represent flexibilities from components in other sectors. 
- Maybe it can also be used to represent a whole sector, using model results, to establish a coherent coupling framework for prospective studies.

## S34
1. The approach is to convert BALMOREL simulation results of heat and hydrogen power demands to a model of curtailable and shiftable demand response in ANTARES
2. Hence, we are comparing explicit- and simplified modelling of other sectors

## S35
- One motivation for this method is that you could couple a sector-coupled ESM to a power system simulation tool that simulates several weather years
1. In that case, it would be much less useful if you'd have to simulate the ESM for all weather years, instead of just for one year and then extrapolate. 
- We tested this for a small case study by simulating BALMOREL for a lot of weather years, and then extrapolate the demand response representation from each of those years, to all weather years in ANTARES input
- This means that we can compare a lot of simulations, and figure out if this method works with just one weather year simulated in the ESM

## S36
- So, to the main findings of this research question...

## S37
- These plots illustrate the deviation in power-to-heat and hydrogen demands between the explicit modelling and the aggregated approach 
- It illustrates that the differences can be up to +-50% across the three regions in any of the weather years.
- The differences are slightly lower when comparing the exact years that demand curves were generated from (blue boxes compared to red), indicating that you may not have to run all weather years in the sectorally explicit model.
- My expectation that increasing sectoral complexity - going towards the right-most scenarios on the x-axis here - seems to be proven false 
- We see that the differences in power-to-hydrogen demands are higher than the differences for power-to-heat
- I explain this by the different flexibility characteristics assumed for each sector (which can be challenged): 
- Hydrogen demand related to renewable fuel production can be satisfied at any point in time in BALMOREL, while heat demand must be delivered hourly according to an exogenous profile.
- Consequently, PtH2 production concentrates around periods of high VRE availability. 
- This means fewer unique price levels in the demand curves, which limits the method’s ability to distinguish between different system states, thereby reducing accuracy compared to PtH

## S38
- Moving on to the results in the large-scale, European case study:
- We compared the same difference here - large-scale system in blue, small-scale system in red
- This indicates that the error i was discussing for hydrogen before is amplified - however, the result for heat indicates that the error of the method does not necessarily scale with geographic scope.

## S39
- The limitation of having to do a full simulation with the sectorally explicit model limits the use cases, maybe that simulation will be enough in most cases. 
- Because of this limitation, a constraint and fixed timeseries of power-to-heat and -hydrogen demands might be a simpler way to do the coupling, if it's not necessary to endogenise demand. 
- In this study, we assumed that the modelling of other sectors in BALMOREL is 'true' - that might of course not be the case, as many assumptions and aggregations are made in BALMOREL's representation of sectors
- Finally, the difference between the two models in term of temporal foresight could have amplified the error of the method - BALMOREL has full foresight within the year, ANTARES has myopic. Maybe it would have been a better choice to stick with one model in this case.

## S40
- In conclusion...
- "How can ..."
- Representing the whole heat and hydrogen sector as a curtailable and shiftable demand response works up to 50% accuracy, compared to explicit modelling of those sectors.
- Expected PtH to be more inaccurately captured than PtH2 because of the more detailed modelling in BALMOREL compared to PtH2 - it was the opposite, exactly because of less details (less detailed supply curves - gets aggregated in implementation)
- It requires a simulation in the sectorally explicit model of one full year
- ..so future research could look into constructing these demand directly from the aggregated investment optimisation run, to make the use cases more broad
- This could help coupling sectorally different models, if it's infeasible to do explicit modelling, for example if the focus is on including more details in the model of lower sectoral resolution.
## S41
- Finally, we have research question III, on how carriers should be represented geographically in energy system models

## S42
- This focuses on the pre-processing part of the toolchain, and in this case there was already some studies looking into soft-linking techniques that decompose the problems spatially
- Hence, the more important research gap to support modellers dealing with the source of complexity from space is in this case an analyses of *how* carriers are defined.
- Our hypothesis was that a hierarchical definition, with different resolutions per carrier, could be an efficient way to aggregate

## S43
- The variants that were compared in this case was the following: 
- In both cases, demand for renewable fuels, policy constraints and financial conditions 
- Then in the uniform representation, demand, transport, and investment options for all carriers are at the same regional level
- In the hierarchical representation, demand for heat and investment options for variable renewable energy is put in a higher resolved level, as studies that have previously included these resources and demands at a highly granulated level found the increased resolution to have an impact.

## S44
- So, to the main findings...

## S45
- These are adequacy indicators resulting from the simulation of the whole year for capacities resulting from optimising various resolutions for unifom and hierarchic representations
- Energy not served on the left axes depicted with bars, LOLE on the right depicted with circles
- We see that adequacy indicators are underestimated at coarser resolutions, if we assume that the highest resolution is the 'correct' one.
- The indicators for hydrogen and renewable fuel were zero
- This result also illustrates that a hierarchical representation can reproduce the heat adequacy indicators, as you can see on the right side of the figure. 
- So if focusing on the adequacy of one carrier, it could be an efficient aggregation strategy

## S46
- The adequacy indicators were quite high in the high spatial resolution case, which means that if we applied the bi-directional strategy from RQI it might exacerbate the differences because loss of load is quite high. On the other hand, energy not supplied is relatively low, and the capacities in the low spatial resolution scenario also increase when running it for all hours.
- Another limitation of this study is coming back to the issue with data availability - other studies found higher discrepancies because they studied a region where weather conditions change more than my relatively small case study
- Finally, uniform transport costs were applied, more geograhic details on this could also show larger discrepancies.

## S47
- So, to conclude...
- A hierarchical configuration can ‘reveal’ adequacy indicators for the carrier you are focusing on
- Uniform, high resolution required for analysing adequacy indicators for both electricity and hydrogen 
- Overall results (capacities and costs) remained similar compared to other uncertainties
- Future research could apply a bi-directional approach to find adequate configurations at high spatio-temporal resolution - this idea is based on one of the limitations...

## S48 
- So, to sum all of this up...

## S49
- These contributions combine to support modellers in developing large-scale energy system models in the tool chain from pre-processing to operational runs, and between sectorally different simulations 
1. A hierarchical spatial representation can be used to focus on a specific carrier 
2. The fictive demand or capacity credit approach can be used in a bi-directional link to explore adequate and cost-optimal configurations
3. Demand response could be used as a rough, endogenous representation for other sectors when coupling sectorally different models

## S50
- The general applicability of these recommendations should be discussed...
1. I don't expect the soft-linking techniques to change behaviour if applied in different frameworks with the same input data and model formulation. Of course, that is not often the case entirely, so the methods needs to be tested in practice for the specific case.
2. This logic is also why I am more confident that the sectoral soft-linking technique has a wide applicability, because it was tested across several scenarios and case studies. 
- With regards to the general applicability of software developed...
- Framework for DK spatial resolution configurations: 
  Modularly developed code, could be adapted to the input format of other frameworks with some work
- Soft-linking processing code could be adapted to linking other frameworks, but was developed less modularly, so would require some more work to generalise - I got more aware of the benefit of modular code for wider applicability in the end of my PhD unfortunately

## S51
- I think my work shows that soft-linking should be seen as a tool in the modeller's toolbox among model reduction techniques, as I illustrated that it can make intractable problems tractable. 
- It also implies that you should do spatial aggregation first, and then temporal aggregation, when trying to build a tractable model, as my thesis contains many example of the effect of temporal resolution and spatial 
- Finally, if we compare the various case studies of the thesis, the point i mentioned in the introduction about precision and accuracy, and how using a variety of models or scenarios can increase accuracy and help shed light on the bigger picture:
1. Starting from research question one, where the case study was an interconnected, European, electricity and hydrogen system.
2. Using bi-directional methods to find adequate configurations by model year 2050 resulted in a 13-17% increase in power generation capacity. 
3. This increase pales compared to when you include the heating system in the analysis, which is a scenario comparison you research question II made possible: a 62% increase in generation capacity.
4. If we then compare the results from the Danish system in research question II to the isolated case in research question III, we find a large increase in storage capacities flexibility that an interconnected system provides.
5. Finally, a small increase in hydrogen storage capacity when increasing spatial resolution.
- My take away from this comparison is that accounting for other sectors is the most important when analysing the configuration of the future energy system, and it makes me curious to explore what could happen if we - on top of this case study (interconnected, sector coupled European system) - account for insights from other fields.
- What else are we missing currently?

## S52
- This question is what makes me think that co-operation across fields is the most interesting and most important task for future research 
1. And of course, my first intuition based on the work in the PhD project would be to attempt to do more soft-linking between these fields.
- But that would be the maximal effort, a minimal effort could just be discussion of results which is also being carried out to some extent
- You could ask if I'm not suggesting to develop an integrated assessment model, but I think my key point here is to preserve the 'worldview' that each model contributes with rather than striving to make one unified and probably intractable model
- It could be a way to provide more nuanced and robust decision support, in turn catalysing the green transition

