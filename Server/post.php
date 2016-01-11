<?php
$gcode = "
".$_POST['gcode'];
file_put_contents('queue.txt', file_get_contents('queue.txt').$gcode);
?>