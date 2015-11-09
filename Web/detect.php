<?php 

header("Content-Type: text/plain");

$message = (isset($_GET["Message"])) ? $_GET["Message"] : NULL;
$version = (isset($_GET["Version"])) ? $_GET["Version"] : NULL;

if ($message) {
	$mail = fopen('temp/mail.txt', 'r+');
	fputs($mail, $message);
	fclose($mail);
	if ($version == "version_1") {
		exec('python /var/www/spam/Version_1/spamDetector.py /var/www/spam/Web/temp/ web',$output,$spam);
	} elseif ($version == "Version_2") {
		exec('cd /var/www/spam/Version_2/ && python /var/www/spam/Version_2/spamDetector.py /var/www/spam/Web/temp/ web',$output,$spam);
	} else {
		exec('cd /var/www/spam/Version_3/ && python /var/www/spam/Version_3/spamDetector.py /var/www/spam/Web/temp/ web',$output,$spam);
	}
	if ($output[4] == (string) 0) {
		echo "ham";
	} else {
		echo "spam";
	}
	$mail = fopen('temp/mail.txt', 'r+');
	ftruncate($mail,0);
	fclose($mail);
} else {
	echo "FAIL";
}

?>