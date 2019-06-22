#! /usr/bin/python3.7
import os, yaml, time
from classes.slack import slack

if __name__ == "__main__":

    username    = 'test'
    email       = 'test@example.com'
    email = 'test@mail.ru'
    password    = 't4too7'
    first_name  = 'test'
    last_name   = 'test'

# class for working with users 
    slack = slack()
    # slack.user_invite(email       = email,
    #                   first_name  = first_name,
    #                   last_name   = last_name)
    slack.user_inactive(username)
