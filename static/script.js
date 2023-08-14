const body = document.getElementById("body");
const vid1_feed = document.getElementById("vid-feed-l1");
const vid2_feed = document.getElementById("vid-feed-l2");
// const pred_feed = document.getElementById("predict-feed-l1")

var myBtn1 = document.getElementById("start-feed-l1");
var myBtn2 = document.getElementById("start-feed-l2");
var isVideoPlaying = false;


const root = document.documentElement;

const left_section = document.getElementById("left-section");
const right_section = document.getElementById("right-section");

const left_input = document.querySelector(".left-input");
const right_input = document.querySelector(".right-input");
let video_feed_running = false;
let img;



const alphabet = {
    ' ': 'space.png',
    a: 'a.png',
    b: 'b.png',
    c: 'c.png',
    d: 'd.png',
    e: 'e.png',
    f: 'f.png',
    g: 'g.png',
    h: 'h.png',
    i: 'i.png',
    j: 'j.png',
    k: 'k.png',
    l: 'l.png',
    m: 'm.png',
    n: 'n.png',
    o: 'o.png',
    p: 'p.png',
    q: 'q.png',
    r: 'r.png',
    s: 's.png',
    t: 't.png',
    u: 'u.png',
    v: 'v.png',
    w: 'w.png',
    x: 'x.png',
    y: 'y.png',
    z: 'z.png'
  };


  
window.onload = function(){

  RenderENGtoASL();
}

function RenderENGtoASL(){
    
  left_section.innerHTML = "";
  left_section.innerHTML = `
  <textarea id="eng-input" class="eng-input" type="text" spellcheck="false" style="height: 300px;" placeholder="Enter text here" onkeypress="return /^[a-zA-Z ]+$/.test(event.key) || event.keyCode === 8;"></textarea>
  
  `
  ;

  right_section.innerHTML = "";
  right_section.innerHTML = `
  <div id="asl-input" class="asl-input" spellcheck="false" placeholder="ASL" style="height: 300px; overflow-y: auto; "></div>
  <div class="symetria"></div>
  `;


}

addEventListener('input', function () {
  var eng_input = document.getElementById("eng-input");
  var asl_input = document.getElementById("asl-input");
  const text = eng_input.value.toLowerCase();
  // Loop through each character in the input text
  let result = '';
  for (let i = 0; i < text.length; i++) {
    const character = text[i];
    // Check if the character is a letter or space bar
    if (/^[a-zA-Z ]$/.test(character)) {
      // Look up the corresponding ASL sign image for this character
      const sign = alphabet[character];
      // If a corresponding ASL sign image was found, add it to the result
      if (sign) {
        result += '<img src="static/letters/' + sign + '" alt="' + character + '">';
        
      } else if (character === ' ') {
        // If the character is a spacebar, add a non-breaking space to the result
        result += '&nbsp;';
      }
    }
  }

  // Insert the generated HTML into the asl-input textarea
  asl_input.innerHTML = result;

});



function toggleCamera_l1() {
  var button = document.getElementById("start-feed-l1");
  if (button.innerText === "Start Camera") {
      button.innerText = "Stop Camera";
      startCamera_l1();
  } else {
      button.innerText = "Start Camera";
      stopCamera_l1();
  }
}

function startCamera_l1() {
  // Send an AJAX request to Flask backend to start the camera
  showLoadingScreen();
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/start_camera_l1", true);
  xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          // Set the src attribute of the img tag to the URL of the video feed
          hideLoadingScreen();

          document.getElementById("predict-feed-l1").src = "/video_feed_l1";
      }
  };
  xhr.send();
}

function stopCamera_l1() {
  // Send an AJAX request to Flask backend to stop the camera
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/stop_camera_l1", true);
  xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          // Set the src attribute of the img tag to an empty string to stop the video feed
          document.getElementById("predict-feed-l1").src = "";
      }
  };
  xhr.send();
}

function toggleCamera_l2() {
  var button = document.getElementById("start-feed-l2");
  if (button.innerText === "Start Camera") {
      button.innerText = "Stop Camera";
      startCamera_l2();
  } else {
      button.innerText = "Start Camera";
      stopCamera_l2();
  }
}

function startCamera_l2() {
  showLoadingScreen();
  // Send an AJAX request to Flask backend to start the camera
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/start_camera_l2", true);
  xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          hideLoadingScreen();
          // Set the src attribute of the img tag to the URL of the video feed
          document.getElementById("predict-feed-l2").src = "/video_feed_l2";
      }
  };
  xhr.send();
}

function stopCamera_l2() {
  // Send an AJAX request to Flask backend to stop the camera
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/stop_camera_l2", true);
  xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          // Set the src attribute of the img tag to an empty string to stop the video feed
          document.getElementById("predict-feed-l2").src = "";
      }
  };
  xhr.send();
}

function showLoadingScreen() {
  document.getElementById("loading-screen").style.display = "flex";
}

function hideLoadingScreen() {
  document.getElementById("loading-screen").style.display = "none";
}