from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import sms
from . import makeSMS

@csrf_exempt
def index(request):
    if(request.method == 'POST'):
        smsObject = None
        try:
            data = json.loads(request.body)
            phono = data['phoneno']
            mess = data['message']
            user = data['username']
            passw = data['password']
            print(data)
            if(verifyPhoneno(phono) and verifyMessage(mess) and verifyCredential(user,passw) and verifyPhoneno(user)):
                smsObject = sms.sms(user,passw)
                if(smsObject.loggedIn):
                    if(smsObject.send(phono,mess)):
                        smsObject.logout()
                        return HttpResponse(json.dumps({"status" : "true" , "message" : "Sucessfully Transferd"}), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({"status" : "false" , "message" : "Invalid Credential"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"status" : "false" , "message" : "Invalid data"}), content_type="application/json")
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status" : "false" , "message" : "Something is Wrong"}), content_type="application/json")
        finally:
            if(smsObject):
                smsObject.logout()

def verifyPhoneno(no):
    if(len(no) == 10):
        return True
    return False

def verifyMessage(message):
    if(len(message) > 0):
        return True
    return False

def verifyCredential(user,passw):
    if(len(user) > 0 and len(passw) > 0):
        return True
    return False


def sample(request):
    return HttpResponse("<center><h1>Hello World</h1><center>")
