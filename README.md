# Federation-RL-Simulator

## Implementation for Autonomous MEC Selection in Federated Next-Gen Networks via Deep Reinforcement Learning
Associated Figures and code snippets from https://ieeexplore.ieee.org/document/10437048


This repo introduces the GYM environment created to simulator a task being offloaded to a network. 

From this a RL agent can be trained to make optimal decision of offloading the task to the lowest cost to the user. 

The publication contributions are as follows: 
>
> A distinctive B5G/6G network model featuring intelligent network selection capabilities 
>
> A reinforcement learning model that optimizes network selection by considering diverse criteria. 
>
> Integration of MEC within a federated multi-domain network environment. 
>

If you make use of this code in your publications please cite https://ieeexplore.ieee.org/document/10437048


For this scenario a GYM environment was created along with the use of different algorithms, Boltzmann and Epsilon Greedy. 

In this repo, a few more scenarios are added showing a dynamic environment with different vendor caps, and also a scenario in which the vendors profit is considered rather than the users cost. 

## Installation

This project best runs on linux however any operating system should suffice. 

1. Python 3.7.17 
    
    Python 3.7.17 is needed due to ```tensorflow==2.1.0``` and ```keras-rl2``` ([KerasRL](https://github.com/inarikami/keras-rl2))

    Passing on Ubuntu 22.04 on 3.7.17 ![image](https://github.com/EPFigetakis/Federation-RL-Simulator/actions/workflows/ci.yml/badge.svg)
    
