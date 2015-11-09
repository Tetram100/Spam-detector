<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Spam Detector - Python Project</title>
	<link rel="icon" type="image/x-icon" href="Assets/favicon.ico" />
	<script src="Assets/jquery-1.11.1.min.js"></script>
	<link href="Assets/bootstrap.min.css" rel="stylesheet">
	<script src="Assets/bootstrap.min.js"></script>
	<script type="text/javascript" src="Assets/oXHR.js"></script>
	<script type="text/javascript">
		<!-- 
		function animateStyle(divID) {

			$("#" + divID).css({ "display": "block", "opacity": "0" }).animate({ "opacity": "1" }, 200);

		}

		function request(callback) {
			if (encodeURIComponent(document.getElementById("message").value) == "") {
				document.getElementById("thanks").style.display="none";
				document.getElementById("spam").style.display="none";
				document.getElementById("ham").style.display="none";
				document.getElementById("response").style.display="none";
				animateStyle("message_empty");
			} else {
				var xhr = getXMLHttpRequest();
				document.getElementById("thanks").style.display="none";
				document.getElementById("message_empty").style.display="none";

				xhr.onreadystatechange = function() {
					if (xhr.readyState == 4 && (xhr.status == 200 || xhr.status == 0)) {
						callback(xhr.responseText);
						document.getElementById("loader").style.display = "none";
					} else if (xhr.readyState < 4) {
						document.getElementById("loader").style.display = "inline";
					}
				};

				var message = encodeURIComponent(document.getElementById("message").value);
				var version = encodeURIComponent($("input[name='version']:checked").val());

				sessionStorage.setItem("message",message);

				xhr.open("GET", "detect.php?Message=" + message + "&Version=" + version, true);
				xhr.send(null);
			}
			
		}

		function readData(sData) {

			sessionStorage.setItem("result",sData);

			if (sData == "spam"){
				animateStyle("spam");
				animateStyle("response");
				document.getElementById("ham").style.display="none";
			} else {
				animateStyle("ham");
				animateStyle("response");
				document.getElementById("spam").style.display="none";
			}
		}

		function learn(){
			
			var xhr2 = getXMLHttpRequest();
			var message = sessionStorage.getItem("message");
			var result = sessionStorage.getItem("result");
			var user_response = encodeURIComponent($("input[name='user_response']:checked").val());

			if ((result == "spam" && user_response == "yes") || (result == "ham" && user_response == "no")){
				var veracity = "spam";
			} else {
				var veracity = "ham";
			}

			xhr2.open("GET", "learn.php?Message=" + message + "&Veracity=" + veracity, true);
			xhr2.send(null);
			document.getElementById("response").style.display="none";
			animateStyle("thanks");
		}

//-->
</script>
</head>
<body>
	<h2 style="text-align:center">Spam Detector - Python Project</h2>
	<div class = "container well">
		<div class="panel panel-default">
			<div class="panel-body">
				<p>This is a web page made for the project of the EP2300 course <em>Management of Networks and Networked Systems</em> in KTH. The website runs on PHP with apache and the spam analyzis in back-end is done with Python scripts.</p>
				<ul>
					<li>The first version used has just a few word in a dictionnary and compares it with the message, it's fast but not very powerful.</li>
					<li>The second learned from a large database of mails the occurence of each word in spam and non-spam message in order to analyze the whole message with the <a href="http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering">Naive Bayes method</a>. It's far more powerful than the first but a little slower.</li>
					<li>The third implements the <a href="http://www.linuxjournal.com/article/6467">fisher method</a>. It's a variant of the Bayes methode with improvements for the rare words.</li>
				</ul>
				<p>The quality of the detection is directly linked with the mails previously analized. The more mails we have, the more efficient the detection is.</p>
			</div>
		</div>
		<br>
		<form>
			<p>
				<ul> <dl class="dl-horizontal">
					<dt> <label for="message">Message :</label> </dt>
					<dd> <textarea class="form-control" id="message" rows="6"></textarea> </dd>
				</dl> </ul>
			</p>

			<ul> <dl class="dl-horizontal">
				<dt>Version: </dt>
				<dd><input type="radio" name="version" value="version_1"  /> Version 1<br></dd>
				<dd><input type="radio" name="version" value="version_2" /> Version 2<br></dd>
				<dd><input type="radio" name="version" value="version_3" checked /> Version 3</dd>
			</dl> </ul>
			<hr>
			<p>
				<input type="button" class="btn btn-primary" onclick="request(readData);" value="Spam or Ham?" />
				<span id="loader" style="display: none;"><img src="Assets/loader.gif" alt="loading" /></span>
			</p>
			<hr>
			<div class="alert alert-warning" role="alert" id="message_empty" style="display:none">Write your message in the text field!</div>
			<div class="alert alert-danger" role="alert" id="spam" style="display:none">Your message is a spam!</div>
			<div class="alert alert-success" role="alert" id="ham" style="display:none">Your message is not a spam!</div>
			<div id="response" style="display:none">
				<hr>
				<ul> <dl class="dl-horizontal">
					<dt>Is it correct: </dt>
					<dd><input type="radio" name="user_response" value="yes"  onclick="learn()"/> Yes</dd>
					<dd><input type="radio" name="user_response" value="no" onclick="learn()" /> No</dd>
				</dl> </ul>
			</div>
			<div class="alert alert-success" role="alert" id="thanks" style="display:none">
				<p> Thanks for your response, it helps to improve the quality of the detection </p>
			</div>
		</form>
	</div>
	<div class = "container well">
		<?php 
			$db = new SQLite3('../spam_db');

			echo "The number of spam analyzed is <strong>";
			echo $db->querySingle('SELECT value FROM stat WHERE name = "nbr_mails_spam"');
			echo "</strong><br>";
			echo "The number of ham analyzed is <strong>";
			echo $db->querySingle('SELECT value FROM stat WHERE name = "nbr_mails_ham"');
			echo "</strong>";

		?>
	</div>
	<div id="property" style="text-align:center">
		<p>Guillaume Dhainaut - All rigths reserved</p>
	</div>
</body>
</html>