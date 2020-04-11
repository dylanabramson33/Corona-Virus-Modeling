import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class Country:
    def __init__(self,initial_values,parameters, name):
        """
            initial_values: Dict(string -> float)
            parameters: Dict(String -> float)
        """
        self.initial_values = initial_values
        self.parameters = parameters
        self.name = name

def calculate_travel_population(rate, numberPeople, population2, modifier):
    if (rate*numberPeople*modifier)/population2 > 0:
        return (rate*numberPeople*modifier)/population2
    else:
        return 0



def base_seir_model(countries, america,t):
    dt = t[1] - t[0]

    us_population = america.initial_values['N']

    s_values, e_values, i_values, r_values = [], [], [], []

    #initial values for Us
    s_us = [america.initial_values["S_0"]]
    e_us = [america.initial_values["E_0"]]
    i_us = [america.initial_values["I_0"]]
    r_us = [america.initial_values["R_0"]]

    #append countries initial values to their respective value arrays
    for country in countries:
        s_values.append([country.initial_values["S_0"]])
        e_values.append([country.initial_values["E_0"]])
        i_values.append([country.initial_values["I_0"]])
        r_values.append([country.initial_values["R_0"]])



    for timestep in t[1:]:
        prevS_US = s_us[-1]
        prevE_US = e_us[-1]
        prevI_US = i_us[-1]

        rhoS_us = 0
        rhoE_us = 0
        rhoI_us = 0

        tauS_us = 0
        tauE_us = 0
        tauI_us = 0

        #iterate over each country updating their models individually
        #while also accumulating previous values to update US model
        for i,country in enumerate(countries):
            prevS = s_values[i][-1]
            prevE = e_values[i][-1]
            prevI = i_values[i][-1]

            alpha = country.parameters['alpha']
            beta = country.parameters['beta']
            gamma = country.parameters['gamma']
            exitRate = country.parameters['exitRate']
            enterRate = country.parameters['enterRate']
            population = country.initial_values['N']


            tauS = calculate_travel_population(enterRate,prevS_US*us_population,population, 1)
            tauE = calculate_travel_population(enterRate,prevE_US*us_population,population, 1)
            tauI = calculate_travel_population(enterRate,prevI_US*us_population,population, 0.2)



            rhoS = max(prevS * exitRate,0)
            rhoE = max(prevE * exitRate,0)
            rhoI = max(prevI * exitRate,0)

            #cache values so iteration is not needed when computing US model
            tauS_us += calculate_travel_population(exitRate, prevS * population,us_population, 1)
            tauE_us += calculate_travel_population(exitRate, prevE * population,us_population, 1)
            tauI_us += calculate_travel_population(exitRate, prevI * population,us_population, 0.2)

            rhoS_us += max(enterRate * prevS_US,0)
            rhoE_us += max(enterRate * prevE_US,0)
            rhoI_us += max(enterRate * prevI_US,0)

            tauS = 0
            tauE = 0
            tauI = 0



            rhoS = 0
            rhoE = 0
            rhoI = 0

            #cache values so iteration is not needed when computing US model
            tauS_us += 0
            tauE_us += 0
            tauI_us += 0

            rhoS_us += 0
            rhoE_us += 0
            rhoI_us += 0


            next_S = max(prevS + (-1*beta*prevS*prevI + tauS - rhoS)*dt,-2)
            next_E = max(prevE + (beta*prevS*prevI - alpha*prevE + tauE - rhoE)*dt,-2)
            next_I = max(prevI + (alpha*prevE - gamma*prevI + tauI - rhoI)*dt,-2)
            next_R = 1 - next_S - next_E - next_I

            s_values[i].append(next_S)
            e_values[i].append(next_E)
            i_values[i].append(next_I)
            r_values[i].append(next_R)



        #update americas weights




        alpha = america.parameters['alpha']
        beta = america.parameters['beta']
        gamma = america.parameters['gamma']
        next_S_us = max(prevS_US + (-1*beta*prevS_US*prevI_US + tauS_us - rhoS_us)*dt,-2)
        next_E_us = max(prevE_US + (beta*prevS_US*prevI_US - alpha*prevE_US + tauE_us - rhoE_us)*dt,-2)
        next_I_us = max(prevI_US + (alpha*prevE_US - gamma*prevI_US + tauI_us - rhoI_us)*dt,-2)
        next_R_us = max(1 - next_S_us - next_E_us - next_I_us,-2)

        s_us.append(next_S_us)
        e_us.append(next_E_us)
        i_us.append(next_I_us)
        r_us.append(next_R_us)




    plots = []
    for i in range(len(countries)):
        plot = np.stack([s_values[i], e_values[i], i_values[i], r_values[i]]).T
        plots.append(plot)
    max0 = max(i_values[0])
    max1 = max(i_values[1])
    max2 = max(i_values[2])
    max3 = max(i_values[3])
    max4 = max(i_values[4])
    max5 = max(i_us)
    print(max0, i_values[0].index(max0))
    print(max1, i_values[1].index(max1))
    print(max2, i_values[2].index(max2))
    print(max3, i_values[3].index(max3))
    print(max4, i_values[4].index(max4))
    print(max5, i_us.index(max5))


    plot = np.stack([s_us, e_us, i_us, r_us]).T
    plots.append(plot)

    return plots



# Define parameters
t_max = 500
dt = .01
t = np.linspace(0, t_max, int(t_max/dt) + 1)

china_pop = 1860000000
china_init_values = {"N": china_pop , "S_0" : 1 - 1/386000000, "E_0" : 1/386000000, "I_0" : 0, "R_0" : 0}
china_parameters =  {   "alpha" : 0.16,
                        "beta" : 1,
                        "gamma" : 0.5,
                        "exitRate" : 0.00000576,
                        "enterRate" : 0.0000280,
                    }
china = Country(china_init_values, china_parameters,"china")


italy_pop = 60360000
italy_init_vals = {"N": italy_pop, "S_0" : 1, "E_0" : 0, "I_0" : 0, "R_0" : 0}
italian_parameters = {  "alpha" : 0.16,
                        "beta" : 1,
                        "gamma" : 0.5,
                        "exitRate" : 0.0000580,
                        "enterRate" : 0.0000515,
}
italy = Country(italy_init_vals, italian_parameters,"italy")


france_pop = 66990000
france_init_vals = {"N": france_pop, "S_0" : 1, "E_0" : 0, "I_0" : 0, "R_0" : 0}
france_parameters = {   "alpha" : 0.16,
                        "beta" : 1,
                        "gamma" : 0.5,
                        "exitRate" : 0.0000792,
                        "enterRate" : 0.0000530,
}
france = Country(france_init_vals, france_parameters,"france")


iran_pop = 81160000
iran_init_vals = {"N": iran_pop, "S_0" : 1, "E_0" : 0, "I_0" : 0, "R_0" : 0}
iran_parameters = {     "alpha" : 0.16,
                        "beta" : 1,
                        "gamma" : 0.5,
                        "exitRate" : 0.00000338,
                        "enterRate" : 0.000000736,
}
iran = Country(iran_init_vals, iran_parameters,"iran")

germany_pop = 83002000
germany_init_vals = {"N": germany_pop, "S_0" : 1, "E_0" : 0, "I_0" : 0, "R_0" : 0}
germany_parameters = {  "alpha" : 0.16,
                        "beta" : 1,
                        "gamma" : 0.5,
                        "exitRate" : 0.00000695,
                        "enterRate" : 0.0000412,
}
germany = Country(germany_init_vals, germany_parameters ,"germany")





america_pop = 372200000
america_init_vals = {"N": america_pop, "S_0" : 1, "E_0" : 0, "I_0" : 0, "R_0" : 0}
america_parameters = {"alpha" : 0.16,
                      "beta" : 1,
                      "gamma" : 0.5,}
america = Country(america_init_vals, america_parameters,"america")



# Run simulation
results = base_seir_model([china,italy,france,iran,germany],america,  t)
fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, sharex=True)
fig.suptitle('Cut Off Travel at Day 50')
#
ax1.set_title("China")
ax2.set_title("Italy")
ax3.set_title("France")
ax4.set_title("Germany")
ax5.set_title("Iran")
ax6.set_title("America")




ax1.plot(results[0])
ax2.plot(results[1])
ax3.plot(results[2])
ax4.plot(results[3])
ax5.plot(results[4])
ax6.plot(results[5])


blue_patch = mpatches.Patch(color='blue', label='S(t)')
orange_patch = mpatches.Patch(color='orange', label='E(t)')
green_patch = mpatches.Patch(color='green', label='I(t)')
red_patch = mpatches.Patch(color='red', label='R(t)')
plt.legend(handles=[blue_patch,orange_patch,green_patch, red_patch])
plt.show()
