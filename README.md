# [Prepare Hardware](hardwares)
# [Burn Firmware](firmware)
# Facebox SDK
## 1 Clone facebox_sdk Repo
### https://github.com/fay1986/facebox_sdk.git
## 2 Usage

### 2.1 Get the ip address of Facebox through 'Circle Point' APP(Chinese version only for now)
### 2.2 Change the IP address in source code
### 2.3 Run the sample code

## Known Person / Stranger Events Format
### Known Person Event
```
{
    "status":"known person",
    "persons":[
        {
          "id": Recognized Person ID,
          "uuid": Facebox Device ID,
          "group_id": Group ID,
          "img_url": Recognized Face Image,
          "current_ts": Current timestamp,
          "accuracy": Accuracy,
          "fuzziness": Image Fuzziness Score
        }
    ],
    "person_id": Recognized Person ID
}
```
### Stranger Event
```
{
    "status":"Stranger",
    "persons": [
        {
            "uuid": Facebox Device ID,
            "group_id": Group ID,
            "img_url": Face Image of detected face,
            "current_ts": Current timestamp,
            "fuzziness": Image Fuzziness Score
        }
    ],
    "person_id": Reversed
}
```

## Language Support

### [Python](python)
### [Nodejs](nodejs)
### [Ruby On Rails](ruby)



