
## Install Dependencies

```
pip install -r requirements.txt
```

## Change the IP address to your facebox

```
client.connect("your facebox ip", 1883, 60)
```

## Run the sample code

```
python main.py
```

### Known Person Event

```
{
  "status":"known person",
  "persons":[
     {
       "id": Recognized Person ID,
        "name" Known Person Name,
        "uuid": Facebox Device ID,
        "group_id": Group ID,
        "img_url": Recognized Face Image,
        "current_ts": Current timestamp,
        "accuracy": Accuracy,
        "fuzziness": Image Fuzziness Score
      }]，
      "person_id":Recognized Person ID
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
    ],"person_id": Reversed
}
```

