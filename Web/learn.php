<?php 

header("Content-Type: text/plain");

$message = (isset($_GET["Message"])) ? $_GET["Message"] : NULL;
$veracity = (isset($_GET["Veracity"])) ? $_GET["Veracity"] : NULL;

if ($message) {
	$mail = fopen('temp/mail.txt', 'r+');
	fputs($mail, $message);
	fclose($mail);
	if ($veracity == "spam") {
		echo "spam";
		exec('cd /var/www/spam/Version_2/ && python /var/www/spam/Version_2/learning_spam.py /var/www/spam/Web/temp/',$output,$spam);
	} elseif ($veracity == "ham") {
		echo "ham"; 
		exec('cd /var/www/spam/Version_2/ && python /var/www/spam/Version_2/learning_ham.py /var/www/spam/Web/temp/',$output,$spam);
	}
	$mail = fopen('temp/mail.txt', 'r+');
	ftruncate($mail,0);
	fclose($mail);
} else {
	echo "FAIL";
}

?>