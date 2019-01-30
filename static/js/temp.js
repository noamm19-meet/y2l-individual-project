Feel free to delete/rename this file and add more .js files in this folder.


// URL for request POST /message
var url = 'https://foo.chat-api.com/message?token=83763g87x';
var data = {
    phone: '972527216320', // Receivers phone
    body: 'Hello, I want to train <Element> ,  ', // Message
};
// Send a request
$.ajax(url, {
    data : JSON.stringify(data),
    contentType : 'application/json',
    type : 'POST'
});


