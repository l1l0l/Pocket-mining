# <span style="color: #5dcfca;">Pocket Authentication API Documentation</span>

<i> <u>source</u>: https://getpocket.com/developer/docs/authentication</i>

### Step 1: Obtain a platform consumer key

Registering the app with Pocket associates it with a platform <b>consumer key</b>. This key identifies your app to Pocket's API.

To obtain a <b>consumer key</b>, you should register for one at http://getpocket.com/developer/apps/new.

<br>


### Step 2: Obtain a request token

To begin the Pocket authorization process, the application must obtain a request token from pocket servers by making a POST request.

##### <b>Pocket API URL:</b>
    
https://getpocket.com/v3/oauth/request

##### <b>My API Method:</b>

The method ``` pocket_api.get_request_token ``` retrieve the <b>request token</b> from the API url https://getpocket.com/v3/oauth/request.

<br>

### Retrieving a User's Pocket Data 
<i> <span style="color : gray;">for more information, please refer to provider doc </span> (https://getpocket.com/developer/docs/v3/retrieve)</i>

#### Method URL
https://getpocket.com/v3/get

Required Parameters

<table  align="left">
    <tbody>
        <tr>
            <td><b>consumer_key</b></td>
            <td>string</td>
            <td></td>
            <td>Your application's Consumer Key</td>
        </tr>
        <tr>
            <td><b>access_token</b></td>
            <td>string</td>
            <td></td>
            <td>The user's Pocket access token</td>
        </tr>
    </tbody>
</table>

<br>


```json
data = {
    'consumer_key': CONSUMER_KEY, 
    'access_token': ACCESS_TOKEN,
    'detailType': 'complete',
    'sort': 'newest',
    'since' : 1585900000
}
```
