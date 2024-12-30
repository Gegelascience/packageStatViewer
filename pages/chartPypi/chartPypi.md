# Stats *Pypi*

<|{packagePypi}|input|label=Package|>
<|{datesPypi}|date_range|label_start=Start Date|label_end=End Date|>
<|Show Stats|button|on_action=change_input|>


<|## Package: {packagePypi}|text|mode=markdown|>

### _Downloads_
<|{dataPypi}|chart|x=day|y=downloads|>
<|{versionsPypi}|table|>