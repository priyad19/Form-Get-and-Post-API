from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from .serializers import RegisterSerializer,ChildrenSerializer,MDataSerializer,ADataSerializer
from .models import manual,Auto_data,child
from rest_framework import status,views
from rest_framework import viewsets
import json
import numpy as np 
import sqlite3
import requests
import json 

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    return Response({
        'status':status.HTTP_200_OK,
        'success':True,
        'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email,
        },
        'message': 'Success'
        
    })

@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'status':status.HTTP_200_OK,
            'success':True,
            'data':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'message': 'Success'
    })
    return Response({'error':'not authenticated'})

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            'status':status.HTTP_200_OK,
            'success':True,
            "data":{
            'id':user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": token
            },
            'message': 'Success'
            
        })
        
@api_view(['POST'])
def ADD_CHILD(request):
        serializer = ChildrenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_child(request,User_id=None):
        if User_id:        
            Child = child.objects.filter(User_id=User_id)
            serializer = ChildrenSerializer(Child, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
        Child = child.objects.all()
        serializer = ChildrenSerializer(Child, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def ADD_mDATA(request):
        serializer = MDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ADD_aDATA(request):
        serializer = ADataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":401, "errors":[serializer.errors]}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_data(request,child_id=None):
        if child_id:
            Data = Auto_data.objects.filter(child_id=child_id)
            serializer = ADataSerializer(Data, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Auto_data.objects.all()
        serializer = ADataSerializer(items, many=True)
        return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)

C="""]
                    }
                  },
                  {
                    "type": "elevated_button",
                    "id": "submit_button",
                     "args": { 
                      "onPressed": "${send()}"
                    },
                    "child": {
                      "type": "container",
                      "args": {
                        "alignment": "center",
                        "width": "infinity"
                      },
                      "child": {
                        "type": "save_context",
                        "args": {
                          "key": "form_context"
                        },
                        "child": {
                          "type": "text",
                          "args": {
                            "text": "Submit"
                          }
                        }
                      }
                    }
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
}"""
A="""{

  "type": "scaffold",

  "args": {

    "appBar": {

      "type": "app_bar",

      "args": {

        "title": {

          "type": "text",

          "args": {

            "text": "Form"

          }

        }

      }

    },

    "backgroundColor": "#e0e0e0",

    "body": {

      "type": "safe_area",



      "args": {

        "bottom": true

      },

      "child": {

        "type": "form",

        "child": {

          "type": "single_child_scroll_view",

          "args": {

            "padding": [

              16,

              0

            ]

          },

          "child": {

            "type": "container",

            "args": {

              "alignment": "topCenter",

              "width": "infinity"

            },

            "child": {

              "type": "container",

              "args": {

                "constraints": {

                  "maxWidth": 450

                }

              },

              "child": {

                "type": "column",

                "args": {

                  "mainAxisSize": "min"

                },

                "children": [

                  {

                    "type": "sized_box",

                    "args": {

                      "height": 16

                    }

                  },

                  {

                    "type": "sized_box",

                    "args": {

                      "height": 8

                    }

                  },

                  {

                    "type": "material",

                    "args": {

                      "borderRadius": 16,

                      "color": "#fff",

                      "elevation": 4,

                      "margin": [

                        0,

                        8

                      ],

                      "padding": 16

                    },

                    "child": {

                      "type": "column",

                      "args": {

                        "mainAxisSize": "min"

                      },

                      "children": ["""
D=""" {
  "type": "text_form_field",
  "id": "first_name",
  "args": {
    "decoration": {
      "hintText":"John",
      "labelText":"First Name",
      "suffixIcon":{
        "type":"icon_button",
        "args":{
          "icon":{
            "type":"icon",
            "args":{
              "icon":{
                "codePoint":57704,
                "fontFamily":"MaterialIcons",
                "size": 50
              }
            }
          },
          "onPressed":"${set_value('first_name','')}"
        }
      }
    },
    "validators": [
      {
        "type":"required"
      }
    ]
  }
},"""
@api_view(['GET'])
def get_kpi(request, kpi_id=None):       
            url = 'http://pmel-backend.solidaridadasia.net/api/get-kpi-form/45'
            r = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
            droplets = r.json()
            B=""
            for passenger in droplets['data'] :
                  if passenger['type'] == "text":
                         B= B+"""{
                              "type": "flexible",
                              "child": {
                                "type": "semantics",
                                "args": {
                                  "sortKey": {
                                    "order": 0.0,
                                    "textField": true
                                  }
                                },
                                "child": {
                                  "type": "exclude_semantics",
                                  "child": {
                                    "type": "text_form_field",
                                    "id": '"""+ str(passenger['name']) +"""',
                                    "args": {
                                      "decoration": {
                                        "hintText": "John",
                                        "labelText":'"""+ str(passenger['label']) +"""' ,
                                        "suffixIcon": {
                                          "type": "icon_button",
                                          "args": {
                                            "icon": {
                                              "type": "icon",
                                              "args": {
                                                "icon": {
                                                  "codePoint": 57704,
                                                  "fontFamily": "MaterialIcons",
                                                  "size": 50
                                                }
                                              }
                                            },
                                            "onPressed": "${set_value('"""+ str(passenger['name']) +"""','')}"
                                          }
                                        }
                                      },
                                      "validators": [
                                        {
                                          "type": "required"
                                        }
                                      ]
                                    }
                                  }
                                }
                              }
                            },"""
                  elif passenger['type'] =="radio":
                    ra="{\"type\":\"set_value\",\"args\":{\"radioGroupValue\":\"Yes\"},\"child\":{\"type\":\"column\",\"children\":[{\"type\":\"text\",\"args\":{\"text\":\"\${radioGroupValue??''}\"}},"
                    rc="],\"args\":{\"crossAxisAlignment\":\"start\"}}},"
                    rb=""
                    rad=passenger['values']
                    for value in rad :
                          radv=value['label']
                          rb=rb+"""{\"type\":\"radio\",\"args\":{\"groupValue\":\"\${radioGroupValue}\",\"id\":\"radioGroupValue\",\"value\":'"""+ str(radv) +"""'}},"""
                    B=B+(ra+rb+rc);
                  elif passenger['type'] =="textarea":
                    B= B+"""{
                          "type": "dropdown_button_form_field",
                          "id": "email_type",
                          "args": {
                          "decoration": {
                            "labelText": "Email Type"
                          },
                          "items": [
                          "Home",
                          "Other",
                          "Work"
                        ],
                        "validators": [
                      {
                      "type": "required"
                   }
                  ]
                } 
              },"""
                  elif passenger['type'] =="phone":
                    B= B+"""{
                              "type": "flexible",
                              "child": {
                                "type": "semantics",
                                "args": {
                                  "sortKey": {
                                    "order": 0.0,
                                    "textField": true
                                  }
                                },
                                "child": {
                                  "type": "exclude_semantics",
                                  "child": {
                                    "type": "text_form_field",
                                    "id": '"""+ str(passenger['name']) +"""',
                                    "args": {
                                      "decoration": {
                                        "hintText": "John",
                                        "labelText":'"""+ str(passenger['label']) +"""' ,
                                        "suffixIcon": {
                                          "type": "icon_button",
                                          "args": {
                                            "icon": {
                                              "type": "icon",
                                              "args": {
                                                "icon": {
                                                  "codePoint": 57704,
                                                  "fontFamily": "MaterialIcons",
                                                  "size": 50
                                                }
                                              }
                                            },
                                            "onPressed": "${set_value('"""+ str(passenger['name']) +"""','')}"
                                          }
                                        }
                                      },
                                      "validators": [
                                        {
                                          "type": "required"
                                        }
                                      ]
                                    }
                                  }
                                }
                              }
                            },"""
                  elif passenger['type'] =="autocomplete":
                    B= B+"""{
                          "type": "dropdown_button_form_field",
                          "id": "email_type",
                          "args": {
                          "decoration": {
                            "labelText": "Email Type"
                          },
                          "items": [
                          "Home",
                          "Other",
                          "Work"
                        ],
                        "validators": [
                      {
                      "type": "required"
                   }
                  ]
                } 
              },"""  
                  elif passenger['type'] == "number":
                         B= B+"""{
                              "type": "flexible",
                              "child": {
                                "type": "semantics",
                                "args": {
                                  "sortKey": {
                                    "order": 0.0,
                                    "textField": true
                                  }
                                },
                                "child": {
                                  "type": "exclude_semantics",
                                  "child": {
                                    "type": "text_form_field",
                                    "id": '"""+ str(passenger['name']) +"""',
                                    "args": {
                                      "decoration": {
                                        "hintText": "John",
                                        "labelText":'"""+ str(passenger['label']) +"""' ,
                                        "suffixIcon": {
                                          "type": "icon_button",
                                          "args": {
                                            "icon": {
                                              "type": "icon",
                                              "args": {
                                                "icon": {
                                                  "codePoint": 57704,
                                                  "fontFamily": "MaterialIcons",
                                                  "size": 50
                                                }
                                              }
                                            },
                                            "onPressed": "${set_value('"""+ str(passenger['name']) +"""','')}"
                                          }
                                        }
                                      },
                                      "validators": [
                                        {
                                          "type": "required"
                                        }
                                      ]
                                    }
                                  }
                                }
                              }
                            },"""                  
                    
            valuestr=A+B+C        
            return Response({"status":200,"success":True,"data":[{"id":"form1","form":valuestr}]})
     