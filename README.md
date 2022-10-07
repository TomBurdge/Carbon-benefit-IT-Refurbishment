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
