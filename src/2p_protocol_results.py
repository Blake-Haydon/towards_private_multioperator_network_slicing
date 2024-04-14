import re
import math
import subprocess
from tqdm import tqdm

# Define a default filepath for MP-SPDZ
MP_SPDZ_VERSION = "0.3.7"
MP_SPDZ_FILEPATH = f"../mp-spdz-{MP_SPDZ_VERSION}"

# MP-SPDZ protocol to use
MP_SPDZ_PROTOCOL = "dealer-ring"
USE_EDABIT = True
MP_SPDZ_EDABIT_FLAG = ""
if USE_EDABIT:
    MP_SPDZ_EDABIT_FLAG = "--edabit"

# Testing constants
N_PARTIES = 2
N_RB = 275
# Number of bits needed to represent N_RB
N_RB_BITS = math.ceil(math.log2(N_RB))
# "Resource Sharing Efficiency in Network Slicing" uses 35 slices for testing
MAX_SLICES = 32


def extract_results(output):
    # Define a regular expression pattern to match the desired format
    time_pattern = r"Time = (\d+\.\d+) seconds"
    data_pattern = r"Data sent = (\d+\.\d+) MB"
    global_data_pattern = r"Global data sent = (\d+\.\d+) MB"
    rounds_pattern = r"in ~(\d+) rounds"

    # Use re.search to find the pattern in the string
    time_match = re.search(time_pattern, output)
    data_match = re.search(data_pattern, output)
    global_data_match = re.search(global_data_pattern, output)
    rounds_match = re.search(rounds_pattern, output)

    # Extract the data from the match
    extracted_time = float(time_match.group(1))
    extracted_data = float(data_match.group(1))
    extracted_global_data = float(global_data_match.group(1))
    extracted_rounds = int(rounds_match.group(1))

    return extracted_time, extracted_data, extracted_global_data, extracted_rounds


print("\nTesting Protocol I")
protocol_name = "2p_protocol_i"
output_filename = f"{protocol_name}_data_{MP_SPDZ_PROTOCOL}_{N_PARTIES}P_{N_RB}RB_edabit{USE_EDABIT}_{MAX_SLICES}slices.csv"
with open(output_filename, "w") as f:
    f.write(
        f"Number Parties,Number RBs,Number Slices,{protocol_name} Time (s),{protocol_name} Single Party Data (MB),{protocol_name} Global Data (MB),{protocol_name} Rounds"
    )
    for num_slices in tqdm(range(2, MAX_SLICES)):
        # Set the command
        command = f"{MP_SPDZ_FILEPATH}/Scripts/compile-run.py {MP_SPDZ_EDABIT_FLAG} -E {MP_SPDZ_PROTOCOL} {protocol_name}.mpc {num_slices}"

        # Run the command in the terminal
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, text=True
        )

        # Extract the results from the output
        time, data, global_data, rounds = extract_results(output)

        f.write("\n")
        f.write(f"{N_PARTIES},{N_RB},{num_slices},{time},{data},{global_data},{rounds}")


print("\nTesting Protocol II")
protocol_name = "2p_protocol_ii"
output_filename = f"{protocol_name}_data_{MP_SPDZ_PROTOCOL}_{N_PARTIES}P_{N_RB}RB_edabit{USE_EDABIT}_{MAX_SLICES}slices.csv"
with open(output_filename, "w") as f:
    f.write(
        f"Number Parties,Number RBs,Number Slices,{protocol_name} Time (s),{protocol_name} Single Party Data (MB),{protocol_name} Global Data (MB),{protocol_name} Rounds"
    )
    for num_slices in tqdm(range(2, MAX_SLICES)):
        # Set the command
        command = f"{MP_SPDZ_FILEPATH}/Scripts/compile-run.py {MP_SPDZ_EDABIT_FLAG} -E {MP_SPDZ_PROTOCOL} {protocol_name}.mpc {num_slices} {N_RB} {N_RB_BITS}"

        # Run the command in the terminal
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, text=True
        )

        # Extract the results from the output
        time, data, global_data, rounds = extract_results(output)

        f.write("\n")
        f.write(f"{N_PARTIES},{N_RB},{num_slices},{time},{data},{global_data},{rounds}")


print("\nTesting Protocol III")
protocol_name = "2p_protocol_iii"
output_filename = f"{protocol_name}_data_{MP_SPDZ_PROTOCOL}_{N_PARTIES}P_{N_RB}RB_edabit{USE_EDABIT}_{MAX_SLICES}slices.csv"
with open(output_filename, "w") as f:
    f.write(
        f"Number Parties,Number RBs,Number Slices,{protocol_name} Time (s),{protocol_name} Single Party Data (MB),{protocol_name} Global Data (MB),{protocol_name} Rounds"
    )
    for num_slices in tqdm(range(2, MAX_SLICES)):
        # Set the command
        command = f"{MP_SPDZ_FILEPATH}/Scripts/compile-run.py {MP_SPDZ_EDABIT_FLAG} -E {MP_SPDZ_PROTOCOL} {protocol_name}.mpc {num_slices} {N_RB} {N_RB_BITS}"

        # Run the command in the terminal
        output = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, text=True
        )

        # Extract the results from the output
        time, data, global_data, rounds = extract_results(output)

        f.write("\n")
        f.write(f"{N_PARTIES},{N_RB},{num_slices},{time},{data},{global_data},{rounds}")
