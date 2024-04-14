
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "times"
plt.rcParams["font.size"] = 15

# data file paths
protocol_i_fp = '2p_protocol_i_data_dealer-ring_2P_275RB_edabitTrue_32slices.csv'
protocol_ii_fp = '2p_protocol_ii_data_dealer-ring_2P_275RB_edabitTrue_32slices.csv'
protocol_iii_fp = '2p_protocol_iii_data_dealer-ring_2P_275RB_edabitTrue_32slices.csv'

# read csv files
protocol_i = pd.read_csv(protocol_i_fp)
protocol_ii = pd.read_csv(protocol_ii_fp)
protocol_iii = pd.read_csv(protocol_iii_fp)

# total Time
print("Plotting Total Time")
plt.figure()
plt.plot(protocol_i["Number Slices"], protocol_i["2p_protocol_i Time (s)"], label="Protocol I", color="red")
plt.plot(protocol_ii["Number Slices"], protocol_ii["2p_protocol_ii Time (s)"], label="Protocol II", color="orange")
plt.plot(protocol_iii["Number Slices"], protocol_iii["2p_protocol_iii Time (s)"], label="Protocol III", color="green")
plt.yscale('log')
plt.title("Total Time")
plt.xlabel("Number of Slices")
plt.ylabel("Time (s)")
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0, frameon=False)
plt.savefig('plots/results_time.eps', bbox_inches="tight")
plt.savefig('plots/results_time.png', bbox_inches="tight")

# total Communication Rounds
print("Plotting Total Communication Rounds")
plt.figure()
plt.plot(protocol_i["Number Slices"], protocol_i["2p_protocol_i Rounds"], label="Protocol I", color="red")
plt.plot(protocol_ii["Number Slices"], protocol_ii["2p_protocol_ii Rounds"], label="Protocol II", color="orange")
plt.plot(protocol_iii["Number Slices"], protocol_iii["2p_protocol_iii Rounds"], label="Protocol III", color="green")
plt.yscale('log')
plt.title("Total Communication Rounds")
plt.xlabel("Number of Slices")
plt.ylabel("Communication Rounds")
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0, frameon=False)
plt.savefig('plots/results_communication_rounds.eps', bbox_inches="tight")
plt.savefig('plots/results_communication_rounds.png', bbox_inches="tight")


# single Party Data Sent
print("Plotting Data Sent Per Party")
plt.figure()
plt.plot(protocol_i["Number Slices"], protocol_i["2p_protocol_i Single Party Data (MB)"], label="Protocol I", color="red")
plt.plot(protocol_ii["Number Slices"], protocol_ii["2p_protocol_ii Single Party Data (MB)"], label="Protocol II", color="orange")
plt.plot(protocol_iii["Number Slices"], protocol_iii["2p_protocol_iii Single Party Data (MB)"], label="Protocol III", color="green")
plt.yscale('log')
plt.title("Data Sent Per Party")
plt.xlabel("Number of Slices")
plt.ylabel("Data Sent (MB)")
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left", borderaxespad=0, frameon=False)
plt.savefig('plots/results_data_sent.eps', bbox_inches="tight")
plt.savefig('plots/results_data_sent.png', bbox_inches="tight")