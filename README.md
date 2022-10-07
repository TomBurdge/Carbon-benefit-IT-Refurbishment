<h1>This project is currently in development.</h1>
Returns the carbon benefit of reuse of an IT asset compared to recycling.


<h3>Introduction</h3>

This carbon benefit calculation measures the the **carbon benefit of reusing IT equipment compared to the next owner buying new.**
“Reuse” here refers to when a product that is no longer needed by its owner (“User 1”) is taken over by a new user (“User 2”) who has a need for it, instead of it becoming waste.

Reusing is the second most desirable way to reduce our waste, right after “prevention” of production, according to the EU Waste Framework Directive (Directive 2008/98/EC).  Reuse is, therefore, better than recycling the product, which is the next most likely destination for IT assets at end of useful life for the first user.

This carbon calculation calculates the carbon avoided by reusing assets compared to recycling. 
The calculation provides the carbon benefit in kg CO2e.

We **assume** that User 2, who purchases the used asset, would have bought new if they had not bought a used product. We can then calculate the carbon savings of re-use.

The carbon benefit calculation is a counter-factual conditional statement. A counterfactual conditional statement makes a conditional claim about something that did not happen – ‘if I had not gone on a run at 9:00 a.m., my heartbeat would have been lower at 9:30 a.m.’ 
The carbon benefit calculation’s counter-factional conditional statement says, ‘if you hadn’t re-used your assets through Global resale, the carbon emission, as a result, would have been X kg CO2e higher.’

You can use this calculation to say, ‘By choosing reuse, we avoided X kg CO2e emissions.’

***This is not a carbon offset***, and does not satisfy PAS 2060:2014. 
As such, the components of this calculation  should never be used to claim a carbon offset, or any contribution to carbon neutrality or net zero, by any party.

<h3>Getting Started</h3>

The calculation uses Python. 
The calculation reads CSV files as inputs to return the final results.


<h3>Requirements</h3>
To run this calculation with a clone of the repository, you will need:

- Python installed ony our device.
- Pandas module installed on your device.
- Google Maps API module installed on your device.
- A Google Maps API key.
- Scope 1 & 2 emissions for your facility, preferably to SECR standards.
- Input data on the product type of your IT products.
- A database for new production of IT products by type.


(Note: This last bullet point is extremely laborious to create from scratch. Fortunately, a database valid to the end of 2022 is available to access in English at: https://inrego.com/co2/ and in Swedish at: https://www.ivl.se/publikationer/publikationer/produktdatabaser-miljofordelar-med-aterbruk----klimatfordelar-med-aterbruk-av-it-produkter-samt-metod-for-databasskapande.html 
I have not shared a copy of the database as I am currently enquiring about the terms of the license for this database.)

<h3>Assumptions and Methodology</h3>

In making this calculation, we make the following assumptions:

- A reused IT product is here assumed to have the same potential performance as a new product in the same category.
- The use phase emissions are not included since the reused product is assumed to be used in the same way as a new product would have been used, and the energy use is assumed to be the same. 
- We assume user 2 would have bought a new product, within the same category, if they had not bought the used one.
- It is assumed that the new product, whose production has been avoided, would have been assembled in Asia.
- We assume that the re-use of the product, sold at a lower price than new, does not result in a rebound effect. A rebound effect is where efficiency improvements through re-use of products are offset by growth in consumption and refresh rates.  
- For components, the impact of reconditioning is assumed to be 0. The reason for this is that their processing at re-conditioning requires relatively little input and much less complicated grading and checks than notebooks or laptops.
- Assets that are re-used include those assets whose components are re-used and harvested for another product. Accounting for waste handling of the parts of the product which Global Resale then recycles as waste material could change the calculation, although that is currently beyond the calculation’s scope.
- Calculating the emissions of a journey from our facility is impractical to calculate, given that products are not all sold at the same time, are not always bought and sold by Global Resale, and can travel a widely varying journey. To make an indicative estimation, it is assumed that goods out of our UK facility travel the average distance of a haul from the UK. Since ‘New Production’ is such a high amount compared to the other metrics, this estimate makes a relatively small change to the result. The average distance of a journey by transport type is sourced from the UK Government’s Average length of a haul by type and weight of vehicle RF S0108. To accommodate for the indeterminacies of the estimated distance, the calculation uses the highest distance of average journeys in the last five years that the government statistics provide. Where this calculation would not be appropriate, for facilities outside of the UK, we remove the benefit of avoiding TRANSPORTp in the calculation. In Global Resale’s case, the journey travelled from reconditioning to user 2 will not be higher than transporting the avoided product from Asia to user 1.

The calculation will be inaccurate or potentially misleading when these assumptions are not met. Since these assumptions are generally true, input data becomes more accurate at higher volumes.

