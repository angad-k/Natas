<?php
/*
function xor_encrypt($in) {
    $key = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw%3D');
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
session_start();
$_SESSION["showpassword"] = "no";
$_SESSION["bgcolor"] = "%23000000";
$JSONvar = json_encode($_SESSION);

$keyWeNeed = xor_encrypt($JSONvar);

echo $keyWeNeed;
*/


function xor_encrypt($in) {
    $key = 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i];
    }

    return $outText;
}

$d['showpassword'] = "yes";

$d['bgcolor'] = "#000000";

echo base64_encode(xor_encrypt(json_encode($d)));




//ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSRwh6QUcIaAw%3D






//ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhURQssFxFeLBdVRQ==
//ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhUUgp5FxFeLBcRGjc= with no and bgcolor white
//ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D actual cookie in above conds
//ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTUh14QhFeLBcRXmgM
//ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTUh14QhFeLBcRXmgM