from application.server import app
from application.extensions import apimanager
from gatco.response import json

from .model import Test, TestUser


apimanager.create_api(
    Test,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api',
    collection_name = "test"
)

apimanager.create_api(
    TestUser,
    methods = ["GET", "POST", "PUT", "DELETE"],
    url_prefix='/api',
    collection_name = "test_user"
)



@app.route("/api/chatbot/text", methods=["POST", "GET"])
def text(request):
    return json({
         "messages": [
           {"text": "Welcome to the Chatfuel Rockets!"},
           {"text": "What are you up to?"}
         ]
    })
    

@app.route("/api/chatbot/images", methods=["POST", "GET"])
def images(request):
    return json({
      "messages": [
        {
          "attachment": {
            "type": "image",
            "payload": {
              "url": "https://rockets.chatfuel.com/assets/welcome.png"
            }
          }
        }
      ]
    })
    


@app.route("/api/chatbot/video", methods=["POST", "GET"])
def video(request):
    return json({
      "messages": [
        {
          "attachment": {
            "type": "video",
            "payload": {
              "url": "https://rockets.chatfuel.com/assets/video.mp4"
            }
          }
        }
      ]
    })
    


@app.route("/api/chatbot/audio", methods=["POST", "GET"])
def audio(request):
    return json({
      "messages": [
        {
          "attachment": {
            "type": "audio",
            "payload": {
              "url": "https://rockets.chatfuel.com/assets/hello.mp3"
            }
          }
        }
      ]
    })
    


@app.route("/api/chatbot/files", methods=["POST", "GET"])
def files(request):
    return json({
      "messages": [
        {
          "attachment": {
            "type": "file",
            "payload": {
              "url": "https://rockets.chatfuel.com/assets/ticket.pdf"
            }
          }
        }
      ]
    })
    



@app.route("/api/chatbot/galleries", methods=["POST", "GET"])
def galleries(request):
    return json({
     "messages": [
        {
          "attachment":{
            "type":"template",
            "payload":{
              "template_type":"generic",
              "image_aspect_ratio": "square",
              "elements":[
                {
                  "title":"Chatfuel Rockets Jersey",
                  "image_url":"https://rockets.chatfuel.com/assets/shirt.jpg",
                  "subtitle":"Size: M",
                  "buttons":[
                    {
                      "type":"web_url",
                      "url":"https://rockets.chatfuel.com/store",
                      "title":"View Item"
                    }
                  ]
                },
                {
                  "title":"Chatfuel Rockets Jersey",
                  "image_url":"https://rockets.chatfuel.com/assets/shirt.jpg",
                  "subtitle":"Size: L",
                  "default_action": {
                    "type": "web_url",
                    "url": "https://rockets.chatfuel.com/store",
                    "messenger_extensions": True
                  },
                  "buttons":[
                    {
                      "type":"web_url",
                      "url":"https://rockets.chatfuel.com/store",
                      "title":"View Item"
                    }
                  ]
                }
              ]
            }
          }
        }
      ]
    })
    
    
@app.route("/api/chatbot/lists", methods=["POST", "GET"])
def lists(request):
    return json({
     "messages": [
        {
          "attachment":{
            "type":"template",
            "payload":{
              "template_type":"list",
              "top_element_style":"large",
              "elements":[
                {
                  "title":"Chatfuel Rockets Jersey",
                  "image_url":"http://rockets.chatfuel.com/assets/shirt.jpg",
                  "subtitle":"Size: M",
                  "buttons":[
                    {
                      "type":"web_url",
                      "url":"https://rockets.chatfuel.com/store",
                      "title":"View Item"
                    }
                  ]
                },
                {
                  "title":"Chatfuel Rockets Jersey",
                  "image_url":"http://rockets.chatfuel.com/assets/shirt.jpg",
                  "subtitle":"Size: L",
                  "default_action": {
                    "type": "web_url",
                    "url": "https://rockets.chatfuel.com/store",
                    "messenger_extensions": True
                  },
                  "buttons":[
                    {
                      "type":"web_url",
                      "url":"https://rockets.chatfuel.com/store",
                      "title":"View Item"
                    }
                  ]
                }
              ]
            }
          }
        }
      ]
    })
    
    
    
@app.route("/api/chatbot/receipts", methods=["POST", "GET"])
def receipts(request):
    return json({
      "messages": [
        {
          "attachment": {
            "type": "template",
            "payload": { 
              "template_type": "receipt",
              "recipient_name": "Mark Zuckerberg",
              "order_number": "12345678901",
              "currency": "USD",
              "payment_method": "Visa 2345",
              "order_url": "https://rockets.chatfuel.com/store?order_id=12345678901",
              "timestamp": "1428444666",
              "address": {
                "street_1": "1 Hacker Way",
                "street_2": "",
                "city": "Menlo Park",
                "postal_code": "94025",
                "state": "CA",
                "country": "US"
              },
              "summary": {
                "subtotal": 105,
                "shipping_cost": 4.95,
                "total_tax": 9,
                "total_cost": 118.95
              },
              "adjustments": [
                {
                  "name": "CF Rockets Superstar",
                  "amount": -25
                }
              ],
              "elements": [
                {
                  "title": "Chatfuel Rockets Jersey",
                  "subtitle": "Size: M",
                  "quantity": 1,
                  "price": 65,
                  "currency": "USD",
                  "image_url":   "http://rockets.chatfuel.com/assets/shirt.jpg"
                },
                {
                  "title": "Chatfuel Rockets Jersey",
                  "subtitle": "Size: L",
                  "quantity": 1,
                  "price": 65,
                  "currency": "USD",
                  "image_url":   "http://rockets.chatfuel.com/assets/shirt.jpg"
                }
              ]
            }
          }
        }
      ]
    })
    


@app.route("/api/chatbot/buttons", methods=["POST", "GET"])
def buttons(request):
    return json({
      "messages":[
        {
          "attachment":{
            "type":"template",
            "payload":{
              "template_type":"generic",
              "elements":[
                {
                  "title":"Get in touch",
                  "image_url":"https://rockets.chatfuel.com/assets/contact.jpg",
                  "subtitle":"Feel free to hit us up!",
                  "buttons":[
                    {
                      "type":"phone_number",
                      "phone_number":"+84916121289",
                      "title":"Call"
                    },
                    {
                      "type":"element_share"
                    }
                  ]
                }
              ]
            }
          }
        }
      ]
    })
    
    
    
@app.route("/api/chatbot/quickreplies", methods=["POST", "GET"])
def quickreplies(request):
    return json({
      "messages": [
        {
          "text":  "Did you enjoy the last game of the CF Rockets?",
          "quick_replies": [
            {
              "title":"Loved it!",
              "block_names": ["Block 1", "Block 2"]
            },
            {
              "title":"Not really...",
              "url": "https://rockets.chatfuel.com/api/sad-match",
              "type":"json_plugin_url"
            }
          ]
        }
      ]
    })
    
    
    
@app.route("/api/chatbot/settinguserattributes", methods=["POST", "GET"])
def settinguserattributes(request):
    return json({
      "set_attributes": 
        {
          "some attribute": "some value",
          "another attribute": "another value"
        },
      "block_names": ["Block 1"],
      "type": "show_block",
      "title": "Go!"
    })
    
    
@app.route("/api/chatbot/redirecttoblocks", methods=["POST", "GET"])
def redirecttoblocks(request):
    return json({
      "redirect_to_blocks": ["Welcome Message", "Default Answer"]
    })
    
