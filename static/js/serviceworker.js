var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/'
];





//solo para cachear todo reemplazar por esta versión del Fetch


self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});



importScripts('https://www.gstatic.com/firebasejs/7.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.10.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyBSIAwxO5geJSslxclj68G33dZ-yumOEMI",
    authDomain: "mapstec-81290.firebaseapp.com",
    databaseURL: "https://mapstec-81290.firebaseio.com",
    projectId: "mapstec-81290",
    storageBucket: "mapstec-81290.appspot.com",
    messagingSenderId: "99396857968",
    appId: "1:99396857968:web:d1023241ff1551546004b5",
    measurementId: "G-85RHV43HWV"
  };
  firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
    console.log("la notificaicon llengo")
    let title = "title";
  let options = {
    body: "este es el mensaje"
  }
    self.registration.showNotification(title,options);
})
