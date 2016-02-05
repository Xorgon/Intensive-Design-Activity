import matplotlib
import numpy as np

plot = matplotlib.pyplot.plot

plateArea = 0.00426667
spikeArea = 0.00317036
currentWidth = 332.21 * 1e-3


def area(width=currentWidth):
    return 0.876 * width + 2 * plateArea


def coeffs(lift, drag, flowV=60.0, area=area(), density=1.225, verbose=True):
    """ Computes and returns an array of CoL and CoD """
    coeffL = (2 * lift) / (flowV ** 2 * density * area)
    coeffD = (2 * drag) / (flowV ** 2 * density * area)
    if verbose:
        print ("Coefficient of lift = " + str(coeffL))
        print ("Coefficient of drag = " + str(coeffD))
        print ("Ratio = " + str(coeffL / coeffD))
    return [coeffL, coeffD]


def incr_ratio(lift, drag, oLift=713.147, oDrag=125.562):
    """ Calculates the ratio of increase for lift and drag """
    return (lift - oLift)/(drag - oDrag)


def density(temp_K, pressure, R=287.0):
    """ Returns the value of air density for some temperature and pressure """
    return pressure / (R * temp_K)


cl, cd = 0, 0
F1, F2 = 0, 0

# 0: inc, 1: cl, 2: cd, 3: F1, 4: F2, 5: flowV
results = np.array(
    [[-3, cl, cd, 19.81, 12.82, 15.2],
     [-6, cl, cd, 19.23, 12.82, 15.2],
     [9, cl, cd, 21.17, 13.89, 15.1],
     [15, cl, cd, 21.17, 13.89, 15.1],
     [12, cl, cd, 21.17, 12.34, 15.1],
     [-15, cl, cd, 17.09, 11.64, 15.2],
     [3, cl, cd, 20.39, 13.24, 15.2],
     [0, cl, cd, 19.81, 7.95, 15.2],
     [0, cl, cd, 20.39, 12.82, 15.1],
     [-9, cl, cd, 18.65, 12.46, 15.2],
     [-12, cl, cd, 17.09, 12.46, 15.2],
     [6, cl, cd, 20.59, 9.85, 15.2],
     [6, cl, cd, 20.59, 13.18, 15.1]])
# 0 lift at -13 incedence
# Stall at ~6-10 deg


def wind_tunnel_test(F1, F2, flowV, temp_K=295,
                     pressure=101.4*1e3, tare_lift=1.874, tare_drag=1.163,
                     weight=1.845):
    """
    Calculates the coefficients of lift and drag based on experimental data.

    returns [coeffL, coeffD]
    """
    lift = F1 - weight - tare_lift
    drag = F2 - tare_drag
    small_area = 1.0/16.0 * area()
    ro = density(temp_K, pressure)
    return coeffs(lift, drag, flowV, small_area, ro, False)


def drag(mm):
    """ Converts mm values to actual force """
    return 12.1 * mm * 9.81 / 1000.0


def downforce(mm):
    """ Converts mm values to actual force """
    return 19.8 * mm * 9.81 / 1000.0


def incs_coeffs(rlts):
    """ Calculates and sets CoL and CoD values for rlts """
    rlts[:, 1:3] = np.transpose(wind_tunnel_test(rlts[:, 3],
                                                 rlts[:, 4],
                                                 rlts[:, 5]))


def res_plot(results, mode="lin"):
    """
    Computes coefficients for lift and drag from results and plots them.

    results -- results as above
    mode -- plotting mode

    modes:
        lin -- linear plot of CoL and CoD against incidence
        polar -- plot of CoL against CoD
    """
    incs_coeffs(results)
    if mode == "lin":
        plot(results[:, 0], results[:, 1], "ro")
        plot(results[:, 0], results[:, 2], "go")
    elif mode == "polar":
        plot(results[:, 1], results[:, 2], "go")
