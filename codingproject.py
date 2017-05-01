from urllib import urlopen
import argparse
import sys


ending = ""
clean_phone = ""
reason = ""

def ask_gender():
    gender = ""

    while gender.lower() not in ['m', 'f', 'male', 'female']:
        gender = raw_input("What gender would you like: ")

    return gender.lower()

def ask_phone():

    phone = ""
    global clean_phone 

    while len(clean_phone) != 10:
        phone = raw_input("What is your phone number?")

        #I wanna go through every character in the phone number string
        for character in phone:
            if character.isdigit():
                clean_phone += character

        if len(clean_phone) != 10:
            clean_phone = ""

    return clean_phone


def ask_reason(gender):

    global reason

    if(gender == 'f'):
        while reason not in ['1', '2', '3', '4', '5']:
            print("Please select your reason..")
            print ("Reason 1. Ingesting old spice")
            print ("Reason 2. Listening to reading")
            print ("Reason 3. Lobster dinner")
            print ("Reason 4. Moon kiss")
            print ("Reason 5. Riding a horse")
            reason = raw_input("Please select your reason [1-5]:")
    else:
        while reason not in ['1', '2', '3', '4']:
            print("Please select your reason..")
            print ("Reason 1. Building")
            print ("Reason 2. Cracking walnuts")
            print ("Reason 3. Polishing monocole")
            print ("Reason 4. Ripping weights")

            reason = raw_input("Please select your reason [1-4]:")

    return reason

def valid_gender(gender):
    return gender in ['m', 'male', 'f', 'female']

def valid_phone(phone):
    clean_phone = ""
    for character in phone:
        if character.isdigit():
            clean_phone += character

    return len(clean_phone) == 10

def ask_ending(gender):

    global ending

    if (gender == 'f'):

        while ending not in ['1', '2']:
            print ("Ending 1. She will get back to you")
            print ("Ending 2. Thanks for calling")
            ending = raw_input("Please choose your ending [1-2]:")
    else:
        while ending not in ['1', '2', '3', '4', '5']:
            print ("Ending 1. Horse")
            print ("Ending 2. Jingle")
            print ("Ending 3. On phone")
            print ("Ending 4. Swan dive")
            print ("Ending 5. Voicemail")
            ending = raw_input("Please choose your ending [1-5]:")

    return ending

def get_mp3s(gender, phone, reason, ending):

    server = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/"

    final_mp3 = open("output.mp3", "wb")
    if (gender == 'm'):
        ##Hello 
        final_mp3.write(urlopen(server + "m-b1-hello.mp3").read())
        ##cellphone number
        for digit in phone:
            final_mp3.write(urlopen(server + digit + ".mp3").read())

        ##UNABLE TO TAKE YOUR CAR
        final_mp3.write(urlopen(server +"m-r0-cannot_come_to_phone.mp3").read())
        ##REASON
        if reason == '1':
            final_mp3.write(urlopen(server + "m-r1-building.mp3").read())
        elif reason == '2':
            final_mp3.write(urlopen(server + "m-r2-cracking_walnuts.mp3").read())
        elif reason == '3':
            final_mp3.write(urlopen(server + "m-r3-polishing_monocole.mp3").read())
        elif reason == '4':
            final_mp3.write(urlopen(server + "m-r4-ripping_weights.mp3").read())

        if ending == '1':
            final_mp3.write(urlopen(server + "m-e1-horse.mp3").read())
        elif ending == '2':
            final_mp3.write(urlopen(server + "m-e2-jingle.mp3").read())
        elif ending == '3':
            final_mp3.write(urlopen(server + "m-e3-on_phone.mp3").read())
        elif ending == '4':
            final_mp3.write(urlopen(server + "m-e4-swan_dive.mp3").read())
        elif ending == '5':
            final_mp3.write(urlopen(server + "m-e5-voicemail.mp3").read())
    else:
        ##Hello :)
        final_mp3.write(urlopen(server + "f-b1-hello_caller.mp3").read())
        ##Cell Phone Numer
        for digit in phone:
            final_mp3.write(urlopen(server + digit + ".mp3").read())  
        ##BUSY
        final_mp3.write(urlopen(server + "f-r0.2-she_is_busy.mp3").read())
        ##REASON  
        if reason == '1':
            final_mp3.write(urlopen(server + "f-r1-ingesting_old_spice.mp3").read())
        elif reason == '2':
            final_mp3.write(urlopen(server + "f-r2-listening_to_reading.mp3").read())
        elif reason == '3':
            final_mp3.write(urlopen(server + "f-r3-lobster_dinner.mp3").read())
        elif reason == '4':
            final_mp3.write(urlopen(server + "f-r4-moon_kiss.mp3").read())
        elif reason == '5':
            final_mp3.write(urlopen(server + "f-r5-riding_a_horse.mp3").read())  

        if ending == '1':
            final_mp3.write(urlopen(server + "f-e1-she_will_get_back_to_you.mp3").read())
        elif ending == '2':
            final_mp3.write(urlopen(server + "f-e2-thanks_for_calling.mp3").read())
    
    final_mp3.close()

   
#this is where the code will start
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'my awesome shit')

    parser.add_argument('-g')
    parser.add_argument('-n')
    parser.add_argument('-r')
    parser.add_argument('-e')
    parser.add_argument('-o')

    args = parser.parse_args()

    print (args.g)
    print (args.n)
    print (args.r)
    print (args.e)
    print (args.o)

    print (valid_gender(args.g))


    gender = ask_gender()
    phone = ask_phone()

    reason = ask_reason(gender)

    ending = ask_ending(gender)
    
    get_mp3s(gender, phone, reason, ending)

    sys.exit()
