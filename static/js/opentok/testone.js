// Initialize an OpenTok Session object
var session = OT.initSession(apiKey, sessionId);
var subscribe;
var publisher;

// Initialize a Publisher, and place it into the element with id="publisher"


var subscriberOptions = {
    insertMode: 'append',
    name : "Asistente "
};





// Attach event handlers
session.on({

  // This function runs when session.connect() asynchronously completes
  sessionConnected: function(event) {



      console.log(event.target.connection.permissions) 
      //console.log(event.target.connection.permissions.publish) 
      console.log("Esto es primero") 

      var publisherOptions = {
              insertMode: 'append',
              width: '900',
              height: '450',
              name : "Expositor"
      };


      var publisher = OT.initPublisher('publisher',publisherOptions);
      session.publish(publisher, function(error) {


          if (error) {
            console.error('Failed to publish', error);
          }
      });
      
      //console.log(event.stream.connection.permissions.publish) 


  },

  // This function runs when another client publishes a stream (eg. session.publish())
  streamCreated: function(event) {

    console.log(session.getPublisherForStream(event.stream))
    console.log("Esto es tercero") 

    /*if(event.connection){

      console.log("Soy publisher");
    }else{
      console.log("Soy suscriptor");

    }*/



    // Create a container for a new Subscriber, assign it an id using the streamId, put it inside
    // the element with id="subscribers"
    var subContainer = document.createElement('div');
    subContainer.id = 'stream-' + event.stream.streamId;
    document.getElementById('subscribers').appendChild(subContainer);



    // Subscribe to the stream that caused this event, put it inside the container we just made
    session.subscribe(event.stream, subContainer, subscriberOptions,function(error) {
      if (error) {
        console.error('Failed to subscribe', error);
      }
    });



  },

streamPropertyChanged: function(event){


    //session.publish(publisher, function(error) {

      //console.log('streamPropertyChanged');

    //}); 

  }

});



session.connect(token, function(error) {

    console.log("Esto es segundo")

});


// Connect to the Session using the 'apiKey' of the application and a 'token' for permission


$(document).ready(function() {





  $('#shared').click(function (event) {
      
    var publisher = OT.initPublisher(
        'publisher', // Replace with the replacement element ID
        {
           name: 'John',
           videoSource:'screen' 
        }
      );
      session.publish(publisher);

     });


});
