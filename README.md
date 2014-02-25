# London Bus Commute calculator

Tool to work out which bus stops you can reach directly from a radius around an
initial bus stop.

Generates a .kml file which can be opened in Google Earth/Maps to see what
areas you could commute directly from on a bus.

## Motivation

I currently always get a seat on my bus commute, and always having a seat means
more time to spend coding side projects twice a day. I want to find out where
else I can commute from and keep this project time intact. This project was
created in a few such coding sessions.

## Setup

`pip install -r requirements.txt`

Sign up for TFL api access and download the bus stops and bus routes csvs. Save
these to `stops.csv` and `routes.csv`

## Usage

`./main.py name radius`

* `name` is the name of the bus stop you wish to commute to
* `radius` is the distance, in metres, you're willing to walk to another
bus stop nearby, from either the initial bus stop or any of the destination
stops

Output will be saved to `out.kml`

## Example usage

`./main.py "EPWORTH STREET" 700`

![example commutes](https://github.com/c-oreills/londoncommute/raw/master/buscommute.png')
