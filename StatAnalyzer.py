import sys
import argparse
import numpy as np
from pyspark import SparkContext
import pickle
import math

def txt_toRdd(sc, file):
    inp = sc.textFile(file).map(eval)
    return inp

def distance(x,y):
    return int(math.floor(math.sqrt(x**2 + y**2)/12))

def rdd_toDistance(rdd):
    return rdd.map(lambda arg: (distance(arg[0],arg[1]), arg[2]))

def rdd_toRange(sc, lower, upper, rdd):
    outside_range = [(x, None) for x in range(0,lower)] + [(x, None) for x in range(upper, 100)]
    keys = sc.parallelize(outside_range)
    return rdd.subtractByKey(keys)

def rdd_toShootingPercentage(rdd):
    total = rdd.count()
    print("{} Shots".format(total))
    return (1.*rdd.map(lambda x: x[len(x)-1]).reduce(lambda x,y: x+y))/total

def txt_toShootingPercentage(sc, lower, upper, file):
    rdd = txt_toRdd(sc, file)
    rdd = rdd_toDistance(rdd)
    rdd = rdd_toRange(sc, lower, upper, rdd)
    return rdd_toShootingPercentage(rdd)
