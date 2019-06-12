# Deliverable
A simple python api for Formating the inputdata of diiferent restuarants openning or closing hour and convert it in human readable format. The deliverable consist on two parts, in first part , we will talk about our coding approach for solving the coding assignment.

## Part 1
For making the required api we have used following stacks (according to requirements):
```
Python 3.7.3,
Flask 1.0.3,
pip 19.1
```
to install these, follow the install part.

### Install
```
pip install flask

```

### run 
```
python api.py

```
It will run the api on localhost or https://127.0.0.1:5000 where 5000 is port number.

A simple way to check the api, a simple postman application can be used or any other can be used which is comfortable for you.

### Example

```
# -----------------------------Example 1--------------
# Input

# api endpints : http://127.0.0.1:5000/openingHours
# data: {"monday" : [],"tuesday" : [{"type" : "open","value" : 36000},{"type" : "close","value" : 64800}],"wednesday" : [],"thursday" : [{"type" : "open","value" : 36000},{"type" : "close","value" : 64800}],"friday" : [{"type" :"open","value" : 36000}],"saturday" : [{"type" : "close","value" : 3600},
{"type" : "open","value" : 36000}],"sunday" : [{"type" : "close","value" : 3600},{"type" : "open","value" : 43200
},{"type" : "close","value" : 75600}]}

# Output

[
        "Monday: Closed",
        "Tuesday: 10 AM - 6 PM",
        "Wednesday: Closed",
        "Thursday: 10 AM - 6 PM",
        "Friday: 10 AM - 1 AM",
        "Saturday: 10 AM - 1 AM",
        "Sunday: 12 PM - 9 PM"
]

# -------------------------------------------

# -----------------------------Example 2--------------
# Input

# api endpints : http://127.0.0.1:5000/openingHours
# data: {"monday" : [],"tuesday" : [{"type" : "open","value" : 36000},{"type" : "close","value" : 64800}],"wednesday" : [],"thursday" : [{"type" : "open","value" : 36000},{"type" : "close","value" : 64800}],"friday" : [{"type" :"open","value" : 36000}],"saturday" : [{"type" : "close","value" : 3600},
{"type" : "open","value" : 32400},{"type" : "close","value" : 39600},{"type" : "open","value" : 57600},{"type" : "close","value" : 82800}],"sunday" :[ {"type" : "open","value" : 43200
},{"type" : "close","value" : 75600}]}

# Output
[
    "Monday : Closed",
    "Tuesday : 10 AM - 6 PM",
    "Wednesday : Closed",
    "Thursday : 10 AM - 6 PM",
    "Friday : 10 AM - 1 AM",
    "Saturday : 9 AM - 11 AM, 4 PM - 11 PM",
    "Sunday : 12 AM - 9 PM"
]
# -------------------------------------------

# -----------------------------Example 3--------------
# Input:

# api endpints : http://127.0.0.1:5000/openingHours
# data: {"monday" : [{"type" : "open","value" : 28800},{"type" : "close","value" : 36000},{"type" : "open","value" : 39600},{"type" : "close","value" : 64800}],"tuesday" : [],"wednesday" : [{"type" : "open","value" : 39600},{"type" : "close","value" : 64800}],"thursday" : [{"type" : "open","value" : 39600},{"type" : "close","value" : 64800}],"friday" : [{"type" :"open","value" : 39600}],"saturday" : [{"type" : "close","value" : 75600},
{"type" : "open","value" : 39600},{"type" : "close","value" : 75600}],"sunday" :[]}

# Output:
[
    "Monday : 8 AM - 10 AM, 11 AM - 6 PM",
    "Tuesday : Closed",
    "Wednesday : 11 AM - 6 PM",
    "Thursday : 11 AM - 6 PM",
    "Friday : 11 AM - 9 PM",
    "Saturday : 11 AM - 9 PM",
    "Sunday : Closed"
]
# -------------------------------------------

```

## Part 2

As a developer, i always love to have something challenging and never say that its tough but there is always have a chance to improve it. If i would be the data provider i would always make is as much simple as possible because it will be helpful for the future perspective. 
