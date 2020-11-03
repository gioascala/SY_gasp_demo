'use strict';

var isChannelReady = false;
var isInitiator = false;
var isStarted = false;
var localStream;
var pc;
var remoteStream;
var turnReady;
var front = true;
var mic = false;
var videooff = false;

var pcConfig = {
  'iceServers': [{
      "urls": "turn:numb.viagenie.ca:3478",
      "username": "hqmac@ramundur.se",
      "credential": "testtest"
    },
	{
    'urls': 'stun:stun.l.google.com:19302'
  }]
};

// Set up audio and video regardless of what devices are present.
var sdpConstraints = {
  offerToReceiveAudio: true,
  offerToReceiveVideo: true
};

var flip = document.getElementById('flip-button');
flip.onclick = function(){changefront()};


var constraints = {
  audio: true,
  video: {facingMode : "environment"}
};

//////////////////////////////////////////////////////

var room = 'foo';
// Could prompt for room name:
//room = prompt('Enter room name:');

var socket = io.connect();

if (room !== '') {
  socket.emit('create or join', room);
  console.log('Attempted to create or  join room', room);
}

socket.on('created', function(room) {
  console.log('Created room ' + room);
  isInitiator = true;
});

socket.on('full', function(room) {
  console.log('Room ' + room + ' is full');
});

socket.on('join', function (room){
  console.log('Another peer made a request to join room ' + room);
  console.log('This peer is the initiator of room ' + room + '!');
  isChannelReady = true;
});

socket.on('joined', function(room) {
  console.log('joined: ' + room);
  isChannelReady = true;
});

socket.on('log', function(array) {
  console.log.apply(console, array);
});

////////////////////////////////////////////////

function sendMessage(message) {
  console.log('Client sending message: ', message);
  socket.emit('message', message);
}

// This client receives a message
socket.on('message', function(message) {
  console.log('Client received message:', message);
  if (message === 'got user media') {
    maybeStart();
  } else if (message.type === 'offer') {
    if (!isInitiator && !isStarted) {
      maybeStart();
    }
    pc.setRemoteDescription(new RTCSessionDescription(message));
    doAnswer();
  } else if (message.type === 'answer' && isStarted) {
    pc.setRemoteDescription(new RTCSessionDescription(message));
  } else if (message.type === 'candidate' && isStarted) {
    var candidate = new RTCIceCandidate({
      sdpMLineIndex: message.label,
      candidate: message.candidate
    });
    localVideo.className = "video-local";
    remoteVideo.className = "video-remote";
    remoteVideo.style.display = "block";
    pc.addIceCandidate(candidate);
  } else if (message === 'bye' && isStarted) {
    handleRemoteHangup();
  }
});

////////////////////////////////////////////////////

var localVideo = document.getElementById('video-local');
var remoteVideo = document.getElementById('video-remote');
var chiudi = document.getElementById('chiudi');
var novideo = document.getElementById('novideo');
var noaudio = document.getElementById('noaudio');
chiudi.onclick = function(){chiudiclick()};

localVideo.className = "video-remote";
remoteVideo.className = "video-local";

function chiudiclick(){
  stop();
  localVideo.className = "video-remote";
  remoteVideo.className = "video-local";
  remoteVideo.style.display = "none";
  
}


navigator.mediaDevices.getUserMedia(constraints)
.then(gotStream)
.catch(function(e) {
  alert('Errore nell\' aprire il microfono o la videocamera:' + e.name);
});

function gotStream(stream) {

  chiudi.className = "chiudi";
  console.log('Adding local stream.');
  localStream = stream;
  localVideo.srcObject = stream;
  sendMessage('got user media');
  if (isInitiator) {
    maybeStart();
  }
}



console.log('Getting user media with constraints', constraints);
if (location.hostname !== 'localhost') { requestTurn( 'https://79.56.159.33:3478/turn?username=user&key=pass' ); }


function maybeStart() {
  console.log('>>>>>>> maybeStart() ', isStarted, localStream, isChannelReady);
  if (!isStarted && typeof localStream !== 'undefined' && isChannelReady) {
    console.log('>>>>>> creating peer connection');
    createPeerConnection();
    pc.addStream(localStream);
    isStarted = true;
    console.log('isInitiator', isInitiator);
    if (isInitiator) {

      chiudi.className = "chiudi";
      doCall();
    }
  }
}

window.onbeforeunload = function() {
  stop();
  localVideo.className = "video-remote";
  remoteVideo.className = "video-local";
  sendMessage('bye');
};

/////////////////////////////////////////////////////////

function createPeerConnection() {
  try {
    pc = new RTCPeerConnection(pcConfig);
    pc.onicecandidate = handleIceCandidate;
    pc.onaddstream = handleRemoteStreamAdded;
    pc.onremovestream = handleRemoteStreamRemoved;
    console.log('Created RTCPeerConnnection');
  } catch (e) {
    console.log('Failed to create PeerConnection, exception: ' + e.message);
    alert('Cannot create RTCPeerConnection object.');
    return;
  }
}

function handleIceCandidate(event) {
  console.log('icecandidate event: ', event);
  if (event.candidate) {
    sendMessage({
      type: 'candidate',
      label: event.candidate.sdpMLineIndex,
      id: event.candidate.sdpMid,
      candidate: event.candidate.candidate
    });
  } else {
    console.log('End of candidates.');
  }
}

function handleCreateOfferError(event) {
  console.log('createOffer() error: ', event);
}

function doCall() {
  console.log('Sending offer to peer');
  pc.createOffer(setLocalAndSendMessage, handleCreateOfferError);
}

function doAnswer() {
  console.log('Sending answer to peer.');
  pc.createAnswer().then(
    setLocalAndSendMessage,
    onCreateSessionDescriptionError
  );
}

function setLocalAndSendMessage(sessionDescription) {
  pc.setLocalDescription(sessionDescription);
  console.log('setLocalAndSendMessage sending message', sessionDescription);
  sendMessage(sessionDescription);
}

function onCreateSessionDescriptionError(error) {
  trace('Failed to create session description: ' + error.toString());
}

function requestTurn(turnURL) {
  var turnExists = false;
  for (var i in pcConfig.iceServers) {
    if (pcConfig.iceServers[i].urls.substr(0, 5) === 'turn:') {
      turnExists = true;
      turnReady = true;
      break;

    }
  }
  if (!turnExists) {
    console.log('Getting TURN server from ', turnURL);
    // No TURN server. Get one from computeengineondemand.appspot.com:
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var turnServer = JSON.parse(xhr.responseText);
        console.log('Got TURN server: ', turnServer);
        pcConfig.iceServers.push({
          'urls': 'turn:' + turnServer.username + '@' + turnServer.turn,
          'credential': turnServer.password
        });
        turnReady = true;
      }
    };
    xhr.open('GET', turnURL, true);
    xhr.send();
  }
}

function handleRemoteStreamAdded(event) {
  console.log('Remote stream added.');
  remoteStream = event.stream;
  remoteVideo.srcObject = remoteStream;
}

function handleRemoteStreamRemoved(event) {
  console.log('Remote stream removed. Event: ', event);
}

function hangup() {
  console.log('Hanging up.');
  stop();
  sendMessage('bye');
}

function handleRemoteHangup() {
  console.log('Session terminated.');
  stop();
  isInitiator = false;
}

function stop() {
  isStarted = false;
  isInitiator = true;
  pc.close();
  pc = null;
}

/////////////////////////////////////////////
//Camera and microfone management


function changefront(){
  front = !front;
  
  console.log(front);
  if (front === true){
    constraints.video.facingMode = "environment";
    navigator.mediaDevices.getUserMedia(constraints)
    .then(gotStream)
    .catch(function(e) {
      alert('getUserMedia() error: ' + e.name);
    });
  }
  else if (front === false) {
    constraints.video.facingMode = "self";
    navigator.mediaDevices.getUserMedia(constraints)
    .then(gotStream)
    .catch(function(e) {
      alert('getUserMedia() error: ' + e.name);
    });
  }
}

function micoff(){
  mic = !mic;
  stop();
  console.log(front);
  if (mic === false){
    navigator.mediaDevices.getUserMedia({
      audio: true,
      video: {facingMode : "environment"} 
    })
    .then(gotStream)
    .catch(function(e) {
      alert('getUserMedia() error: ' + e.name);
    });
  }
  else if (front === false) {
    navigator.mediaDevices.getUserMedia({
      audio: true,
      video: {facingMode : "self"} 
    })
    .then(gotStream)
    .catch(function(e) {
      alert('getUserMedia() error: ' + e.name);
    });
  }
}

var videoon = true;
novideo.onclick = function(){novideos()};
function novideos(){
  console.log(videoon);
  videoon = !videoon;
  localStream.getVideoTracks()[0].enabled = videoon;
  console.log(videoon);
}

var audioon = true;
noaudio.onclick = function(){noaudios()};
function noaudios(){
  console.log(audioon);
  audioon = !audioon;
  localStream.getAudioTracks()[0].enabled = audioon;
  console.log(audioon);
}