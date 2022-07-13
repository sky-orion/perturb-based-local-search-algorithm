from local_search_operator import *
from utils import improve, calculate_cost


def PLS(instance):
    s = initialization(instance=instance)
    lambdaI = 10
    lambdaO = 10
    sign = False
    gbest = s
    wi = 0
    wo = 0
    operatorlist = [Relocationmove_operator(instance=instance),
                    twoExchangemove_operator(instance=instance),
                    twoOptmove_operator(instance=instance),
                    ArcNodeExchangemove_operator(instance=instance),
                    OrOptmove_operator(instance=instance),
                    # CrossExchangemove_operator(instance=instance, arclenset=2),
                    # CrossExchangemove_operator(instance=instance, arclenset=3)
                    ArbitryCrossExchangemove_operator(instance=instance, fastmode=True)
                    ]
    random_perturbation_operator = random_perturbation(instance=instance)
    removeinsert_perturbation_operator = removeinsert_perturbation(instance=instance)
    globalbest = gbest
    maxiter = 1000
    iter = 0
    while sign is False and iter < maxiter:
        gbest, update = localsearch(s, operatorlist)
        print("iteration {}| gbest cost {:.2f} | s cost {:.2f} ".format(iter,
                                                                                calculate_cost(
                                                                                    gbest)
                                                                                ,
                                                                                calculate_cost(
                                                                                    s),
                                                                                ))
        iter = iter + 1
        if update:
            wi = 0
            wo = 0
            s = gbest
        if wi < lambdaI:
            s = random_perturbation_operator.operate(s)
            print("random_perturbation,wi {},wo {},s {:.2f}".format(wi, wo, calculate_cost(s)))
            wi = wi + 1
        elif wo < lambdaO:
            s = removeinsert_perturbation_operator.operate(s)
            print("removeinsert_perturbation,wi {},wo {},s {:.2f}".format(wi, wo, calculate_cost(s)))
            wi = 0
            wo = wo + 1
        else:
            sign = True
    return gbest


def localsearch(s, operatorlist):
    # print("local search #############")
    for operator in operatorlist:
        news = operator.operate(s, random_choice=False)
        # print(calculate_cost(news))
        if improve(s, news):  # or improve(lastgbest, news)
            return news, True
    return s, False


def main():
    instancename = "p01"
    instance = load_instance(name=instancename)
    bestsolution = PLS(instance=instance)
    print(calculate_cost(bestsolution, True))


if __name__ == '__main__':
    main()
