text = '''
<html>
<head>
<title>Tomato Timer</title>
<meta name="description" content="TomatoTimer is a flexible and easy to use online Pomodoro Technique Timer">
<meta name="keywords" content="pomodoro technique, tomato timer, pomodoro timer, online pomodoro timer, software timer, pomodoro software timer, productivity tools, gtd, getting things done, productivity, digital timer, concentration techniques, pomodoro resources, pomodoro software">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="manifest" href="/manifest.json">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#ff4343">
<meta name="theme-color" content="#ffffff">
<link rel="stylesheet" href="foundation/stylesheets/foundation.css">
<link rel="stylesheet" href="app.css">
<script src="foundation/javascripts/foundation.min.js"></script>
<script src="howler2.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.20.1/moment-with-locales.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
<script src="timer_fixes/HackTimer.js"></script>
<script src="timer_fixes/HackTimerWorker.js"></script>
</head>
<body>
<!-- Header and Nav -->
<div class="panel">
	<div class="row">
    <div class="three columns">
        <h2>TomatoTimer</h2></div>
    <div class="nine columns">
      <ul class="nav-bar right">
        <li><a href="#" data-reveal-id="trackerModal">Log</a></li>
        <li><a href="#" data-reveal-id="faqModal">FAQ</a></li>
        <li><a href="#" data-reveal-id="settingsModal">Settings</a></li>
        <li><a href="https://bit.ly/sharetomatotimer" target="_blank">Tweet about us!</a></li>
      </ul>
    </div>
  </div>
<!---->
</div>
<!---->
	<div class="row">
    <div class="ten columns centered">
    <ul class="button-group even three-up" id="timer_selection">
        <li><button class="button active" id="pomodoro" type="submit" value="Pomodoro">Pomodoro</button></li>
        <li><button class="button" id="short_break" type="submit" value="Short Break">Short Break</button></li>
        <li><button class="button" id="long_break" type="submit" value="Long Break">Long Break</button></li>
    </ul>
</div>
</div>
<br>
<!-- Header -->
<div class="row">
    <div class="twelve columns text-center">
    <div id='default_container'>
  		<h1 id="timer_default"></h1><br />
	</div>
</div>
<!-- End Header -->
<!-- End Header and Nav -->
</div>
<br>
<br>
<div class="row">
    <div class="six columns centered">

    <div class="four columns">
        <button class="success radius large button" id="timer_start" type="submit" value="Start">Start</button>
    </div>
    <div class="four columns">
        <button class="alert radius large button" id="timer_pause" type="submit" value="Stop">Stop</button>
    </div>
    <div class="four columns">
        <button class="radius large secondary button" id="timer_reset" type="submit" value="Reset">Reset</button>
    </div>
    </div>
 </div>
<br />
<div class="row"><br></div>
<div class="row">
          <div class="row">
              <div class="four columns">
                <div class="panel">
                  <h5>Keyboard Shortcuts</h5>
                <ul class="disc">
  <li><strong>SPACE  </strong>&nbsp;&nbsp;Start or Stop the timer</li>
  <li><strong>ALT + P</strong>&nbsp;&nbsp;Pomodoro</li>
  <li><strong>ALT + S</strong>&nbsp;&nbsp;Short Break</li>
  <li><strong>ALT + L</strong>&nbsp;&nbsp;Long Break</li>
  <li><strong>ALT + R</strong>&nbsp;&nbsp;Reset Timer</li>
</ul>
                </div>
              </div>
              <div class="four columns">
                <div class="panel">
                    <h5>Notifications</h5>
                  <h6 class="subheader">You can change the audio tone and volume via Settings</h6>
                  <h6 class="subheader">Desktop Notifications are currently supported in Chrome, Firefox and Safari </h6>
                  <a href="#" onclick="permit();" class="small button">Enable Desktop Alerts</a>
                </div>
              </div>
              <div class="four columns">
                <div class="panel">
									<h5>Settings</h5>
                  <h6 class="subheader">You can set custom times, audio tone and volume via Settings.</h6>
			<script async type="text/javascript" src="//cdn.carbonads.com/carbon.js?serve=CKYIC5QI&placement=tomatotimercom" id="_carbonads_js"></script>
		      </div>
              </div>
</div>

<script type='text/javascript' src="notify.js"></script>
<script type="text/javascript" src="jquery.countdown.js"></script>
<script type='text/javascript' src="tomato_2.js"></script>

<div id="faqModal" class="reveal-modal medium">
	<div>
		Q. What is Pomodoro Technique?
	</div>

	<div>
		A. The time management technique created by Francesco Cirillo for a	more productive way to work and study. For more information,&nbsp;<a href="http://www.pomodorotechnique.com" target="_blank">click here</a>.
	</div>

	<div>
		<br>
	</div>

	<div>
		Q. Can you tell me the story without having to visit the website?
	</div>

	<div>
		<div>
			A. Well, it comprises of the following basic steps:
		</div>

		<ul>
			<li>Decide on the task at hand</li>
			<li>Set the <strong>Pomodoro</strong> (timer) to 25 minutes</li>
			<li>Work on the task until the timer expires; Record with an X</li>
			<li>Take a <strong>Short Break</strong> (5 minutes)</li>
			<li>Every four "<em>pomodoros</em>", take a <strong>Long Break</strong> (10 minutes)</li>
		</ul>
	</div>

	<div>
		Q. What is TomatoTimer?
	</div>

	<div>
		A. It's an easy to use, flexible Pomodoro Technique timer. It was inspired by Tomatoi.st and it uses jQuery and HTML5 features like Desktop Notifications, Audio API and Local Storage instead of relying on Adobe Flash and other such technologies.
	</div>

	<div>
		<br>
	</div>

	<div>
		Q. Why use TomatoTimer?
	</div>

	<div>
		A.&nbsp;Here's why:
			<ul>
				<li>Clean and Crisp interface with a Mobile friendly layout.</li>
				<li>Ability to Pause or Reset the timer intervals.</li>
				<li>Audio notifications at the end of a timer period.</li>
				<li>Desktop notifications. (Only supported in Google Chrome)</li>
				<li>Keyboard shortcuts.</li>
				<li>Ability to change the alert sound + volume via Settings</li>
				<li>Custom Timer Intervals</li>
				<li>A history of your activity. (Coming soon.)</li>
			</ul>
		<br>
	</div>

	<div>
		Q. I've got some feedback. How do I get in touch with you?
	</div>

	<div>
		A. <a href="mailto:mpcovcd@gmail.com">Email me</a>.
	</div>

  <div>
    <br>
  </div>

  <div>
    Receive early access to our new platform and news about feature updates to TomatoTimer! Signup for our mailing list: <a href="http://eepurl.com/c5uCuz"> Sign up!</a>
  </div>
<a class="close-reveal-modal">&#215;</a>
  </div>

<div id="settingsModal" class="reveal-modal medium">
  <h2>Options</h2>
  <h3>User preferences</h3>
  <p class="flex-container flex-center-items">
    <input id="checkBoxTimerIndication" type="checkbox">
    <label for="checkBoxTimerIndication">Timer indication in title?</label>
  </p>

  <p class="flex-container flex-center-items">
    <input id="checkBoxNotifications" type="checkbox">
    <label for="checkBoxNotifications">Browser notifications?</label>
  </p>

  <p class="flex-container flex-center-items">
    <input id="checkBoxAutoStartSequence" type="checkbox">
    <label for="checkBoxAutoStartSequence">Auto start pomodoros and breaks?</label>
  </p>

  <p class="flex-container flex-center-items ">
    <label for="pomodoro_goal">Pomodoro goal for the day</label>
    <input class="small-input" type="number" id="pomodoro_goal" step="1" min="1" name="pomodoro_goal">
  </p>

  <p><h3>Select Sound</h3>
  <select id="alertoption" size="5">
      <option value="80sAlarm">80s Alarm</option>
      <option value="alarmclock">Alarm Clock</option>
      <option value="alarmwatch">Wristwatch Alarm</option>
      <option value="ding">Elevator Ding</option>
      <option value="doorbell">Door Bell</option>
  </select>
  <br /><h3>Select Volume</h3>
  <select id="volume" size=5>
      <option value="0">Mute</option>
      <option value="0.25">25%</option>
      <option value="0.5">50%</option>
      <option value="0.75">75%</option>
      <option value="1.0">100%</option> <br />
  </select>
  <br /><h3>Set Custom Times <small>(in minutes)</small></h3>
  <div class="row">
    <div class="four columns">
      <label for="time_pomodoro">Pomodoro</label>
      <input type="number" id="time_pomodoro" step="1" min="1" name="time_pomodoro">
    </div>
    <div class="four columns">
      <label for="time_shortbreak">Short Break</label>
      <input type="number" id="time_shortbreak" step="1" min="1" name="time_shortbreak">
    </div>
    <div class="four columns">
      <label for="time_longbreak">Long Break</label>
      <input type="number" id="time_longbreak" step="1" min="1" name="time_longbreak">
    </div>
  </div>
  </p>
  <input type="button" id="submit" value="Save" class="button" onclick="saveSETTINGS();">
  <input type="button" id="reset" value="Reset" class="button" onclick="resetSETTINGS();">
  <input type="button" id="soundtest" value="Sound Test" class="button" onclick="soundTEST();">
  <br />
  <a class="close-reveal-modal">&#215;</a>
</div>

<div id="trackerModal" class="reveal-modal large">
  <h2>Time log</h2>
  <div class="flex-container flex-center-items margin-large-bottom ">
    <div class="margin-small-right">Pomodoro goal tracker:</div>
    <div id="tracker-goal-pomodoros" class="flex-container"></div>
  </div>
  <div class="margin-large-bottom"><button id="pomodoroGoalClear" class="button" onClick="clearPomodoroGoalTracker();">Clear pomodoro's done today</button></div>
  <table id="tracker-time-list" style="width:100%">
    <tr>
      <th>Session</th>
      <th>Start time</th>
      <th>End time</th>
      <th>Description</th>
    </tr>
  </table>

  <div class="margin-large-bottom"><button id="pomodoroTimerClear" class="button" onClick="clearPomodoroLog();">Clear timer log</button></div>

  <a class="close-reveal-modal">&#215;</a>
</div>
<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-18513817-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

function saveSETTINGS() {
  var snd = $('#alertoption').val();
  var vol = $('#volume').val();
  var pomodoro = $("#time_pomodoro").val();
  var shortbreak = $("#time_shortbreak").val();
  var longbreak = $("#time_longbreak").val();

  if (!isInteger(pomodoro) || !isInteger(shortbreak) || !isInteger(longbreak))
    alert('Please use positive integers for all timers');
  else {
    localStorage.setItem("alertoption", snd);
    localStorage.setItem("volumeoption", vol);
    localStorage.setItem("pomodoro", parseInt(pomodoro));
    localStorage.setItem("shortbreak", parseInt(shortbreak));
    localStorage.setItem("longbreak", parseInt(longbreak));

    updateTimers();

    $('#settingsModal .close-reveal-modal')[0].click();
  }
}

function resetSETTINGS() {
    $("#alertoption").val("alarmwatch");
    $("#volume").val(0.5);
    $("#time_pomodoro").val(25);
    $("#time_shortbreak").val(5);
    $("#time_longbreak").val(10);
}

function soundTEST() {
    buzzer(true);
}

function isInteger(num) {
  return num && Math.floor(num) == num && $.isNumeric(num) && num > 0;
}
</script>
</body>
</html>
'''