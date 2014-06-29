<?php
$sid = file_get_contents("./sebastian/sid.txt");
$token = file_get_contents("./sebastian/access_token.txt");
$uid = file_get_contents("./sebastian/uid.txt")
$url = 'https://upload.ybox.yahooapis.jp/v1/upload';
$file = './bin/kamonegi-release.apk';
$file_name = 'kamonegi-release.apk';
$body = file_get_contents($file);
$headers = array(
  'Authorization: Bearer '.$token,
  'Content-Type: mulitipart/form-data',
  'Content-length: '.filesize($file),
  'box-obj-sid: '.$sid,
  'box-obj-parentuniqid: '.$uid,
  'box-obj-filename: '.$file_name,
  'box-obj-md5: '.Md5($body),
  'box-force:1'
);
$url = 'https://upload.ybox.yahooapis.jp/v1/upload';
$curl = curl_init($url);
curl_setopt($curl,CURLOPT_HEADER, true);
curl_setopt($curl,CURLOPT_HTTPHEADER, $headers);
curl_setopt($curl,CURLOPT_POST, true);
curl_setopt($curl,CURLOPT_POSTFIELDS, $body);
curl_setopt($curl,CURLOPT_VERBOSE, true);
$result = curl_exec($curl);
if(curl_errno($curl)) {
  $response_header = curl_getinfo($curl);
}
curl_close($curl);
var_dump($result);

?>
