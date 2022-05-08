# webdata
Get website info.

## What is it??
It is a library to get data from websites.

## Examples

### 1. Check if webpage up.

```
import webdata
isup = webdata.up_chk("example.com")
if isup == True:
    print("Is up :)")
else:
    print("Down :(")
```

## Documentation

### up_chk()
Checks if a website is up. returns True if up.

### get_response()
Gets response from web server (ex. html files).
