# Define a default version and filepath for MP-SPDZ
MP_SPDZ_VERSION ?= 0.3.7
MP_SPDZ_FILEPATH ?= ../mp-spdz-$(MP_SPDZ_VERSION)

# Specify protocol for MP-SPDZ
MP_SPDZ_PROTOCOL ?= dealer-ring
USE_EDABIT ?= 1
ifeq ($(USE_EDABIT), 1)
	MP_SPDZ_EDABIT_FLAG = --edabit
endif

N_RB = 275
N_RB_BITS = 9 # as we calculate log2(N_RB)

# Download MP-SPDZ library
download: 
	@echo "Downloading MP-SPDZ library"
	wget https://github.com/data61/MP-SPDZ/releases/download/v$(MP_SPDZ_VERSION)/mp-spdz-$(MP_SPDZ_VERSION).tar.xz
	tar -xvf mp-spdz-$(MP_SPDZ_VERSION).tar.xz -C ../
	rm mp-spdz-$(MP_SPDZ_VERSION).tar.xz

# This only has to be run once to setup mp-spdz and generate
# SSL certificates for each party
setup:
	@echo "Make setup for MP-SPDZ"
	cd $(MP_SPDZ_FILEPATH) && make setup
	@echo "Setting up SSL certificates for each party"
	$(MP_SPDZ_FILEPATH)/Scripts/setup-ssl.sh

# Run all protocol benchmarks
run: 2p_protocol_i 2p_protocol_ii 2p_protocol_iii

# Run separate protocol benchmarks
2p_protocol_i: 2p_protocol_i_4_slices 2p_protocol_i_8_slices 2p_protocol_i_16_slices 2p_protocol_i_32_slices
2p_protocol_ii: 2p_protocol_ii_4_slices 2p_protocol_ii_8_slices 2p_protocol_ii_16_slices 2p_protocol_ii_32_slices
2p_protocol_iii: 2p_protocol_iii_4_slices 2p_protocol_iii_8_slices 2p_protocol_iii_16_slices 2p_protocol_iii_32_slices

# Collect results from MP-SPDZ
results:
	@echo "Collecting results"
	python 2p_protocol_results.py

# Plot results
plot:
	@echo "Plotting results"
	mkdir -p plots
	python 2p_protocol_plot.py

############# 2-party protocols #############

# Protocol I tests
2p_protocol_i_4_slices:
	@echo "--------------------\nRunning 2p_protocol_i.mpc with 4 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_i.mpc 4

2p_protocol_i_8_slices:
	@echo "--------------------\nRunning 2p_protocol_i.mpc with 8 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_i.mpc 8

2p_protocol_i_16_slices:
	@echo "--------------------\nRunning 2p_protocol_i.mpc with 16 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_i.mpc 16

2p_protocol_i_32_slices:
	@echo "--------------------\nRunning 2p_protocol_i.mpc with 32 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_i.mpc 32


# Protocol II tests
2p_protocol_ii_4_slices:
	@echo "--------------------\nRunning 2p_protocol_ii.mpc with 4 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_ii.mpc 4 $(N_RB) $(N_RB_BITS)

2p_protocol_ii_8_slices:
	@echo "--------------------\nRunning 2p_protocol_ii.mpc with 8 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_ii.mpc 8 $(N_RB) $(N_RB_BITS)

2p_protocol_ii_16_slices:
	@echo "--------------------\nRunning 2p_protocol_ii.mpc with 16 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_ii.mpc 16 $(N_RB) $(N_RB_BITS)

2p_protocol_ii_32_slices:
	@echo "--------------------\nRunning 2p_protocol_ii.mpc with 32 SIDs\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_ii.mpc 32 $(N_RB) $(N_RB_BITS)


# Protocol III tests
2p_protocol_iii_4_slices:
	@echo "--------------------\nRunning 2p_protocol_iii.mpc with 4 SIDs and $(N_RB) slots\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_iii.mpc 4 $(N_RB) $(N_RB_BITS)

2p_protocol_iii_8_slices:
	@echo "--------------------\nRunning 2p_protocol_iii.mpc with 8 SIDs and $(N_RB) slots\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_iii.mpc 8 $(N_RB) $(N_RB_BITS)

2p_protocol_iii_16_slices:
	@echo "--------------------\nRunning 2p_protocol_iii.mpc with 16 SIDs and $(N_RB) slots\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_iii.mpc 16 $(N_RB) $(N_RB_BITS)

2p_protocol_iii_32_slices:
	@echo "--------------------\nRunning 2p_protocol_iii.mpc with 32 SIDs and $(N_RB) slots\n"
	$(MP_SPDZ_FILEPATH)/Scripts/compile-run.py $(MP_SPDZ_EDABIT_FLAG) -E $(MP_SPDZ_PROTOCOL) 2p_protocol_iii.mpc 32 $(N_RB) $(N_RB_BITS)
