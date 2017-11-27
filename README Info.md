# Distributed Evaluation of Agents

In this problem, we will focus on two-player games, such as rock-paper-scissors, chess, or Dota 2 1v1 mid.
When working on a game-playing AI, we end up running many experiments over time and create many different agents.
In order to track our progress and make decisions, it is critical to evaluate the quality of the bots, by having them play many games against one another.

## Objective

The goal of this task is to create a working distributed system that can evaluate the quality of a given set of game playing agents.
We have a set of test games and agents that we will test your system on.

You can spend up to 10 hours on this problem (does not have to be contiguous). You are expected to produce a working solution. If there are any optimizations that you'd like to add if you had more time, briefly state them in your write up. 

## Details

We provide two abstract interfaces: `Game` and `Agent`.
Your task will be to, given a `Game` and a list of `Agent`s, evaluate the quality of each `Agent`.
To do this, play multiple games between the agents using the function `Game.play(agent1, agent2)`, and compute the [TrueSkill](http://trueskill.org/) of each agent.
We suggest you use the [Python TrueSkill package](https://github.com/sublee/trueskill).

A key requirement for the solution is *scalability*.
For more complex games, it can take hundreds of CPU hours to get a good evaluation.
Your code should be able to **utilize multiple machines** to play games between the agents.

We ask that you don't make any extra assumptions about the `Game` and `Agent` interfaces.
Beyond that, we leave the system usage specification up to you, including the input and output formats.

### Extra limits

Correctness:
- The scoreboard is a critical piece of code that guides decision making; **it is very important that the code is correct**.
- You should assume that `game.play` will sometimes fail.

Games and agents:
- You can assume we won't need to play more than 100,000 games per minute.
- You can assume that time to complete a game is between 1 microsecond and 5 minutes.
- You can assume that the game and all the agents can comfortably fit on a single machine.
- You can assume each `game.play` call uses exactly one CPU core.
- The same agent can play multiple games at the same time.
- Multiple instances of the same game can be played concurrently.

Cluster setup:
- The code will be run on up to 1000 machines.
- Each machine will have up to 20 core CPU. 

### Testing your code on multiple machines

To assist you with validating your solution we provided a script that emulates multimachine setup using docker. It requires [Docker](https://www.docker.com/) and Python 3. To use it simply run `python3 docker.py`. By default the script will create 2 machines and run `ls -l && cat ips.txt && sleep 2m` on each of them. The script supports the following conveinence features:

- all the files from takehome folder are copied to home directory (`/root`) on each machine, as per default `Dockerfile`
- the script prints out commands that allow you to ssh to all the machines
- IPs of all the machines are available in `~/ips.txt` (order of IPs is fixed accross machines)
- you can see logs from each machine in `<take_home_folder>/logs`

Type `python3 docker.py --help` to learn about the arguments supported by the file.
Hint: add all your setup code such as `pip install package` to `Dockerfile` for fast iteration speed.
