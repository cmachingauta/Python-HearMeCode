# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can
# make a peanut butter and jelly sandwich

# Second Goal: Create a program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Create a program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Create a program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Create a program to tell you: if you have enough bread and peanut butter but no jelly,
#that you can make a peanut butter sandwich but you should take a hard, honest look at your life.
#Wow, your program is kinda judgy.


# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

bread=13
pb=13
jelly=1
#
ingredients= (bread>=2, pb>=1, jelly>=1)
if all(ingredients):
    print "You can make a peanut butter and jelly sandwich"
else:
    print "Looks like you don't have a lunch today" 
    
####   ### To satisfy the second goal:
#####		Continue from the first goal, and add:
#####		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1),
######              print a message like "I can make this many sandwiches: " and then calculate the result.
#####		If you don't; you can print the same message as before
#####   To calculate which ingredient you have the least of, the min() function will be useful.
#####   min() will calculate the smallest number of all of the numbers in the parentheses and tell you which it is
#####   For example, min(4, 83, 6) will return 4
#####    print "I can make this many sandwiches:"
####
if all(ingredients):
    print "You can make this many sandwiches :{0}".format(min(bread,pb,jelly))
else:
   print "Looks like you don't have a lunch today"
##    
###      To satisfy the third goal:
###		Continue from the second goal, and add:
###		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
###		If you don't have enough ingredients; still print the same message as before
###		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py
if all(ingredients):
   if (bread%2==1):
        print "You can make this many sandwiches:{0}, and you can make an open sandwich too".format(min(bread/2,pb,jelly))
else:
    print "Looks like you don't have a lunch today" 
#                                                               
## To satisfy the fourth goal:
##		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message 
## that tells you that you can make a peanut butter sandwich
##		Or if you have more peanut butter and bread than jelly, that you can make 
## a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches
#
if (bread>=2 and pb>=1 and jelly==0):
   print "You can only make a peanut butter sandwich, but you should take a hard, honest look at your life!"
   if (bread%2==1):
       print "You can make an open sandwich too"
if (bread>=2 and pb>=1 and pb>jelly):
  print "You can make this many peanut butter and jelly sandwiches:{0}, and {1} peanut butter sandwiches".format(min(bread/2,pb,jelly),pb-jelly)
  if (bread%2==1):
      print "You can make an open sandwich too"
   
## To satisfy the fifth goal:
##		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.

if (bread>=2 and pb>=1 and jelly<1):
   print "You're missing jelly"
elif (bread>=2 and pb<1 and jelly>=1):
  print "You're missing peanut butter"
elif (bread>=2 and pb<1 and jelly<1):
  print "You're missing jelly and peanut butter"
elif (bread<2 and pb<1 and jelly>=1):
  print "You're missing bread and peanut butter" 
  if (bread==1):
      print "There's one slice to make an open face jelly sandwich"
elif (bread<2 and pb<=1 and jelly<1):
  print "You're missing bread and jelly"  
  if (bread==1):
      print "There's one slice to make an open face pb sandwich"
elif (bread<2 and pb>=1 and jelly>=1):
    print "You're missing bread"
    if (bread==1):
      print "There's one slice to make an open face sandwich"
elif all(ingredients):
     print "You can make this many sandwiches:{0}".format(min(bread/2,pb,jelly))
     if (bread%2==1): 
       print "You can make this many sandwiches:{0}, and you can make an open sandwich too".format(min(bread/2,pb,jelly))   
else:
   print "Time to go shopping if you want lunch!"
   
