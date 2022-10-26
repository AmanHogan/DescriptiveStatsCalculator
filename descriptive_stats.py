import matplotlib.pyplot as plt
import pandas as pd


#################################################################################
#
# Class - DescriptiveStats
# FUNCTION: Calculates mean, frequency table, std deviation, and quartiles
# print_data - prints descriptive statistics and frequency table to a .txt file
# create_graphs - creates a histogram and boxplot from data and saves file
#
#################################################################################
class DescriptiveStats:
    ind = 0

    def __init__(self, data_list, num):

        self.num = num
        self.data = pd.DataFrame(data_list)

        # get the names of the columns of data
        self.column_names = list(data_list[0].keys())
        self.column_1 = self.column_names[0]
        self.column_2 = self.column_names[1]

        # calculate descriptive statistics
        self.frequency_table = self.data[self.column_2].value_counts(bins=5)
        self.mean = self.data.mean(numeric_only=True)
        self.median = self.data.median(numeric_only=True)
        self.deviation = self.data.std(numeric_only=True)
        self.q1 = self.data.shape[0]
        self.q1 = self.data[str(self.column_2)].quantile(0.25)
        self.q2 = self.data[str(self.column_2)].quantile(0.50)
        self.q3 = self.data[str(self.column_2)].quantile(0.75)

    ###############################################
    #
    # FUNCTION : create_graphs
    #   Displays histogram and boxplot
    #   Saves the histogram and boxplot
    #
    # PARAMS:
    #   df - Dataframe object
    #   num - 0 for events, 1 for continuous samples
    #
    # RETURNS
    #   None
    #
    ##############################################
    def create_graphs(self, df, num):
        ind = 0

        # if event times are being graphed
        if num == 0:
            bxplt = df.boxplot(column=[self.column_2], return_type="axes", figsize=(6, 6))
            bxplt.set_ylabel("Inter-arrival time (t) [seconds]")
            bxplt.set_xlabel("Data Set")
            bxplt.set_title("Boxplot of Inter-arrival times at Dallas Love Field")
            plt.gcf().savefig("event" + str(ind) + ".png", format="png")

            ind = ind + 1
            hst = df.plot.hist(column=[self.column_2], figsize=(5, 5),
                               title="Histogram of inter-arrival times at Dallas Love Field", bins=10)
            hst.set_xlabel("Inter-arrival time (t) [seconds]")
            hst.set_ylabel("Frequency (f) [#]")
            plt.gcf().savefig("event" + str(ind) + ".png", format="png")

            plt.show()
            plt.close()

        # if a continuous random sample is being graphed
        else:
            bxplt = df.boxplot(column=[self.column_2], return_type="axes", figsize=(6, 6))
            bxplt.set_ylabel("Length of Major US Rivers (m) [Miles]")
            bxplt.set_xlabel("Data Set")
            bxplt.set_title("Boxplot of Major US Rivers in Miles")
            plt.gcf().savefig("object" + str(ind) + ".png", format="png")

            ind = ind + 1
            hst = df.plot.hist(column=[self.column_2], figsize=(5, 5),
                               title="Histogram of Major US Rivers", bins=10)
            hst.set_xlabel("Length of Major US Rivers (m) [Miles]")
            hst.set_ylabel("Frequency (f) [#]")
            plt.gcf().savefig("object" + str(ind) + ".png", format="png")

            plt.show()
            plt.close()

    ###############################################
    #
    # FUNCTION : print_data
    #   Prints descriptive statistics to a file
    #
    # PARAMS:
    #   None
    # RETURNS
    #   None
    #
    ##############################################
    def print_data(self):

        print("___________________FREQUENCY TABLE_______________")
        print("Frequency Table")
        print(str(self.frequency_table))
        print("\n", end="")
        print("___________________MEAN_________________________")
        print(str(self.mean))
        print("\n", end="")
        print("___________________STD DEVIATION_________________")
        print(str(self.deviation))
        print("\n", end="")
        print("___________________QUARTILES_____________________")
        print(f"Q1: {self.q1}")
        print("\n", end="")
        print(f"Q1: {self.q2}")
        print("\n", end="")
        print(f"Q1: {self.q3}")
        print("\n", end="")
        print("__________________________________________________")
