# Stats *NPM*

<|{packageNpm}|input|label=NPM Package|>
<|{datesNPM}|date_range|label_start=Start Date|label_end=End Date|>
<|Show Stats|button|on_action=change_input|>


<|## Package: {packageNpm}|text|mode=markdown|>

### _Downloads_
<|{dataDownloadNpm}|chart|x=day|y=downloads|layout={layoutNpm}|>
<|{versionsNpm}|table|>