from weather import average_wind_speed
import pandas as pd
from pytest from approx 
def test_average_wind_speed():

    df = pd.read_csv('update_rexburg.csv', parse_dates=["readDate"])

    wind_num = 'AWND'
    wind_df = average_wind_speed(df, wind_num)

    assert len(wind_df.index) > 0

    for value in wind_df["weather"]:
        assert value == wind_num

def test_get_tempt_max():

    df = pd.read_csv('update_rexburg.csv', parse_dates=["readDate"])
    tempt_max_num = 'TMAX'
    tempt_max_df = get_tempt_max(df, tempt_max_num)

    assert len(tempt_max_df.index) > 0

    for value in tempt_max_df["weather"]:
        assert value == tempt_max_num

pytest.main(["-v", "--tb=line", "-rN", "test_weather.py"])