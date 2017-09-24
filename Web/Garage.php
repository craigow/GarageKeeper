<?php
$on='gpio mode 5 out';
$off='gpio mode 5 in';
$command = 'gpio write 5 0';
$command2= 'gpio write 5 1';
exec($on);
exec($command);
sleep(1);
exec($command2);
exec($off);
header ("Location: Garage.html");
?>