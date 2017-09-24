<?php
$status ='gpio -g read 17';
//f = open('/var/www/html/relay-status2.txt','w')
//	    f.write(exec ($status))
  //          f.close()
//echo $status;
if (exec ($status) =="1"){
echo "<p> <font color=green font face='verdana' size='8pt'>Garage door Closed</font> </p>";
}
else{
echo "<p> <font color=red font face='verdana' size='8pt'>Garage door Open</font> </p>";
}
?>

<form action="Garage.html" method="Get">
 <input type="submit" value="Home" style="width: 800px;
 height:100px; font-size:80px;border-radius: 25px;
 background-color: 2DA3A7;">
 </form>