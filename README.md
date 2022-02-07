URl shortener Advance project

Project details:

        language : python3
        framework : FastAPI,jinja2
        server run : uvicorn
        database : sqlite3

Architecture:

    
     All original url that need to turn into clean url , this project can achieve this with more feature then other projects
     reason is user have more control on what args in url to be shown with customized message , user can update url key words for special things.

        1. project work on hash key as base to store all urls
        2. for each url user can assign expiry date count eg. expire after 5 days.
        3. with args customization, company can hide their tracking codes,args but still to show about policy,right to info custom 
            message   can be add to url as args
        4. for one time use , with help of one flag and counter of visitor to use same link this project covers it with ease
        5. for expiry date it work as per day count , else default is 5 days , after expiry user can visit link redirected site.
        6. with special key you can create url more friendly with your company
        7. if you are wondering how user can continue to know or what to do once url expired, we popup a message with email provide by  
            firm user,
        
API :

        #1. Api to generate urls
        
           url : /quick_link , method = POST
       
           example of
           payload : {
               "original_url":"https://www.company.com/diwali_offer?utm_locat=socail_media&utm_track=true",
               "special_key":"diwali_offer",
               "message":["track_on","diwali_special"],
               "one_time_use":False,
               "email: "abc@company.com",
               "expire_date":5
           }
           
           required_fields:
                original_url,email
                
           optional:
               "special_key":"",
               "message":[],
               "one_time_use":False,
               "expire_date":5
               
           output for above payload:
                short url : https://url_shortner_project.herokuapp.com/4asdkb2h1b213/diwali_offer?message1=track_on&message2=diwali_special
                key = 4adsk2h1b213 is hash piece

        2. Api to redirect to original url
            url : /{key:path} ,  method = GET
            eg, https://url_shortner_project.herokuapp.com/4asdkb2h1b213/diwali_offer?message1=track_on&message2=diwali_special

            if not expired and not one time used then it will redirect to original url
            it search for hash and redirect with database data this can achieve prevention of alteration in original url


UI:
   
        Design is complete and consist of form and teamplates

Setup:

        1. set virtual env
            virtualenv env
            source env/bin/activate
        2. install requirements file
            pip3 install -r requirments.txt
        3. run server:
            uvicorn main:app --reload --port 8080
        
        

