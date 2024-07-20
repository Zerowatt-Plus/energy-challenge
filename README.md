# Energy Challenge

Energy Challenge for Alphageek dev position

The repository contains 2 CSV file with the power (watt) and energy (watt-hour) consumption for a 3 phase motor for 24 hours duration with its timestamp

## Definitions

1. Power consumed by the motor is the sum of the power consumed by all the phases `P = P1 + P2 + P3`
2. Rated power is the power the motor will draw at max load `motor_rating = equipment_ rating / efficiency`
3. Vampire power is the power consumed by a motor when it is not in use. For calculation, `0 < P <= (0.01 X motor_rating)` is considered as vampire power
4. Idle power is the power consumed by a motor when it is running but not loaded. For calculation, `(0.01 X motor_rating) < P <= (0.3 X motor_rating)` is considered as idle power
5. Operating above idle power till overloading is considered as normal operation
6. Overload is when the motor is drawing more power than its service factor

## Motor detail

```python
subject_motor = {
    'equipment_rating': 90, # kW
    'phase': 3,
    'efficiency': 0.9,
    'service_factor': 1.2,
}
```
Service factor is the allowed overloading of a motor. Service factor of 1.1 means the motor can be overloaded by 10% above motor rating

## Challenge 1

Analyse the power conception of the motor for vampire condition, idling and overload situation. Calculate the energy consumption (Sum of the column energy in the csv) for the 4 operating condition - vampire, idling, normal, and overload. The energy values in the dataset is in Watt-Hours and the output shall be in kiloWatt-Hours (*no decimals*) Output shall be in the format:

```python
{
    'vampire': 5000,
    'idle': 15000,
    'normal': 250000,
    'overload': 7000
}
```

## Challenge 2

Find all instances of vampire, idle and overload operations and list the durations. Output shall be in the format:

```python
{
    'vampire': [(06:00, 06:13), (07:10, 07:17)],
    'idle': [(12:00, 13:00), (15:30, 16:00)],
    'overload': [(18:02, 18:15), (19:10, 19:13)],
}
```

The tuples in the list are start and end times

## Challenge 3

Calculate the energy cost of vampire and idle Running. Hint - use electricity charges as given below

```python
tariff  = [
    {'zone': 1, 'start_time': '6AM', 'end_time': '6PM', 'rate': 790},
    {'zone': 2, 'start_time': '6PM', 'end_time':'10PM', 'rate': 1185},
    {'zone': 3, 'start_time': '10PM', 'end_time': '6AM', 'rate': 593}
]
```

Rate is the energy charges per Unit in paise. The function should be able to calculate the cost for any given tariff rate. For instance, `tariff.py` can return different tariffs based on the `id`

Output shall be in the format:

```python
{
    'vampire': 5000,
    'idle': 15000
}
```

## Notes:
1. Please do not reach out asking doubts. Instead, make assumptions as needed to solve the questions and document them
2. If you use an AI assistant, add a note (e.g., in a README) mentioning how and for what you used it. Honesty won't be penalized.
