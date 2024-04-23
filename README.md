# Towards Private Multi-Operator Network Slicing

This repository contains the [code](./src) and [results](./results) from the paper "_Towards Private Multi-Operator Network Slicing_".

## Abstract

Network slicing allows customers to obtain networking resources down to the physical level and enables unprecedented resource isolation and fine-grained control.
Such a technique is gaining adoption in current 5G networks and is poised to be influential in 6G and beyond.
However, slicing may occupy finite spectrum resources, which require network operators to work cooperatively to optimise slice placement.

Such cooperation raises critical privacy concerns.
If mobile network operators share spectrum and customers, sensitive customer information can leak to cooperating operators throughout the slice optimisation process.

To solve this issue, we construct three protocols of varying privacy levels for securely enabling network slicing among different mobile network operators.
Our protocols employ efficient secure multiparty computation techniques to collaboratively optimise slicing without revealing customers' identities or orders.
We implement our protocols for the two-party setting using the MP-SPDZ framework.
Our results highlight that for $32$ slices on two basestations, we can produce allocations in under $5$ms with a balanced security and efficiency requirement.
Under the highest privacy level and similar parameters, our protocol generates a slicing allocation in under $7$s.
Similar to non-private methods, our solution finishes within the $60$s heartbeat period of a Spectrum Access System, allowing for real-time updates with a changing spectrum allocation.

## Code

The code is written using the [MP-SPDZ](https://github.com/data61/MP-SPDZ) DSL which is very similar to python. The code is located in the [src](./src/) directory with file type `*.mpc`. To re-run the experiments and generate the results, you can follow the steps below:

```bash
cd src
make download   # Download the MP-SPDZ framework
make setup      # Setup the MP-SPDZ framework

make run        # Run each protocol with differing parameters (this will not record data)

make results    # Record results from protocol benchmarks
make plot       # Plot the results as seen in the paper
```

## Results

The results used in the paper can be found in the [results](./results/) directory. The results are stored in CSV format and can be used to generate the plots seen in the paper.

## Acknowledgements

This research paper is conducted under the 6G Security Research and Development Project, as led by the Commonwealth Scientific and Industrial Research Organisation (CSIRO) through funding appropriated by the Australian Government’s Department of Home Affairs.
This paper does not reflect any Australian Government policy position.
For more information regarding this Project, please refer to https://research.csiro.au/6gsecurity/.
