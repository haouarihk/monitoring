# monitoring Multiple Sites For A Secific Changes

 just monitoring

# Starter:

  this is a project that allowes you to check if the cites had changed a specific element (with id class...etc) and refeash every sometime

 
 # How to start:
 
   ## install requirements
   ``pip install -r requirements.txt``
   or
   ``pip install -r requirements2.txt``
   
   ## How to use
   in the ``map.json`` file you can add objects as array that every object containers ``url`` and ``props`` properties

   ## Note that:
   -``url``: is the page url

   -``props``: is the variable properties like ``type.class#id`` of the element that you want to observe, you can use ``body`` or ``html``

   -this file should be an array, And you can't have two objects with the same url.

   ## The output:
   it outputs in the ``monitoringData.json`` as array of object 
        
   every object has this structor:
   ```js
               { 
                    "url": "https://evergreen-olivine-sardine.glitch.me", // the url of the site
                    "LastInner": "1ddddd",                                // the last change inner
                    "Lastsaved": "2020-05-30 10:36:18.631454",            // time that the last change happen
                    "dateChanged": [                                      // array of changes            
                        {
                            "inner": "1ddddd",                  // this change inner
                            "time": "2020-05-30 10:36:18.631454"// this change when it happen
                        }
               }
   ```
