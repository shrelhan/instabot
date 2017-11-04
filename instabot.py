import requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt


APP_ACCESS_TOKEN = '2998169764.79464b2.16a0a97fcccd477d9868e84b418679f0'
#Sandbox Users : streethustler_1, vivek3273, rahulbhagoti

BASE_URL = 'https://api.instagram.com/v1/'

'''
Function declaration to get your own info
'''
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get the ID of a user by username
'''

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

'''
Function declaration to get the info of a user by username
'''

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get your recent post
'''

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the recent post of a user by username
'''

def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Requested image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get the recent media liked by a user
'''

def get_recent_media_liked():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    liked_media = requests.get(request_url).json()

    if liked_media['meta']['code'] == 200:
        if len(liked_media['data']):
            print 'Liked image id : %s' % (liked_media['data'][0]['id'])
        else:
            print 'Post does not exist'
    else:
        print 'Status code other than 200 received!'




'''
Funtion declaration to get the list of comments on your recent post
'''

def get_recent_comment_list(media_id):
    list_of_comments = get_recent_comment_list(media_id)
    if list_of_comments == None:
        print 'Media does not exist!'
        exit()
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s')%(list_of_comments ,APP_ACCESS_TOKEN)
    print 'GET request url : %s'%(request_url)
    comments_list = requests.get(request_url).json()

    if comments_list['meta']['code'] == 200:
        if len(comments_list['data']):
            print 'Commented list : %s'%(comments_list['data'][0]['id'])
        else:
            print 'No comments on the post! '
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the list of user who liked the user recent post
'''

def get_recent_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s')%(media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s'%(request_url)
    liked_list = requests.get(request_url).json()

    if liked_list['meta']['code'] == 200:
            print liked_list
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the ID of the recent post of a user by username
'''

def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to like a post 
'''

def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes')%(media_id)
    payload = {"access_token":APP_ACCESS_TOKEN}
    print 'POST request url : %s' %(request_url)
    post_a_like = requests.post(request_url,payload).json()

    if post_a_like['meta']['code'] == 200:
        print 'Like was successful'
    else:
        print 'Your like was unsuccessful. Try again!'


'''
Function declaratin to comment on a post
'''

def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    make_comment = requests.post(request_url,payload).json()

    if make_comment['meta']['code'] == 200:
        print 'Successfully added a comment!'
    else:
        print 'Unable to add comment. Try again!'

'''
Function declaration to make delete negative comments from the recent post
'''

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


'''
Function to create pis chart of positvie and negative comments
'''

def pie_chart(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):

            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                positive_comment = blob.sentiment.p_pos
                negative_comment = blob.sentiment.p_neg
                # Data to plot
                labels = 'Positive Comment', 'Negative Comment'
                sizes = [positive_comment,negative_comment]
                colors = [ 'yellowgreen', 'lightcoral',]
                explode = ( 0, 0)

                # Plot
                plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                        autopct='%1.1f%%', shadow=True, startangle=140)

                plt.axis('equal')
                plt.show()

        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


'''
Function declarartion to give the user choices to choose
'''

def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get the recent media liked by user\n"
        print "f.Get the list of comments on your post\n"
        print "g.Get a list of people who have liked the recent post of a user\n"
        print "h.Like the recent post of a user\n"
        print "i.Make a comment on the recent post of a user\n"
        print "j.Delete negative comments from the recent post of a user\n"
        print "m.Exit"

        choice=raw_input("Enter you choice: ")
        if choice=="a":
            self_info()
        elif choice=="b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice=="c":
            get_own_post()
        elif choice=="d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="e":
            get_recent_media_liked()
        elif choice=="f":
            media_id = raw_input("Enter the media id : ")
            get_recent_comment_list(media_id)
        elif choice=="g":
            insta_username = raw_input("Enter the username of the user: ")
            get_recent_like_list(insta_username)
        elif choice=="h":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice=="i":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice=="j":
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
        elif choice=="k":
            insta_username = raw_input("Enter the username")
            get_post_id(insta_username)
        elif choice=="l":
            insta_username = raw_input("Enter the username")
            pie_chart(insta_username)
        elif choice=="m":
            exit()
        else:
            print "wrong choice"

start_bot()