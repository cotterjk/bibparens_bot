import random;
import tweepy;

# Authenticate to Twitter
auth = tweepy.OAuthHandler("###REDACTED###", "###REDACTED###") #API Key , API Key Secret
auth.set_access_token("###REDACTED###", "###REDACTED###") #Access Token and Secret

##########################
### ↓↓↓ FUNCTIONS ↓↓↓ ###
##########################

def empty_source():
    api.update_status("My text source is empty, please stop me.");
    quit();

def tweet(l):
    # TODO replace w/ tweeting
    api.update_status(l);
    print(l);

def long_tweet(l):
    print(":::LONG ONE:::");
    l_list = [];
    l_list.append(l[:279]);
    l_list.append(l[279:]);
    while (len(l_list[-1])>279):
        tail = l_list.pop();
        l_list.append(tail[:279]);
        l_list.append(tail[279:]);
    print(l_list);

    #Tweet list as sequence of replies
    tweet_status = api.update_status(l_list[0]);
    #Loop through remaining part of tweet as replies
    ## Reference: https://stackoverflow.com/questions/9322465/reply-to-tweet-with-tweepy-python
    for l_part in l_list[1:] :
        next_tweet_status = api.update_status(status = l_part, in_reply_to_status_id = tweet_status.id_str , auto_populate_reply_metadata=True)
        tweet_status = next_tweet_status; #replace as end of the thread to reply to

##########################
### ↓↓↓ MAIN BLOCK ↓↓↓ ###
##########################

# Create API object
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

try:
    with open('assets/kjv_final.txt', 'r+') as f:
        lines = f.readlines();
        if len(lines) == 0:
            empty_source();
        else:
            l_pick_index = random.randint(0, len(lines)-1)
            l_pick = lines[l_pick_index].strip();
            l_pick += random.choice([' ⛪️',' 🙏',' 😇',' 🕯',' 📜',' 🕊️'])
            if (len(l_pick)) > 279: #paren doesn't fit in 1 tweet
                long_tweet(l_pick);
            else:
                tweet(l_pick);

            #now remove the tweeted line
            del lines[l_pick_index];
            f.seek(0);
            f.truncate();
            f.writelines(lines);


except Exception as e:
    print("=== MAIN BLOCK FAILED ===");
    print(e);
