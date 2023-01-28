from pyspark import SparkConf, SparkContext
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import pyarrow.parquet as pq
import os
from pyspark.sql import SparkSession
import pyspark.sql.types as T
import pyspark.sql.functions as F
from functools import reduce
from pyspark.sql.window import Window