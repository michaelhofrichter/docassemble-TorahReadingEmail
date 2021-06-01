Uses the [Hebcal Triennial reading list](https://www.hebcal.com/sedrot/) and a separate Google Sheet with readers names to populate a way to easily send out an email about who is handling torah readings this week. 

## To Setup
Copy the HebCal Triennial reading list for the current cycle into your own Google Drive and share it with your Docassemble Service account (see [Docassemble's Google Sheets example](https://docassemble.org/docs/functions.html#google%20sheets%20example)). Currently 5780-5782 is hardcoded into the package and you'll have to add a new code line for a different year.

```
code: | 
  torahlist = read_sheet("Triennial-####-####", 0) 
```

Create a Google Sheet with the name `Torah Readers`. The columns should be: `First Name`, `Last Name`, `Email`, `Always Email`. Capitalization and spacing matters on these columns. `Always Email` should be configured with Data Validation for checkboxes only. Fill this in with any regular members of your Torah reading team. Add anyone else who needs to get these emails with the checkbox `Always Email` set to True. Delete any blank rows of the document. 

When completed, emails will be sent to any individuals named for a role and anyone who was listed with the `Always Email` attribute set to True in the Google Sheet. 

## Changelog:
* 0.0.1 - MVP
* 0.0.2 - Added link for Hebcal Licsense and expanded Readme.md
* 0.0.3 - Added emailing support.

## Future Improvements:
* increased recognition of the data from Hebcal including license clarification.
* ability to pick the date of the next event (currently defaults to any within 7 days). 