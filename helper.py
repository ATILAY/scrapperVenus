from constants import YEARLY_WORKING_HOURS

def check_comma_in_string(str_val):
    return ',' in str_val

def convert_string_to_float(str_val):
    try:
        float_val = float(str_val.replace(",","").strip(",").strip(" "))
        rounded_float_val = round(float_val,2)

        return rounded_float_val
    except ValueError:
        return 0.0

def convert_yearly_to_hourly_rate(float_val):
    return float_val / YEARLY_WORKING_HOURS

def elaborate_wage(val_str):
    val = (check_comma_in_string(val_str) and convert_yearly_to_hourly_rate(convert_string_to_float(val_str))) or convert_string_to_float(val_str)

    return val