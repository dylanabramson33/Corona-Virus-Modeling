# Corona-Virus-Modeling
An attempt to see how population movements affect Coronavirus outcomes
In particular, uses the SEIR model with various modifications. My personal favorite, is a cutoff date 

 Dylan Abramson Differential Equations
1 Introduction
On February 2, Donald Trump imposed strict travel restrictions on passengers from China in an attempt to limit the spread of Coronavirus. Soon after, on February 29 these restrictions were extended to Iran. Restrictions now include China, Iran, the UK, Ireland, and the European Schengen area (France, Germany, Italy, and Spain being the countries most impacted in this area). These restrictions have been a major theme in Trump's narrative on the federal government's response to Coronavirus. Trump went as far as to claim, “I do think we were very early, but I also think that we were very smart because we stopped China”. ​In ​this paper, I will attempt to evaluate how travel restrictions can alter the outcomes of the Coronavirus for the United States and restricted countries. I will analyze three situations: no travel restrictions, light to moderate travel restriction, and total travel restriction. I will use what is generally referred to as a metapopulation model to account for the movements of individuals between populations, with an SEIR model underneath. The SEIR model is similar to the SIR model except that it includes E(t) which represents the “exposed” population. The exposed population accounts for individuals who have been exposed to the virus and are contagious but have not yet shown symptoms. This exposed variable is crucial in the analysis as travel rates for exposed and infected individuals vary dramatically for Coronavirus.
2 Modeling Population Movement (Method and Assumptions)
When epidemiologists model the flow of disease through discrete subpopulations they use what are generally referred to as “metapopulation” models. Metapopulation models are graphs with the nodes representing subpopulations (countries in our case) and the edges representing a system of movement between these subpopulations. I will be using a deterministic metapopulation m​odel, which means that the movement between populations does not involve probability. This design choice restricts the predictive power of the following models as individuals don’t travel in a det​erministic fashion. However, this decision makes implementation simpler and still allows us to get a high-level overview of the ways population movements affect disease dynamics. We will be modeling the movement of individuals in the most elementary way possible. Each country will be represented by its own SEIR model. We will assume that America is the central node and that movement can only occur only between America and the other countries of study. For example, our model will account for visitors from America and China traveling back and forth, but will not consider the movement between Italy and China. This assumption drastically reduces the amount of data necessary and limits the computational complexity. To account for the movement of individuals between populations we will include two terms τ xi and ρxi . τ xi represents the per capita rate of travellers that travel to country x from

 America from disease category i . So τ C hinaS would be the per capita daily rate of susceptible people that travel to China from America with respect to America's population. ρxi represents the per capita rate of people that travel to America from country x with respect to country x’s population.
3 The Model
Other Variables:
α = Inverse of incubation period = 0.16 (Peng)
γ = Inverse of mean infection period = 0.5 (Peng) β = Average contact rate = 1 (Peng)
Ny = Population of country c.
Therefore our model for country a given y where y =/ America dSy = −βy *Sy *Iy +(τyS *SUSA )*NUSA/Ny −ρyS *Sy
dEy = βy *Sy *Iy −αEy +(τyE *EUSA )*NUSA/Ny −ρyE *Ey dt
dIy = αEy −γIy +(τyI *IUSA )*NUSA/Ny −ρyI *Iy dt
would be:
dt
Notes on Model:
● If we computed R in the same way that we computed S, E, and I, populations that had
more citizens leaving the country than visitors entering would eventually go to zero given enough time. Therefore we let R = N - S - E - I to ensure that the population of the country remains fixed. This is a reasonable decision as the dynamics of a disease change far quicker than population levels.
● Since S, E, and I are all proportions of populations, in order to get the proportion of travelers with respect to the country they are entering we must multiply by the population of the country of origin and then divide by population of the country of entry. For example, since the population of China is about five times that of America, if 0.1 percent of susceptible people from America go to China that would only represent a 0.02 percent increase in the number of susceptible people in China (assuming that population movements are about equal which the data below shows they are).

 The SEIR model for America is similar except that we must sum over the τ and ρ values of each country of interest:
dS numCountries America = −βUSA *SUSA *IUSA + ∑
numCountries (ρyS *Sy) *Ny/NUSA - ∑
y=0
τyS *SUSA
dt y=0
dEAmerica = βy * Sy * Iy − αEy + ... ^ with E’s substituted for S’s
 dt
dIAmerica =αEy −γIy + .... dt
Notice how tau and rho have been changed to reflect the change of perspective from people leaving a country to people entering.
4 Assumptions,Data Acquisition, and Computation Technique
For this analysis, we will use values of 𝛽 = 1, 𝛾 = 0.5, and 𝛼 = 0.16, that researchers found based on data from China (Peng). The values of 𝛾, and 𝛼 are derived from the disease properties of Coronavirus therefore it is safe to assume these values are close to the same for every country. 𝛽 refers to the average rate of contact in a population, therefore it will vary from country to country. We will assume all countries share a value of 𝛽 but this is almost certainly not true.
To model the effects of outcomes with no travel restrictions in place we will use historical airline data to estimate values for 𝜏 and 𝜚. There are a few caveats to consider when finding data for this analysis. The first is that data that lists the country of origin and country of arrival for flights entering and leaving the US will be heavily skewed towards hub countries. For example, many flights will transition to Heathrow ​Airport London before reaching their final destination which would make it appear that more US visitors are travelling to the UK. Therefore we will use data that lists the nationality of citizens that arrive in the US/the final destination of countries for citizens leaving the US. One problem with this is that using this system doesn’t account that some people in the data may be Expats and live in a country other than their country of nationality. Another caveat to consider is that by calculating ​𝜏 and 𝜚 in this fashion, ​we are implicitly assuming that without travel restrictions, travel rates would remain the same as prior to the beginning of the virus. Travel rates would almost certainly decline without restrictions due to natural consumer hestiance but we proceed with caution. Using these numbers is probably the best we can do.

 US Population - ​327,200,000
4 Data
ρyS , ρyE
0.0000580
0.0000792
0.00000338 0.00000695
      y
Italy France Iran Germany
Visit US
1,278,304 1,935,609 <100,000 2,105,073
Population
60,360,000 66,990,000 81,160,000 83,002,000
US visitors
7,000,000 7,200,000 <500,000 5,600,000
τ yS , τ yE,
0.0000515
0.0000530 0.000000736 0.0000412
 China
     2,912,745
      1,386,000,000
    2,912,754 = ​0.00000576 1,386,000,000*365
     3,800,000
    3,800,000 372,200,000*365
0.0000280
=
                                             Source:
https://travel.trade.gov/outreachpages/outbound.general_information.outbound_overview.asp
*Note: Iran was not in the top 50 for either number of people who visit the US or number of people from the US that visit it. Therefore I put the smallest amount listed in the data for each.
Notice how ρyI and τyI are not listed in the table. This is because we compute them by multiplying ρyS by 0.2. This is because around 20% of people with Coronavirus are completely
asymptomatic (Lee). I assume people showing any symptoms will not travel, therefore to calculate ρyI and τyI we multiply the per capita daily travel rate for asymptomatic individuals
by 0.2. This method is applied in all three models. Therefore our analysis will be grounded in tweaking values of 𝜏 and 𝜚 to see what behavior occurs.
For computing results, I used python and matplotlib to apply Euler's method.The code can be found here: https://github.com/dylanabramson33/Corona-Virus-Modeling/blob/master/travelpolicy.py
For every country except China, I set S(0) =1 and E(0), I(0) = 0. For China, I set S(0) = 1 - 1/population, E(0) = 1/population, and I(0) = 0.
  
 5 No Travel Restrictions
  Country
  Peak Infection Percentage
   Day of Peak Infection
China 3.7% Italy 4.4%
France 4.3% Germany 3.7% Iran 4.2% America 3.3%
188.54 267.12
269.27 319.33 274.54 246.01
                                 
 Implications/Comments:
With a peak infection rate and of 3.3% in the US, there would be 11,880,000 cases at peak. With a fatality rate of 1.5% this would yield a lower bound of 178,200 deaths. This is well within the bounds of models presented by the White House so this model is at least somewhat grounded in reality. Also, the x value axis lists days in the 100’s as we used a delta t for eulers of 0.01.
5 Moderate Travel Restrictions/Natural Decline in Travel Rates
We now apply various travel restriction strategies. First, we see how a reduction to 50%, 20%, 10%, and 1%, and .1% normal travel capacity affect outcomes.
  Country
  Peak Infection Percentage
   Day of Peak Infection
China Italy France Germany Iran
3.7% 188.5 4.1% 282.92 4.0% 284.46 3.7% 331.36 3.9% 289.42
                         America
  3.5%
   250.66

 Implications:
Paradoxically, with a 50% decrease in the amount of travel the number of US cases actually observed a peak increase of 0.2%. Every country except China experienced noticeably longer delays in the time to the peak case which aligns with expectations.
 Country
  Peak Infection Percentage
   Day of Peak Infection
China
Italy France Germany Iran
25% Reduction
3.7% 188.53
4.0% 297.49 3.9% 298.68
3.7% 343.76
3.8% 303.43
1% Reduction
3.7% 188.52
3.7% 369.46 3.7% 360.68 3.7% 403.10 3.7% 364.69
                         America
  3.6%
   256.23
 Country
  Peak Infection Percentage
   Day of Peak Infection
China
Italy France Germany Iran
                         America
  3.7%
   285.85

 Implications:
As travel rates decrease, the countries' peak infection percentage approaches Chinas. This is probably because as travel rates decrease, the dynamics of the disease become determined by the parameters 𝛽, 𝛾, and, which are the same for each country. Peak infection also occurs at a later date which aligns with expectations.
6 Total Shutdown of incoming travellers after Fixed Time
If we completely shutdown all incoming travelers at t=0 the model predicts a very boring outcome: no one in any country but China gets sick. Let's instead model what actually occurred in the US. We will allow normal travel until some fixed t value. After this time t, we completely bar entry. This is done by simply adding a conditional in our Euler's method that checks if the cutoff time has occurred. If it has, the values of tau and rho are set to 0.
 
  Country
  Peak Infection Percentage
   Day of Peak Infection
China 3.7%
Italy 4.4% France 4.3% Germany 3.6% Iran 4.2%
188.54
267.12 269.27 319.33 274.54
                         America
  3.3%
   246.01
At first I was nervous that my code was wrong as these values are the exact same as the ones given by the model for doing nothing. To check this, I plugged in the value of t=1. Shockingly, my model predicted significantly different outcomes for this tiny t value. This leads me to believe that the reason shutting down the borders after a fixed time had no effect is that ten days is a lifetime in terms of the spread of an exponential disease. By the time ten days arrived the trajectory of the virus was already determined. At this point shutting down the borders had no effect.
8 Conclusion
The largest source of potential error in our model is our choice of 𝛽. We assumed that all countries had the same disease parameters, so as the rate of travel decreased the outcomes of the countries began to align with each other. In the future, I plan on playing around with this 𝛽 value in a way that reflects the effects of social distancing to see what the model predicts. Another problem with our model was our assumption of homogenous mixing. Travellers in a foreign country will have a lower contact rate with the native members of the population just because tourists are naturally less integrated into the mesh of society.
Despite these shortcomings, I was still impressed with how well this simple model mirrored expectations and provided surprising insights. According to this model, banning movement from other countries actually has no effect on the number of peak cases or the time at which peak cases occur unless the ban occurs incredibly early after the onset of the disease. Additionally, lowering the percent of traffic to the US actually increases the peak number of cases but

 dramatically shifts the time when this peak occurs. These results are a strong indication that the model is probably broken in some fundamental way. That doesn’t mean the model is useless though. For example, seeing that banning movement after a mere ten days has zero impact on the number of cases or peak case time really gives you a greater appreciation for the powers of exponentiation. It also highlights how incredibly difficult it is to accurately predict outcomes in such a highly connected world. With only 5 countries, subtle variations of parameters produced massive results.
Citations
Lee, Bruce Y. “Study: 17.9% Of People With COVID-19 Coronavirus Had No Symptoms.” Forbes​, 18 Mar. 2020,
www.forbes.com/sites/brucelee/2020/03/18/what-percentage-have-covid-19-coronavirus- but-do-not-know-it/#51f012377e90​.
Peng, Liangrong. “Epidemic Analysis of COVID-19 in China by Dynamical Modeling.” ​Arxiv​.
  
