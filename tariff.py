def get_tariff(id: int):
    match id:
        case 1:
            return [
                {"zone": 1, "start_time": "6AM", "end_time": "6PM", "rate": 790},
                {"zone": 2, "start_time": "6PM", "end_time": "10PM", "rate": 1185},
                {"zone": 3, "start_time": "10PM", "end_time": "6AM", "rate": 593},
            ]
        case 2:
            return [
                {"zone": 1, "start_time": "6AM", "end_time": "6PM", "rate": 500},
                {"zone": 2, "start_time": "6PM", "end_time": "10PM", "rate": 750},
                {"zone": 3, "start_time": "10PM", "end_time": "6AM", "rate": 380},
            ]
        case _:
            return None
