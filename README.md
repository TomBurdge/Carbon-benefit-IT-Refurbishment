<h1>This project provides a guide to calculating the carbon benefit of reuse of an IT asset compared to recycling.</h1>

Start by reading through this Read Me, then go through the Start Here Jupyter Notebook.
At this point, you will have a preliminary understanding of the calculation.<br><br>
The second notebook, Boavizta-Data-Transformation, transforms a public database for the calculation. If you are interested or wish to scrutinise and improve the calculation, please take a look and I would love to hear your thoughts.<br><br>
The third notebook provides a brief guide to performing the calculation for your own organisation. Please make sure you read the 'Start-Here' notebook before moving to the third, as you will need to know the components of the calculation before you perform it.

<h2>Introduction</h2>

This carbon benefit calculation measures the the **carbon benefit of reusing IT equipment compared to the next owner buying new.**
“Reuse” here refers to when a product that is no longer needed by its owner (“User 1”) is taken over by a new user (“User 2”) who has a need for it, instead of it becoming waste.

Reusing is the second most desirable way to reduce our waste, right after “prevention” of production, according to the EU Waste Framework Directive (Directive 2008/98/EC).  Reuse is, therefore, better than recycling the product, which is the next most likely destination for IT assets at end of useful life for the first user.

This carbon calculation calculates the carbon avoided by reusing assets compared to recycling. 
The calculation provides the carbon benefit in kg CO2e.

We **assume** that User 2, who purchases the used asset, would have bought new if they had not bought a used product. We can then calculate the carbon savings of re-use.

The carbon benefit calculation is a counter-factual conditional statement. A counterfactual conditional statement makes a conditional claim about something that did not happen – ‘if I had not gone on a run at 9:00 a.m., my heartbeat would have been lower at 9:30 a.m.’ 
The carbon benefit calculation’s counter-factional conditional statement says, ‘if you hadn’t re-used your assets, the carbon emission, as a result, would have been X kg CO2e higher.’

You can use this calculation to say, ‘By choosing reuse, we avoided X kg CO2e emissions.’

***This is not a carbon offset***, and does not satisfy PAS 2060:2014. 
As such, the components of this calculation  should never be used to claim a carbon offset, or any contribution to carbon neutrality or net zero, by any party.

<h3>Who is this for?</h3>
This project is for IT Refurbishers, of all sizes, who wish to quantify the environmental benefit they achieve.
IT Refurbishing provides a environmental benefit, but it is often difficult to quantify this benefit for stakeholders.
In the age of sustainability reports, activist investing, and the climate crisis, it is important that refurbishers can effectively communicate their operations' environmental benefits (and costs).

As such, we have decided to share a method to calculate the carbon benefit of refurbishing.
This is a *significantly simplified* version of a carbon calculation that is used in industry.

The calculation, in the form availabe in this project, will work best for small to medium sized Refurbishers.
There are still manual inputs, but so long as you are not calculating a massive number of pickups and volume, this will be usable.
For larger IT refurbishers, this should provide a useful start-point to integrate carbon calulations into your data strategy.

<h2>Getting Started</h2>
To get started, the best place to start is to go through the Jupyter Notebook which provides a step by step through how this calculation works.
Then, try running the code with the sample data.
Then, have a go at running it with your own data.

The calculation uses Python. 
The calculation reads CSV files as inputs to return the final results.

At some points in the main file's code, there are empty variables, to which you should assign your own data (outlined in requirements).


<h3>Requirements</h3>
To run this calculation with a clone of the repository, you will need:

- Python installed on your device.
- Pandas module installed on your device.
- Google Maps API module installed on your device.
- A Google Maps API key.

Data requirements:
- Scope 1 & 2 emissions for your facility, preferably to SECR standards. If you are a small refurbisher, estimates will be adequate.
- Input data on the product type of your IT products (e.g. laptop, or server).

<h2>Assumptions and Methodology</h2>

In making this calculation, we make the following assumptions.<br>
When sharing these figures, it is important to share the assumptions too:

- A reused IT product is here assumed to have the same potential performance as a new product in the same category.
- The use phase emissions are not included since the reused product is assumed to be used in the same way as a new product would have been used, and the energy use is assumed to be the same. 
- We assume user 2 would have bought a new product, within the same category, if they had not bought the used one.
- It is assumed that the new product, whose production has been avoided, would have been assembled in Asia.
- We assume that the re-use of the product, sold at a lower price than new, does not result in a rebound effect. A rebound effect is where efficiency improvements through re-use of products are offset by growth in consumption and refresh rates.  
- Currently, the Google Maps API returns the distance in miles driven from the original facility to the destination. For air and sea miles, this currently remains a manual calculation that we are looking to integrate with APIs. Since ‘New Production’ is such a high amount compared to the other metrics, this estimate makes a relatively small change to the result. The average distance of a journey by transport type is sourced from the UK Government’s Average length of a haul by type and weight of vehicle RF S0108. To accommodate for the indeterminacies of the estimated distance, the calculation uses the highest distance of average journeys in the last five years that the government statistics provide. Where this calculation would not be appropriate, for facilities outside of the UK, we remove the benefit of avoiding TRANSPORTp in the calculation. Assuming the asset travels to Europe or North America from Asia, the journey travelled from reconditioning to user 2 will likely not be higher than transporting the avoided product from Asia to user 1.
- It is assumed that the product will be recycled after its second use, as (we assume) it would have been originally had it not been reused after first use.
- A reused IT product is here assumed to have the same potential performance as a new product in the same category. This includes use span and energy efficiency.

The calculation will be inaccurate or potentially misleading when these assumptions are not met. Since these assumptions are generally true, input data becomes more accurate at higher volumes.

The methodology for this calculation originates in resarch conducted by the IVL. 
In effect, this is a code implementation of the methodology with a greater focus on its relation to the regulations and standards at the time (but constantly changing - please research the latest standards), and a guide to practical implementation.
