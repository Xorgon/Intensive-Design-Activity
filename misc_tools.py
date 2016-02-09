def incr_ratio(lift, drag, oLift=713.147, oDrag=125.562):
    """ Calculates the ratio of increase for lift and drag """
    return (lift - oLift)/(drag - oDrag)


def drag(mm, gpmm=12.1):
    """ Converts mm values to actual force """
    return gpmm * mm * 9.81 / 1000.0


def downforce(mm, gpmm=19.8):
    """ Converts mm values to actual force """
    return gpmm * mm * 9.81 / 1000.0
