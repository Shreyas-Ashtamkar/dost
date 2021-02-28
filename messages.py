shortMenu = """
This is a Whatsapp Chatbot, Built by Space-For-Inception.
These are the following services I can offer: 
1. Wikipedia     wiki   <thing>
2. Covid-19      covid  <Country>
3. Youtube       video  <thing>
4. DownVideo     dvideo <thing>
5. Lyrics        lyrics <song>
6. News          news

For Detailed Explaination, send help-all
"""

MainMenu = """
This is a Whatsapp Chatbot, Built by Space-For-Inception.
These are the following services I can offer.: 
1. *Wikipedia* -- 
    Get the wikipedia Info of Something.
    
    example : 
        wiki India
        
2. *Covid-19* -- 
    Get Covid-19 Live Numebrs some country.
    
    example : 
        covid India
        
3. *Youtube Video* -- 
    Responds you with the most Relevent 3 Videos.
    
    example : 
        youtube Tom and Jerry
        
4. *Download Youtube Video* -- 
    Responds you with the download link to most Relevent 3 Videos.
    
    example : 
        dvideo Tom and Jerry

5. *Lyrics of Song* -- 
    Get the Lyrics of your Favourite Song.
    
    example : 
        lyrics Vande Mataram

6. *Latest News* -- 
    Get the Latest.
    
    example : 
        news
"""

ErrorReply = "Invalid Option. please type 'info' or 'help' for help."

introPage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Space for Inception</title>
    <style>
        body{
            background: rgb(31, 28, 28);
        }
        a, a:active, a:hover, a:visited, a:default{
            margin: 0;

            position: absolute;               

            top: 50%;
            left: 50%;
            margin-right: -50%;
            transform: translate(-50%, -50%);

            text-decoration: none;

            color: white;

            display: block;
            float:left;

            width: 10%;
            text-align: center;
            
            background-color: rgb(24, 124, 61);
            
            padding: 20px;

            border-radius: 15px;
        }

        a:hover{
            background-color: #25D366;

            box-shadow: aqua;
        }

    </style>
</head>
<body>
    <a class="button" href="whatsapp://send?phone=<+1 415 523 8886>&text=join teacher-spite" role="button">Join</a>
</body>
</html>
"""

n = """

"""