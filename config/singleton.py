"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:singleton.
@Description:This function is decorator singleton function.
"""


def singleton(myClass):
    """
    This function provides only single object creation.
    """
    instances={}
    def get_instance(*args,**kwargs):

        if myClass not in instances:

            instances[myClass]=myClass(*args,**kwargs)

        return instances[myClass]
    return get_instance

